

# GAP = 2  # Gap (in spaces) between columns  (not used to simplify the testing)


def card_maker(title, entries, align, lang):
    """align: list[Literal[-1, 1]]: -1 (align column to the left); 1 (align column to the right)"""

    if title == '':
        TITLE = ''
    else:
        TITLE = title + '\n\n'

    nrow = len(entries)     # Number of rows
    ncol = len(entries[0])  # Number of columns
    lens = [max([len(entries[r][c]) for r in range(nrow)]) for c in range(ncol)]  # Length of each column

    lines = []
    for entry in entries:
        line = []
        for ele_idx, ele in enumerate(entry):  # ele: element
            spaces = " "*(lens[ele_idx] - len(ele))
            if align[ele_idx] == -1: line.append(ele + spaces)
            if align[ele_idx] ==  1: line.append(spaces + ele)
        lines.append('  '.join(line))  # 2 spaces between columns
    
    code_block = '\n'.join(lines)

    return (
        TITLE +
        f'```{lang}\n' +
        code_block + '\n' +
        '```'
    )