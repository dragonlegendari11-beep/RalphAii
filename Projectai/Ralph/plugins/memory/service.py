from plugins.memory.storage import JsonStorage


class MemoryService:

    DEFAULT_STRUCTURE = {
        "profile": {},
        "facts": [],
        "notes": [],
        "projects": [],
        "history": [],
        "settings": {},
    }

    def __init__(self):

        self.storage = JsonStorage()
        self.memory = self.storage.load()

        self._migrate()

    def _migrate(self):
        """Приводит старый плоский memory.json к новой структуре."""

        changed = False

        for key, default in self.DEFAULT_STRUCTURE.items():
            if key not in self.memory:
                self.memory[key] = default
                changed = True

        # старый формат хранил имя прямо в корне: {"name": "Dragon"}
        if "name" in self.memory:
            old_name = self.memory.pop("name")
            if old_name is not None and "name" not in self.memory["profile"]:
                self.memory["profile"]["name"] = old_name
            changed = True

        if changed:
            self.storage.save(self.memory)

    # ---------- Совместимость со старым API (main.py, ralph.py) ----------

    def remember(self, key, value):
        if key == "name":
            self.set_profile("name", value)
        else:
            self.memory[key] = value
            self.storage.save(self.memory)

    def recall(self, key):
        if key == "name":
            return self.get_profile("name")
        return self.memory.get(key)

    def forget(self, key):
        if key == "name":
            self.memory["profile"].pop("name", None)
            self.storage.save(self.memory)
        elif key in self.memory:
            del self.memory[key]
            self.storage.save(self.memory)

    # ---------- Profile ----------

    def set_profile(self, key, value):
        self.memory["profile"][key] = value
        self.storage.save(self.memory)

    def get_profile(self, key):
        return self.memory["profile"].get(key)

    # ---------- Facts ----------

    def add_fact(self, fact):
        self.memory["facts"].append(fact)
        self.storage.save(self.memory)

    def get_facts(self):
        return self.memory["facts"]

    def remove_fact(self, index):
        if 0 <= index < len(self.memory["facts"]):
            self.memory["facts"].pop(index)
            self.storage.save(self.memory)

    # ---------- Notes ----------

    def add_note(self, text):
        self.memory["notes"].append(text)
        self.storage.save(self.memory)

    def get_notes(self):
        return self.memory["notes"]

    # ---------- Projects ----------

    def create_project(self, name):
        project = {"name": name, "status": "active"}
        self.memory["projects"].append(project)
        self.storage.save(self.memory)
        return project

    def get_project(self, name):
        for project in self.memory["projects"]:
            if project["name"].lower() == name.lower():
                return project
        return None

    def get_projects(self):
        return self.memory["projects"]

    # ---------- History ----------

    def log_history(self, text):
        self.memory["history"].append(text)
        self.storage.save(self.memory)

    def get_history(self, limit=10):
        return self.memory["history"][-limit:]

    # ---------- Settings ----------

    def set_setting(self, key, value):
        self.memory["settings"][key] = value
        self.storage.save(self.memory)

    def get_setting(self, key, default=None):
        return self.memory["settings"].get(key, default)
