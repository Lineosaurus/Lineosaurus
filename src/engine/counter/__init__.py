import os

from mykit.kit.pLog import pL
from mykit.kit.utils import merging_dicts, add_dict_val

from src.constants import NON_TEXT_FILENAME, NON_TEXT_TYPE


## Note: not sure if total_char_in(file) will always equal to size(file)?  ~Nicholas@20230806


def counter(ONLY_TYPE, IGNORE_TYPE, dir_path):

    line_per_ext = {}  # For cards: line/type
    size_per_ext = {}  # For cards: size
    char_per_ext = {}  # For cards: char
    file_per_ext = {}  # For cards: file

    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)
        ext = os.path.splitext(name)[1].lower()

        if os.path.isfile(path):
            if (name.lower() in NON_TEXT_FILENAME) or (ext in NON_TEXT_TYPE):
                pass
            else:

                ## Gate
                if ONLY_TYPE is not None:
                    if ext not in ONLY_TYPE: continue
                else:
                    if IGNORE_TYPE is not None:
                        if ext in IGNORE_TYPE: continue

                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        text = f.read()
                except Exception as err:
                    pL.error(f'path: {repr(path)}  err: {err}')

                LINE = len(text.split('\n'))
                SIZE = os.path.getsize(path)
                CHAR = len(text)

                add_dict_val(line_per_ext, ext, LINE, LINE)
                add_dict_val(size_per_ext, ext, SIZE, SIZE)
                add_dict_val(char_per_ext, ext, CHAR, CHAR)
                add_dict_val(file_per_ext, ext, 1   , 1)
        else:
            _line_per_ext, _size_per_ext, _char_per_ext, _file_per_ext = counter(ONLY_TYPE, IGNORE_TYPE, path)
            merging_dicts(line_per_ext, _line_per_ext)
            merging_dicts(size_per_ext, _size_per_ext)
            merging_dicts(char_per_ext, _char_per_ext)
            merging_dicts(file_per_ext, _file_per_ext)

    return line_per_ext, size_per_ext, char_per_ext, file_per_ext