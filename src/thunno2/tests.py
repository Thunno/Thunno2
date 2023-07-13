from thunno2.commands import *

"""Here we test every command implemented in the commands dictionary"""

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

tests_counter = 0
tested_commands = []

UNTESTABLE = [
    "ɼ",
    "øv",
    "øV",
    "ø^",
    "µr",
    "ÆC",
    "ÆD",
    "ÆE",
    "ÆL",
    "ÆN",
    "ÆR",
    "ÆS",
    "ÆT",
    "Æc",
    "Æl",
    "Æs",
    "Æt",
    "Æḷ",
]


def call(cmd, *stk):
    ctx.stack = Stack(stk)
    ctx.warnings = True
    tested_commands.append(cmd)
    return get_a_function(cmd)()


def assert_eq(a, *b):
    global tests_counter
    tests_counter += 1
    #                  Because 1 == True
    #                  but '1' != 'True'
    #               (we don't want booleans)
    #                         ↓↓
    assert a == b and repr(a) == repr(b), f"\n\nTest {tests_counter}\n{a!r} != {b!r}"


# A

assert_eq(call("A", -1), 1)
assert_eq(call("A", 1.23), 1.23)
assert_eq(call("A", [-1, 2.3, [-4.56]]), [1, 2.3, [4.56]])
assert_eq(call("A", [[[[[[-123.456]]]]]]), [[[[[[123.456]]]]]])

assert_eq(call("A", "abc"), 1)
assert_eq(call("A", "123"), 0)
assert_eq(call("A", ""), 0)
assert_eq(call("A", ["a", ["b", ["1", ["2"]]]]), [1, [1, [0, [0]]]])

assert_eq(call("A", ["abc", 123, "123", -0.123]), [1, 123, 0, 0.123])

# B

assert_eq(call("B", 2, 12), [1, 1, 0, 0])
assert_eq(call("B", [100, 1000], 12345), [[1, 23, 45], [12, 345]])
assert_eq(
    call("B", [0, 1, 2], [5, 10, 15]),
    [[5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1]],
)

assert_eq(call("B", "12", 12), "2211")
assert_eq(call("B", ["ab", "cde", "fghi"], [12, 34, 56]), ["bbaa", "dced", "ihf"])

assert_eq(call("B", 2, "abcdefghijkl"), [1, 1, 0, 0])
assert_eq(call("B", [0, 1, 2, 3], "zyxwv"), ["5", "00000", [1, 0, 1], [1, 2]])

assert_eq(call("B", "56", "abcdefghijkl"), "6655")
assert_eq(call("B", ["ab", "cde", "fghi"], "acegikmoqsuwy"), ["bbab", "ddd", "ig"])

# C

assert_eq(call("C", 65), "A")
assert_eq(call("C", [104, 101, 108, 108, 111]), ["h", "e", "l", "l", "o"])
assert_eq(call("C", [97, [66, [99, [68, [101]]]]]), ["a", ["B", ["c", ["D", ["e"]]]]])

assert_eq(call("C", "hello"), [104, 101, 108, 108, 111])
assert_eq(
    call("C", ["abc", ["def", ["ghi"]]]),
    [[97, 98, 99], [[100, 101, 102], [[103, 104, 105]]]],
)

assert_eq(
    call("C", ["a", [97], "b", [98], "c", [99]]),
    [[97], ["a"], [98], ["b"], [99], ["c"]],
)

# D

assert_eq(call("D", 10), 10, 10)
assert_eq(call("D", "abc"), "abc", "abc")
assert_eq(call("D", [1, 2, 3]), [1, 2, 3], [1, 2, 3])

# E

assert_eq(call("E", 12), 1)
assert_eq(call("E", [1, 2, 3, 4, 5]), [0, 1, 0, 1, 0])

assert_eq(call("E", "[*range(5)]"), [0, 1, 2, 3, 4])
assert_eq(call("E", ["abc", "[1, 2, 3]"]), [0, [1, 2, 3]])

assert_eq(call("E", ["12", 12, "34", 34]), [12, 1, 34, 1])

# F

assert_eq(call("F", 24), [1, 2, 3, 4, 6, 8, 12, 24])
assert_eq(
    call("F", [5, 10, 15, 20]),
    [[1, 5], [1, 2, 5, 10], [1, 3, 5, 15], [1, 2, 4, 5, 10, 20]],
)

assert_eq(
    call("F", "abcde"),
    [
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "b",
        "bc",
        "bcd",
        "bcde",
        "c",
        "cd",
        "cde",
        "d",
        "de",
        "e",
    ],
)
assert_eq(
    call("F", ["abc", "def", "ghi"]),
    [
        ["a", "ab", "abc", "b", "bc", "c"],
        ["d", "de", "def", "e", "ef", "f"],
        ["g", "gh", "ghi", "h", "hi", "i"],
    ],
)

assert_eq(call("F", [10, "abc"]), [[1, 2, 5, 10], ["a", "ab", "abc", "b", "bc", "c"]])

# G

assert_eq(call("G", 123), 3)
assert_eq(call("G", -6.54), 6)

assert_eq(call("G", "abc"), "c")
assert_eq(call("G", ""), "")

assert_eq(call("G", [1, 2, 3]), 3)
assert_eq(call("G", ["a", 2, "c"]), ["a", 2, "c"])

# H

assert_eq(call("H", 81), 129)
assert_eq(call("H", "A0"), 160)

assert_eq(call("H", [12, "34", 56]), [18, 52, 86])
assert_eq(
    call("H", [1234, [5678, ["9ABC", ["DEF0"]]]]), [4660, [22136, [39612, [57072]]]]
)

# I

assert_eq(call("I", 10, 5), [5, 6, 7, 8, 9, 10])
assert_eq(call("I", -3, 3), [3, 2, 1, 0, -1, -2, -3])

assert_eq(call("I", 2, [0, 2, 4, 6, 8, 10]), [0, 4, 8])
assert_eq(call("I", [0, 2, 4, 6, 8, 10], 9), [0])

assert_eq(call("I", 1, "abc"), "abc")
assert_eq(call("I", "abc", 2), "ac")

assert_eq(call("I", "abc", "def"), "daebfc")
assert_eq(call("I", "abcxyz", "def"), "daebfcxyz")

assert_eq(call("I", [1, 2, 3], [4, 5, 6]), [4, 1, 5, 2, 6, 3])
assert_eq(call("I", [1], [2, 3, 4, 5, 6]), [2, 1, 3, 4, 5, 6])

# J

assert_eq(call("J", 10), "10")

assert_eq(call("J", "abc"), "abc")

assert_eq(call("J", [1, 2, 3]), "123")
assert_eq(call("J", ["a", 2, "c"]), "a2c")
assert_eq(call("J", [[1, 2, 3], ["a", "b", "c"]]), "123abc")

# L

assert_eq(call("L", 10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
assert_eq(call("L", -5), [0, -1, -2, -3, -4])
assert_eq(
    call("L", [-3, -2, -1, 0, 1, 2, 3]),
    [[0, -1, -2], [0, -1], [0], [], [0], [0, 1], [0, 1, 2]],
)

assert_eq(call("L", "ABCDE"), "abcde")
assert_eq(call("L", ["aBc", "DeF", "gHi", "JkL"]), ["abc", "def", "ghi", "jkl"])

assert_eq(
    call("L", [5, "abc", 10, "DEF"]),
    [[0, 1, 2, 3, 4], "abc", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "def"],
)

# M

assert_eq(call("M", 123), 1)
assert_eq(call("M", -6.54), 4)

assert_eq(call("M", "abc"), "a")
assert_eq(call("M", ""), "")

assert_eq(call("M", [1, 2, 3]), 1)
assert_eq(call("M", ["a", 2, "c"]), ["a", 2, "c"])

# N

assert_eq(call("N", 1.23), 1)
assert_eq(call("N", 123), 123)
assert_eq(call("N", [1.23, -4.56, 789.0]), [1, -4, 789])

assert_eq(call("N", "123"), 123)
assert_eq(call("N", "abc"), "abc")
assert_eq(call("N", ["123", "456", "abc"]), [123, 456, "abc"])

assert_eq(call("N", [1.23, "456", 7.89, "abc"]), [1, 456, 7, "abc"])

# O

assert_eq(call("O", 10), 1024)
assert_eq(call("O", [-1, 0, 1, 2]), [0.5, 1, 2, 4])

assert_eq(call("O", "abc def ghi jkl"), ["abc", "def", "ghi", "jkl"])
assert_eq(
    call("O", ["abc def", "ghi jkl", "mno pqr"]),
    [["abc", "def"], ["ghi", "jkl"], ["mno", "pqr"]],
)

assert_eq(call("O", ["abc def ghi", 5, 7]), [["abc", "def", "ghi"], 32, 128])

# P

assert_eq(call("P", 7), 1)
assert_eq(call("P", 10), 0)
assert_eq(call("P", [-3, -2, -1, 0, 1, 2, 3, 4]), [0, 0, 0, 0, 0, 1, 1, 0])

assert_eq(call("P", "Abc"), "aBC")
assert_eq(call("P", "DeF?!gHi"), "dEf?!GhI")
assert_eq(call("P", ["abc", "DEF", "ghi"]), ["ABC", "def", "GHI"])

assert_eq(call("P", [2.34, "", -1.23, "XyZ"]), [1, "", 0, "xYz"])

# Q

assert_eq(call("Q", 1, 2), 1)
assert_eq(call("Q", 2, 2), 0)
assert_eq(call("Q", [1, 2, 3], [1, 3, 5]), [0, 1, 1])

assert_eq(call("Q", "abc", 2), 1)
assert_eq(call("Q", ["abc", "def", "ghi"], 2), [1, 1, 1])

assert_eq(call("Q", "abc", "abc"), 0)
assert_eq(call("Q", "abc", "def"), 1)
assert_eq(call("Q", ["abc", "def", "ghi"], ["abc", "xyz", "ghi"]), [0, 1, 0])

# R

assert_eq(call("R", 5), [1, 2, 3, 4, 5])
assert_eq(call("R", 1.23), [1])
assert_eq(call("R", -5), [-1, -2, -3, -4, -5])
assert_eq(call("R", [-2, -1, 0, 1, 2]), [[-1, -2], [-1], [], [1], [1, 2]])

assert_eq(call("R", "abcde"), "ABCDE")
assert_eq(call("R", ["aBc", "DeF", "gHi", "JkL"]), ["ABC", "DEF", "GHI", "JKL"])

assert_eq(
    call("R", [5, "abc", 10, "DEF"]),
    [[1, 2, 3, 4, 5], "ABC", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "DEF"],
)

# S

assert_eq(call("S", 123), 6)
assert_eq(call("S", -4.56), 15)

assert_eq(call("S", [1, 2, 3]), 6)
assert_eq(call("S", [4, 5, 6]), 15)

assert_eq(call("S", "abc"), "abc")
assert_eq(call("S", ["abc", 123, 456]), "abc123456")

# T

assert_eq(call("T"), 10)

# U

assert_eq(call("U", 123), 123)
assert_eq(call("U", -1.2123), -1.23)

assert_eq(call("U", "abcdcba"), "abcd")
assert_eq(call("U", "zyxzyxzyxw"), "zyxw")

assert_eq(call("U", [1, 2, 3, 2, 1]), [1, 2, 3])
assert_eq(call("U", [123, "abc", 123, "abc"]), [123, "abc"])
assert_eq(call("U", []), [])

# V

assert_eq(call("V", 123.456), 123)
assert_eq(call("V", -1.23), -1)
assert_eq(call("V", 456.789), 457)

assert_eq(call("V", "Abc, Def?"), "Nop, Qrs?")
assert_eq(call("V", "..."), "...")

assert_eq(call("V", ["abc", 1.0, "", "def", 0]), [0, 1, 3])

# W

assert_eq(call("W", 1), [1])
assert_eq(call("W", "abc"), ["abc"])
assert_eq(call("W", [1, "a"]), [[1, "a"]])

# Z

assert_eq(call("Z", 3, 5), [[5, 1], [5, 2], [5, 3]])
assert_eq(call("Z", -3.45, 0.2), [[0.2, -1], [0.2, -2], [0.2, -3]])

assert_eq(call("Z", "abc", 5), [[1, "a"], [2, "b"], [3, "c"]])
assert_eq(call("Z", "xyz", -2.34), [[-1, "x"], [-2, "y"]])

assert_eq(call("Z", [7, 8, 9], 5), [[1, 7], [2, 8], [3, 9]])
assert_eq(call("Z", ["abc", "def", "ghi"], -2.34), [[-1, "abc"], [-2, "def"]])

assert_eq(call("Z", 5, "abc"), [["a", 1], ["b", 2], ["c", 3]])
assert_eq(call("Z", -2.34, "xyz"), [["x", -1], ["y", -2]])

assert_eq(call("Z", 5, [7, 8, 9]), [[7, 1], [8, 2], [9, 3]])
assert_eq(call("Z", -2.34, ["abc", "def", "ghi"]), [["abc", -1], ["def", -2]])

assert_eq(call("Z", "abc", "def"), [["d", "a"], ["e", "b"], ["f", "c"]])
assert_eq(call("Z", "abc", [1, 2, 3, 4]), [[1, "a"], [2, "b"], [3, "c"]])

assert_eq(
    call("Z", [9, 8, 7, 6], ["abc", "def", "ghi"]), [["abc", 9], ["def", 8], ["ghi", 7]]
)
assert_eq(call("Z", [1, 2, 3, 4], "abc"), [["a", 1], ["b", 2], ["c", 3]])

# a

assert_eq(call("a", 2, 1), [1, 2])
assert_eq(call("a", "abc", "def"), ["d", "e", "f", "abc"])

assert_eq(call("a", 5, [1, 2, 3, 4]), [1, 2, 3, 4, 5])
assert_eq(call("a", "ghi", ["abc", "def"]), ["abc", "def", "ghi"])

# b

assert_eq(call("b", 2, "1100"), 12)
assert_eq(call("b", [0, 1, 2], ["5", "0000000000", "1111"]), ["5", 10, 15])

assert_eq(call("b", "12", "2211"), 12)
assert_eq(call("b", ["ab", "cde", "fghi"], ["bbaa", "dced", "ihf"]), [12, 34, 56])

# c

assert_eq(call("c", 5, 10), 252)
assert_eq(call("c", 10, 20), 184756)

assert_eq(call("c", "abc", "abcbabcbabcba"), 3)
assert_eq(call("c", [123, 321], "1232123212321"), [3, 3])

assert_eq(call("c", 1, [1, 2, 3, 2, 1, 2, 3]), 2)
assert_eq(call("c", [1, "a"], [1, "a", 1, "b", 1, "c"]), [3, 1])

# d

assert_eq(call("d", 123), [1, 2, 3])
assert_eq(call("d", [-1.23, 1.23]), [[1, 2, 3], [1, 2, 3]])

assert_eq(call("d", "abc"), ["a", "b", "c"])
assert_eq(
    call("d", ["abc", "def", "ghi"]),
    [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
)

assert_eq(
    call("d", [123, "abc", 456, "def"]),
    [[1, 2, 3], ["a", "b", "c"], [4, 5, 6], ["d", "e", "f"]],
)

# e

assert_eq(call("e", 5), 100000)
assert_eq(call("e", [1, 2, 3, 4, 5]), [10, 100, 1000, 10000, 100000])

assert_eq(call("e", "abc,def,ghi"), ["abc", "def", "ghi"])
assert_eq(call("e", ["abc,def", "123,456"]), [["abc", "def"], ["123", "456"]])

assert_eq(
    call("e", ["123,456", -2, "abc,def", 2]),
    [["123", "456"], 0.01, ["abc", "def"], 100],
)

# f

assert_eq(call("f", 100), [2, 2, 5, 5])
assert_eq(call("f", 30), [2, 3, 5])
assert_eq(call("f", [20, 25, 30, 35]), [[2, 2, 5], [5, 5], [2, 3, 5], [5, 7]])

assert_eq(call("f", "AbCd EfGh"), [1, 0, 1, 0, -1, 1, 0, 1, 0])
assert_eq(call("f", ["Abc", "dEf", "!?."]), [[1, 0, 0], [0, 1, 0], [-1, -1, -1]])

assert_eq(call("f", [123, "aBc"]), [[3, 41], [0, 1, 0]])

# g

assert_eq(call("g", 369), 3)

assert_eq(call("g", "!@£$"), 1)

assert_eq(call("g", [10, 15, 20, "abc"]), 5)

# h

assert_eq(call("h", 123), 1)

assert_eq(call("h", "abc"), "a")

assert_eq(call("h", [1, 2, 3]), 1)
assert_eq(call("h", []), [])

# i

assert_eq(call("i", 5, 1234567), 6)

assert_eq(call("i", [1, 2, 3], 2), 3)
assert_eq(
    call("i", [2, 4, 6], ["abc", "def", "ghi", "jkl", "mno"]), ["ghi", "mno", "def"]
)

assert_eq(call("i", 10, "abcd"), "c")

assert_eq(call("i", "abcde", "abc"), "c")

# j

assert_eq(call("j", "abc", [1, 2, 3, 4, 5]), "1abc2abc3abc4abc5")

assert_eq(call("j", 0, "abc"), "a0b0c")

assert_eq(call("j", "xyz", 123), "1xyz2xyz3")

# l

assert_eq(call("l", 123), 3)
assert_eq(call("l", 1.234), 5)

assert_eq(call("l", "abcd"), 4)
assert_eq(call("l", ""), 0)

assert_eq(call("l", [1, 2, 3]), 3)
assert_eq(call("l", [["a"]]), 1)

# m

assert_eq(call("m", -1.23), 2.0)

assert_eq(call("m", "abc"), 98.0)

assert_eq(call("m", [1, 2, 3, 4]), 2.5)
assert_eq(call("m", []), 0)

# o

assert_eq(call("o", 234, 12345), 15)
assert_eq(call("o", 0.12, -123.45), -123.45)

assert_eq(call("o", "a", "abcbabcba"), "bcbbcb")
assert_eq(call("o", 0, "abcb0bcba"), "abcbbcba")

assert_eq(call("o", 2, [1, 2, 3, 2, 1]), [1, 3, 1])
assert_eq(call("o", ["abc", "def", "ghi"], "abc"), ["def", "ghi"])

# p

assert_eq(call("p", 1234), 24)
assert_eq(call("p", -13.579), 945)

assert_eq(call("p", "abc"), 941094)

assert_eq(call("p", [1, 2, "abc", 3]), 6)

# r

assert_eq(call("r", 1.23), 32.1)
assert_eq(call("r", -456), "654-")
assert_eq(call("r", 3210), 123)

assert_eq(call("r", "abcd"), "dcba")
assert_eq(call("r", ""), "")

assert_eq(call("r", [1, 2, 3, 4]), [4, 3, 2, 1])
assert_eq(call("r", [123, "abc", 456, "def"]), ["def", 456, "abc", 123])

# s

assert_eq(call("s", 1, 2), 1, 2)
assert_eq(call("s", "abc", "def"), "abc", "def")
assert_eq(call("s", [1, 2, 3], 4), [1, 2, 3], 4)

# t

assert_eq(call("t", 123), 3)

assert_eq(call("t", "abc"), "c")

assert_eq(call("t", [1, 2, 3]), 3)
assert_eq(call("t", []), [])

# u

assert_eq(call("u"), -1)

# v

assert_eq(call("v", 123, 456, 1234567890), "1231237890")
assert_eq(call("v", 123, "abc", "abcdefghi"), "123defghi")
assert_eq(call("v", "", "a", "abcbabcba"), "bcbbcb")

assert_eq(call("v", 0, 1, [1, 2, 1, 2, 1]), [0, 2, 0, 2, 0])
assert_eq(call("v", 123, "abc", [1, 2, 1, 2, 1]), [1, 2, 1, 2, 1])

# w

assert_eq(call("w", 5), 120)
assert_eq(call("w", [-1, 0, 1, 2, 3]), [1, 1, 1, 2, 6])

assert_eq(call("w", "a\t b\r\n c"), "abc")
assert_eq(call("w", ["a b \n c", "d\t e\nf"]), ["abc", "def"])

assert_eq(call("w", [10, "a b \n c \t d"]), [3628800, "abcd"])

# z

assert_eq(call("z", 12345), [[1, 3, 5], [2, 4]])
assert_eq(call("z", -6.789), [[6, 8], [7, 9]])

assert_eq(call("z", "abcdef"), ["ace", "bdf"])
assert_eq(call("z", "xyz"), ["xz", "y"])

assert_eq(call("z", [1, 2, 3, 4]), [[1, 3], [2, 4]])
assert_eq(call("z", []), [[], []])

# Ȧ

assert_eq(call("Ȧ", 0.0), 0)
assert_eq(call("Ȧ", -1), 1)

assert_eq(call("Ȧ", "abcd1234"), 1)
assert_eq(call("Ȧ", "xyz?"), 0)

assert_eq(call("Ȧ", [0.0, "", "abc"]), 1)
assert_eq(call("Ȧ", ["", 0, []]), 0)

# Ḃ

assert_eq(call("Ḃ", 1010), 10)
assert_eq(call("Ḃ", [11001, 10101, 10011]), [25, 21, 19])

assert_eq(call("Ḃ", "11111"), 31)
assert_eq(call("Ḃ", ["1", 10, "11", 100, "101"]), [1, 2, 3, 4, 5])

# Ċ

assert_eq(call("Ċ", 200), "Ṁ")
assert_eq(call("Ċ", [500, 1000, 1500]), ["ṡ", "ċ", "ṇ"])

assert_eq(call("Ċ", "abcd"), [97, 98, 99, 100])
assert_eq(call("Ċ", ["abcd", "ĖḞĠḢ"]), [[97, 98, 99, 100], [194, 195, 196, 197]])

assert_eq(call("Ċ", [1, "2", 3, "4"]), ["¢", [50], "¤", [52]])

# Ḋ

assert_eq(call("Ḋ", 3, 6), 1)
assert_eq(call("Ḋ", 2, 5), 0)
assert_eq(call("Ḋ", [1, 2, 3, 4, 5], 10), [1, 1, 0, 0, 1])

assert_eq(call("Ḋ", "abc", 12), 1)
assert_eq(call("Ḋ", 5, "abcdefgh"), 0)
assert_eq(call("Ḋ", "abc", "abcdef"), 1)

# Ė

assert_eq(call("Ė", 10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert_eq(call("Ė", -5), [0, -1, -2, -3, -4, -5])

assert_eq(call("Ė", "abcd"), [[0, "a"], [1, "b"], [2, "c"], [3, "d"]])
assert_eq(call("Ė", ""), [])

assert_eq(call("Ė", [123, 456, 789]), [[0, 123], [1, 456], [2, 789]])
assert_eq(call("Ė", ["abc", "def", "ghi"]), [[0, "abc"], [1, "def"], [2, "ghi"]])

# Ḟ

assert_eq(call("Ḟ", 1234), 1234)
assert_eq(call("Ḟ", "abcd"), "abcd")

assert_eq(call("Ḟ", [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
assert_eq(
    call("Ḟ", [["abc", "def"], [1, 2, 3], ["ghi", "jkl"], [4, 5, 6]]),
    ["abc", "def", 1, 2, 3, "ghi", "jkl", 4, 5, 6],
)

assert_eq(call("Ḟ", [0, [1, [2, [3, [4, [5]]]]], 6]), [0, 1, 2, 3, 4, 5, 6])

# Ġ

assert_eq(call("Ġ", 12, 21), 3)
assert_eq(call("Ġ", [10, 12, 14, 16, 18, 20], 8), [2, 4, 2, 8, 2, 4])

assert_eq(call("Ġ", "ABC", 20), [5, 2, 1])

# Ḣ

assert_eq(call("Ḣ", 123), 23, 1)

assert_eq(call("Ḣ", "abc"), "bc", "a")

assert_eq(call("Ḣ", [1, 2, 3]), [2, 3], 1)
assert_eq(call("Ḣ", []), [])

# İ

assert_eq(call("İ", 5, 1234567), 5)

assert_eq(call("İ", [1, 2, 3], 2), 2)
assert_eq(
    call("İ", [2, 4, 6], ["abc", "def", "ghi", "jkl", "mno"]), ["def", "jkl", "abc"]
)

assert_eq(call("İ", 10, "abcd"), "b")

assert_eq(call("İ", "abcde", "abc"), "b")

# Ŀ

assert_eq(call("Ŀ", 5, "a", "abc"), "abcaa")
assert_eq(
    call("Ŀ", [-3, -2, -1, 0, 1, 2, 3], "def", "x"),
    ["xdd", "xd", "x", "x", "x", "xd", "xdd"],
)
assert_eq(
    call("Ŀ", [5, 6, 7, 8], ["abc", "def", "ghi", ""], "xyz"),
    ["xyzaa", "xyzddd", "xyzgggg", "xyz     "],
)

# Ṁ

assert_eq(call("Ṁ", 123.1231), 1)
assert_eq(call("Ṁ", 456), 4)

assert_eq(call("Ṁ", "cbbaaa"), "a")
assert_eq(call("Ṁ", ""), "")

assert_eq(call("Ṁ", [4, 7, 5, 5, 1, 3, 8, 6, 2, 1, 3, 8, 3, 2, 9]), 3)

# Ṅ

assert_eq(call("Ṅ", 123), -123)
assert_eq(call("Ṅ", [-3, -2, -1, 0, 1, 2, 3]), [3, 2, 1, 0, -1, -2, -3])
assert_eq(
    call("Ṅ", [-1.23, [2.34, [-3.45, [4.56, [-5.67, [6.78, [-7.89]]]]]]]),
    [1.23, [-2.34, [3.45, [-4.56, [5.67, [-6.78, [7.89]]]]]]],
)

assert_eq(call("Ṅ", "abbcccbba"), [1, 2, 3, 2, 1])
assert_eq(call("Ṅ", ["aab", "aba", "baa"]), [[2, 1], [1, 1, 1], [1, 2]])

# Ȯ

assert_eq(call("Ȯ", 2, 123), 1)
assert_eq(call("Ȯ", 4, 123), -1)

assert_eq(call("Ȯ", "abc", "cbabcba"), 2)
assert_eq(call("Ȯ", 8, [4, 7, 5, 5, 1, 3, 8, 6, 2, 1, 3, 8, 3, 2, 9]), 6)

# Ṗ

assert_eq(
    call("Ṗ", 5, 3),
    [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 1],
        [2, 2],
        [2, 3],
        [2, 4],
        [2, 5],
        [3, 1],
        [3, 2],
        [3, 3],
        [3, 4],
        [3, 5],
    ],
)
assert_eq(
    call("Ṗ", "def", "abc"),
    [
        ["a", "d"],
        ["a", "e"],
        ["a", "f"],
        ["b", "d"],
        ["b", "e"],
        ["b", "f"],
        ["c", "d"],
        ["c", "e"],
        ["c", "f"],
    ],
)
assert_eq(
    call("Ṗ", 3, ["abc", "def", "ghi"]),
    [
        ["abc", 1],
        ["abc", 2],
        ["abc", 3],
        ["def", 1],
        ["def", 2],
        ["def", 3],
        ["ghi", 1],
        ["ghi", 2],
        ["ghi", 3],
    ],
)

# Ṙ

assert_eq(call("Ṙ", 123), "123")
assert_eq(call("Ṙ", "abc"), '"abc"')
assert_eq(call("Ṙ", '"abc"'), '"\\"abc\\""')
assert_eq(call("Ṙ", [123, ['"abc"', "'abc'"]]), '[123, ["\\"abc\\"", "\'abc\'"]]')

# Ṡ

assert_eq(call("Ṡ", 456.321), 123456)

assert_eq(call("Ṡ", "Thunno 2 is the best!"), "    !2Tbeehhinnossttu")
assert_eq(
    call("Ṡ", [4, 7, 5, 5, 1, 3, 8, 6, 2, 1, 3, 8, 3, 2, 9]),
    [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9],
)

# Ṫ

assert_eq(call("Ṫ", 123), 12, 3)

assert_eq(call("Ṫ", "abc"), "ab", "c")

assert_eq(call("Ṫ", [1, 2, 3]), [1, 2], 3)
assert_eq(call("Ṫ", []), [])

# Ẇ

assert_eq(call("Ẇ", 3, 10), [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]])

assert_eq(call("Ẇ", "abcbabcbabcba", 5), ["abc", "bab", "cba", "bc", "ba"])
assert_eq(call("Ẇ", 5, "abc"), ["a", "b", "c"])

assert_eq(
    call("Ẇ", [4, 7, 5, 5, 1, 3, 8, 6, 2, 1, 3, 8, 3, 2, 9], 6),
    [[4, 7, 5], [5, 1, 3], [8, 6, 2], [1, 3], [8, 3], [2, 9]],
)

# Ż

assert_eq(call("Ż", 13579), 13579, [0, 1, 2, 3, 4])
assert_eq(call("Ż", "abc"), "abc", [0, 1, 2])
assert_eq(
    call("Ż", ["x", "y", "z", 1, 2, 3]), ["x", "y", "z", 1, 2, 3], [0, 1, 2, 3, 4, 5]
)

# ,

assert_eq(call(",", 1, 2), [2, 1])
assert_eq(call(",", "abc", "def"), ["def", "abc"])

# ⁺

assert_eq(call("⁺", 123), 124)
assert_eq(call("⁺", [10, 20, 30, 40, 50]), [11, 21, 31, 41, 51])

assert_eq(call("⁺", "abc"), "bcd")
assert_eq(call("⁺", "123ABC"), "234BCD")

# ⁻

assert_eq(call("⁻", 124), 123)
assert_eq(call("⁻", [11, 21, 31, 41, 51]), [10, 20, 30, 40, 50])

assert_eq(call("⁻", "bcd"), "abc")
assert_eq(call("⁻", "234BCD"), "123ABC")

# ⁼

assert_eq(call("⁼", 1, 2), 0)
assert_eq(call("⁼", 2, 2), 1)
assert_eq(call("⁼", [1, 2, 3], [1, 3, 5]), 0)

assert_eq(call("⁼", "abc", 2), 0)
assert_eq(call("⁼", ["abc", "def", "ghi"], 2), 0)

assert_eq(call("⁼", "abc", "abc"), 1)
assert_eq(call("⁼", "abc", "def"), 0)
assert_eq(call("⁼", ["abc", "def", "ghi"], ["abc", "xyz", "ghi"]), 0)
assert_eq(call("⁼", ["abc", "def"], ["abc", "def"]), 1)

# +

assert_eq(call("+", 1, 2), 3)
assert_eq(call("+", [1, 2, 3, 4], 5), [6, 7, 8, 9])
assert_eq(call("+", [1, 2, 3], [4, 5, 6]), [5, 7, 9])

assert_eq(call("+", "abc", 123), "123abc")
assert_eq(call("+", "def", "abc"), "abcdef")
assert_eq(call("+", [12, 34, 56, 78], "xyz"), ["xyz12", "xyz34", "xyz56", "xyz78"])
assert_eq(call("+", ["abc", "xyz"], ["def", "uvw"]), ["defabc", "uvwxyz"])

# -

assert_eq(call("-", 5, 3), -2)
assert_eq(call("-", [3, 4, 5], 10), [7, 6, 5])
assert_eq(call("-", [1, 2, 3], [4, 5, 6]), [3, 3, 3])

assert_eq(call("-", 2, "abcde"), "abc")
assert_eq(call("-", [3, 4, 5], "abcde"), ["ab", "a", ""])
assert_eq(call("-", "abcde", 2), "cde")
assert_eq(call("-", "abcde", [3, 4, 5]), ["de", "e", ""])

assert_eq(call("-", ["ab", "bc"], "abcbabc"), ["cbc", "aba"])

# ×

assert_eq(call("×", 2.5, 2), 5.0)
assert_eq(call("×", [1, 2, 3, 4, 5], 3), [3, 6, 9, 12, 15])

assert_eq(call("×", 3, "abc"), "abcabcabc")
assert_eq(
    call("×", ["abc", "def", "ghi"], [2, 3, 4]), ["abcabc", "defdefdef", "ghighighighi"]
)

assert_eq(call("×", "ab", "cd"), ["ca", "cb", "da", "db"])
assert_eq(
    call("×", [1, "ab", 2, "cd"], "ef"),
    ["ef", ["ea", "eb", "fa", "fb"], "efef", ["ec", "ed", "fc", "fd"]],
)

# /

assert_eq(call("/", 2, 1), 0.5)
assert_eq(call("/", [1, 2, 5, 10], 10), [10.0, 5.0, 2.0, 1.0])

assert_eq(call("/", 2, "abcde"), ["abc", "de"])
assert_eq(
    call("/", [-1, 0, 1, 2, 3], "abcdefghij"),
    [
        "abcdefghij",
        "abcdefghij",
        ["abcdefghij"],
        ["abcde", "fghij"],
        ["abcd", "efg", "hij"],
    ],
)

assert_eq(call("/", "b", "abcbabcba"), ["a", "c", "a", "c", "a"])
assert_eq(
    call("/", ["a", "ab", "abc"], "abcbabcba"),
    [["", "bcb", "bcb", ""], ["", "cb", "cba"], ["", "b", "ba"]],
)

# *

assert_eq(call("*", 3, 5), 125)
assert_eq(call("*", [0.25, 0.5, 1, 2], 16), [2.0, 4.0, 16, 256])

assert_eq(call("*", 5, "abc"), "abcaa")
assert_eq(call("*", ["abc", "defghi", ""], 4), ["abca", "defghi", "    "])

assert_eq(call("*", "\\d+", "123abcd7890"), ["123", "7890"])

assert_eq(call("*", [], []), [])

# %

assert_eq(call("%", 3, 10), 1)
assert_eq(call("%", [1, 2, 3, 4, 5], 13), [0, 1, 1, 1, 3])

assert_eq(call("%", 123, "abc%def"), "abc123def")
assert_eq(
    call("%", "abc", ["123%456", "%%%", "ab%c"]), ["123abc456", "abcabcabc", "ababcc"]
)

# ÷

assert_eq(call("÷", 2, 5), 2)
assert_eq(
    call("÷", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 97),
    [97, 48, 32, 24, 19, 16, 13, 12, 10, 9],
)

assert_eq(call("÷", 2, "abcde"), "abc")
assert_eq(
    call("÷", [-1, 0, 1, 2, 3], "abcdefghij"), ["a", "a", "abcdefghij", "abcde", "abcd"]
)

assert_eq(call("÷", "b", "abcbabcba"), "a")
assert_eq(call("÷", ["a", "ab", "abc"], "abcbabcba"), ["", "", ""])

# _

assert_eq(call("_", 5, 3), 2)
assert_eq(call("_", [3, 4, 5], 10), [-7, -6, -5])
assert_eq(call("_", [1, 2, 3], [4, 5, 6]), [-3, -3, -3])

assert_eq(call("_", 2, "abcde"), "cde")
assert_eq(call("_", [3, 4, 5], "abcde"), ["de", "e", ""])
assert_eq(call("_", "abcde", 2), "abc")
assert_eq(call("_", "abcde", [3, 4, 5]), ["ab", "a", ""])

assert_eq(call("_", ["ab", "bc"], "abcbabc"), ["ab", "bc"])

# \

assert_eq(call("\\", 2, 1), 2.0)
assert_eq(call("\\", [1, 2, 5, 10], 10), [0.1, 0.2, 0.5, 1.0])

assert_eq(call("\\", 2, "abcde"), ["abc", "de"])
assert_eq(
    call("\\", [-1, 0, 1, 2, 3], "abcdefghij"),
    [
        "abcdefghij",
        "abcdefghij",
        ["abcdefghij"],
        ["abcde", "fghij"],
        ["abcd", "efg", "hij"],
    ],
)

assert_eq(call("\\", "b", "abcbabcba"), ["b"])
assert_eq(call("\\", ["a", "ab", "abc"], "abcbabcba"), [["a"], ["ab"], ["abc"]])

# @

assert_eq(call("@", 3, 5), 243)
assert_eq(
    call("@", [0.25, 0.5, 1, 2], 16),
    [2.3283064365386963e-10, 1.52587890625e-05, 1, 65536],
)

assert_eq(call("@", 5, "abc"), "abcaa")
assert_eq(call("@", ["abc", "defghi", ""], 4), ["cabc", "defghi", "    "])

assert_eq(call("@", "\\d+", "123abcd7890"), [])

# Œ

assert_eq(call("Œ", 3, 10), 3)
assert_eq(call("Œ", [1, 2, 3, 4, 5], 13), [1, 2, 3, 4, 5])

assert_eq(call("Œ", 123, "abc%def"), "abc123def")
assert_eq(call("Œ", "abc", ["123%456", "%%%", "ab%c"]), ["abc", "abc", "abc"])

# ¦

assert_eq(call("¦", 2, 5), 0)
assert_eq(
    call("¦", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 97), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
)

assert_eq(call("¦", 2, "abcde"), "de")
assert_eq(
    call("¦", [-1, 0, 1, 2, 3], "abcdefghij"), ["j", "j", "abcdefghij", "fghij", "hij"]
)

assert_eq(call("¦", "b", "abcbabcba"), "a")
assert_eq(call("¦", ["a", "ab", "abc"], "abcbabcba"), ["", "cba", "ba"])

# =

assert_eq(call("=", 1, 2), 0)
assert_eq(call("=", 2, 2), 1)
assert_eq(call("=", [1, 2, 3], [1, 3, 5]), [1, 0, 0])

assert_eq(call("=", "abc", 2), 0)
assert_eq(call("=", ["abc", "def", "ghi"], 2), [0, 0, 0])

assert_eq(call("=", "abc", "abc"), 1)
assert_eq(call("=", "abc", "def"), 0)
assert_eq(call("=", ["abc", "def", "ghi"], ["abc", "xyz", "ghi"]), [1, 0, 1])

# <

assert_eq(call("<", 1, 2), 0)
assert_eq(call("<", 2, 2), 0)
assert_eq(call("<", 3, 2), 1)

assert_eq(call("<", 98, "abc"), [1, 0, 0])
assert_eq(
    call("<", [67, 68, 69], "ABCDE"),
    [[1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 0]],
)

assert_eq(call("<", "abc", "def"), 0)
assert_eq(call("<", ["xyz", "abc"], "def"), [1, 0])

# >

assert_eq(call(">", 1, 2), 1)
assert_eq(call(">", 2, 2), 0)
assert_eq(call(">", 3, 2), 0)

assert_eq(call(">", 98, "abc"), [0, 0, 1])
assert_eq(
    call(">", [67, 68, 69], "ABCDE"),
    [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]],
)

assert_eq(call(">", "abc", "def"), 1)
assert_eq(call(">", ["xyz", "abc"], "def"), [0, 1])

# ©

assert_eq(call("©", 1, 2), 0)
assert_eq(call("©", 2, 2), 1)
assert_eq(call("©", 3, 2), 1)

assert_eq(call("©", 98, "abc"), [1, 1, 0])
assert_eq(
    call("©", [67, 68, 69], "ABCDE"),
    [[1, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]],
)

assert_eq(call("©", "abc", "def"), 0)
assert_eq(call("©", ["xyz", "abc"], "def"), [1, 0])

# ®

assert_eq(call("®", 1, 2), 1)
assert_eq(call("®", 2, 2), 1)
assert_eq(call("®", 3, 2), 0)

assert_eq(call("®", 98, "abc"), [0, 1, 1])
assert_eq(
    call("®", [67, 68, 69], "ABCDE"),
    [[0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]],
)

assert_eq(call("®", "abc", "def"), 1)
assert_eq(call("®", ["xyz", "abc"], "def"), [0, 1])

# &

assert_eq(call("&", 123, 456), 123)
assert_eq(call("&", 123, 0), 0)

assert_eq(call("&", -123, "abc"), -123)
assert_eq(call("&", "xyz", 0), 0)

assert_eq(call("&", [-1, 0, 1], ["abc", "def", ""]), [-1, 0, ""])

# |

assert_eq(call("|", 123, 456), 456)
assert_eq(call("|", 123, 0), 123)

assert_eq(call("|", -123, "abc"), "abc")
assert_eq(call("|", "xyz", 0), "xyz")

assert_eq(call("|", [-1, 0, 1], ["abc", "def", ""]), ["abc", "def", 1])

# ^

assert_eq(call("^", 12345), [1, 3, 5], [2, 4])
assert_eq(call("^", -6.789), [6, 8], [7, 9])

assert_eq(call("^", "abcdef"), "ace", "bdf")
assert_eq(call("^", "xyz"), "xz", "y")

assert_eq(call("^", [1, 2, 3, 4]), [1, 3], [2, 4])
assert_eq(call("^", []), [], [])

# ~

assert_eq(call("~", 123), 0)
assert_eq(call("~", 0), 1)

assert_eq(call("~", "abc"), 0)
assert_eq(call("~", ""), 1)

assert_eq(call("~", [-1, 0, 1, 2, "", "a"]), [0, 1, 0, 0, 1, 0])

# ð

assert_eq(call("ð"), " ")

# Ð

assert_eq(call("Ð", 10), 10, 10, 10)
assert_eq(call("Ð", "abc"), "abc", "abc", "abc")
assert_eq(call("Ð", [1, 2, 3]), [1, 2, 3], [1, 2, 3], [1, 2, 3])

# ȧ

assert_eq(call("ȧ", 5, 2, [1, 2, 3, 4, 5]), [1, 2, 5, 4, 5])
assert_eq(call("ȧ", "x", "abc", 11), "abx")

assert_eq(call("ȧ", "abc", "def", "ghijkl"), "ghiabckl")
assert_eq(call("ȧ", 123, 4, 56789), [5, 6, 7, 8, 123])

# ḃ

assert_eq(call("ḃ", 10), "1010")
assert_eq(
    call("ḃ", [50, 60, 70, 80, 90]),
    ["110010", "111100", "1000110", "1010000", "1011010"],
)

assert_eq(call("ḃ", "abcde"), ["1100001", "1100010", "1100011", "1100100", "1100101"])
assert_eq(
    call("ḃ", [-1, "abc", -2, "def", -3]),
    [
        "-1",
        ["1100001", "1100010", "1100011"],
        "-10",
        ["1100100", "1100101", "1100110"],
        "-11",
    ],
)

# ċ

assert_eq(
    call("ċ", 3, 5),
    [
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 4],
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 4],
        [2, 3, 5],
        [2, 4, 5],
        [3, 4, 5],
    ],
)
assert_eq(call("ċ", "xyz", 2), [["x", "y"], ["x", "z"], ["y", "z"]])
assert_eq(call("ċ", 10, [1, 2, 3]), [[1, 2, 3]])

assert_eq(call("ċ", "abcde", "cdefg"), ["c", "d", "e", "f", "g", "a", "b"])
assert_eq(call("ċ", [3, 4, 5], [1, 2, 3]), [1, 2, 3, 4, 5])

# ḋ

assert_eq(call("ḋ", 15, 99), [6, 9])

assert_eq(call("ḋ", 5, [1, 2, 3]), 38)
assert_eq(call("ḋ", [10, 20, 30], -2), 30)

# ė

assert_eq(call("ė", 5), [1, 2, 3, 4])
assert_eq(call("ė", "abc"), [1, 2, 3])
assert_eq(call("ė", []), [])

# ḟ

assert_eq(call("ḟ", 60), [2, 1, 1])
assert_eq(
    call("ḟ", [10, 11, 12, 13, 14]),
    [[1, 0, 1], [0, 0, 0, 0, 1], [2, 1], [0, 0, 0, 0, 0, 1], [1, 0, 0, 1]],
)

assert_eq(call("ḟ", "abc def ghi jkl"), "Abc Def Ghi Jkl")

# ġ

assert_eq(call("ġ", 1122231), [[1, 1], [2, 2, 2], [3], [1]])
assert_eq(call("ġ", "aabbbca"), ["aa", "bbb", "c", "a"])
assert_eq(call("ġ", [1, 2, 3]), [[1], [2], [3]])

# ḣ

assert_eq(call("ḣ", 123), 23)

assert_eq(call("ḣ", "abc"), "bc")

assert_eq(call("ḣ", [1, 2, 3]), [2, 3])
assert_eq(call("ḣ", []), [])

# ŀ

assert_eq(call("ŀ", 369), 18)

assert_eq(call("ŀ", "!@"), 2112)

assert_eq(call("ŀ", [10, 15, 20, "abc"]), 60)

# ṁ

assert_eq(call("ṁ", 1470369258), 4.5)
assert_eq(call("ṁ", "abc"), 98)
assert_eq(call("ṁ", [1, 4, 3, 2]), 2.5)

# ȯ

assert_eq(call("ȯ", 2, 1.2345), 1.23)

assert_eq(call("ȯ", 5, [-1, 1, 3, 5, 7]), [1, 3, 5])
assert_eq(call("ȯ", [10, 9, 8, 7], 6), [])

assert_eq(call("ȯ", "abcde", "gfedc"), ["e", "d", "c"])

# ṗ

assert_eq(
    call("ṗ", 2, 5),
    [
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 1],
        [2, 3],
        [2, 4],
        [2, 5],
        [3, 1],
        [3, 2],
        [3, 4],
        [3, 5],
        [4, 1],
        [4, 2],
        [4, 3],
        [4, 5],
        [5, 1],
        [5, 2],
        [5, 3],
        [5, 4],
    ],
)
assert_eq(
    call("ṗ", "xyz", 2),
    [["x", "y"], ["x", "z"], ["y", "x"], ["y", "z"], ["z", "x"], ["z", "y"]],
)
assert_eq(
    call("ṗ", 10, [1, 2, 3]),
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
)

assert_eq(call("ṗ", "abcde", "cdefg"), ["f", "g"])
assert_eq(call("ṗ", [3, 4, 5], [1, 2, 3]), [1, 2])

# ṙ

assert_eq(call("ṙ", 5, "a", "abc"), "aaabc")
assert_eq(
    call("ṙ", [-3, -2, -1, 0, 1, 2, 3], "def", "x"),
    ["ddx", "dx", "x", "x", "x", "dx", "ddx"],
)
assert_eq(
    call("ṙ", [5, 6, 7, 8], ["abc", "def", "ghi", ""], "xyz"),
    ["aaxyz", "dddxyz", "ggggxyz", "     xyz"],
)

# ṡ

assert_eq(call("ṡ", 135420), [1, 4, 9, 13, 15, 15])

assert_eq(call("ṡ", "abcd"), ["a", "ab", "abc", "abcd"])

assert_eq(
    call("ṡ", [1, 4, 7, 0, 3, 6, 9, 2, 5, 8]), [1, 5, 12, 12, 15, 21, 30, 32, 37, 45]
)
assert_eq(
    call("ṡ", [1, 4, 7, 0, 3, 6, 9, 2, 5, "8"]),
    [
        "1",
        "14",
        "147",
        "1470",
        "14703",
        "147036",
        "1470369",
        "14703692",
        "147036925",
        "1470369258",
    ],
)

# ṫ

assert_eq(call("ṫ", 123), 12)

assert_eq(call("ṫ", "abc"), "ab")

assert_eq(call("ṫ", [1, 2, 3]), [1, 2])
assert_eq(call("ṫ", []), [])

# ẇ

assert_eq(call("ẇ", 3, 10), [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])

assert_eq(call("ẇ", "abcbabcbabcba", 5), ["abcba", "bcbab", "cba"])
assert_eq(call("ẇ", 5, "abc"), ["abc"])

assert_eq(
    call("ẇ", [4, 7, 5, 5, 1, 3, 8, 6, 2, 1, 3, 8, 3, 2, 9], 6),
    [[4, 7, 5, 5, 1, 3], [8, 6, 2, 1, 3, 8], [3, 2, 9]],
)

# ż

assert_eq(call("ż", 13579), 13579, [1, 2, 3, 4, 5])
assert_eq(call("ż", "abc"), "abc", [1, 2, 3])
assert_eq(
    call("ż", ["x", "y", "z", 1, 2, 3]), ["x", "y", "z", 1, 2, 3], [1, 2, 3, 4, 5, 6]
)

# Ạ

assert_eq(call("Ạ"), "abcdefghijklmnopqrstuvwxyz")

# Ḅ

assert_eq(call("Ḅ", 2, 14), "1110")
assert_eq(call("Ḅ", [5, 10, 15, 20], [28, 29, 30, 31]), ["103", "29", "20", "1B"])

assert_eq(call("Ḅ", 3, "abcd"), "aaabbbcccddd")
assert_eq(call("Ḅ", ["abc", "xyz"], 2), ["aabbcc", "xxyyzz"])

assert_eq(call("Ḅ", "\\d+", "abc123def456ghi"), ["abc", "def", "ghi"])

# Ḍ

assert_eq(call("Ḍ", 5), 10)
assert_eq(call("Ḍ", "abc"), "abcabc")
assert_eq(call("Ḍ", [123, "abc", 456, "def"]), [246, "abcabc", 912, "defdef"])

# Ẹ

assert_eq(call("Ẹ", 1234), 1, 2, 3, 4)
assert_eq(call("Ẹ", -789.123), 7, 8, 9, 1, 2, 3)

assert_eq(call("Ẹ", "abcde"), "a", "b", "c", "d", "e")
assert_eq(call("Ẹ", ""))

assert_eq(call("Ẹ", [1, 2, 3, 4, 5]), 1, 2, 3, 4, 5)

# Ḥ

assert_eq(call("Ḥ", 10), "a")
assert_eq(call("Ḥ", [50, 60, 70, 80, 90]), ["32", "3c", "46", "50", "5a"])

assert_eq(call("Ḥ", "abcde"), ["61", "62", "63", "64", "65"])
assert_eq(
    call("Ḥ", [-1, "abc", -2, "def", -3]),
    ["-1", ["61", "62", "63"], "-2", ["64", "65", "66"], "-3"],
)

# Ị

assert_eq(call("Ị", 5), 0.2)
assert_eq(call("Ị", [-2, -1, 1, 2]), [-0.5, -1.0, 1.0, 0.5])

assert_eq(call("Ị", "Hello, World!"), "HelloWorld")

# Ḳ

assert_eq(call("Ḳ", 1.23), 1.23, 32.1)
assert_eq(call("Ḳ", -456), -456, "654-")

assert_eq(call("Ḳ", "abcd"), "abcd", "dcba")
assert_eq(call("Ḳ", ""), "", "")

assert_eq(call("Ḳ", [1, 2, 3, 4]), [1, 2, 3, 4], [4, 3, 2, 1])
assert_eq(
    call("Ḳ", [123, "abc", 456, "def"]),
    [123, "abc", 456, "def"],
    ["def", 456, "abc", 123],
)

# Ḷ

assert_eq(call("Ḷ", 12, 21), 84)
assert_eq(call("Ḷ", 30, [18, 19, 20, 21, 22]), [90, 570, 60, 210, 330])

assert_eq(
    call("Ḷ", "abc", [10, 11, 12]),
    [[970, 490, 990], [1067, 1078, 99], [1164, 588, 396]],
)

# Ṃ

assert_eq(call("Ṃ", 1.23), "1.2332.1")
assert_eq(call("Ṃ", -456), "-456654-")
assert_eq(call("Ṃ", 1234), 12344321)

assert_eq(call("Ṃ", "abcd"), "abcddcba")
assert_eq(call("Ṃ", ""), "")

assert_eq(call("Ṃ", [1, 2, 3, 4]), [1, 2, 3, 4, 4, 3, 2, 1])
assert_eq(
    call("Ṃ", [123, "abc", 456, "def"]),
    [123, "abc", 456, "def", "def", 456, "abc", 123],
)

# Ṇ

assert_eq(
    call(
        "Ṇ", "ZYXWVUTSRQPONMLKJIHGFEDCBA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "HELLO, WORLD!"
    ),
    "SVOOL, DLIOW!",
)
assert_eq(call("Ṇ", "wxyz", 4321, "abcd1234"), "abcdzyxw")
assert_eq(
    call("Ṇ", "abc", 123, ["1", "9", "4", "7", "8", "5", "6", "2", "3"]),
    ["a", "9", "4", "7", "8", "5", "6", "b", "c"],
)
assert_eq(call("Ṇ", 456, [1, "y", 3], "123xyz"), "426x5z")

# Ọ

assert_eq(call("Ọ", 123, 456), 123)
assert_eq(call("Ọ", -1.23, -4.56), -4.56)

assert_eq(call("Ọ", "abcd", "efgh"), "abcd")
assert_eq(call("Ọ", "abc", "aac"), "aac")

assert_eq(call("Ọ", "abc", 123), 123)
assert_eq(call("Ọ", 123, ""), "")

assert_eq(
    call("Ọ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
)

# Ṛ

assert_eq(call("Ṛ", 3, 2), [[1, 1], [1, 2], [2, 2]])

assert_eq(
    call("Ṛ", "xyz", 2),
    [["x", "x"], ["x", "y"], ["x", "z"], ["y", "y"], ["y", "z"], ["z", "z"]],
)

assert_eq(
    call("Ṛ", 10, [1, 2, 3]),
    [
        [1, 1, 1],
        [1, 1, 2],
        [1, 1, 3],
        [1, 2, 2],
        [1, 2, 3],
        [1, 3, 3],
        [2, 2, 2],
        [2, 2, 3],
        [2, 3, 3],
        [3, 3, 3],
    ],
)

# Ṣ

assert_eq(call("Ṣ", 3.141592653589), [-2, 3, -3, 4, 4, -7, 4, -1, -2, 2, 3, 1])

assert_eq(call("Ṣ", "thunno"), [-12, 13, -7, 0, 1])

assert_eq(
    call("Ṣ", [100, 50, 25, 12, 6, 3, 2, 1, 0]), [-50, -25, -13, -6, -3, -1, -1, -1]
)

# Ṭ

assert_eq(call("Ṭ", 123), [[1, 2, 3]])
assert_eq(call("Ṭ", "abc"), [["a", "b", "c"]])
assert_eq(call("Ṭ", []), [])

assert_eq(call("Ṭ", [1, 2, 3, 4]), [[1, 2, 3, 4]])
assert_eq(call("Ṭ", [123, 456, 789]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

assert_eq(
    call("Ṭ", ["abc", "defg", "hijkl"]),
    [["a", "d", "h"], ["b", "e", "i"], ["c", "f", "j"]],
)
assert_eq(call("Ṭ", ["abc", "", "defg", "hijkl"]), [])

assert_eq(
    call("Ṭ", [[123, 456], ["abc", "def"], [[1, 2], [3, 4]]]),
    [[123, "abc", [1, 2]], [456, "def", [3, 4]]],
)

# Ụ

assert_eq(call("Ụ", 123), 231)
assert_eq(call("Ụ", -4.56), "4.56-")

assert_eq(call("Ụ", "abcd"), "bcda")
assert_eq(call("Ụ", ""), "")

assert_eq(call("Ụ", [1, 2, 3, 4]), [2, 3, 4, 1])
assert_eq(call("Ụ", []), [])

# Ṿ

assert_eq(call("Ṿ", 123), 312)
assert_eq(call("Ṿ", -4.56), 1.5)

assert_eq(call("Ṿ", "abcd"), "dabc")
assert_eq(call("Ṿ", ""), "")

assert_eq(call("Ṿ", [1, 2, 3, 4]), [4, 1, 2, 3])
assert_eq(call("Ṿ", []), [])

# Ẉ

assert_eq(call("Ẉ", 3, 12345), [[1, 4], [2, 5], [3]])

assert_eq(call("Ẉ", 4, "abcdefghij"), ["aei", "bfj", "cg", "dh"])
assert_eq(call("Ẉ", "xyz", -4), ["x", "y", "z", ""])

assert_eq(call("Ẉ", 0, [1, 2, 3]), [1, 2, 3])
assert_eq(call("Ẉ", [], 3), [[], [], []])

# Ỵ

assert_eq(call("Ỵ", 3, 100), 800)
assert_eq(call("Ỵ", -3, -100), -13)
assert_eq(call("Ỵ", 0, -1.23), -1)

assert_eq(call("Ỵ", 5, "abc"), "cab")
assert_eq(call("Ỵ", "xyz", -2), "yzx")
assert_eq(call("Ỵ", "", 2), "")

assert_eq(call("Ỵ", 3, [1, 2, 3, 4, 5]), [4, 5, 1, 2, 3])
assert_eq(call("Ỵ", [1, 2, 3], 0), [1, 2, 3])

# Ẓ

assert_eq(call("Ẓ", 3, 100), 12)
assert_eq(call("Ẓ", -3, -100), -800)
assert_eq(call("Ẓ", 0, -1.23), -1)

assert_eq(call("Ẓ", 5, "abc"), "bca")
assert_eq(call("Ẓ", "xyz", -2), "zxy")
assert_eq(call("Ẓ", "", 2), "")

assert_eq(call("Ẓ", 3, [1, 2, 3, 4, 5]), [3, 4, 5, 1, 2])
assert_eq(call("Ẓ", [1, 2, 3], 0), [1, 2, 3])

# Ƈ

assert_eq(call("Ƈ", 5, 10), 30240)
assert_eq(call("Ƈ", 10, 20), 670442572800)

assert_eq(call("Ƈ", "abc", "abcbabcbabcba"), 1)
assert_eq(call("Ƈ", [123, 321, 132], "1232123212321"), [1, 1, 0])

assert_eq(call("Ƈ", 1, [1, 2, 3, 2, 1, 2, 3]), 1)
assert_eq(call("Ƈ", [1, 2, "a"], [1, "a", 1, "b", 1, "c"]), [1, 0, 1])

# Ɗ

assert_eq(call("Ɗ", 2, 123), "12")
assert_eq(call("Ɗ", 10, -1.23), "1.23")

assert_eq(call("Ɗ", 3, ""), "")
assert_eq(call("Ɗ", "abc", 2), "ab")
assert_eq(call("Ɗ", -2, "xyz"), "xz")

assert_eq(call("Ɗ", [], 5), [])
assert_eq(call("Ɗ", 10, [1, 2, 3]), [1, 3])
assert_eq(
    call("Ɗ", ["abc", "def", "ghi", "jkl", "mno"], -10), ["def", "ghi", "jkl", "mno"]
)

# Ƒ

assert_eq(call("Ƒ", 100), [2, 5])
assert_eq(call("Ƒ", 30), [2, 3, 5])
assert_eq(call("Ƒ", -10), [])

assert_eq(
    call("Ƒ", "abcd"), ["a", "ab", "abc", "abcd", "b", "bc", "bcd", "c", "cd", "d"]
)
assert_eq(call("Ƒ", ""), [])
assert_eq(call("Ƒ", "xxx"), ["x", "xx", "xxx", "x", "xx", "x"])

assert_eq(call("Ƒ", [1, 2, 3]), [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]])
assert_eq(
    call("Ƒ", ["abc", "def", "ghi", "jkl", "mno"]),
    [
        ["abc"],
        ["abc", "def"],
        ["abc", "def", "ghi"],
        ["abc", "def", "ghi", "jkl"],
        ["abc", "def", "ghi", "jkl", "mno"],
        ["def"],
        ["def", "ghi"],
        ["def", "ghi", "jkl"],
        ["def", "ghi", "jkl", "mno"],
        ["ghi"],
        ["ghi", "jkl"],
        ["ghi", "jkl", "mno"],
        ["jkl"],
        ["jkl", "mno"],
        ["mno"],
    ],
)
assert_eq(call("Ƒ", []), [])

# Ɠ

assert_eq(call("Ɠ"), 16)

# Ɱ

assert_eq(call("Ɱ", 123), 12321)
assert_eq(call("Ɱ", -4.56), "-4.565.4-")

assert_eq(call("Ɱ", "abcde"), "abcdedcba")
assert_eq(call("Ɱ", ""), "")

assert_eq(call("Ɱ", [1, 2, 3]), [1, 2, 3, 2, 1])
assert_eq(
    call("Ɱ", [1, [2, [3, [4, "d"], "c"], "b"], "a"]),
    [1, [2, [3, [4, "d"], "c"], "b"], "a", [2, [3, [4, "d"], "c"], "b"], 1],
)
assert_eq(call("Ɱ", []), [])

# Ɲ

assert_eq(
    call("Ɲ", 5),
    [[1, 1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1], [2, 2, 1], [4, 1], [3, 2], [5]],
)
assert_eq(call("Ɲ", -4.56), [[-1, -1, -1, -1], [-2, -1, -1], [-3, -1], [-2, -2], [-4]])

assert_eq(call("Ɲ", "abcd"), "abcd")

assert_eq(call("Ɲ", [1, 2, 3, 4]), "1\n2\n3\n4")
assert_eq(call("Ɲ", ["abc", 123, "def", 456]), "abc\n123\ndef\n456")

assert_eq(call("Ɲ", [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), "123\n456\n789")
assert_eq(
    call("Ɲ", ["abc", [123, 456], 789, ["def", "ghi"]]), "abc\n123456\n789\ndefghi"
)

# Ƥ

assert_eq(call("Ƥ", 2, 1), [2, 1])
assert_eq(call("Ƥ", "abc", "def"), ["abc", "d", "e", "f"])

assert_eq(call("Ƥ", 5, [1, 2, 3, 4]), [5, 1, 2, 3, 4])
assert_eq(call("Ƥ", "ghi", ["abc", "def"]), ["ghi", "abc", "def"])
assert_eq(call("Ƥ", [], []), [[]])

# Ƭ

assert_eq(call("Ƭ", 123, 456), 456, [[1, 2, 3]])
assert_eq(call("Ƭ", "abc", "def"), "def", [["a", "b", "c"]])

assert_eq(
    call("Ƭ", 0, [123, "abcde", [789, "xyz"]]),
    [[1, "a", 789], [2, "b", "xyz"], [3, "c", 0], [0, "d", 0], [0, "e", 0]],
)
assert_eq(
    call("Ƭ", "abc", [[], 123, "abcdefghij"]),
    [
        ["abc", 1, "a"],
        ["abc", 2, "b"],
        ["abc", 3, "c"],
        ["abc", "abc", "d"],
        ["abc", "abc", "e"],
        ["abc", "abc", "f"],
        ["abc", "abc", "g"],
        ["abc", "abc", "h"],
        ["abc", "abc", "i"],
        ["abc", "abc", "j"],
    ],
)
assert_eq(
    call("Ƭ", [[123, 456], ["abc", "def", "ghi"]], [[123, 456], ["abc", "def", "ghi"]]),
    [[123, "abc"], [456, "def"], [[[123, 456], ["abc", "def", "ghi"]], "ghi"]],
)

# ɓ

assert_eq(call("ɓ", 123), 1)
assert_eq(call("ɓ", 0), 0)

assert_eq(call("ɓ", "abc"), 1)
assert_eq(call("ɓ", ""), 0)

assert_eq(call("ɓ", [-1, 0, 1, 2, "", "a"]), [1, 0, 1, 1, 0, 1])
assert_eq(call("ɓ", []), [])

# ƈ

assert_eq(
    call("ƈ", 1212323434545656767878989),
    [[1, 2], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 2]],
)

assert_eq(
    call("ƈ", "the quick brown fox jumps over the lazy dog"),
    [
        ["t", 2],
        ["h", 2],
        ["e", 3],
        [" ", 8],
        ["q", 1],
        ["u", 2],
        ["i", 1],
        ["c", 1],
        ["k", 1],
        ["b", 1],
        ["r", 2],
        ["o", 4],
        ["w", 1],
        ["n", 1],
        ["f", 1],
        ["x", 1],
        ["j", 1],
        ["m", 1],
        ["p", 1],
        ["s", 1],
        ["v", 1],
        ["l", 1],
        ["a", 1],
        ["z", 1],
        ["y", 1],
        ["d", 1],
        ["g", 1],
    ],
)
assert_eq(call("ƈ", ""), [])

assert_eq(
    call(
        "ƈ",
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3],
    ),
    [[3, 6], [1, 2], [4, 3], [5, 3], [9, 3], [2, 3], [6, 3], [8, 2], [7, 1]],
)
assert_eq(call("ƈ", []), [])

# ɗ

assert_eq(call("ɗ", 123), 1)
assert_eq(call("ɗ", -1.5), 0.5)
assert_eq(call("ɗ", [10, 11, 12, 13, 14]), [0, 1, 0, 1, 0])

assert_eq(call("ɗ", "abcdefghij"), "fghij")
assert_eq(call("ɗ", ""), "")

assert_eq(call("ɗ", ["abcd", 1234, "efg", 567]), ["cd", 0, "g", 1])

# ƒ

assert_eq(
    call("ƒ", 3141592653589),
    [
        [3],
        [3, 1],
        [3, 1, 4],
        [3, 1, 4, 1],
        [3, 1, 4, 1, 5],
        [3, 1, 4, 1, 5, 9],
        [3, 1, 4, 1, 5, 9, 2],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [3, 1, 4, 1, 5, 9, 2, 6, 5],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9],
    ],
)
assert_eq(call("ƒ", 111), [[1], [1, 1], [1, 1, 1]])

assert_eq(call("ƒ", "abcde"), ["a", "ab", "abc", "abcd", "abcde"])
assert_eq(call("ƒ", ""), [])

assert_eq(
    call("ƒ", [123, "abc", 456, "def", 789, "ghi"]),
    [
        [123],
        [123, "abc"],
        [123, "abc", 456],
        [123, "abc", 456, "def"],
        [123, "abc", 456, "def", 789],
        [123, "abc", 456, "def", 789, "ghi"],
    ],
)
assert_eq(call("ƒ", []), [])

# ɠ

assert_eq(call("ɠ"), 256)

# ɦ

assert_eq(call("ɦ"), 100)

# ƙ

assert_eq(call("ƙ", 123), 125)
assert_eq(call("ƙ", -1.23), 0.77)

assert_eq(
    call("ƙ", "The quick brown fox jumps over the lazy dog"),
    [
        3,
        9,
        15,
        19,
        25,
        30,
        34,
        39,
        0,
        36,
        10,
        7,
        40,
        2,
        28,
        33,
        16,
        42,
        1,
        32,
        6,
        20,
        8,
        35,
        22,
        14,
        12,
        17,
        26,
        41,
        23,
        4,
        11,
        29,
        24,
        31,
        5,
        21,
        27,
        13,
        18,
        38,
        37,
    ],
)
assert_eq(call("ƙ", ""), [])

assert_eq(
    call("ƙ", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]),
    [1, 3, 6, 0, 9, 2, 4, 8, 10, 7, 11, 5, 12],
)
assert_eq(call("ƙ", []), [])

# ɱ

assert_eq(call("ɱ", 3, 3.14159), 3.1)

assert_eq(call("ɱ", 5, "Hello, World!"), "Hello")
assert_eq(call("ɱ", -1, "abc"), "ab")

assert_eq(call("ɱ", 4, [1, 2, 3]), [1, 2, 3])
assert_eq(call("ɱ", -5, ["abc", "def", "ghi"]), [])

# ɲ

assert_eq(call("ɲ", 3, 3.14159), 159)

assert_eq(call("ɲ", 5, "Hello, World!"), "orld!")
assert_eq(call("ɲ", -1, "abc"), "bc")

assert_eq(call("ɲ", 4, [1, 2, 3]), [1, 2, 3])
assert_eq(call("ɲ", -5, ["abc", "def", "ghi"]), [])

# ƥ

assert_eq(call("ƥ", 123))
assert_eq(call("ƥ", "abc"))
assert_eq(call("ƥ", [1, [2, [3]]]))

# ʠ

assert_eq(
    call("ʠ", 5),
    [
        [],
        [1],
        [2],
        [1, 2],
        [3],
        [1, 3],
        [2, 3],
        [1, 2, 3],
        [4],
        [1, 4],
        [2, 4],
        [1, 2, 4],
        [3, 4],
        [1, 3, 4],
        [2, 3, 4],
        [1, 2, 3, 4],
        [5],
        [1, 5],
        [2, 5],
        [1, 2, 5],
        [3, 5],
        [1, 3, 5],
        [2, 3, 5],
        [1, 2, 3, 5],
        [4, 5],
        [1, 4, 5],
        [2, 4, 5],
        [1, 2, 4, 5],
        [3, 4, 5],
        [1, 3, 4, 5],
        [2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ],
)
assert_eq(
    call("ʠ", -3.14), [[], [-1], [-2], [-1, -2], [-3], [-1, -3], [-2, -3], [-1, -2, -3]]
)

assert_eq(
    call("ʠ", "abcde"),
    [
        "",
        "a",
        "b",
        "ab",
        "c",
        "ac",
        "bc",
        "abc",
        "d",
        "ad",
        "bd",
        "abd",
        "cd",
        "acd",
        "bcd",
        "abcd",
        "e",
        "ae",
        "be",
        "abe",
        "ce",
        "ace",
        "bce",
        "abce",
        "de",
        "ade",
        "bde",
        "abde",
        "cde",
        "acde",
        "bcde",
        "abcde",
    ],
)
assert_eq(call("ʠ", ""), [""])

assert_eq(
    call("ʠ", [123, "abc", 456, "def"]),
    [
        [],
        [123],
        ["abc"],
        [123, "abc"],
        [456],
        [123, 456],
        ["abc", 456],
        [123, "abc", 456],
        ["def"],
        [123, "def"],
        ["abc", "def"],
        [123, "abc", "def"],
        [456, "def"],
        [123, 456, "def"],
        ["abc", 456, "def"],
        [123, "abc", 456, "def"],
    ],
)
assert_eq(call("ʠ", []), [[]])

# ʂ

assert_eq(call("ʂ", 123), 1)
assert_eq(call("ʂ", -1.23), -1)
assert_eq(call("ʂ", 0), 0)

assert_eq(
    call("ʂ", 'tHe QuIcK, bRoWn FoX. hE "jUmPeD" oVeR? tHe LaZy DoG! wHaT?!'),
    'The quick, brown fox. He "jumped" over? The lazy dog! What?!',
)
assert_eq(call("ʂ", "abcdef"), "Abcdef")

assert_eq(
    call("ʂ", [123, "abc", [4, 5, 6], [7, "eight", 9]]), [6, "abc", 15, "7eight9"]
)
assert_eq(call("ʂ", []), [])

# ƭ

assert_eq(call("ƭ", 100), 10)
assert_eq(call("ƭ", 10), 3.1622776601683795)
assert_eq(
    call("ƭ", [-2, -1, 0, 1, 2]), [1.4142135623730951, 1, 0, 1, 1.4142135623730951]
)
assert_eq(call("ƭ", 6.25), 2.5)

assert_eq(call("ƭ", "abcdef"), "ace")
assert_eq(call("ƭ", "xyz"), "xz")
assert_eq(call("ƭ", ""), "")

# ¶

assert_eq(call("¶"), "\n")

# Ç

assert_eq(call("Ç"), "|")

# ¬

assert_eq(call("¬", 123), 0)
assert_eq(call("¬", 0), 1)

assert_eq(call("¬", "abc"), 0)
assert_eq(call("¬", ""), 1)

assert_eq(call("¬", [-1, 0, 1, 2, "", "a"]), 0)
assert_eq(call("¬", []), 1)

# §

assert_eq(call("§", 123, 456), 456)
assert_eq(call("§", -1.23, -4.56), -1.23)

assert_eq(call("§", "abcd", "efgh"), "efgh")
assert_eq(call("§", "abc", "aac"), "abc")

assert_eq(call("§", "abc", 123), "abc")
assert_eq(call("§", 123, ""), 123)

assert_eq(
    call("§", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    [10, 9, 8, 7, 6, 6, 7, 8, 9, 10],
)

# Ä

assert_eq(call("Ä", 10), "J")
assert_eq(call("Ä", [20, 8, 21, 14, 14, 15]), ["T", "H", "U", "N", "N", "O"])

assert_eq(call("Ä", "Abc"), [1, 2, 3])
assert_eq(call("Ä", "Hello, World!"), [8, 5, 12, 12, 15, 0, 0, 23, 15, 18, 12, 4, 0])
assert_eq(
    call("Ä", ["Thunno 2", "is the", "best!"]),
    [[20, 8, 21, 14, 14, 15, 0, 0], [9, 19, 0, 20, 8, 5], [2, 5, 19, 20, 0]],
)

assert_eq(call("Ä", [123, "abc", -4.56, "?!."]), ["S", [1, 2, 3], "V", [0, 0, 0]])

# ½

assert_eq(call("½", 10), 5)
assert_eq(call("½", [-10, -5, 0, 5, 10]), [-5, -2.5, 0, 2.5, 5])

assert_eq(call("½", "abcdefg"), ["abcd", "efg"])
assert_eq(
    call("½", ["abc", 123, "defg", 4567, "hijkl", 89012]),
    [["ab", "c"], 61.5, ["de", "fg"], 2283.5, ["hij", "kl"], 44506],
)

# ²

assert_eq(call("²", 5), 25)
assert_eq(call("²", [-3, -2, -1, 0, 1, 2, 3]), [9, 4, 1, 0, 1, 4, 9])

assert_eq(call("²", "abcdefghij"), ["ab", "cd", "ef", "gh", "ij"])
assert_eq(call("²", "a"), ["a"])

assert_eq(
    call("²", [12, "abcde", 34, "fghijklm"]),
    [144, ["ab", "cd", "e"], 1156, ["fg", "hi", "jk", "lm"]],
)

# ³

assert_eq(call("³", 5), 125)
assert_eq(call("³", [-3, -2, -1, 0, 1, 2, 3]), [-27, -8, -1, 0, 1, 8, 27])

assert_eq(call("³", "abcdefghij"), ["abc", "def", "ghi", "j"])
assert_eq(call("³", "a"), ["a"])

assert_eq(
    call("³", [12, "abcde", 34, "fghijklm"]),
    [1728, ["abc", "de"], 39304, ["fgh", "ijk", "lm"]],
)

# ⁴

assert_eq(call("⁴", 5), 625)
assert_eq(call("⁴", [-3, -2, -1, 0, 1, 2, 3]), [81, 16, 1, 0, 1, 16, 81])

assert_eq(call("⁴", "abcdefghij"), ["abcd", "efgh", "ij"])
assert_eq(call("⁴", "a"), ["a"])

assert_eq(
    call("⁴", [12, "abcde", 34, "fghijklm"]),
    [20736, ["abcd", "e"], 1336336, ["fghi", "jklm"]],
)

# ⁵

assert_eq(call("⁵", 5), 3125)
assert_eq(call("⁵", [-3, -2, -1, 0, 1, 2, 3]), [-243, -32, -1, 0, 1, 32, 243])

assert_eq(call("⁵", "abcdefghij"), ["abcde", "fghij"])
assert_eq(call("⁵", "a"), ["a"])

assert_eq(
    call("⁵", [12, "abcde", 34, "fghijklm"]),
    [248832, ["abcde"], 45435424, ["fghij", "klm"]],
)

# ạ

assert_eq(call("ạ", 123), 0)
assert_eq(call("ạ", 111), 1)
assert_eq(call("ạ", -1.1), 0)

assert_eq(call("ạ", "abc"), 0)
assert_eq(call("ạ", "aaa"), 1)
assert_eq(call("ạ", ""), 1)

assert_eq(call("ạ", [1, 2, 3]), 0)
assert_eq(call("ạ", [1, 1, 1]), 1)
assert_eq(call("ạ", []), 1)

# ḅ

assert_eq(call("ḅ", 1), 1)
assert_eq(call("ḅ", -1.23), 0)
assert_eq(call("ḅ", [-2, -1, 0, 1, 2]), [0, 0, 0, 1, 0])

assert_eq(call("ḅ", "abc"), 0)
assert_eq(call("ḅ", ""), 0)

assert_eq(call("ḅ", ["abc", 1, "", 123, "def", 1.0]), [0, 1, 0, 0, 0, 1])

# ḍ

assert_eq(call("ḍ", 1234, 314159), [5, 9, 2])
assert_eq(call("ḍ", 121, 234), [3, 4, 1])

assert_eq(call("ḍ", "abc123", 12345), "45abc")
assert_eq(call("ḍ", 3.14, "xyz"), "xyz3.14")

assert_eq(call("ḍ", [123, "abc", 456, "def"], ["abc", "def", "ghi"]), ["ghi", 123, 456])
assert_eq(call("ḍ", [1, 2, 3], 123), [])

# ẹ

assert_eq(call("ẹ", 123), 1231)
assert_eq(call("ẹ", -4.56), "-4.56-")

assert_eq(call("ẹ", "abc"), "abca")
assert_eq(call("ẹ", "xxx"), "xxxx")
assert_eq(call("ẹ", ""), "")

assert_eq(call("ẹ", [123, 456, 789]), [123, 456, 789, 123])
assert_eq(call("ẹ", []), [])

# ḥ

assert_eq(call("ḥ", 123, 456), [4, 5, 6, 1, 2, 3])

assert_eq(call("ḥ", 123, "abc"), ["a", "b", "c", 1, 2, 3])
assert_eq(call("ḥ", "def", "abc"), ["a", "b", "c", "d", "e", "f"])

assert_eq(call("ḥ", 123, [123, 456, 789]), [123, 456, 789, 1, 2, 3])
assert_eq(
    call("ḥ", ["abc", 123, "def", 456], "xyz"), ["x", "y", "z", "abc", 123, "def", 456]
)

assert_eq(call("ḥ", [123], ["abc"]), ["abc", 123])

# ị

assert_eq(call("ị", 10203040, 12345678), [1, 3, 5, 7])
assert_eq(call("ị", 123, "abcdefghij"), "abc")

assert_eq(call("ị", ["abc", 0, 123, [], "", [123, 456]], 1234567890), [1, 3, 6])
assert_eq(call("ị", [], "abcdef"), "")
assert_eq(call("ị", [1, 2, 3, 4, 5], [6, 7, 8]), [6, 7, 8])

# ḳ

assert_eq(call("ḳ", 3.141592653589), [1, 2, 3, 4, 5, 6, 8, 9])
assert_eq(call("ḳ", 0), [0])

assert_eq(call("ḳ", "Hello, World!"), " !,HWdelor")
assert_eq(call("ḳ", "cba"), "abc")

assert_eq(
    call(
        "ḳ",
        [
            123,
            456,
            789,
            12,
            345,
            678,
            901,
            234,
            567,
            890,
            123,
            456,
            789,
            12,
            345,
            678,
            901,
            234,
            567,
            890,
        ],
    ),
    [12, 123, 234, 345, 456, 567, 678, 789, 890, 901],
)

# ḷ

assert_eq(call("ḷ", 123), -122)
assert_eq(call("ḷ", 0.25), 0.75)

assert_eq(call("ḷ", "Hello, World!"), 0)
assert_eq(call("ḷ", "hello, world!"), 1)
assert_eq(call("ḷ", ""), 1)

assert_eq(
    call("ḷ", [1234, "xyz", [123, 456], 0, "", ["abc", "def", "ghi", "jkl", "mno"]]),
    [4, 3, 2, 1, 0, 5],
)

# ṃ

assert_eq(call("ṃ", 1.23), 2)
assert_eq(call("ṃ", -12.34), -12)

assert_eq(call("ṃ", "Hello, World!"), [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0])
assert_eq(call("ṃ", "aeiou"), [1, 1, 1, 1, 1])

assert_eq(
    call("ṃ", [123, "abc", ["xyz", 1.23, "def", 456]]),
    [321, "cba", [456, "def", 1.23, "xyz"]],
)

# ọ

assert_eq(call("ọ", 3, 123), [1, 2, 3, 1, 2, 3, 1, 2, 3])
assert_eq(call("ọ", -1, 456), [])

assert_eq(
    call("ọ", 5, "abc"),
    ["a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c"],
)
assert_eq(call("ọ", "xyz", 3), ["x", "y", "z", "x", "y", "z", "x", "y", "z"])

assert_eq(call("ọ", 2, [123, 456, 789]), [123, 456, 789, 123, 456, 789])
assert_eq(
    call("ọ", ["abc", 123, "def", 456], 5),
    [
        "abc",
        123,
        "def",
        456,
        "abc",
        123,
        "def",
        456,
        "abc",
        123,
        "def",
        456,
        "abc",
        123,
        "def",
        456,
        "abc",
        123,
        "def",
        456,
    ],
)

assert_eq(call("ọ", ["xyz", 123], "abc"), ["xyz", 123, "xyz", 123, "xyz", 123])
assert_eq(call("ọ", [123, 456], ["abc", "def"]), ["abc", "def", "abc", "def"])

# ṛ

assert_eq(call("ṛ", 5, 3), 2)
assert_eq(call("ṛ", 3, 5), 2)
assert_eq(
    call("ṛ", 10, [-10, -5, 0, 5, 10, 15, 20, 25, 30]),
    [20, 15, 10, 5, 0, 5, 10, 15, 20],
)

assert_eq(call("ṛ", 8, "abcde"), "000abcde")
assert_eq(call("ṛ", "abcde", 3), "abcde")
assert_eq(
    call("ṛ", "xyz", [-10, -5, 0, 5, 10]),
    ["xyz0000000", "xyz00", "xyz", "00xyz", "0000000xyz"],
)

assert_eq(call("ṛ", "abc", "defghi"), "abcdefghiabc")
assert_eq(
    call("ṛ", ["123", "abc", "456", "def"], "xyz"),
    ["123xyz123", "abcxyzabc", "456xyz456", "defxyzdef"],
)

# ṣ

assert_eq(call("ṣ", 5), "     ")
assert_eq(call("ṣ", 3.14), "   ")
assert_eq(call("ṣ", -2), "")

assert_eq(call("ṣ", "abcdef"), ["f", "ef", "def", "cdef", "bcdef", "abcdef"])
assert_eq(
    call("ṣ", "Hello, World!"),
    [
        "!",
        "d!",
        "ld!",
        "rld!",
        "orld!",
        "World!",
        " World!",
        ", World!",
        "o, World!",
        "lo, World!",
        "llo, World!",
        "ello, World!",
        "Hello, World!",
    ],
)

assert_eq(
    call("ṣ", [1, 2, 3, 4, 5]), [[5], [4, 5], [3, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5]]
)
assert_eq(call("ṣ", []), [])

# ṭ

assert_eq(call("ṭ", 123, 456, 789), 123, 789, 456)
assert_eq(call("ṭ", "abc", "def", "ghi"), "abc", "ghi", "def")
assert_eq(
    call("ṭ", [123, "abc", 456], ["def", 789, "ghi"], [123, "jkl", 456]),
    [123, "abc", 456],
    [123, "jkl", 456],
    ["def", 789, "ghi"],
)

# ẉ

assert_eq(
    call("ẉ", 3, 5),
    [
        [1, 1, 1],
        [1, 1, 2],
        [1, 1, 3],
        [1, 1, 4],
        [1, 1, 5],
        [1, 2, 1],
        [1, 2, 2],
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 1],
        [1, 3, 2],
        [1, 3, 3],
        [1, 3, 4],
        [1, 3, 5],
        [1, 4, 1],
        [1, 4, 2],
        [1, 4, 3],
        [1, 4, 4],
        [1, 4, 5],
        [1, 5, 1],
        [1, 5, 2],
        [1, 5, 3],
        [1, 5, 4],
        [1, 5, 5],
        [2, 1, 1],
        [2, 1, 2],
        [2, 1, 3],
        [2, 1, 4],
        [2, 1, 5],
        [2, 2, 1],
        [2, 2, 2],
        [2, 2, 3],
        [2, 2, 4],
        [2, 2, 5],
        [2, 3, 1],
        [2, 3, 2],
        [2, 3, 3],
        [2, 3, 4],
        [2, 3, 5],
        [2, 4, 1],
        [2, 4, 2],
        [2, 4, 3],
        [2, 4, 4],
        [2, 4, 5],
        [2, 5, 1],
        [2, 5, 2],
        [2, 5, 3],
        [2, 5, 4],
        [2, 5, 5],
        [3, 1, 1],
        [3, 1, 2],
        [3, 1, 3],
        [3, 1, 4],
        [3, 1, 5],
        [3, 2, 1],
        [3, 2, 2],
        [3, 2, 3],
        [3, 2, 4],
        [3, 2, 5],
        [3, 3, 1],
        [3, 3, 2],
        [3, 3, 3],
        [3, 3, 4],
        [3, 3, 5],
        [3, 4, 1],
        [3, 4, 2],
        [3, 4, 3],
        [3, 4, 4],
        [3, 4, 5],
        [3, 5, 1],
        [3, 5, 2],
        [3, 5, 3],
        [3, 5, 4],
        [3, 5, 5],
        [4, 1, 1],
        [4, 1, 2],
        [4, 1, 3],
        [4, 1, 4],
        [4, 1, 5],
        [4, 2, 1],
        [4, 2, 2],
        [4, 2, 3],
        [4, 2, 4],
        [4, 2, 5],
        [4, 3, 1],
        [4, 3, 2],
        [4, 3, 3],
        [4, 3, 4],
        [4, 3, 5],
        [4, 4, 1],
        [4, 4, 2],
        [4, 4, 3],
        [4, 4, 4],
        [4, 4, 5],
        [4, 5, 1],
        [4, 5, 2],
        [4, 5, 3],
        [4, 5, 4],
        [4, 5, 5],
        [5, 1, 1],
        [5, 1, 2],
        [5, 1, 3],
        [5, 1, 4],
        [5, 1, 5],
        [5, 2, 1],
        [5, 2, 2],
        [5, 2, 3],
        [5, 2, 4],
        [5, 2, 5],
        [5, 3, 1],
        [5, 3, 2],
        [5, 3, 3],
        [5, 3, 4],
        [5, 3, 5],
        [5, 4, 1],
        [5, 4, 2],
        [5, 4, 3],
        [5, 4, 4],
        [5, 4, 5],
        [5, 5, 1],
        [5, 5, 2],
        [5, 5, 3],
        [5, 5, 4],
        [5, 5, 5],
    ],
)

assert_eq(
    call("ẉ", -3, "abc"),
    [
        ["a", "a", "a"],
        ["a", "a", "b"],
        ["a", "a", "c"],
        ["a", "b", "a"],
        ["a", "b", "b"],
        ["a", "b", "c"],
        ["a", "c", "a"],
        ["a", "c", "b"],
        ["a", "c", "c"],
        ["b", "a", "a"],
        ["b", "a", "b"],
        ["b", "a", "c"],
        ["b", "b", "a"],
        ["b", "b", "b"],
        ["b", "b", "c"],
        ["b", "c", "a"],
        ["b", "c", "b"],
        ["b", "c", "c"],
        ["c", "a", "a"],
        ["c", "a", "b"],
        ["c", "a", "c"],
        ["c", "b", "a"],
        ["c", "b", "b"],
        ["c", "b", "c"],
        ["c", "c", "a"],
        ["c", "c", "b"],
        ["c", "c", "c"],
    ],
)
assert_eq(
    call("ẉ", "xyz", 2),
    [
        ["x", "x"],
        ["x", "y"],
        ["x", "z"],
        ["y", "x"],
        ["y", "y"],
        ["y", "z"],
        ["z", "x"],
        ["z", "y"],
        ["z", "z"],
    ],
)

assert_eq(
    call("ẉ", 2, ["abc", "def", "ghi"]),
    [
        ["abc", "abc"],
        ["abc", "def"],
        ["abc", "ghi"],
        ["def", "abc"],
        ["def", "def"],
        ["def", "ghi"],
        ["ghi", "abc"],
        ["ghi", "def"],
        ["ghi", "ghi"],
    ],
)
assert_eq(call("ẉ", [1, 2, 3, 4, 5], 0), [[]])
assert_eq(call("ẉ", 5, []), [])

# ỵ

assert_eq(call("ỵ", 2, 12345), 345)
assert_eq(call("ỵ", 5, 3.14), "")

assert_eq(call("ỵ", -3, "abcde"), "cde")
assert_eq(call("ỵ", "", 10), "")

assert_eq(call("ỵ", 2, [123, 456, 789]), [789])
assert_eq(call("ỵ", ["abc", "def", "ghi", "jkl", "mno"], 3), ["jkl", "mno"])

# ẓ

assert_eq(call("ẓ", 2, 12345), 123)
assert_eq(call("ẓ", 5, 3.14), "")

assert_eq(call("ẓ", -3, "abcde"), "abc")
assert_eq(call("ẓ", "", 10), "")

assert_eq(call("ẓ", 2, [123, 456, 789]), [123])
assert_eq(call("ẓ", ["abc", "def", "ghi", "jkl", "mno"], 3), ["abc", "def"])

# øB

assert_eq(call("øB", "([{}])"), 1)
assert_eq(call("øB", "{]"), 0)
assert_eq(call("øB", ["(abc)", "{}[xyz]()", "{abc", ""]), [1, 1, 0, 1])

# øD

assert_eq(call("øD", "Hello, World!"), "Ƙ¥, «ʋ!")
assert_eq(call("øD", "thunnobest"), "thunnoÇ&")
assert_eq(call("øD", "withree"), "wiċŀ")
assert_eq(call("øD", 123456), "123456")

# ø<

assert_eq(call("ø<", 123, 123456), 1)
assert_eq(call("ø<", -1, -1.23), 1)
assert_eq(call("ø<", 1, [123, -1, 456, 1, 1.23]), [1, 0, 0, 1, 1])

assert_eq(call("ø<", "abc", "abcdef"), 1)
assert_eq(call("ø<", "xyz", "abcdef"), 0)

# ø>

assert_eq(call("ø>", 456, 123456), 1)
assert_eq(call("ø>", -1, -1.23), 0)
assert_eq(call("ø>", 1, [321, -1, 456, 1, 1.23]), [1, 1, 0, 1, 0])

assert_eq(call("ø>", "def", "abcdef"), 1)
assert_eq(call("ø>", "xyz", "abcdef"), 0)

# ØC

assert_eq(call("ØC", 123), 123)
assert_eq(call("ØC", "abc"), "abc")

assert_eq(call("ØC", [123, 4567, 8, 90]), "123 \n4567\n 8  \n 90 ")
assert_eq(
    call("ØC", ["abc", 1234, "xy", 56789, "z"]), " abc \n 1234\n  xy \n56789\n  z  "
)
assert_eq(call("ØC", []), "")

# ØD

assert_eq(call("ØD", 123), 0)
assert_eq(call("ØD", -4.56), 0)
assert_eq(call("ØD", "abc"), 0)

assert_eq(call("ØD", [1, 2, 3]), 1)
assert_eq(call("ØD", [["abc", "def", "ghi"], 123, 456, 789]), 2)
assert_eq(call("ØD", [1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]), 10)

assert_eq(call("ØD", []), 1)
assert_eq(call("ØD", [[[[[[[[[[]]]]]]]]]]), 10)

# ØE

assert_eq(call("ØE", 6, 123), 123123)
assert_eq(call("ØE", 10, 4.56), "4.564.564.")

assert_eq(call("ØE", 15, "abcd"), "abcdabcdabcdabc")
assert_eq(call("ØE", "thunno", -5.67), "thunn")
assert_eq(call("ØE", 3, ""), "")
assert_eq(call("ØE", "abc", 0), "")

assert_eq(
    call("ØE", [123, 456, 789], 10), [123, 456, 789, 123, 456, 789, 123, 456, 789, 123]
)
assert_eq(call("ØE", -3, ["abc", 123, "def", 456, "ghi", 789]), ["abc", 123, "def"])
assert_eq(call("ØE", 3, []), [])
assert_eq(call("ØE", [123, 456, 789], 0), [])

# ØG

assert_eq(call("ØG", [123, 4567, 89]), 4567)
assert_eq(call("ØG", ["abcd", "ef", "ghi"]), "abcd")
assert_eq(call("ØG", []), [])

assert_eq(call("ØG", 123), 123)
assert_eq(call("ØG", "abc"), "abc")

# ØI

assert_eq(call("ØI", 5, [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]), [1, 0, 0])
assert_eq(call("ØI", [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 8), [1, 1, 1])
assert_eq(
    call("ØI", [2, 3, 5, 7], [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
    [[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0]],
)

assert_eq(call("ØI", "abc", [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]), [])
assert_eq(call("ØI", [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9), [])

assert_eq(call("ØI", 123, 456), 456, 123)
assert_eq(call("ØI", "abc", "def"), "def", "abc")

# ØM

assert_eq(call("ØM", [123, 4567, 89]), 89)
assert_eq(call("ØM", ["abcd", "ef", "ghi"]), "ef")
assert_eq(call("ØM", []), [])

assert_eq(call("ØM", 123), 123)
assert_eq(call("ØM", "abc"), "abc")

# Ø.

assert_eq(call("Ø.", [1, 2, 3], [4, 5, 6]), 32)
assert_eq(call("Ø.", [123], [456, 789]), 56088)
assert_eq(call("Ø.", [], [123, 456, 789]), 0)

assert_eq(
    call("Ø.", [5, 6, 7], ["abc", "def", "ghi"]),
    "abcabcabcabcabcdefdefdefdefdefdefghighighighighighighi",
)

# Ø\

assert_eq(call("Ø\\", [123, 456, 789]), [1, 5, 9])
assert_eq(call("Ø\\", ["abcd", 12345, "xyz", 67]), ["a", 2])
assert_eq(call("Ø\\", [[123, 456, 789], ["abc", "def", "ghi"]]), [123, "def"])
assert_eq(call("Ø\\", []), [])

assert_eq(call("Ø\\", 123), 123)
assert_eq(call("Ø\\", "abc"), "abc")

# Ø/

assert_eq(call("Ø/", [123, 456, 789]), [3, 5, 7])
assert_eq(call("Ø/", ["abcd", 12345, "xyz", 67]), ["b", 1])
assert_eq(call("Ø/", [[123, 456, 789], ["abc", "def", "ghi"]]), [456, "abc"])
assert_eq(call("Ø/", []), [])

assert_eq(call("Ø/", 123), 123)
assert_eq(call("Ø/", "abc"), "abc")

# Ø“

assert_eq(call("Ø“", [123, 456, 789]), [[1, 5, 9], [2, 6], [3], [7], [4, 8]])
assert_eq(
    call("Ø“", ["abcd", 12345, "xyz", 67]), [["a", 2], ["b"], [6], ["x", 7], [1, "y"]]
)
assert_eq(
    call("Ø“", [[123, 456, 789], ["abc", "def", "ghi"]]),
    [[123, "def"], [456, "ghi"], [789], ["abc"]],
)
assert_eq(call("Ø“", []), [])

assert_eq(call("Ø“", 123), 123)
assert_eq(call("Ø“", "abc"), "abc")

# Ø”

assert_eq(call("Ø”", [123, 456, 789]), [[3, 5, 7], [2, 4], [1], [9], [6, 8]])
assert_eq(
    call("Ø”", ["abcd", 12345, "xyz", 67]), [["b", 1], ["a"], [7], ["y", 6], [2, "x"]]
)
assert_eq(
    call("Ø”", [[123, 456, 789], ["abc", "def", "ghi"]]),
    [[456, "abc"], [123], ["ghi"], [789, "def"]],
)
assert_eq(call("Ø”", []), [])

assert_eq(call("Ø”", 123), 123)
assert_eq(call("Ø”", "abc"), "abc")

# # ÆC
#
# assert_eq(call("ÆC", 0), 1.0)  # ~ 1
# assert_eq(call("ÆC", 0.524), 0.8658247218821449)  # ~ sqrt(3) / 2
# assert_eq(call("ÆC", 0.785), 0.7073882691671998)  # ~ sqrt(2) / 2
# assert_eq(call("ÆC", 1.047), 0.5001710745970702)  # ~ 1/2
# assert_eq(call("ÆC", 1.571), -0.00020367320369517789)  # ~ 0

# # ÆE
#
# assert_eq(call("ÆE", 0), 1.0)
# assert_eq(call("ÆE", 1), 2.718281828459045)
# assert_eq(
#     call("ÆE", [-1.23, 4.56, -7.89, 10.11]),
#     [0.2922925776808594, 95.58347983006624, 0.00037446957498607833, 24587.660736455156]
# )

# ÆF

assert_eq(call("ÆF", 0), 0)
assert_eq(call("ÆF", 5), 5)
assert_eq(call("ÆF", 1.23), 1)
assert_eq(call("ÆF", [10, 11, 12, 13, 14]), [55, 89, 144, 233, 377])

# ÆH

assert_eq(call("ÆH", 3, 4), 5.0)
assert_eq(call("ÆH", 12, 5), 13.0)
assert_eq(call("ÆH", 7, 24), 25.0)

assert_eq(call("ÆH", 123, "abc"), [123, "abc"])

# ÆI

assert_eq(call("ÆI", 0), 1)
assert_eq(call("ÆI", 123), 0)
assert_eq(call("ÆI", -1.23), 0)

assert_eq(
    call("ÆI", [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]), [0, 0, 1, 1, 1, 1, 1, 0, 0]
)

assert_eq(call("ÆI", "abc"), ["abc"])

# # ÆL
#
# assert_eq(call("ÆL", 3, 30), 3.0959032742893844)
# assert_eq(call("ÆL", 10, 50), 1.6989700043360185)
# assert_eq(
#     call("ÆL", 2.5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
#     [0.0, 0.75647079736603, 1.19897784671579, 1.51294159473206, 1.7564707973660298,
#      1.95544864408182, 2.1236820163783645, 2.26941239209809, 2.39795569343158, 2.51294159473206]
# )
#
# assert_eq(call("ÆL", "abc", "def"), ["abc", "def"])

# # ÆN
#
# assert_eq(call("ÆN", 0.1), -2.3025850929940455)
# assert_eq(call("ÆN", 0.25), -1.3862943611198906)
# assert_eq(call("ÆN", 0.5), -0.6931471805599453)
# assert_eq(call("ÆN", 0.75), -0.2876820724517809)
# assert_eq(call("ÆN", 0.9), -0.10536051565782628)
# assert_eq(call("ÆN", 1.0), 0.0)
# assert_eq(call("ÆN", 1.3), 0.26236426446749106)
#
# assert_eq(call("ÆN", 2), 0.6931471805599453)
# assert_eq(call("ÆN", 2.718281828459045), 1.0)
# assert_eq(call("ÆN", 3.141592653589793), 1.1447298858494002)
# assert_eq(call("ÆN", 4), 1.3862943611198906)
# assert_eq(call("ÆN", 5), 1.6094379124341003)
# assert_eq(call("ÆN", 7), 1.9459101490553132)
#
# assert_eq(call("ÆN", 10), 2.302585092994046)
# assert_eq(call("ÆN", 53), 3.970291913552122)
# assert_eq(call("ÆN", 54.59815003314423), 4.0)
# assert_eq(call("ÆN", 99), 4.59511985013459)

# ÆP

assert_eq(call("ÆP", 0), 2)
assert_eq(call("ÆP", 5), 13)
assert_eq(call("ÆP", 1.23), 3)
assert_eq(call("ÆP", [10, 11, 12, 13, 14]), [31, 37, 41, 43, 47])

# # ÆS
#
# assert_eq(call("ÆS", 0), 0.0)  # ~ 0
# assert_eq(call("ÆS", 0.524), 0.5003474302699141)  # ~ 1/2
# assert_eq(call("ÆS", 0.785), 0.706825181105366)  # ~ sqrt(2) / 2
# assert_eq(call("ÆS", 1.047), 0.8659266112878228)  # ~ sqrt(3) / 2
# assert_eq(call("ÆS", 1.571), 0.9999999792586128)  # ~ 1

# # ÆT
#
# assert_eq(call("ÆT", 0), 0.0)  # ~ 0
# assert_eq(call("ÆT", 0.524), 0.5778853590392409)  # ~ sqrt(3) / 3
# assert_eq(call("ÆT", 0.785), 0.9992039901050427)  # ~ 1
# assert_eq(call("ÆT", 1.047), 1.73126087306308)  # ~ sqrt(3)

# # Æc
#
# assert_eq(call("Æc", 0), 1.5707963267948966)  # ~ pi/2
# assert_eq(call("Æc", 0.5), 1.0471975511965976)  # ~ pi/3
# assert_eq(call("Æc", 0.707), 0.7855491633997437)  # ~ pi/4
# assert_eq(call("Æc", 0.866), 0.5236495809318289)  # ~ pi/6
# assert_eq(call("Æc", 1), 0.0)  # ~ 0

# # Æl
#
# assert_eq(call("Æl", 0.1), -1.0)
# assert_eq(call("Æl", 0.25), -0.6020599913279624)
# assert_eq(call("Æl", 0.5), -0.3010299956639812)
# assert_eq(call("Æl", 0.75), -0.12493873660829995)
# assert_eq(call("Æl", 0.9), -0.045757490560675115)
# assert_eq(call("Æl", 1.0), 0.0)
# assert_eq(call("Æl", 1.3), 0.11394335230683679)
#
# assert_eq(call("Æl", 2), 0.3010299956639812)
# assert_eq(call("Æl", 2.718281828459045), 0.4342944819032518)
# assert_eq(call("Æl", 3.141592653589793), 0.49714987269413385)
# assert_eq(call("Æl", 4), 0.6020599913279624)
# assert_eq(call("Æl", 5), 0.6989700043360189)
# assert_eq(call("Æl", 7), 0.8450980400142568)
#
# assert_eq(call("Æl", 10), 1.0)
# assert_eq(call("Æl", 53), 1.724275869600789)
# assert_eq(call("Æl", 54.59815003314423), 1.7371779276130073)
# assert_eq(call("Æl", 99), 1.99563519459755)

# # Æs
#
# assert_eq(call("Æs", 0), 0.0)  # ~ 0
# assert_eq(call("Æs", 0.5), 0.5235987755982988)  # ~ pi/6
# assert_eq(call("Æs", 0.707), 0.785247163395153)  # ~ pi/4
# assert_eq(call("Æs", 0.866), 1.0471467458630677)  # ~ pi/3
# assert_eq(call("Æs", 1), 1.5707963267948966)  # ~ pi/2

# # Æt
#
# assert_eq(call("Æt", 0), 0.0)  # ~ 0
# assert_eq(call("Æt", 0.577), 0.5233360338618205)  # ~ pi/6
# assert_eq(call("Æt", 1), 0.7853981633974483)  # ~ pi/4
# assert_eq(call("Æt", 1.732), 1.0471848490249274)  # ~ pi/3

# # Æḷ
#
# assert_eq(call("Æḷ", 0.1), -3.321928094887362)
# assert_eq(call("Æḷ", 0.25), -2.0)
# assert_eq(call("Æḷ", 0.5), -1.0)
# assert_eq(call("Æḷ", 0.75), -0.4150374992788438)
# assert_eq(call("Æḷ", 0.9), -0.15200309344504995)
# assert_eq(call("Æḷ", 1.0), 0.0)
# assert_eq(call("Æḷ", 1.3), 0.37851162325372983)
#
# assert_eq(call("Æḷ", 2), 1.0)
# assert_eq(call("Æḷ", 2.718281828459045), 1.4426950408889634)
# assert_eq(call("Æḷ", 3.141592653589793), 1.6514961294723187)
# assert_eq(call("Æḷ", 4), 2.0)
# assert_eq(call("Æḷ", 5), 2.321928094887362)
# assert_eq(call("Æḷ", 7), 2.807354922057604)
#
# assert_eq(call("Æḷ", 10), 3.321928094887362)
# assert_eq(call("Æḷ", 53), 5.727920454563199)
# assert_eq(call("Æḷ", 54.59815003314423), 5.7707801635558535)
# assert_eq(call("Æḷ", 99), 6.6293566200796095)

# Æ&

assert_eq(call("Æ&", 123, 456), 72)
assert_eq(call("Æ&", -12.34, 56.78), 48)

assert_eq(
    call("Æ&", 100, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
    [0, 0, 4, 4, 32, 32, 36, 68, 64, 64, 100],
)
assert_eq(call("Æ&", [12, 34, 56, 78, 90], [2, 4, 6, 8, 10]), [0, 0, 0, 8, 10])

assert_eq(call("Æ&", "abc", 123), ["abc", 123])

# Æ|

assert_eq(call("Æ|", 123, 456), 507)
assert_eq(call("Æ|", -12.34, 56.78), -4)

assert_eq(
    call("Æ|", 100, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
    [100, 110, 116, 126, 108, 118, 124, 102, 116, 126, 100],
)
assert_eq(call("Æ|", [12, 34, 56, 78, 90], [2, 4, 6, 8, 10]), [14, 38, 62, 78, 90])

assert_eq(call("Æ|", "abc", 123), ["abc", 123])

# Æ^

assert_eq(call("Æ^", 123, 456), 435)
assert_eq(call("Æ^", -12.34, 56.78), -52)

assert_eq(
    call("Æ^", 100, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
    [100, 110, 112, 122, 76, 86, 88, 34, 52, 62, 0],
)
assert_eq(call("Æ^", [12, 34, 56, 78, 90], [2, 4, 6, 8, 10]), [14, 38, 62, 70, 80])

assert_eq(call("Æ^", "abc", 123), ["abc", 123])

# Æ~

assert_eq(call("Æ~", 123), -124)
assert_eq(call("Æ~", 12.34), -13)
assert_eq(call("Æ~", -1.23), 0)

assert_eq(
    call("Æ~", [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
    [-12, -13, -14, -15, -16, -17, -18, -19, -20, -21],
)

assert_eq(call("Æ~", "abc"), ["abc"])

# Æ²

assert_eq(call("Æ²", 100), 1)
assert_eq(call("Æ²", 10), 0)
assert_eq(call("Æ²", 6.25), 0)

assert_eq(call("Æ²", [-3, -2, -1, 0, 1, 2, 3]), [0, 0, 0, 1, 1, 0, 0])
assert_eq(call("Æ²", [9998, 9999, 10000, 10001, 10002]), [0, 0, 1, 0, 0])

assert_eq(call("Æ²", "abc"), "abc")

# Æ³

assert_eq(call("Æ³", 1000), 1)
assert_eq(call("Æ³", 100), 0)
assert_eq(call("Æ³", 15.625), 0)

assert_eq(call("Æ³", [-3, -2, -1, 0, 1, 2, 3]), [0, 0, 0, 1, 1, 0, 0])
assert_eq(call("Æ³", [998, 999, 1000, 1001, 1002]), [0, 0, 1, 0, 0])

assert_eq(call("Æ³", "abc"), "abc")

# Æ⁴

assert_eq(call("Æ⁴", 256), 1)
assert_eq(call("Æ⁴", 1000), 0)
assert_eq(call("Æ⁴", 39.0625), 0)

assert_eq(call("Æ⁴", [-3, -2, -1, 0, 1, 2, 3]), [0, 0, 0, 1, 1, 0, 0])
assert_eq(call("Æ⁴", [623, 624, 625, 626, 627]), [0, 0, 1, 0, 0])

assert_eq(call("Æ⁴", "abc"), "abc")

# Æ⁵

assert_eq(call("Æ⁵", 1024), 1)
assert_eq(call("Æ⁵", 512), 0)
assert_eq(call("Æ⁵", 97.65625), 0)

assert_eq(call("Æ⁵", [-3, -2, -1, 0, 1, 2, 3]), [0, 0, 0, 1, 1, 0, 0])
assert_eq(call("Æ⁵", [241, 242, 243, 244, 245]), [0, 0, 1, 0, 0])

assert_eq(call("Æ⁵", "abc"), "abc")

# µR

assert_eq(call("µR", 12), "XII")
assert_eq(call("µR", -4.56), "-IV")
assert_eq(
    call("µR", [123, 456, 789, 1234, 5678, 9012]),
    ["CXXIII", "CDLVI", "DCCLXXXIX", "MCCXXXIV", "MMMMMDCLXXVIII", "MMMMMMMMMXII"],
)

assert_eq(call("µR", "CMXCIX"), 999)
assert_eq(call("µR", ""), 0)
assert_eq(call("µR", "abcdef"), 0)

# µT

assert_eq(call("µT", 123), 0)
assert_eq(call("µT", -456), 0)

assert_eq(call("µT", 1.23), 1)
assert_eq(call("µT", -4.56), 1)

assert_eq(call("µT", "abc"), 2)
assert_eq(call("µT", ""), 2)

assert_eq(call("µT", [123, 456, 789]), 3)
assert_eq(call("µT", []), 3)

# µU

assert_eq(call("µU", 122333444455555), 12345)
assert_eq(call("µU", 123112233111222333), 123123123)
assert_eq(call("µU", 123), 123)
assert_eq(call("µU", 111), 1)

assert_eq(call("µU", "abbcccddddeeeee"), "abcde")
assert_eq(call("µU", "abcaabbccaaabbbccc"), "abcabcabc")
assert_eq(call("µU", "xyz"), "xyz")
assert_eq(call("µU", "aaa"), "a")
assert_eq(call("µU", ""), "")

assert_eq(call("µU", [123, 456, 456, 789, 789, 789]), [123, 456, 789])
assert_eq(
    call("µU", [123, 456, 789, 123, 123, 456, 456, 789, 789]),
    [123, 456, 789, 123, 456, 789],
)
assert_eq(call("µU", ["abc", "def"]), ["abc", "def"])
assert_eq(call("µU", ["abc", "abc", "abc"]), ["abc"])
assert_eq(call("µU", []), [])

# µv

assert_eq(call("µv", 1, 111222333111), "222333")
assert_eq(call("µv", 123, 111222333111), "")

assert_eq(call("µv", "a", "aaabbbcccaaa"), "bbbccc")
assert_eq(call("µv", "abc", "aaabbbcccaaa"), "")
assert_eq(call("µv", "xyz", "aaabbbcccaaa"), "aaabbbcccaaa")

assert_eq(
    call("µv", 123, [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123]),
    [456, 456, 456, 789, 789, 789],
)
assert_eq(
    call(
        "µv",
        ["abc", "def", "ghi"],
        [
            "abc",
            "abc",
            "abc",
            "def",
            "def",
            "def",
            "ghi",
            "ghi",
            "ghi",
            "abc",
            "abc",
            "abc",
        ],
    ),
    [],
)
assert_eq(
    call(
        "µv",
        ["abc", "def", "ghi"],
        [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123],
    ),
    [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123],
)

# µ<

assert_eq(call("µ<", 1, 111222333111), "222333111")
assert_eq(call("µ<", 123, 111222333111), "")

assert_eq(call("µ<", "a", "aaabbbcccaaa"), "bbbcccaaa")
assert_eq(call("µ<", "abc", "aaabbbcccaaa"), "")
assert_eq(call("µ<", "xyz", "aaabbbcccaaa"), "aaabbbcccaaa")

assert_eq(
    call("µ<", 123, [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123]),
    [456, 456, 456, 789, 789, 789, 123, 123, 123],
)
assert_eq(
    call(
        "µ<",
        ["abc", "def", "ghi"],
        [
            "abc",
            "abc",
            "abc",
            "def",
            "def",
            "def",
            "ghi",
            "ghi",
            "ghi",
            "abc",
            "abc",
            "abc",
        ],
    ),
    [],
)
assert_eq(
    call(
        "µ<",
        ["abc", "def", "ghi"],
        [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123],
    ),
    [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123],
)

# µ>

assert_eq(call("µ>", 1, 111222333111), "111222333")
assert_eq(call("µ>", 123, 111222333111), "")

assert_eq(call("µ>", "a", "aaabbbcccaaa"), "aaabbbccc")
assert_eq(call("µ>", "abc", "aaabbbcccaaa"), "")
assert_eq(call("µ>", "xyz", "aaabbbcccaaa"), "aaabbbcccaaa")

assert_eq(
    call("µ>", 123, [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123]),
    [123, 123, 123, 456, 456, 456, 789, 789, 789],
)
assert_eq(
    call(
        "µ>",
        ["abc", "def", "ghi"],
        [
            "abc",
            "abc",
            "abc",
            "def",
            "def",
            "def",
            "ghi",
            "ghi",
            "ghi",
            "abc",
            "abc",
            "abc",
        ],
    ),
    [],
)
assert_eq(
    call(
        "µ>",
        ["abc", "def", "ghi"],
        [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123],
    ),
    [123, 123, 123, 456, 456, 456, 789, 789, 789, 123, 123, 123],
)

# µ&

assert_eq(call("µ&", 123, 456), 123)
assert_eq(call("µ&", 123, 0), 0)

assert_eq(call("µ&", -123, "abc"), -123)
assert_eq(call("µ&", "xyz", 0), 0)

assert_eq(call("µ&", [-1, 0, 1], ["abc", "def", ""]), [-1, 0, 1])
assert_eq(call("µ&", 5, []), [])

# µ|

assert_eq(call("µ|", 123, 456), 456)
assert_eq(call("µ|", 123, 0), 123)

assert_eq(call("µ|", -123, "abc"), "abc")
assert_eq(call("µ|", "xyz", 0), "xyz")

assert_eq(call("µ|", [-1, 0, 1], ["abc", "def", ""]), ["abc", "def", ""])
assert_eq(call("µ|", 5, []), 5)

# µ^

assert_eq(call("µ^", 123, 456), 0)
assert_eq(call("µ^", 123, 0), 1)

assert_eq(call("µ^", -123, "abc"), 0)
assert_eq(call("µ^", "xyz", 0), 1)

assert_eq(call("µ^", [-1, 0, 1], ["abc", "def", ""]), 0)
assert_eq(call("µ^", 5, []), 1)

# µ/

assert_eq(call("µ/", "b", "abcbabcba"), ["a", "c", "a", "c", "a"])
assert_eq(
    call("µ/", 3, 12345432123454321), [[1, 2], [4, 5, 4], [2, 1, 2], [4, 5, 4], [2, 1]]
)

assert_eq(call("µ/", 123, [123, 456, 789, 123, 456, 789]), [[], [456, 789], [456, 789]])

# After all the tests

all_commands = (
    [*commands]
    + ["ø" + cmd1 for cmd1 in string_digraphs]
    + ["Ø" + cmd2 for cmd2 in list_digraphs]
    + ["Æ" + cmd3 for cmd3 in random_digraphs_1]
    + ["µ" + cmd4 for cmd4 in random_digraphs_2]
)

untested_commands = sorted(
    {*all_commands} - {*tested_commands} - {*UNTESTABLE}, key=all_commands.index
)
if untested_commands:
    print(f'\u001b[33mUntested commands: {", ".join(untested_commands)}')

print(f"\u001b[32mPassed {tests_counter} tests on {len({*tested_commands})} commands.")

avg_tests = tests_counter / len({*tested_commands})
if avg_tests < 4:
    print(end=f"\u001b[33m")

print(f"Average tests per command: {avg_tests:.2f}")
print("\u001b[32m")
