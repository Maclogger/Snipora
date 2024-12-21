from back_end.core import highlighter, image_creator
from back_end.core.html import html_creator
from back_end.utilities.json_manager import JsonManager


def run(config: JsonManager, code: str) -> bool:
    if not JsonManager().validate(config): return False

    code, styles = highlighter.highlight(config, code)
    successfully_created_html: bool = html_creator.create_html(config, code, styles)

    if not successfully_created_html: return False
    
    image_creator.generate_image_from_html()
    return True