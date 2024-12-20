from pygments import highlight

import HTML.HtmlCreator
import Highlighter
from Loaders.TextLoader import TextLoader


def main():
    loader = TextLoader()
    code: str = loader.to_string({'language': "java"})
    code, styles = Highlighter.highlight(code)
    HTML.HtmlCreator.create_html(code, styles)

if __name__ == '__main__':
    main()
    print("OK")
