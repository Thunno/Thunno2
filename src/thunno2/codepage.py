# This codepage is exactly the same as the Jelly codepage
# (https://github.com/DennisMitchell/jellylanguage/blob/master/jelly/interpreter.py#L7)

"""The 256-character Single Byte Character Set for encoding Thunno 2 programs (https://en.wikipedia.org/wiki/SBCS)"""

CODEPAGE = (
    r"""¡¢£¤¥¦©¬®µ½¿€ÆÇÐÑ×ØŒÞßæçðıȷñ÷øœþ !"#$%&'()*+,-./0123456789:;<=>?"""
    r"""@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¶"""
    r"""°¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ƁƇƊƑƓƘⱮƝƤƬƲȤɓƈɗƒɠɦƙɱɲƥʠɼʂƭʋȥẠḄḌẸḤỊḲḶṂṆỌṚṢṬỤṾẈỴẒȦḂ"""
    r"""ĊḊĖḞĠḢİĿṀṄȮṖṘṠṪẆẊẎŻạḅḍẹḥịḳḷṃṇọṛṣṭ§Äẉỵẓȧḃċḋėḟġḣŀṁṅȯṗṙṡṫẇẋẏż«»‘’“”"""
)

assert len(CODEPAGE) == 256


def codepage_index(*chars):
    for char in chars:
        if char in CODEPAGE:
            yield CODEPAGE.index(char)
        else:
            yield -1


def utf8_to_thunno2(string):
    ret = ""
    for char in string:
        if ord(char) < 256:
            ret += CODEPAGE[ord(char)]
        else:
            ret += char
    return ret


def thunno2_to_utf8(string):
    ret = ""
    for char in string:
        if char in CODEPAGE:
            ret += chr(CODEPAGE.index(char))
        else:
            ret += char
    return ret
