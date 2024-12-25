import shutil

from back_end.utilities.json_manager import JsonManager

_prefix = "back_end/core/html/"

def _create_output_html_from_template():
    shutil.copyfile(f"{_prefix}template.html", f"{_prefix}output.html")


def _load_template_content() -> str:
    with open(f"{_prefix}output.html", "r", encoding="utf-8") as file:
        return file.read()


def _save_output_html(content):
    with open(f"{_prefix}/output.html", "w", encoding="utf-8") as file:
        file.write(content)


def create_html(config: JsonManager, code: str, styles: str = "") -> bool:
    try:
        _create_output_html_from_template()
        content = _load_template_content()
        content = content.replace("@__CONTENT__@", code)
        content = content.replace("@__STYLES__@", styles)

        theme = config.get("theme")
        fixed_conf = JsonManager()

        content = content.replace("@__BAR_BACKGROUND__@", fixed_conf.get("themes")[theme]["bar_background"])
        content = content.replace("@__CODE_BACKGROUND__@", fixed_conf.get("themes")[theme]["code_background"])
        content = content.replace("@__BACKGROUND_COLOR__@", config.get("background_color"))
        content = content.replace("@__FILENAME__@", config.get("filename"))
        content = content.replace("@__LANGUAGE_ICON__@", config.get("language_icon"))

        _save_output_html(content)
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
