import json
import shutil
from typing import Any, Dict


class JsonManager:
    def __init__(self, file_path: str = "back_end/utilities/data.json"):
        self.file_path = file_path
        self._data: Dict[str, Any] = {}
        self._load()

    def _load(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self._data = json.load(f)
        except FileNotFoundError:
            self._data = {}  # Start with an empty config if file doesn't exist
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {self.file_path}: {e}")

    def _save(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self._data, f, indent=4)

    def get(self, key: str) -> Any:
        return self._data.get(key)

    def set(self, key: str, value: Any):
        self._data[key] = value
        self._save()

    def remove(self, key: str):
        if key in self._data:
            del self._data[key]
            self._save()

    def validate(self, input_config) -> bool:
        try:
            if input_config.get("version") != self.get("version"): return False
            if input_config.get("theme") not in self.get("themes").keys(): return False
            return True
        except:
            return False


def create_template_config(file_path: str) -> JsonManager:
    shutil.copy("back_end/core/config.json", file_path)
    return JsonManager(file_path)


# Example usage
if __name__ == "__main__":
    config: JsonManager = JsonManager()
    config.set('language', "python")
    config.set('output', "clipboard")
