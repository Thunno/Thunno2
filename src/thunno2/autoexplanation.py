from thunno2.tokens import *
from thunno2.lexer import *


def auto_explain(code, indent=0, comment_indent=0, tkn=True, post_indent=0):
    if tkn:
        _, lexed = tokenise(code)
    else:
        lexed = code
    ret = ""
    index = 0
    for chars, info, other in lexed:
        if "single function" in info or info in (
            "outer product",
            "apply to x",
            "apply to y",
            "execute without popping",
            "apply to every nth item",
        ):
            if len(chars) == 2:
                i = 1
            elif len(chars) == 4:
                i = 2
            else:
                if chars[-2] in DIGRAPHS:
                    i = 2
                else:
                    i = 1
            ret += (
                " " * (index + indent)
                + chars[:-i]
                + (len(code) - index - len(chars) + i) * " "
                + post_indent * " "
                + "  # "
                + " " * comment_indent
                + info
                + ":\n"
                + " " * (index + indent + len(chars) - i)
                + chars[-i:]
                + (len(code) - index - len(chars)) * " "
                + post_indent * " "
                + "  #  "
                + " " * comment_indent
            )
            ret += other.keywords[0] + "\n"
        else:
            ret += (
                " " * (index + indent)
                + chars
                + (len(code) - index - len(chars)) * " "
                + post_indent * " "
                + "  # "
                + " " * comment_indent
            )
            if isinstance(other, list):
                ret += info + ":\n"
                ret += auto_explain(
                    code[index + 1 :], index + indent + 1, comment_indent + 1
                )
            elif info == "if statement":
                t, f = other
                ret += info + ":\n"
                ret += auto_explain(
                    t,
                    index + indent + 1,
                    comment_indent + 1,
                    False,
                    len(code) - len("".join(x[0] for x in t)) - index - 1,
                )
                index += len("".join(x[0] for x in t)) + 1
                if f:
                    ret += (
                        " " * (index + indent)
                        + ":"
                        + (len(code) - index - 1) * " "
                        + post_indent * " "
                        + "  # "
                        + " " * comment_indent
                        + "else:\n"
                    )
                    ret += auto_explain(
                        f,
                        index + indent + 1,
                        comment_indent + 1,
                        False,
                        len(code) - len("".join(x[0] for x in f)) - index - 1,
                    )
                    index += len("".join(x[0] for x in f)) + 1
            elif info not in ("command", "digraph"):
                ret += info + "\n"
            else:
                ret += (
                    dict([(j, i) for i, j in full_list[::-1]])[chars].replace("_", " ")
                    + "\n"
                )
        index += len(chars)
    return ret
