import back_end.core.html.html_creator
from back_end.core import highlighter, image_creator, core
from back_end.utilities.json_manager import JsonManager, create_template_config
from front_end.loaders.text_loader import TextLoader


def main():
    code: str = TextLoader().to_string({'language': "java"})
    config = create_template_config("test.json")
    config.set('language', "java")
    config.set('filename', "Test.java")
    config.set('background_color', "#F3F3F3")
    config.set('theme', "lightbulb")
    success: bool = core.run(config, code)
    print(f"Success: {success}")

if __name__ == '__main__':
    main()
