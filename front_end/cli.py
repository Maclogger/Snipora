from back_end.utilities.json_manager import JsonManager, create_template_config
from front_end.loaders.clipboard_loader import ClipboardLoader
from front_end.loaders.text_loader import TextLoader
from back_end.core import highlighter, image_creator, core


class Cli:
    def __init__(self):
        self.config = JsonManager("front_end/cli_settings.json")

    def _get_code(self) -> str:
        input_type: str = self.config.get('input_type')
        if input_type == "clipboard":
            return ClipboardLoader().to_string()
        elif input_type == "textloader":
            return TextLoader().to_string({'language': "java"})
        else:
            return TextLoader().to_string({'language': "python"})

    def _get_saver(self):
        pass

    def run_with_prompts(self) -> None:
        code: str = self._get_code()
        success: bool = core.run(code=code, config_path="cli.json", language="python", file_name="scriptik.py")
        if not success:
            print("Niekde sa stala chyba. Screenshot neuložený :(")
            return

        saver = self._get_saver()
        saver.save()
