from back_end.utilities.json_manager import JsonManager, create_template_config
from front_end.cli_helper_functions import get_choice, get_string
from front_end.loaders.clipboard_loader import ClipboardLoader
from front_end.loaders.text_loader import TextLoader
from back_end.core import highlighter, image_creator, core
from front_end.savers.clipboard_saver import ClipboardSaver
from front_end.savers.i_saver import ISaver


def _get_language():
    avaible_languages = list(JsonManager().get("languages").keys())
    index = get_choice("Ktorý programovací jazyk? ", avaible_languages)
    return avaible_languages[index]


class Cli:
    def __init__(self):
        self.config = JsonManager("front_end/cli_settings.json")

    def _get_code(self) -> str:
        input_type: str = self.config.get('input_type')
        if input_type == "clipboard":
            try:
                return ClipboardLoader().to_string()
            except:
                return "SNIPORA ERROR: There was no code in your clipboard."
        elif input_type == "textloader":
            return TextLoader().to_string({'language': "java"})
        else:
            return TextLoader().to_string({'language': "python"})

    def _get_saver(self) -> ISaver:
        output_type: str = self.config.get('output_type')
        if output_type == "clipboard":
            return ClipboardSaver()
        else:
            return ClipboardSaver()

    def run(self, code, language, filename):
        success: bool = core.run(code=code, config_path="cli.json", language=language, file_name=filename)
        if not success:
            print("Niekde sa stala chyba. Screenshot neuložený :(")
            return

        saver = self._get_saver()
        saver.save("output.png")

    def run_with_prompts(self) -> None:
        code: str = self._get_code()
        language = _get_language()
        filename = get_string("Názov súboru: ")
        self.run(code, language, filename)


    def run_with_auto_prompts(self):
        code: str = self._get_code()
        self.run(code, self.config.get("language"), self.config.get("filename"))
