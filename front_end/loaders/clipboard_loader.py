from front_end.loaders.i_loader import ILoader
import pyperclip

class ClipboardLoader(ILoader):

    def to_string(self) -> str:
        return pyperclip.paste()