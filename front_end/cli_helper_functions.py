def get_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Získa od užívateľa celé číslo."""
    while True:
        try:
            num = int(input(f"{prompt}: "))
            if min_val is not None and num < min_val:
                print(f"Číslo musí byť >= {min_val}")
                continue
            if max_val is not None and num > max_val:
                print(f"Číslo musí byť <= {max_val}")
                continue
            return num
        except ValueError:
            print("Zadajte platné celé číslo")

def get_float(prompt: str, min_val: float = None, max_val: float = None) -> float:
    """Získa od užívateľa desatinné číslo."""
    while True:
        try:
            num = float(input(f"{prompt}: ").replace(',', '.'))
            if min_val is not None and num < min_val:
                print(f"Číslo musí byť >= {min_val}")
                continue
            if max_val is not None and num > max_val:
                print(f"Číslo musí byť <= {max_val}")
                continue
            return num
        except ValueError:
            print("Zadajte platné desatinné číslo")

def get_string(prompt: str, min_length: int = 0, max_length: int = 100) -> str:
    """Získa od užívateľa text."""
    while True:
        text = input(f"{prompt}: ").strip()
        if min_length <= len(text) <= max_length:
            return text
        print(f"Text musí mať {min_length} až {max_length} znakov")

def get_boolean(prompt: str) -> bool:
    """Získa od užívateľa boolean ako 0/1."""
    print(f"\n{prompt}")
    print("[0]: Nie")
    print("[1]: Áno")
    return bool(get_int("Vaša voľba", 0, 1))

def get_choice(prompt: str, options: list) -> int:
    """Získa od užívateľa výber z možností."""
    print(f"\n{prompt}")
    for i, option in enumerate(options):
        print(f"[{i}]: {option}")
    return get_int("Vaša voľba: ", 0, len(options) - 1)
