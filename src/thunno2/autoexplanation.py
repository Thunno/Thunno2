from thunno2.tokens import *
from thunno2.lexer import *


def auto_explain(code, indent=0):
    _, lexed = tokenise(code)
    ret = ""
    index = 0
    for chars, info, other in lexed:
        ret += (
            " " * (index + indent)
            + chars
            + (len(code) - index - len(chars)) * " "
            + "  # "
        )
        if isinstance(other, list):
            ret += info + "\n"
            ret += auto_explain(code[index + 1 :], index + indent + 1)
        elif info not in ("command", "digraph"):
            ret += info + "\n"
        else:
            ret += (
                dict([(j, i) for i, j in full_list[::-1]])[chars].replace("_", " ")
                + "\n"
            )
        index += len(chars)
    return ret
