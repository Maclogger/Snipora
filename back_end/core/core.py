from back_end.core import highlighter, image_creator
from back_end.core.html import html_creator
from back_end.utilities.json_manager import JsonManager, create_template_config


def run_with_manager(config: JsonManager, code: str) -> bool:
    if not JsonManager().validate(config): return False

    config.set('language_icon', JsonManager().get("languages")[config.get("language")]["icon"])
    code, styles = highlighter.highlight(config, code)
    successfully_created_html: bool = html_creator.create_html(config, code, styles)

    if not successfully_created_html: return False
    
    image_creator.generate_image_from_html()
    return True


def run(code: str, config_path: str, language: str, file_name: str) -> bool:

    config = create_template_config(config_path)
    config.set('language', language)
    config.set('filename', file_name)
    config.set('background_color', "#F3F3F3")
    config.set('theme', "lightbulb")

    return run_with_manager(config, code)

