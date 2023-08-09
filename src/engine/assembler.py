from src.constants import __version__


CREDIT = f'Counted by [Lineosaurus v{__version__}](https://github.com/nvfp/Line-O-Saurus)'


def assembler(header, custom_title, cards, footer, show_credit, auto_line_break):

    sections = []

    if header != '':
        sections.append(header)

    if custom_title != '':
        sections.append(custom_title)

    if cards != '':
        sections.append(cards)

    if footer != '':
        sections.append(footer)

    if show_credit:
        sections.append(CREDIT)

    if auto_line_break:
        return '\n\n'.join(sections)
    else:
        return ''.join(sections)