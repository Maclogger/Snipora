from pygments import highlight

import HTML.HtmlCreator
import Highlighter
from Config import Config
from Loaders.TextLoader import TextLoader


def main():
    config = Config()
    loader = TextLoader()
    code: str = loader.to_string({'language': config.get('language')})
    code, styles = Highlighter.highlight(code)
    HTML.HtmlCreator.create_html(code, styles)

if __name__ == '__main__':
    main()
    print("OK")
