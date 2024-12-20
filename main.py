import HTML.HtmlCreator
from Loaders.TextLoader import TextLoader


def main():
    loader = TextLoader()
    code: str = loader.to_string({'language': "c#"})
    code = f"{code}"
    # todo: create Lexer, and add styles
    HTML.HtmlCreator.create_html(code)


if __name__ == '__main__':
    main()
    print("OK")
