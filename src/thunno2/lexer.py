from thunno2.commands import commands, DIGRAPHS, get_a_function, Void
from thunno2.constants import CONSTANTS
from thunno2.codepage import codepage_index
from thunno2.dictionary import dictionary_codepage

"""Splits Thunno 2 code into tokens to make it easier for the interpreter"""

"""Creative Commons Legal Code

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the
     European Parliament and of the Council of 11 March 1996 on the legal
     protection of databases, and under any national implementation
     thereof, including any amended or successor version of such
     directive); and
vii. other similar, equivalent or corresponding rights throughout the
     world based on applicable law or treaty, and any national
     implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
member of the public at large and to the detriment of Affirmer's heirs and
successors, fully intending that such Waiver shall not be subject to
revocation, rescission, cancellation, termination, or any other legal or
equitable action to disrupt the quiet enjoyment of the Work by the public
as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason
be judged legally invalid or ineffective under applicable law, then the
Waiver shall be preserved to the maximum extent permitted taking into
account Affirmer's express Statement of Purpose. In addition, to the
extent the Waiver is so judged Affirmer hereby grants to each affected
person a royalty-free, non transferable, non sublicensable, non exclusive,
irrevocable and unconditional license to exercise Affirmer's Copyright and
Related Rights in the Work (i) in all territories worldwide, (ii) for the
maximum duration provided by applicable law or treaty (including future
time extensions), (iii) in any current or future medium and for any number
of copies, and (iv) for any purpose whatsoever, including without
limitation commercial, advertising or promotional purposes (the
"License"). The License shall be deemed effective as of the date CC0 was
applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder
of the License, and in such case Affirmer hereby affirms that he or she
will not (i) exercise any of his or her remaining Copyright and Related
Rights in the Work or (ii) assert any associated claims and causes of
action with respect to the Work, in either case contrary to Affirmer's
express Statement of Purpose.

4. Limitations and Disclaimers.

 a. No trademark or patent rights held by Affirmer are waived, abandoned,
    surrendered, licensed or otherwise affected by this document.
 b. Affirmer offers the Work as-is and makes no representations or
    warranties of any kind concerning the Work, express, implied,
    statutory or otherwise, including without limitation warranties of
    title, merchantability, fitness for a particular purpose, non
    infringement, or the absence of latent or other defects, accuracy, or
    the present or absence of errors, whether or not discoverable, all to
    the greatest extent permissible under applicable law.
 c. Affirmer disclaims responsibility for clearing rights of other persons
    that may apply to the Work or any use thereof, including without
    limitation any person's Copyright and Related Rights in the Work.
    Further, Affirmer disclaims responsibility for obtaining any necessary
    consents, permissions or other rights required for any use of the
    Work.
 d. Affirmer understands and acknowledges that Creative Commons is not a
    party to this document and has no duty or obligation with respect to
    this CC0 or use of the Work.
"""


def tokenise(code, expected_end=""):
    index = 0
    ret = []
    while index < len(code):
        char = code[index]
        if char in commands:
            ret.append((char, "command", commands[char]))
        elif char in DIGRAPHS:
            index += 1
            try:
                x = code[index]
                y = char + x
                if y == "µµ":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "recursive environment", r))
                elif y == "µ£":
                    ret.append((y, "print each", 0))
                elif y == "µƲ":
                    index += 1
                    cmd = code[index]
                    if cmd in DIGRAPHS:
                        index += 1
                        cmd += code[index]
                    func = get_a_function(cmd)
                    ret.append((y + cmd, "single function reduce by", func))
                elif y == "µɼ":
                    index += 1
                    cmd = code[index]
                    if cmd in DIGRAPHS:
                        index += 1
                        cmd += code[index]
                    func = get_a_function(cmd)
                    ret.append((y + cmd, "single function right reduce by", func))
                elif y == "µƇ":
                    index += 1
                    cmd = code[index]
                    if cmd in DIGRAPHS:
                        index += 1
                        cmd += code[index]
                    func = get_a_function(cmd)
                    ret.append(
                        (y + cmd, "single function right cumulative reduce by", func)
                    )
                elif y == "µʋ":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "right reduce by", r))
                elif y == "µ€":
                    index += 1
                    cmd = code[index]
                    if cmd in DIGRAPHS:
                        index += 1
                        cmd += code[index]
                    func = get_a_function(cmd)
                    ret.append((y + cmd, "apply to every nth item", func))
                elif y == "µ«":
                    ret.append((y, "rotate stack left", 0))
                elif y == "µ»":
                    ret.append((y, "rotate stack right", 0))
                elif y == "µ!":
                    ret.append((y, "reverse stack", 0))
                elif y == "µÑ":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "adjacent group by", r))
                elif y == "µñ":
                    index += 1
                    cmd = code[index]
                    if cmd in DIGRAPHS:
                        index += 1
                        cmd += code[index]
                    func = get_a_function(cmd)
                    ret.append((y + cmd, "single function adjacent group by", func))
                elif y == "µı":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "nmap", r))
                elif y == "µ²":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "2map", r))
                elif y == "µ³":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "3map", r))
                elif y == "µq":
                    ret.append((y, "quit", 0))
                elif y == "µƘ":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "first integer", r))
                elif y == "µK":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "first n integers", r))
                elif y == "µ¥":
                    i, r = tokenise(code[index + 1 :], expected_end=";")
                    index += i + 1
                    ret.append((y, "while unique", r))
                elif y == "µ‘":
                    compressed_string = ""
                    index += 1
                    try:
                        while code[index] != "‘":
                            compressed_string += code[index]
                            index += 1
                    except:
                        pass
                    ret.append(
                        (
                            y + compressed_string + "‘",
                            "space autofill lowercase dictionary compression",
                            compressed_string,
                        )
                    )
                elif y == "µ’":
                    compressed_string = ""
                    index += 1
                    try:
                        while code[index] != "’":
                            compressed_string += code[index]
                            index += 1
                    except:
                        pass
                    ret.append(
                        (
                            y + compressed_string + "’",
                            "space autofill title case dictionary compression",
                            compressed_string,
                        )
                    )
                else:
                    ret.append((y, "digraph", get_a_function(y)))
            except:
                pass
        elif char in "0123456789.":
            s = char
            index += 1
            try:
                while code[index] in "0123456789.":
                    s += code[index]
                    index += 1
            except:
                pass
            index -= 1
            try:
                while s[0] == "0":
                    ret.append(("0", "number", 0))
                    try:
                        s = s[1:]
                    except:
                        break
                if s == ".":
                    ret.append((".", "number", 0.5))
                else:
                    x = eval(s)
                    if s.endswith("."):
                        x += 0.5
                    ret.append((s, "number", x))
            except:
                pass
        elif char == '"':
            s = char
            index += 1
            try:
                while (code[index] != '"') or (code[index - 1] == "\\"):
                    s += code[index]
                    index += 1
                s += code[index]
            except:
                s += '"'
            try:
                ret.append((s, "string", eval(s).replace("¶", "\n")))
            except:
                ret.append((s, "string", s[1:-1].replace("¶", "\n")))
        elif char == "'":
            index += 1
            try:
                x = code[index]
                ret.append(("'" + x, "one character", x))
            except:
                ret.append(("'", "one character", ""))
        elif char == "`":
            index += 2
            x = code[index - 1 : index + 1]
            if (
                (len(x) != 2)
                or (x[0] not in dictionary_codepage)
                or (x[1] not in dictionary_codepage)
            ):
                ret.append(("`" + x, "two characters", x))
            else:
                ret.append(("`" + x, "one word dictionary compression", x))
        elif char == "ʋ":
            index += 3
            x = code[index - 2 : index + 1]
            try:
                nxt = code[index + 1]
            except:
                nxt = ""
            if (len(x) != 3) or (
                (x[0] not in dictionary_codepage)
                or (x[1] not in dictionary_codepage)
                or (x[2] not in dictionary_codepage)
                or (nxt not in dictionary_codepage)
            ):
                ret.append(("ʋ" + x, "three characters", x))
            else:
                index += 1
                ret.append(("ʋ" + x + nxt, "two words dictionary compression", x + nxt))
        # elif char == "[":
        #     s = char
        #     index += 1
        #     try:
        #         in_string = ""
        #         nests = 1
        #         while nests:
        #             c = code[index]
        #             s += c
        #             if in_string == "" and c in ('"', "'"):
        #                 in_string = c
        #             elif in_string != "" and c == in_string:
        #                 if code[index - 1] != "\\":
        #                     in_string = ""
        #             if in_string == "":
        #                 if c == "[":
        #                     nests += 1
        #                 elif c == "]":
        #                     nests -= 1
        #             index += 1
        #     except:
        #         s += "]"
        #     try:
        #         ret.append((s, "list", eval(s)))
        #     except:
        #         ret.append((s, "list", s))
        # elif char == "]":
        #     ret.append(("]", "list", []))
        elif char == "[":
            r = []
            i, x = tokenise(code[index + 1 :], expected_end=";]")
            index += i + 1
            r.append(x)
            try:
                while code[index] == ";":
                    i, x = tokenise(code[index + 1 :], expected_end=";]")
                    index += i + 1
                    r.append(x)
            except:
                pass
            ret.append((char, "list", r))
        elif char == "#":
            index += 1
            try:
                if code[index] == " ":
                    while code[index] not in "¶\n":
                        index += 1
                elif code[index] == "{":
                    while code[index] != "#" or code[index - 1] != "}":
                        index += 1
            except:
                pass
        elif char == "“":
            compressed_string = ""
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append(
                (
                    char + compressed_string + char,
                    "lowercase alphabetic compression",
                    compressed_string,
                )
            )
        elif char == "”":
            compressed_string = ""
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append(
                (
                    char + compressed_string + char,
                    "title case alphabetic compression",
                    compressed_string,
                )
            )
        elif char == "‘":
            compressed_string = ""
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append(
                (
                    char + compressed_string + char,
                    "lowercase dictionary compression",
                    compressed_string,
                )
            )
        elif char == "’":
            compressed_string = ""
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append(
                (
                    char + compressed_string + char,
                    "title case dictionary compression",
                    compressed_string,
                )
            )
        elif char == "»":
            compressed_string = ""
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append(
                (
                    char + compressed_string + char,
                    "compressed number",
                    compressed_string,
                )
            )
        elif char == "«":
            compressed_string = code[index + 1 : index + 3]
            index += 2
            ret.append(
                (char + compressed_string, "small compressed number", compressed_string)
            )
        elif char == "¿":
            compressed_string = ""
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append(
                (char + compressed_string + char, "compressed list", compressed_string)
            )
        elif char == "¡":
            index += 1
            try:
                var = code[index]
            except:
                var = ""
            ret.append((char + var, "variable get", var))
        elif char == "!":
            index += 1
            try:
                var = code[index]
            except:
                var = ""
            ret.append((char + var, "variable set", var))
        elif char == "€":
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, "single function map", func))
        elif char == "ȷ":
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, "outer product", func))
        elif char == "œ":
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, "single function filter", func))
        elif char == "þ":
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, "single function sort by", func))
        elif char == "ñ":
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, "single function group by", func))
        elif char == "n":
            ret.append((char, "context variable", 0))
        elif char == "ṅ":
            ret.append((char, "iteration index", 0))
        elif char == "x":
            ret.append((char, "get x", 0))
        elif char == "y":
            ret.append((char, "get y", 0))
        elif char == "X":
            ret.append((char, "set x", 0))
        elif char == "Y":
            ret.append((char, "set y", 0))
        elif char == "Ẋ":
            ret.append((char, "set x without popping", 0))
        elif char == "Ẏ":
            ret.append((char, "set y without popping", 0))
        elif char == "ẋ":
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char, "apply to x", func))
        elif char == "ẏ":
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char, "apply to y", func))
        elif char == "Ȥ":
            ret.append((char, "get global array", 0))
        elif char == "ȥ":
            ret.append((char, "add to global array", 0))
        elif char == "K":
            ret.append((char, "stack", 0))
        elif char == "k":
            index += 1
            try:
                if code[index] in CONSTANTS:
                    x = code[index]
                    c = CONSTANTS[x]
                    if type(c) == type(lambda: 0):
                        ret.append((char + x, "callable constant", c))
                    else:
                        ret.append((char + x, "constant", c))
            except:
                pass
        elif char == "ṇ":
            index += 1
            try:
                x = code[index]
                ret.append(
                    (char + x, "codepage compression", next(codepage_index(x)) + 101)
                )
            except:
                pass
        elif char == "$":
            ret.append((char, "next input", 0))
        elif char == "¤":
            ret.append((char, "input list", 0))
        elif char == "°":
            ret.append((char, "first input", 0))
        elif char == "¹":
            ret.append((char, "second input", 0))
        elif char == "⁶":
            ret.append((char, "third input", 0))
        elif char == "⁷":
            ret.append((char, "third last input", 0))
        elif char == "⁸":
            ret.append((char, "second last input", 0))
        elif char == "⁹":
            ret.append((char, "last input", 0))
        elif char == "£":
            ret.append((char, "print", 0))
        elif char == "¢":
            ret.append((char, "print without newline", 0))
        elif char == "ß":
            ret.append((char, "print without popping", 0))
        elif char == "ı":
            i, r = tokenise(code[index + 1 :], expected_end=";")
            index += i + 1
            ret.append((char, "map", r))
        elif char == "æ":
            i, r = tokenise(code[index + 1 :], expected_end=";")
            index += i + 1
            ret.append((char, "filter", r))
        elif char == "Þ":
            i, r = tokenise(code[index + 1 :], expected_end=";")
            index += i + 1
            ret.append((char, "sort by", r))
        elif char == "Ñ":
            i, r = tokenise(code[index + 1 :], expected_end=";")
            index += i + 1
            ret.append((char, "group by", r))
        elif char == "¥":
            i, r = tokenise(code[index + 1 :], expected_end=";")
            index += i + 1
            ret.append((char, "fixed point", r))
        elif char == "Ƙ":
            i, r = tokenise(code[index + 1 :], expected_end=";")
            index += i
            ret.append((char, "first positive integer", r))
        elif char == "Ʋ":
            i, r = tokenise(code[index + 1 :], expected_end=";")
            index += i + 1
            ret.append((char, "cumulative reduce by", r))
        elif char == "{":
            i, r = tokenise(code[index + 1 :], expected_end="}")
            index += i + 1
            ret.append((char, "for loop", r))
        elif char == "(":
            i, r1 = tokenise(code[index + 1 :], expected_end=";)")
            index += i + 1
            r2 = []
            try:
                if code[index] in (";", "}", ":"):
                    i, r2 = tokenise(code[index + 1 :], expected_end=")")
                    index += i
            except:
                pass
            ret.append((char, "while loop", (r1, r2)))
        elif char == "⁽":
            i, r = tokenise(code[index + 1 :], expected_end="⁾")
            index += i + 1
            ret.append((char, "forever loop", r))
        elif char == "?":
            i, r1 = tokenise(code[index + 1 :], expected_end=":;")
            index += i + 1
            r2 = []
            try:
                if code[index] == ":":
                    i, r2 = tokenise(code[index + 1 :], expected_end=";")
                    index += i
            except:
                pass
            ret.append((char, "if statement", (r1, r2)))
        elif char == "Ɓ":
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, "execute without popping", func))
        elif char == "ç":
            try:
                index += 1
                cmd1 = code[index]
                if cmd1 in DIGRAPHS:
                    index += 1
                    cmd1 += code[index]
                func1 = get_a_function(cmd1)
            except:
                func1, cmd1 = Void, ""
            try:
                index += 1
                cmd2 = code[index]
                if cmd2 in DIGRAPHS:
                    index += 1
                    cmd2 += code[index]
                func2 = get_a_function(cmd2)
            except:
                func2, cmd2 = Void, ""
            ret.append((char + cmd1 + cmd2, "pair apply", (func1, func2)))
        elif char == "Ç":
            try:
                index += 1
                cmd1 = code[index]
                if cmd1 in DIGRAPHS:
                    index += 1
                    cmd1 += code[index]
                func1 = get_a_function(cmd1)
            except:
                func1, cmd1 = Void, ""
            try:
                index += 1
                cmd2 = code[index]
                if cmd2 in DIGRAPHS:
                    index += 1
                    cmd2 += code[index]
                func2 = get_a_function(cmd2)
            except:
                func2, cmd2 = Void, ""
            ret.append((char + cmd1 + cmd2, "pair apply dump", (func1, func2)))
        elif char in expected_end:
            return index, ret
        elif char == ":":
            ret.append((":", "command", commands["="]))
            return index, ret
        elif char == "}":
            ret.append(("}", "command", commands["¬"]))
            return index, ret
        index += 1
    return index + 1, ret
