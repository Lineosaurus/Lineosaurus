

def main(banner_path, banner_alt):

    if banner_path != '':
        header = f'![{banner_alt}]({banner_path})\n\n'
    else:
        header = ''
    header += "_OWNER_'s repos (_LINESFMT_ lines of code, _CMITFMT_ commits, _CHARSFMT_ chars)"

    OPTIONS = {
        'HEADER': header,
        'FOOTER': '<sub>last update: _DATE_ - _CREDIT_</sub>',
        'CARD_ORDER': 'cmit\n',
        'SHOW_CREDIT': 'false',
    }

    return OPTIONS