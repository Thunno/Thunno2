from thunno2.dictionary import *
from thunno2.helpers import *
import sys

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


class TerminateProgramException(BaseException):
    pass


class Stack(list):
    # Push one item to the front
    def push(self, item):
        self.insert(0, item)

    # Remove n items from the front
    def rmv(self, num, default=0):
        for _ in range(num):
            if list(self):
                yield self.pop(0)
            else:
                if (not ctx.vyxal_mode) or ctx.context is None:
                    if ctx.other_il:
                        x = ctx.other_il.pop(0)
                        ctx.other_il.append(x)
                        yield x
                    else:
                        yield default
                else:
                    yield ctx.context


class Context:
    def __init__(self):
        self.stack = Stack()
        self.og_input_list = []
        self.other_il = []
        self.implicit_print = True
        self.warnings = False
        self.context = None
        self.vyxal_mode = False


ctx = Context()


class VoidType:
    def __call__(self, *args, **kwds):
        return ()

    def __eq__(self, other):
        return isinstance(other, VoidType)

    def __ne__(self, other):
        return not isinstance(other, VoidType)

    def __bool__(self):
        return False

    def __int__(self):
        return 0

    def __float__(self):
        return 0.0

    def __str__(self):
        return "Void"

    def __repr__(self):
        return "Void"

    def __iter__(self):
        yield from []


Void = VoidType()


def recursively_vectorise(lst, dct):
    for item in lst:
        if isinstance(item, list):
            yield list(recursively_vectorise(item, dct))
        else:
            for key, val in dct.items():
                if isinstance(item, key):
                    try:
                        yield val(item)
                    except Exception as E:
                        if ctx.warnings:
                            print("TRACEBACK: [ERROR - CAUGHT]", file=sys.stderr)
                            print(E, file=sys.stderr)
                        pass
                    break
            else:
                if ctx.warnings:
                    print("TRACEBACK: [UNEXPECTED TYPE]", file=sys.stderr)
                    print("Got", type(item), file=sys.stderr)
                yield Void


def recursively_distribute(x, y, dct, main=1):
    if (not isinstance(x, list)) and (not isinstance(y, list)):
        for (a, b), f in dct.items():
            if isinstance(x, a) and isinstance(y, b):
                yield f(x, y)
                break
        else:
            if ctx.warnings:
                print("TRACEBACK: [UNEXPECTED TYPE]", file=sys.stderr)
                print("Got", (type(x), type(y)), file=sys.stderr)
            yield Void
    elif isinstance(x, list) and not isinstance(y, list):
        r = []
        for i in x:
            if isinstance(i, list):
                r += (next(recursively_distribute(i, y, dct, 0)),)
            else:
                for (a, b), f in dct.items():
                    if isinstance(i, a) and isinstance(y, b):
                        r += (f(i, y),)
                        break
                else:
                    if ctx.warnings:
                        print("TRACEBACK: [UNEXPECTED TYPE]", file=sys.stderr)
                        print("Got", (type(i), type(y)), file=sys.stderr)
        yield r
    elif isinstance(y, list) and not isinstance(x, list):
        r = []
        for i in y:
            if isinstance(i, list):
                r += (next(recursively_distribute(x, i, dct, 0)),)
            else:
                for (a, b), f in dct.items():
                    if isinstance(x, a) and isinstance(i, b):
                        r += (f(x, i),)
                        break
                else:
                    if ctx.warnings:
                        print("TRACEBACK: [UNEXPECTED TYPE]", file=sys.stderr)
                        print("Got", (type(x), type(i)), file=sys.stderr)
        yield r
    else:
        if not (x + y):
            if main:
                yield []
        elif not x:
            yield from y
        elif not y:
            yield from x
        else:
            if main:
                yield list(recursively_distribute(x[0], y[0], dct, 0)) + list(
                    recursively_distribute(x[1:], y[1:], dct, 0)
                )
            else:
                yield from list(recursively_distribute(x[0], y[0], dct, 0)) + list(
                    recursively_distribute(x[1:], y[1:], dct, 0)
                )


def repeat_to_longest(*lsts):
    max_len = max(map(len, lsts))
    for inner_list in lsts:
        if not inner_list:
            yield Void
        else:
            yield (inner_list * max_len)[:max_len]


class Overload:
    def __init__(
        self,
        pop,  #: int,  # How many items do we need to pop?
        funcs,  #: dict[tuple[type], Callable],  # A mapping of the type overloads to functions
        vectorise,  #: #int,    # What vectorisation type?
        #  0 = no vectorisation,
        #  1 = monadic recursive vectorisation,
        #  2 = dyadic recursive vectorisation,
        #  3 = triadic one-level vectorisation
        keywords,  #: tuple[str]    # This is just an experiment with tokens, might not be implemented
    ):
        self.pop = pop
        self.funcs = {k if isinstance(k, tuple) else (k,): v for k, v in funcs.items()}
        self.vectorise = vectorise
        self.keywords = keywords

    def __call__(self, pop=True):
        if pop:
            items = list(ctx.stack.rmv(self.pop))
        else:
            items = list((ctx.stack + ctx.other_il + [0] * self.pop)[: self.pop])
        if self.vectorise == 0:
            for typ, fun in self.funcs.items():
                if all(isinstance(x, y) for x, y in zip(items, typ)):
                    try:
                        r = fun(*items)
                        if not isinstance(r, tuple):
                            return (r,)
                        else:
                            return r
                    except Exception as E:
                        if ctx.warnings:
                            print("TRACEBACK: [ERROR - CAUGHT]", file=sys.stderr)
                            print(E, file=sys.stderr)
                        return Void
            if ctx.warnings:
                print("TRACEBACK: [UNEXPECTED TYPE]", file=sys.stderr)
                print("Got", (*map(type, items),), file=sys.stderr)
            return Void
        elif self.vectorise == 1:
            if len(items) == 1:
                if isinstance(items[0], list):
                    try:
                        return (list(recursively_vectorise(items[0], self.funcs)),)
                    except Exception as E:
                        if ctx.warnings:
                            print("TRACEBACK: [ERROR - CAUGHT]", file=sys.stderr)
                            print(E, file=sys.stderr)
                        return Void
                else:
                    for typ, fun in self.funcs.items():
                        if isinstance(items[0], typ):
                            try:
                                r = fun(*items)
                                if not isinstance(r, tuple):
                                    return (r,)
                                else:
                                    return r
                            except Exception as E:
                                if ctx.warnings:
                                    print(
                                        "TRACEBACK: [ERROR - CAUGHT]", file=sys.stderr
                                    )
                                    print(E, file=sys.stderr)
                    else:
                        if ctx.warnings:
                            print("TRACEBACK: [UNEXPECTED TYPE]", file=sys.stderr)
                            print("Got", type(items[0]), file=sys.stderr)
            else:
                if ctx.warnings:
                    print("TRACEBACK: [IMPLEMENTATION FAULT]", file=sys.stderr)
                    print("Expected 1 item, got", len(items), file=sys.stderr)
                return Void
        elif self.vectorise == 2:
            try:
                r = tuple(recursively_distribute(items[0], items[1], self.funcs))
                return r
            except Exception as E:
                if ctx.warnings:
                    print("TRACEBACK: [ERROR - CAUGHT]", file=sys.stderr)
                    print(E, file=sys.stderr)
                return Void
        elif self.vectorise == 3:
            if not any(isinstance(it, list) for it in items):
                for typ, fun in self.funcs.items():
                    if all(isinstance(x, y) for x, y in zip(items, typ)):
                        try:
                            r = fun(*items)
                            if not isinstance(r, tuple):
                                return (r,)
                            else:
                                return r
                        except Exception as E:
                            if ctx.warnings:
                                print("TRACEBACK: [ERROR - CAUGHT]", file=sys.stderr)
                                print(E, file=sys.stderr)
                            return Void
                else:
                    if ctx.warnings:
                        print("TRACEBACK: [UNEXPECTED TYPE]", file=sys.stderr)
                        print("Got", (*map(type, items),), file=sys.stderr)
                return Void
            lst = [
                i if isinstance(i, list) else [i] * safe_max_len(*items) for i in items
            ]
            ret = []
            for il in itertools.zip_longest(*lst):
                if None in il:
                    ret.append(first_non_none(il))
                else:
                    for typ, fun in self.funcs.items():
                        if all(isinstance(x, y) for x, y in zip(il, typ)):
                            try:
                                ret.append(fun(*il))
                            except Exception as E:
                                if ctx.warnings:
                                    print(
                                        "TRACEBACK: [ERROR - CAUGHT]", file=sys.stderr
                                    )
                                    print(E, file=sys.stderr)
                                pass
                            break
                    else:
                        if ctx.warnings:
                            print("TRACEBACK: [UNEXPECTED TYPE]", file=sys.stderr)
                            print("Got", (*map(type, items),), file=sys.stderr)
            return (ret,)
        if ctx.warnings:
            print("TRACEBACK: [IMPLEMENTATION FAULT]", file=sys.stderr)
            print("Unknown vectorisation argument", self.vectorise, file=sys.stderr)
        return Void


Number = ((int, float),)
Iterable = ((list, str),)
Any = ((int, float, list, str),)

# Which characters start digraphs?
DIGRAPHS = "ØøÆµ"

"""DICTIONARY"""

commands = {
    "A": Overload(
        1, {Number: abs, str: isalpha}, 1, ("abs", "absolute", "isalpha", "is_alpha")
    ),
    "B": Overload(
        2,
        {
            (int, int): ntb,
            (str, int): to_custom_base_string,
            (int, str): length_to_base,
            (str, str): length_custom_base_string,
            (float, Any): pass_,
        },
        2,
        ("to_base", "from_decimal"),
    ),
    "C": Overload(
        1, {Number: chr2, str: ord2}, 1, ("chr", "character", "ord", "ordinal")
    ),
    "D": Overload(1, {Any: duplicate}, 0, ("dup", "duplicate")),
    "E": Overload(1, {Number: is_even, str: eval2}, 1, ("even", "is_even", "eval")),
    "F": Overload(1, {Number: factors, str: substrings}, 1, ("factors", "substrings")),
    "G": Overload(1, {Number: max2, Iterable: max3}, 0, ("max", "maximum", "greatest")),
    "H": Overload(
        1, {(int, str): from_hex, float: pass_}, 1, ("from_hex", "from_hexadecimal")
    ),
    "I": Overload(
        2,
        {
            (Number[0], Number[0]): binary_range,
            (Number[0], Iterable[0]): slice1,
            (Iterable[0], Number[0]): slice2,
            (list, list): interleave_lst,
            (str, str): interleave_str,
        },
        0,
        ("inclusive_range", "slice", "interleave"),
    ),
    "J": Overload(1, {Number: str, Iterable: empty_join}, 0, ("empty_join", "str")),
    # K is defined in the run function
    "L": Overload(
        1,
        {Number: lowered_range, str: str.lower},
        1,
        ("lowered_range", "zero_range", "lower", "lowercase"),
    ),
    "M": Overload(1, {Number: min2, Iterable: min3}, 0, ("min", "minimum")),
    "N": Overload(1, {(Number[0], str): safe_int}, 1, ("int", "integer")),
    "O": Overload(
        1, {Number: two_power, str: str.split}, 1, ("two_power", "space_split")
    ),
    "P": Overload(
        1, {Number: is_prime, str: str.swapcase}, 1, ("prime", "is_prime", "swapcase")
    ),
    "Q": Overload(
        2,
        {((Number[0], str), (Number[0], str)): not_equal},
        2,
        ("not_equal", "inequality"),
    ),
    "R": Overload(
        1,
        {Number: one_range, str: str.upper},
        1,
        ("one_range", "range", "upper", "uppercase"),
    ),
    "S": Overload(1, {Number: digit_sum, Iterable: it_sum}, 0, ("sum",)),
    "T": Overload(0, {Any: (lambda: 10)}, 0, ("ten",)),
    "U": Overload(
        1,
        {Number: uniquify_num, str: uniquify_str, list: uniquify_lst},
        0,
        ("uniquify",),
    ),
    "V": Overload(
        1,
        {Number: round, str: rot_13, list: indices_where_truthy},
        0,
        ("where_truthy", "rot13"),
    ),
    "W": Overload(1, {Any: wrap}, 0, ("wrap",)),
    # X is defined in the run function
    # Y is defined in the run function
    "Z": Overload(
        2,
        {
            (Number[0], Number[0]): range_zip1,
            (Number[0], Iterable[0]): range_zip2,
            (Iterable[0], Number[0]): range_zip3,
            (Iterable[0], Iterable[0]): zip2,
        },
        0,
        ("zip",),
    ),
    "a": Overload(
        2,
        {
            (Any[0], list): append,
            (list, Any[0]): swapped_append,
            (Any[0], Any[0]): append2,
        },
        0,
        ("append",),
    ),
    "b": Overload(
        2,
        {
            (int, (int, str)): convert_from_base,
            (str, (int, str)): convert_from_custom_base,
            (float, Any): pass_,
            (Any, float): pass_,
        },
        2,
        ("from_base", "to_decimal"),
    ),
    "c": Overload(
        2,
        {
            (Number[0], Number[0]): nCr,
            (Any, str): string_count,
            (Any, list): list_count,
        },
        0,
        ("ncr", "count"),
    ),
    "d": Overload(1, {Number: digits, str: list}, 1, ("digits", "characters", "chars")),
    "e": Overload(
        1, {Number: ten_power, str: comma_split}, 1, ("ten_power", "comma_split")
    ),
    "f": Overload(1, {Number: prime_factors, str: case}, 1, ("prime_factors", "case")),
    "g": Overload(
        1,
        {Number: digits_gcd, str: ords_gcd, list: gcd},
        0,
        ("gcd", "greatest_common_divisor"),
    ),
    "h": Overload(1, {Number: num_head, Iterable: head}, 0, ("head", "first")),
    "i": Overload(
        2,
        {
            (Number[0], Number[0]): num_ind0,
            (Number[0], Iterable[0]): indexing_0,
            (Iterable[0], Number[0]): swapped_ind0,
            (str, Iterable[0]): length_ind0,
            (list, Iterable[0]): vectorised_ind0,
        },
        0,
        ("indexing", "zero_indexing"),
    ),
    "j": Overload(
        2, {(Any, Number[0]): num_join, (Any, Iterable[0]): join}, 0, ("join",)
    ),
    # k is defined in the run function
    "l": Overload(1, {Number: num_length, Iterable: len}, 0, ("len", "length")),
    "m": Overload(
        1, {Number: num_mean, str: ord_mean, list: mean}, 0, ("mean", "avg", "average")
    ),
    # n is defined in the run function
    "o": Overload(
        2,
        {
            (Number[0], Number[0]): num_rmv,
            (Any[0], list): list_rmv,
            (list, Any[0]): swapped_list_rmv,
            (Any[0], str): str_rmv,
        },
        0,
        ("rmv", "remove"),
    ),
    "p": Overload(
        1,
        {Number: digit_product, str: ord_product, list: product},
        0,
        ("product", "prod"),
    ),
    # q is defined in the run function
    "r": Overload(1, {Number: digit_reverse, Iterable: reverse}, 0, ("reverse",)),
    "s": Overload(2, {(Any[0], Any[0]): swap}, 0, ("swap",)),
    "t": Overload(1, {Number: num_tail, Iterable: tail}, 0, ("tail", "last")),
    "u": Overload(0, {Any: (lambda: -1)}, 0, ("negative_one",)),
    "v": Overload(
        3,
        {
            (Any[0], Any[0], list): list_replace,
            (Any[0], Any[0], Any[0]): string_replace,
        },
        0,
        ("replace",),
    ),
    "w": Overload(
        1,
        {Number: factorial, str: remove_whitespace},
        1,
        ("factorial", "remove_whitespace"),
    ),
    # x is defined in the run function
    # y is defined in the run function
    "z": Overload(
        1, {Number: num_uninterleave, Iterable: uninterleave}, 0, ("uninterleave",)
    ),
    "Ȧ": Overload(
        1,
        {Number: bool2, str: isalphanum, list: any2},
        0,
        ("any", "is_alphanum", "is_alpha_num"),
    ),
    "Ḃ": Overload(1, {(int, str): from_binary, float: pass_}, 1, ("from_binary",)),
    "Ċ": Overload(
        1,
        {Number: codepage_chr, str: codepage_ord},
        1,
        ("codepage_chr", "codepage_character", "codepage_ord", "codepage_ordinal"),
    ),
    "Ḋ": Overload(
        2,
        {
            (Number[0], Number[0]): is_divisible,
            (str, Number[0]): length_divisible1,
            (Number[0], str): length_divisible2,
            (str, str): length_divisible3,
        },
        2,
        ("divisible", "is_divisible"),
    ),
    "Ė": Overload(
        1,
        {Number: inclusive_zero_range, Iterable: zero_enumerate},
        0,
        ("enumerate", "inclusive_zero_range"),
    ),
    "Ḟ": Overload(1, {Any: recursive_flatten}, 0, ("flatten", "recursive_flatten")),
    "Ġ": Overload(
        2,
        {
            (Number[0], Number[0]): dyadic_gcd,
            (str, Number[0]): ordinal_gcd1,
            (Number[0], str): ordinal_gcd2,
            (str, str): longest_common_substring,
        },
        2,
        ("dyadic_gcd",),
    ),
    "Ḣ": Overload(
        1, {Number: num_head_extract, Iterable: head_extract}, 0, ("head_extract",)
    ),
    "İ": Overload(
        2,
        {
            (Number[0], Number[0]): num_ind1,
            (Number[0], Iterable[0]): indexing_1,
            (Iterable[0], Number[0]): swapped_ind1,
            (str, Iterable[0]): length_ind1,
            (list, Iterable[0]): vectorised_ind1,
        },
        0,
        ("one_indexing",),
    ),
    "Ŀ": Overload(
        3,
        {
            (Any[0], Number[0], Any[0]): ljust1,
            (Number[0], Any[0], Any[0]): ljust2,
            (Any[0], Any[0], Any[0]): ljust3,
        },
        3,
        ("ljust", "left_justify"),
    ),
    "Ṁ": Overload(
        1, {Number: num_mode, Iterable: mode}, 0, ("mode", "most_common_element")
    ),
    "Ṅ": Overload(
        1, {Number: negate, str: rle}, 1, ("negate", "neg", "rle", "run_length_encode")
    ),
    "Ȯ": Overload(
        2,
        {
            ((str, int, float), Iterable[0]): index_of,
            (list, (str, int, float)): swapped_index_of,
            (Number[0], (str, int, float)): num_index_of,
            (list, Iterable[0]): vectorised_index_of,
        },
        0,
        ("index_of", "find"),
    ),
    "Ṗ": Overload(
        2,
        {
            (Iterable[0], Iterable[0]): cartesian_product,
            (Number[0], Iterable[0]): range_product1,
            (Iterable[0], Number[0]): range_product2,
            (Number[0], Number[0]): range_product3,
        },
        0,
        ("cartesian_product",),
    ),
    "Ṙ": Overload(1, {Number: str, str: string_repr, list: list_repr}, 0, ("repr",)),
    "Ṡ": Overload(1, {Number: digits_sort, str: str_sort, list: sort}, 0, ("sort",)),
    "Ṫ": Overload(
        1, {Number: num_tail_extract, Iterable: tail_extract}, 0, ("tail_extract",)
    ),
    "Ẇ": Overload(
        2,
        {
            (Iterable[0], Number[0]): split1,
            (Number[0], Iterable[0]): split2,
            (Number[0], Number[0]): chunk1,
            (Iterable[0], Iterable[0]): chunk2,
        },
        0,
        ("chunk", "chunk_split"),
    ),
    # Ẋ is defined in the run function
    # Ẏ is defined in the run function
    "Ż": Overload(
        1,
        {Number: num_length_range_0, Iterable: length_range_0},
        0,
        ("zero_length_range",),
    ),
    ",": Overload(2, {(Any[0], Any[0]): pair}, 0, ("pair",)),
    "⁺": Overload(
        1, {Number: increment, str: str_increment}, 1, ("increment", "incr", "plus_one")
    ),
    "⁻": Overload(
        1,
        {Number: decrement, str: str_decrement},
        1,
        ("decrement", "decr", "minus_one"),
    ),
    "⁼": Overload(
        2, {(Any[0], Any[0]): equals}, 0, ("exactly_equal", "exactly_equals")
    ),
    "+": Overload(
        2,
        {
            (Number[0], Number[0]): add,
            (str, Number[0]): string_add,
            (Number[0], str): string_add,
            (str, str): string_add,
        },
        2,
        ("add", "plus"),
    ),
    "-": Overload(
        2,
        {
            (Number[0], Number[0]): subtract,
            (str, Number[0]): slice_start,
            (Number[0], str): slice_end,
            (str, str): replace_with_nothing,
        },
        2,
        ("subtract", "minus"),
    ),
    "×": Overload(
        2,
        {
            (Number[0], Number[0]): multiply,
            (str, Number[0]): multiply,
            (Number[0], str): multiply,
            (str, str): string_cartesian_product,
        },
        2,
        ("multiply", "times"),
    ),
    "/": Overload(
        2,
        {
            (Number[0], Number[0]): divide,
            (str, Number[0]): split1,
            (Number[0], str): split2,
            (str, str): split3,
        },
        2,
        ("divide", "split"),
    ),
    "*": Overload(
        2,
        {
            (Number[0], Number[0]): exponentiate,
            (str, Number[0]): append_first1,
            (Number[0], str): append_first2,
            (str, str): regex_findall,
        },
        2,
        ("exponentiate", "power", "pow", "regex", "findall"),
    ),
    "%": Overload(
        2,
        {
            (Number[0], Number[0]): modulo,
            (str, Number[0]): swapped_format,
            (Number[0], str): str_format,
            (str, str): str_format,
        },
        2,
        ("modulo", "mod", "format"),
    ),
    "÷": Overload(
        2,
        {
            (Number[0], Number[0]): integer_divide,
            (str, Number[0]): first_split1,
            (Number[0], str): first_split2,
            (str, str): first_split3,
        },
        2,
        ("floor_divide", "integer_divide"),
    ),
    "_": Overload(
        2,
        {
            (Number[0], Number[0]): swapped_subtract,
            (str, Number[0]): slice_end2,
            (Number[0], str): slice_start2,
            (str, str): replace_with_nothing2,
        },
        2,
        ("swapped_subtract", "swapped_minus"),
    ),
    "\\": Overload(
        2,
        {
            (Number[0], Number[0]): swapped_divide,
            (str, Number[0]): split1,
            (Number[0], str): split2,
            (str, str): split4,
        },
        2,
        ("swapped_divide", "swapped_split"),
    ),
    "@": Overload(
        2,
        {
            (Number[0], Number[0]): swapped_exponentiate,
            (str, Number[0]): prepend_last1,
            (Number[0], str): prepend_last2,
            (str, str): swapped_regex_findall,
        },
        2,
        ("swapped_exponentiate", "swapped_pow", "swapped_findall", "swapped_regex"),
    ),
    "Œ": Overload(
        2,
        {
            (Number[0], Number[0]): swapped_modulo,
            (str, Number[0]): swapped_format,
            (Number[0], str): str_format,
            (str, str): str_format2,
        },
        2,
        ("swapped_modulo", "swapped_mod", "swapped_format"),
    ),
    "¦": Overload(
        2,
        {
            (Number[0], Number[0]): swapped_integer_divide,
            (str, Number[0]): last_split1,
            (Number[0], str): last_split2,
            (str, str): last_split3,
        },
        2,
        ("swapped_floor_divide", "swapped_integer_divide"),
    ),
    "=": Overload(2, {(Any[0], Any[0]): equals}, 2, ("equal", "equals")),
    "<": Overload(
        2,
        {
            (Number[0], Number[0]): less_than,
            (str, Number[0]): ord_less_than2,
            (Number[0], str): ord_less_than1,
            (str, str): less_than,
        },
        2,
        ("less_than",),
    ),
    ">": Overload(
        2,
        {
            (Number[0], Number[0]): greater_than,
            (str, Number[0]): ord_greater_than2,
            (Number[0], str): ord_greater_than1,
            (str, str): greater_than,
        },
        2,
        ("greater_than",),
    ),
    "©": Overload(
        2,
        {
            (Number[0], Number[0]): less_than_or_equal_to,
            (str, Number[0]): ord_less_than_or_equal_to2,
            (Number[0], str): ord_less_than_or_equal_to1,
            (str, str): less_than_or_equal_to,
        },
        2,
        ("less_than_or_equal_to",),
    ),
    "®": Overload(
        2,
        {
            (Number[0], Number[0]): greater_than_or_equal_to,
            (str, Number[0]): ord_greater_than_or_equal_to2,
            (Number[0], str): ord_greater_than_or_equal_to1,
            (str, str): greater_than_or_equal_to,
        },
        2,
        ("greater_than_or_equal_to",),
    ),
    "&": Overload(2, {(Any[0], Any[0]): logical_and}, 2, ("and", "logical_and")),
    "|": Overload(2, {(Any[0], Any[0]): logical_or}, 2, ("or", "logical_or")),
    "^": Overload(
        1,
        {Number: num_uninterleave_dump, Iterable: uninterleave_dump},
        0,
        ("uninterleave_dump",),
    ),
    "~": Overload(1, {Any: logical_not}, 1, ("not", "logical_not")),
    "ð": Overload(0, {Any: (lambda: " ")}, 0, ("space",)),
    "Ð": Overload(1, {Any: triplicate}, 0, ("triplicate",)),
    "ȧ": Overload(
        3,
        {
            (Any[0], Number[0], Iterable[0]): assign,
            (Any[0], Iterable[0], Number[0]): swapped_assign,
            (Any[0], list, Iterable[0]): vectorised_assign,
            (Any[0], str, Iterable[0]): length_assign,
            (Any[0], Number[0], Number[0]): num_assign,
        },
        0,
        ("assign",),
    ),
    "ḃ": Overload(
        1, {Number: to_binary, str: ord_bin}, 1, ("bin", "binary", "to_binary")
    ),
    "ċ": Overload(
        2,
        {
            (Number[0], Iterable[0]): combinations1,
            (Iterable[0], Number[0]): combinations2,
            (Number[0], Number[0]): combinations3,
            (Iterable[0], Iterable[0]): set_union,
        },
        0,
        ("combinations", "union"),
    ),
    "ḋ": Overload(
        2,
        {
            (Number[0], Number[0]): divmod2,
            (Number[0], list): from_list_of_digits,
            (list, Number[0]): from_list_of_digits_2,
            (Any[0], Any[0]): pass_,
        },
        0,
        ("divmod", "from_digits"),
    ),
    "ė": Overload(
        1,
        {Number: exclusive_one_range, Iterable: length_range},
        0,
        ("length_range", "exclusive_one_range"),
    ),
    "ḟ": Overload(
        1,
        {Number: prime_factor_exponents, str: str.title},
        1,
        ("prime_factor_exponents", "title", "title_case"),
    ),
    "ġ": Overload(
        1,
        {Number: consecutive_digits, Iterable: group_consecutive},
        0,
        ("group_consecutive",),
    ),
    "ḣ": Overload(
        1, {Number: num_head_remove, Iterable: head_remove}, 0, ("head_remove",)
    ),
    "ŀ": Overload(
        1,
        {Number: digits_lcm, str: ords_lcm, list: lcm},
        0,
        ("lcm", "lowest_common_multiple"),
    ),
    "ṁ": Overload(
        1, {Number: num_median, str: ord_median, list: median}, 0, ("median",)
    ),
    # ṅ is defined in the run function
    "ȯ": Overload(
        2,
        {
            (Number[0], Number[0]): round_decimal_places,
            (Number[0], Iterable[0]): range_intersection1,
            (Iterable[0], Number[0]): range_intersection2,
            (Iterable[0], Iterable[0]): set_intersection,
        },
        0,
        ("set_intersection", "round_dps"),
    ),
    "ṗ": Overload(
        2,
        {
            (Number[0], Iterable[0]): permutations1,
            (Iterable[0], Number[0]): permutations2,
            (Number[0], Number[0]): permutations3,
            (Iterable[0], Iterable[0]): set_difference,
        },
        0,
        ("permutations", "set_difference"),
    ),
    "ṙ": Overload(
        3,
        {
            (Any[0], Number[0], Any[0]): rjust1,
            (Number[0], Any[0], Any[0]): rjust2,
            (Any[0], Any[0], Any[0]): rjust3,
        },
        3,
        ("rjust", "right_justify"),
    ),
    "ṡ": Overload(
        1,
        {Number: numcumsum, str: prefixes, list: cumsum},
        0,
        ("cumsum", "cumulative_sums"),
    ),
    "ṫ": Overload(
        1, {Number: num_tail_remove, Iterable: tail_remove}, 0, ("tail_remove",)
    ),
    "ẇ": Overload(
        2,
        {
            (Number[0], Number[0]): chunk5,
            (Number[0], Iterable[0]): chunk3,
            (Iterable[0], Number[0]): chunk4,
            (Iterable[0], Iterable[0]): chunk6,
        },
        0,
        ("chunk_wrap", "split_chunk"),
    ),
    "ż": Overload(
        1,
        {Number: num_length_range, Iterable: length_range_no_pop},
        0,
        ("length_range_no_pop",),
    ),
    "Ạ": Overload(
        0,
        {Any: (lambda: string.ascii_lowercase)},
        0,
        ("alphabet", "lowercase_alphabet"),
    ),
    "Ḅ": Overload(
        2,
        {
            (int, int): ntbs,
            (str, int): character_multiply1,
            (int, str): character_multiply2,
            (str, str): regex_split,
            (float, Any): pass_,
        },
        2,
        ("to_base_string", "character_multiply", "regex_split"),
    ),
    "Ḍ": Overload(1, {Any: double}, 1, ("double",)),
    "Ẹ": Overload(
        1,
        {Number: num_dump, Iterable: dump},
        0,
        ("dump",),
    ),
    "Ḥ": Overload(
        1, {Number: to_hex, str: ord_hex}, 1, ("hex", "hexadecimal", "to_hexadecimal")
    ),
    "Ị": Overload(
        1,
        {Number: reciprocal, str: remove_non_alphabets},
        1,
        ("reciprocal", "inverse", "filter_isalpha", "only_alphabetic"),
    ),
    "Ḳ": Overload(1, {Number: num_bifurcate, Iterable: bifurcate}, 0, ("bifurcate",)),
    "Ḷ": Overload(
        2,
        {
            (Number[0], Number[0]): dyadic_lcm,
            (str, Number[0]): ordinal_lcm1,
            (Number[0], str): ordinal_lcm2,
            (str, str): ordinal_lcm3,
        },
        2,
        ("dyadic_lcm",),
    ),
    "Ṃ": Overload(1, {Number: num_mirror, Iterable: mirror}, 0, ("mirror",)),
    "Ṇ": Overload(
        3,
        {
            (list, list, (int, float, str)): str_transliterate,
            (list, list, list): list_transliterate,
            (list, (int, float, str), (int, float, str)): str_transliterate_overload_1,
            (list, (int, float, str), list): list_transliterate_overload_1,
            ((int, float, str), list, (int, float, str)): str_transliterate_overload_2,
            ((int, float, str), list, list): list_transliterate_overload_2,
            (
                (int, float, str),
                (int, float, str),
                (int, float, str),
            ): str_transliterate_overload_3,
            ((int, float, str), (int, float, str), list): list_transliterate_overload_3,
        },
        0,
        ("transliterate",),
    ),
    "Ọ": Overload(
        2,
        {
            (Number[0], Number[0]): dyadic_minimum,
            (Any[0], Any[0]): string_dyadic_minimum,
        },
        2,
        ("dyadic_minimum",),
    ),
    "Ṛ": Overload(
        2,
        {
            (Number[0], Iterable[0]): combinations_with_replacement1,
            (Iterable[0], Number[0]): combinations_with_replacement2,
            (Number[0], Number[0]): combinations_with_replacement3,
            (Iterable[0], Iterable[0]): combinations_with_replacement4,
        },
        0,
        ("combinations_with_replacement",),
    ),
    "Ṣ": Overload(
        1,
        {Number: digit_deltas, str: ord_deltas, list: deltas},
        0,
        ("deltas", "forward_differences"),
    ),
    "Ṭ": Overload(
        1, {Number: digits_wrap, str: list_wrap, list: transpose}, 0, ("transpose",)
    ),
    "Ụ": Overload(
        1,
        {Number: num_rotate_left_once, Iterable: rotate_left_once},
        0,
        ("rotate_left_once",),
    ),
    "Ṿ": Overload(
        1,
        {Number: num_rotate_right_once, Iterable: rotate_right_once},
        0,
        ("rotate_right_once",),
    ),
    "Ẉ": Overload(
        2,
        {
            (Number[0], Number[0]): num_uninterleave2,
            (Number[0], Iterable[0]): uninterleave2,
            (Iterable[0], Number[0]): swapped_uninterleave,
            (Iterable[0], Iterable[0]): len_uninterleave,
        },
        0,
        ("uninterleave_into_pieces",),
    ),
    "Ỵ": Overload(
        2,
        {
            (Number[0], Number[0]): left_bit_shift,
            (Number[0], Iterable[0]): rotate_left,
            (Iterable[0], Number[0]): swapped_rotate_left,
            (Iterable[0], Iterable[0]): len_rotate_left,
        },
        0,
        ("rotate_left", "left_bit_shift"),
    ),
    "Ẓ": Overload(
        2,
        {
            (Number[0], Number[0]): right_bit_shift,
            (Number[0], Iterable[0]): rotate_right,
            (Iterable[0], Number[0]): swapped_rotate_right,
            (Iterable[0], Iterable[0]): len_rotate_right,
        },
        0,
        ("rotate_right", "right_bit_shift"),
    ),
    "Ä": Overload(
        1,
        {Number: num_to_alphabet, str: alphabet_to_num},
        1,
        ("num_to_alphabet", "alphabet_to_num"),
    ),
    "¶": Overload(0, {Any: (lambda: "\n")}, 0, ("newline",)),
    "Ç": Overload(0, {Any: (lambda: "|")}, 0, ("pipe",)),
    "¬": Overload(
        1, {Any: logical_not}, 0, ("non_vectorised_not", "non_vectorised_logical_not")
    ),
    "§": Overload(
        2,
        {
            (Number[0], Number[0]): dyadic_maximum,
            (Any[0], Any[0]): string_dyadic_maximum,
        },
        2,
        ("dyadic_maximum",),
    ),
    "½": Overload(1, {Number: halve, str: chunk_halve}, 1, ("halve",)),
    "Ƈ": Overload(
        2,
        {
            (Number[0], Number[0]): nPr,
            (Any, list): list_contains,
            (Any, str): string_contains,
        },
        0,
        ("npr", "contains"),
    ),
    "Ɗ": Overload(
        2,
        {
            (Number[0], (int, float, str)): str_remove_at_index,
            (Number[0], list): list_remove_at_index,
            (str, Number[0]): swapped_str_remove_at_index,
            (list, Number[0]): swapped_list_remove_at_index,
            (Any[0], list): list_rmv,
            (list, Any[0]): swapped_list_rmv,
            (Any[0], str): str_rmv,
        },
        0,
        ("drop_at_index", "remove_at_index"),
    ),
    "Ƒ": Overload(
        1,
        {Number: unique_prime_factors, Iterable: substrings},
        0,
        ("unique_prime_factors", "sublists"),
    ),
    "Ɠ": Overload(0, {Any: (lambda: 16)}, 0, ("sixteen",)),
    "Ɱ": Overload(
        1, {Number: num_palindromise, Iterable: palindromise}, 0, ("palindromise",)
    ),
    "Ɲ": Overload(
        1,
        {Number: integer_partitions, Iterable: newline_join},
        0,
        ("integer_partitions", "newline_join", "join_by_newlines"),
    ),
    "Ƥ": Overload(
        2,
        {
            (Any[0], list): prepend,
            (list, Any[0]): swapped_prepend,
            (Any[0], Any[0]): prepend2,
        },
        0,
        ("prepend",),
    ),
    "Ƭ": Overload(
        2,
        {
            (Any[0], list): transpose_with_filler,
            (list, Any[0]): swapped_transpose_with_filler,
            (Number[0], Any[0]): digits_wrap_2,
            (str, Any[0]): list_wrap_2,
        },
        0,
        ("transpose_with_filler",),
    ),
    "ɓ": Overload(1, {Any: boolify}, 1, ("boolify",)),
    "ƈ": Overload(1, {Number: num_counts, Iterable: counts}, 0, ("counts",)),
    "ɗ": Overload(1, {Number: parity, str: second_half}, 1, ("parity", "second_half")),
    "ƒ": Overload(1, {Number: num_prefixes, Iterable: prefixes}, 0, ("prefixes",)),
    "ɠ": Overload(
        0, {Any: (lambda: 256)}, 0, ("two_fifty_six", "two_hundred_fifty_six")
    ),
    "ɦ": Overload(0, {Any: (lambda: 100)}, 0, ("hundred", "one_hundred")),
    "ƙ": Overload(
        1,
        {Number: increment_twice, Iterable: grade_up},
        0,
        ("grade_up", "increment_twice"),
    ),
    "ɱ": Overload(
        2,
        {
            (Number[0], Number[0]): num_head_slice,
            (Number[0], Iterable[0]): head_slice,
            (Iterable[0], Number[0]): swapped_head_slice,
            (Iterable[0], Iterable[0]): len_head_slice,
        },
        0,
        ("head_slice",),
    ),
    "ɲ": Overload(
        2,
        {
            (Number[0], Number[0]): num_tail_slice,
            (Number[0], Iterable[0]): tail_slice,
            (Iterable[0], Number[0]): swapped_tail_slice,
            (Iterable[0], Iterable[0]): len_tail_slice,
        },
        0,
        ("tail_slice",),
    ),
    "ƥ": Overload(1, {Any: pop_}, 0, ("pop",)),
    "ʠ": Overload(1, {Number: num_powerset, Iterable: powerset}, 0, ("powerset",)),
    "ɼ": Overload(
        1,
        {Number: randint, Iterable: randchoice},
        0,
        ("random", "random_choice", "randint"),
    ),
    "ʂ": Overload(
        1,
        {Number: sign, str: sentence_case, list: sum_each},
        0,
        ("sign", "sentence_case", "sum_each"),
    ),
    "ƭ": Overload(
        1,
        {Number: square_root, str: every_second_item},
        1,
        ("square_root", "every_second_item"),
    ),
    "²": Overload(1, {Number: square, str: chunk_wrap_2}, 1, ("square",)),
    "³": Overload(1, {Number: cube, str: chunk_wrap_3}, 1, ("cube",)),
    "⁴": Overload(
        1, {Number: fourth, str: chunk_wrap_4}, 1, ("fourth", "fourth_power")
    ),
    "⁵": Overload(1, {Number: fifth, str: chunk_wrap_5}, 1, ("fifth", "fifth_power")),
    "ạ": Overload(1, {Number: num_all_equal, Iterable: all_equal}, 0, ("all_equal",)),
    "ḅ": Overload(1, {Any: equals_one}, 1, ("equals_one",)),
    "ḍ": Overload(
        2,
        {
            (Number[0], Number[0]): range_ssd1,
            (Number[0], Iterable[0]): range_ssd2,
            (Iterable[0], Number[0]): range_ssd3,
            (Iterable[0], Iterable[0]): symmetric_set_difference,
        },
        0,
        ("symmetric_set_difference",),
    ),
    "ẹ": Overload(1, {Number: num_enclose, Iterable: enclose}, 0, ("enclose",)),
    "ḥ": Overload(
        2,
        {
            (list, list): add,
            (list, Any[0]): add_digits1,
            (Any[0], list): add_digits2,
            (Any[0], Any[0]): add_digits3,
        },
        0,
        ("concatenate", "merge"),
    ),
    "ị": Overload(
        2,
        {
            (Number[0], Number[0]): corresponding_digit_filter_1,
            (Number[0], Iterable[0]): corresponding_digit_filter_2,
            (Iterable[0], Number[0]): corresponding_digit_filter_3,
            (Iterable[0], Iterable[0]): corresponding_filter,
        },
        0,
        ("corresponding_filter",),
    ),
    "ḳ": Overload(
        1,
        {Number: num_sort_uniquify, str: str_sort_uniquify, list: list_sort_uniquify},
        0,
        ("sorted_uniquify",),
    ),
    "ḷ": Overload(
        1,
        {Number: complement, str: islower, list: length_of_each},
        0,
        ("length_of_each", "complement", "is_lower"),
    ),
    "ṃ": Overload(
        1,
        {Number: math.ceil, str: is_vowel, list: reverse_each},
        0,
        ("ceil", "is_vowel", "reverse_each"),
    ),
    "ọ": Overload(
        2,
        {
            (Number[0], list): multiply,
            (list, Number[0]): multiply,
            (Number[0], Any[0]): digits_repeat1,
            (Any[0], Number[0]): digits_repeat2,
            (list, (int, float, str)): length_repeat1,
            (Any[0], Any[0]): length_repeat2,
        },
        0,
        ("repeat",),
    ),
    "ṛ": Overload(
        2,
        {
            (Number[0], Number[0]): absolute_difference,
            (Number[0], str): zfill1,
            (str, Number[0]): zfill2,
            (str, str): surround,
        },
        2,
        ("absolute_difference", "zfill", "surround"),
    ),
    "ṣ": Overload(1, {Number: spaces, Iterable: suffixes}, 0, ("suffixes", "spaces")),
    "ṭ": Overload(3, {(Any[0], Any[0], Any[0]): triple_swap}, 0, ("triple_swap",)),
    "ẉ": Overload(
        2,
        {
            (Number[0], Number[0]): range_cartesian_power,
            (Number[0], Iterable[0]): cartesian_power,
            (Iterable[0], Number[0]): swapped_cartesian_power,
            (Iterable[0], Iterable[0]): cartesian_product,
        },
        0,
        ("cartesian_power",),
    ),
    "ỵ": Overload(
        2,
        {
            (Number[0], Number[0]): num_head_remove_2,
            (Number[0], Iterable[0]): head_remove_2,
            (Iterable[0], Number[0]): swapped_head_remove_2,
            (Iterable[0], Iterable[0]): len_head_remove_2,
        },
        0,
        ("head_remove_many",),
    ),
    "ẓ": Overload(
        2,
        {
            (Number[0], Number[0]): num_tail_remove_2,
            (Number[0], Iterable[0]): tail_remove_2,
            (Iterable[0], Number[0]): swapped_tail_remove_2,
            (Iterable[0], Iterable[0]): len_tail_remove_2,
        },
        0,
        ("tail_remove_many",),
    ),
}

string_digraphs = {
    "B": Overload(
        1,
        {Any: brackets_are_balanced},
        1,
        ("balanced_brackets", "brackets_are_balanced"),
    ),
    "D": Overload(
        1, {Any: optimal_dictionary_compression}, 1, ("optimal_dictionary_compression",)
    ),
    "v": Overload(
        2,
        {
            (list, Any[0]): canvas_draw,
            (Number[0], str): digits_canvas_draw,
            (str, list): swapped_canvas_draw,
            (str, Number[0]): swapped_digits_canvas_draw,
            (Any[0], Any[0]): pass_,
        },
        0,
        ("canvas", "draw", "canvas_draw"),
    ),
    "V": Overload(
        2,
        {
            (list, Any[0]): blank_canvas_draw,
            (Number[0], str): blank_digits_canvas_draw,
            (str, list): blank_swapped_canvas_draw,
            (str, Number[0]): blank_swapped_digits_canvas_draw,
            (Any[0], Any[0]): pass_,
        },
        0,
        ("blank_canvas", "blank_draw", "blank_canvas_draw"),
    ),
    "^": Overload(0, {Any: clear_canvas}, 0, ("clear_canvas",)),
    "<": Overload(2, {(Any[0], Any[0]): str_starts_with}, 2, ("starts_with",)),
    ">": Overload(2, {(Any[0], Any[0]): str_ends_with}, 2, ("starts_with",)),
}

list_digraphs = {
    "C": Overload(
        1, {((int, float, str),): pass_, list: centre_list}, 0, ("center", "centre")
    ),
    "D": Overload(1, {Any: depth}, 0, ("depth",)),
    "E": Overload(
        2,
        {
            (Number[0], Iterable[0]): extend_truncate,
            (Iterable[0], Number[0]): swapped_extend_truncate,
            (Iterable[0], Iterable[0]): length_extend_truncate,
            (Number[0], Number[0]): num_extend_truncate,
        },
        0,
        (
            "extend",
            "truncate",
            "extend_truncate",
            "extend_to_length",
            "truncate_to_length",
        ),
    ),
    "G": Overload(1, {((int, float, str),): pass_, list: longest}, 0, ("longest",)),
    "I": Overload(
        2,
        {
            ((int, float, str), list): multidimensional_index,
            (list, (int, float, str)): swapped_multidimensional_index,
            (list, list): vectorised_multidimensional_index,
            (Any[0], Any[0]): pass_,
        },
        0,
        ("multidimensional_index",),
    ),
    "M": Overload(1, {((int, float, str),): pass_, list: shortest}, 0, ("shortest",)),
    ".": Overload(
        2, {(list, list): dot_product, (Any[0], Any[0]): pass_}, 0, ("dot_product",)
    ),
    "\\": Overload(
        1, {((int, float, str),): pass_, list: main_diagonal}, 0, ("main_diagonal",)
    ),
    "/": Overload(
        1, {((int, float, str),): pass_, list: anti_diagonal}, 0, ("anti_diagonal",)
    ),
    "“": Overload(
        1, {((int, float, str),): pass_, list: all_diagonals}, 0, ("all_diagonals",)
    ),
    "”": Overload(
        1,
        {((int, float, str),): pass_, list: all_anti_diagonals},
        0,
        ("all_anti_diagonals",),
    ),
}

random_digraphs_1 = {
    "C": Overload(1, {Any: cosine}, 1, ("cosine", "cos")),
    "D": Overload(1, {Any: degrees}, 1, ("degrees",)),
    "E": Overload(1, {Any: exponent}, 1, ("exponent",)),
    "F": Overload(1, {Any: nth_fibonacci_number}, 1, ("nth_fibonacci_number",)),
    "H": Overload(2, {(Any[0], Any[0]): hypotenuse}, 2, ("hypot", "hypotenuse")),
    "I": Overload(1, {Any: insignificant}, 1, ("insignificant",)),
    "L": Overload(2, {(Any[0], Any[0]): logarithm}, 2, ("log", "logarithm")),
    "N": Overload(1, {Any: ln}, 1, ("natural_log", "natural_logarithm")),
    "P": Overload(1, {Any: nth_prime}, 1, ("nth_prime",)),
    "R": Overload(1, {Any: radians}, 1, ("radians",)),
    "S": Overload(1, {Any: sine}, 1, ("sine", "sin")),
    "T": Overload(1, {Any: tangent}, 1, ("tangent", "tan")),
    "c": Overload(1, {Any: arc_cosine}, 1, ("arc_cosine", "arccos")),
    "l": Overload(1, {Any: log10}, 1, ("log10", "common_log", "common_logarithm")),
    "s": Overload(1, {Any: arc_sine}, 1, ("arc_sine", "arcsin")),
    "t": Overload(1, {Any: arc_tangent}, 1, ("arc_tangent", "arctan")),
    "ḷ": Overload(1, {Any: log2}, 1, ("log2", "log_base_2")),
    "&": Overload(2, {(Any[0], Any[0]): bitwise_and}, 2, ("bitwise_and",)),
    "|": Overload(2, {(Any[0], Any[0]): bitwise_or}, 2, ("bitwise_or",)),
    "^": Overload(2, {(Any[0], Any[0]): bitwise_xor}, 2, ("bitwise_xor",)),
    "~": Overload(1, {Any: bitwise_not}, 1, ("bitwise_not",)),
    "²": Overload(1, {Any: perfect_square}, 1, ("perfect_square",)),
    "³": Overload(1, {Any: perfect_cube}, 1, ("perfect_cube",)),
    "⁴": Overload(1, {Any: perfect_fourth}, 1, ("perfect_fourth",)),
    "⁵": Overload(1, {Any: perfect_fifth}, 1, ("perfect_fifth",)),
}

random_digraphs_2 = {
    "R": Overload(
        1, {Number: to_roman_numerals, str: from_roman_numerals}, 1, ("roman_numerals",)
    ),
    "T": Overload(1, {Any: type_of}, 0, ("type",)),
    "U": Overload(
        1,
        {
            Number: num_connected_uniquify,
            str: str_connected_uniquify,
            list: connected_uniquify,
        },
        0,
        ("connected_uniquify",),
    ),
    "r": Overload(
        1,
        {Number: range_shuffle, str: str_shuffle, list: shuffle},
        0,
        ("random_shuffle",),
    ),
    "v": Overload(
        2,
        {
            (list, list): vectorised_trim,
            (Any[0], list): trim,
            (list, Any[0]): swapped_trim,
            (Any[0], (int, float, str)): str_trim,
        },
        0,
        ("trim",),
    ),
    "<": Overload(
        2,
        {
            (list, list): vectorised_left_trim,
            (Any[0], list): left_trim,
            (list, Any[0]): swapped_left_trim,
            (Any[0], (int, float, str)): str_left_trim,
        },
        0,
        ("left_trim",),
    ),
    ">": Overload(
        2,
        {
            (list, list): vectorised_right_trim,
            (Any[0], list): right_trim,
            (list, Any[0]): swapped_right_trim,
            (Any[0], (int, float, str)): str_right_trim,
        },
        0,
        ("right_trim",),
    ),
    "&": Overload(
        2,
        {(Any[0], Any[0]): logical_and},
        0,
        ("non_vectorised_and", "non_vectorised_logical_and"),
    ),
    "|": Overload(
        2,
        {(Any[0], Any[0]): logical_or},
        0,
        ("non_vectorised_or", "non_vectorised_logical_or"),
    ),
    "^": Overload(
        2,
        {(Any[0], Any[0]): logical_xor},
        0,
        ("non_vectorised_xor", "non_vectorised_logical_xor"),
    ),
    "/": Overload(
        2,
        {
            (list, Any[0]): swapped_split_on,
            (Any[0], Iterable[0]): split_on,
            (Any[0], Number[0]): num_split_on,
        },
        0,
        ("split_on",),
    ),
}


def get_a_function(command):
    if not command:
        return Void
    if len(command) == 1:
        return commands.get(command, Void)
    if command[0] == "ø":
        return string_digraphs.get(command[1], Void)
    if command[0] == "Ø":
        return list_digraphs.get(command[1], Void)
    if command[0] == "Æ":
        return random_digraphs_1.get(command[1], Void)
    if command[0] == "µ":
        return random_digraphs_2.get(command[1], Void)
    return Void
