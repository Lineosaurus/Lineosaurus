

def progress_bars(portion, total, pb_char, pb_len):
    return pb_char*round(pb_len*portion/total)


def progress_bars_alternating(portion, total, pb_char_1, pb_char_2, pb_len):
    """
    if `pb_char_1 = 'X'` and `pb_char_2 = 'Y'`, then:
      -> XYXYXYXY...
    """
    bars = ''
    for b in range(round(pb_len*portion/total)):
        if (b%2) == 0: bars += pb_char_1
        else: bars += pb_char_2
    return bars