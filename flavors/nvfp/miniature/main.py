

def main(banner_path, banner_alt):

    if banner_path != '':
        header = (
            f"![{banner_alt}]({banner_path})\n\n"
            "_OWNER_'s repos (_LINESROUND_ lines of code, _CMIT_ commits, _CHARSAPPROX_ chars)"
        )
    else:
        header = (
            "_OWNER_'s repos (_LINESROUND_ lines of code, _CMIT_ commits, _CHARSAPPROX_ chars)"
        )

    OPTIONS = {
        'HEADER': header,
        'FOOTER': '*last update: _DATE_ - _CREDIT_*',
        'CARD_ORDER': 'cmit\n',
        'SHOW_CREDIT': 'false',
    }

    return OPTIONS