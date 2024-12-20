from Loaders.ILoader import ILoader
import pyperclip

class ClipboardLoader(ILoader):

    def to_string(self) -> str:
        return pyperclip.paste()