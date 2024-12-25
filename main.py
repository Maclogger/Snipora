import back_end.core.html.html_creator
from back_end.core import highlighter, image_creator, core
from back_end.utilities.json_manager import JsonManager, create_template_config
from front_end.cli import Cli
from front_end.loaders.clipboard_loader import ClipboardLoader
from front_end.loaders.text_loader import TextLoader


if __name__ == '__main__':
    cli = Cli()
    cli.run_with_prompts()
    #main()
