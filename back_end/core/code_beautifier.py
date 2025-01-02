
def find_first_not_space_char(line: str) -> int:
    for i, character in enumerate(line):
        if character != ' ':
            return i
    return len(line)  # Ak je riadok prázdny alebo obsahuje len medzery

def beautify(code: str) -> str:
    lines = code.splitlines()

    # Nájdeme minimálny počet medzier na začiatku každého riadku
    min_leading_spaces = float('inf')
    for line in lines:
        leading_spaces = len(line) - len(line.lstrip(' '))
        if line.strip():  # Zohľadníme len neprázdne riadky
            min_leading_spaces = min(min_leading_spaces, leading_spaces)

    # Orežeme medzery na začiatku všetkých riadkov na minimálnu hodnotu
    beautified_lines = []
    for line in lines:
        beautified_lines.append(line[min_leading_spaces:])

    return '\n'.join(beautified_lines)
