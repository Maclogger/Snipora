import pygments.util
from pygments.formatters.html import HtmlFormatter
from pygments.lexer import Lexer
from pygments.lexers import guess_lexer, get_lexer_by_name

from back_end.utilities.json_manager import JsonManager

def highlight(config: JsonManager, code: str)->(str, str):
    language = config.get("language")
    lexer: Lexer | None = _get_lexer(language, code)
    if lexer is None:
        return code, ""

    formatter = HtmlFormatter(style=config.get("theme"), linenos=True)
    return pygments.highlight(code, lexer, formatter), formatter.get_style_defs()

def _get_lexer(language: str, code: str) -> Lexer | None:
    try:
        if language == "guess":
            lexer: Lexer = guess_lexer(code)
        else:
            lexer: Lexer = get_lexer_by_name(language)
        return lexer
    except pygments.util.ClassNotFound:
        print(f"Lexer was not found for: {language}. Code was not highlighted.")
        return None