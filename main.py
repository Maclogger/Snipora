from pygments import highlight

import HTML.html_creator
import highlighter
import image_creator
from config import Config
from Loaders.TextLoader import TextLoader


def main():
    config = Config()
    loader = TextLoader()
    code: str = loader.to_string({'language': config.get('language')})
    code, styles = highlighter.highlight(code)
    success: bool = HTML.html_creator.create_html(code, styles)
    if success:
        image_creator.generate_image_from_html()


if __name__ == '__main__':
    main()
    print("OK")
