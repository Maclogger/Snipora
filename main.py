import argparse

from front_end.cli import Cli

def main():
    parser = argparse.ArgumentParser(description="Snipora - Code Snippet Generator")
    parser.add_argument("mode", choices=["prompts", "auto"],
                        help="Choose a mode: 'prompts' for manual prompts or 'auto' for automatic generation based on a configfile.")
    args = parser.parse_args()

    cli = Cli()

    if args.mode == "prompts":
        cli.run_with_prompts()
    else:  # This will handle the 'auto' mode
        cli.run_with_auto_prompts()

if __name__ == '__main__':
    main()
