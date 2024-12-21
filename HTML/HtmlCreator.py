import shutil

from Config import Config

_prefix = "HTML/"

def _create_output_html_from_template() -> bool:
    shutil.copyfile(f"{_prefix}template.html", f"{_prefix}output.html")


def _load_template_content() -> str:
    with open(f"{_prefix}output.html", "r", encoding="utf-8") as file:
        return file.read()


def _save_output_html(content):
    with open(f"{_prefix}/output.html", "w", encoding="utf-8") as file:
        file.write(content)


def create_html(code: str, styles: str = "") -> bool:
    try:
        _create_output_html_from_template()
        content = _load_template_content()
        content = content.replace("@__CONTENT__@", code)
        content = content.replace("@__STYLES__@", styles)

        config = Config()
        theme = config.get("current_theme")

        content = content.replace("@__BAR_BACKGROUND__@", config.get("colors")[theme]["bar_background"])
        content = content.replace("@__CODE_BACKGROUND__@", config.get("colors")[theme]["code_background"])
        content = content.replace("@__BACKGROUND_COLOR__@", config.get("background_color"))
        _save_output_html(content)
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
