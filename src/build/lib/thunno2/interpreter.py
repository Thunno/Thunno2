from thunno2 import dictionary
from thunno2.commands import *
from thunno2.lexer import tokenise
import string
import copy
import sys

"""The main interpreter. To run a Thunno 2 program, use the run function."""

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

vars_dict = {
    "x": 1,  # x defaults to 1
    "y": 2,  # y defaults to 2
    "ga": [],  # global array defaults to []
}

"""RUN FUNCTION"""


def run(code, *, context=None, iteration_index=None):
    if context is None:
        n = 0
    else:
        n = context
    ctx.context = context
    # while ctx.index < len(code):
    for chars, desc, info in code:
        if desc == "command" or desc == "digraph":
            if info != Void:
                values = info()
                for value in values:
                    ctx.stack.push(value)
        elif desc in (
            "number",
            "string",
            "one character",
            "two characters",
            "three characters",
            "list",
        ):
            ctx.stack.push(info)
        elif desc == "lowercase alphabetic compression":
            base255_number = decompress(info, "“")
            decompressed_string = to_custom_base_string(
                " " + string.ascii_lowercase, base255_number
            )
            ctx.stack.push(decompressed_string)
        elif desc == "title case alphabetic compression":
            base255_number = decompress(info, "”")
            decompressed_string = to_custom_base_string(
                " " + string.ascii_lowercase, base255_number
            )
            ctx.stack.push(decompressed_string.title())
        elif desc == "lowercase dictionary compression":
            lst = []
            i = 0
            while i < len(info):
                c = info[i]
                if c in dictionary.dictionary_codepage:
                    try:
                        i += 1
                        lst.append(dictionary.dictionary_decompress_string(c + info[i]))
                    except:
                        pass
                elif c == "\\":
                    try:
                        i += 1
                        lst.append(info[i])
                    except:
                        lst.append("\\")
                else:
                    lst.append(c)
                i += 1
            ctx.stack.push("".join(lst))
        elif desc == "title case dictionary compression":
            lst = []
            i = 0
            while i < len(info):
                c = info[i]
                if c in dictionary.dictionary_codepage:
                    try:
                        i += 1
                        lst.append(
                            dictionary.dictionary_decompress_string(c + info[i]).title()
                        )
                    except:
                        pass
                elif c == "\\":
                    try:
                        i += 1
                        lst.append(info[i])
                    except:
                        lst.append("\\")
                else:
                    lst.append(c)
                i += 1
            ctx.stack.push("".join(lst))
        elif desc == "one word dictionary compression":
            ctx.stack.push(dictionary.dictionary_decompress_string(info).title())
        elif desc == "two words dictionary compression":
            ctx.stack.push(
                dictionary.dictionary_decompress_string(info[:2]).title()
                + dictionary.dictionary_decompress_string(info[2:]).title()
            )
        elif desc == "compressed number" or desc == "small compressed number":
            base255_number = decompress(info, "»")
            ctx.stack.push(base255_number)
        elif desc == "compressed list":
            base255_number = decompress(info, "¿")
            decompressed_string = to_custom_base_string("0123456789-.,", base255_number)
            try:
                if decompressed_string[:1] == ",":
                    decompressed_string = "0" + decompressed_string
                if decompressed_string[-1:] == ",":
                    decompressed_string += "0"
                if decompressed_string[:1] == ".":
                    decompressed_string = ".5" + decompressed_string[1:]
                if decompressed_string[-1:] == ".":
                    decompressed_string += "5"
                decompressed_string = decompressed_string.replace(",,", ",0,").replace(
                    ",.,", ",.5,"
                )
                e = eval(decompressed_string)
                if isinstance(e, tuple):
                    ctx.stack.push(list(e))
                else:
                    ctx.stack.push(e)
            except:
                ctx.stack.push(decompressed_string)
        elif desc == "variable get":
            ctx.stack.push(vars_dict.get(info, 0))
        elif desc == "variable set":
            a = next(ctx.stack.rmv(1))
            vars_dict[info] = a
        elif desc == "single function map":
            a = next(ctx.stack.rmv(1))
            func = info
            if func != Void:
                x = listify(a)
                r = []
                old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
                for i in x:
                    ctx.stack = Stack(copy.deepcopy(list(old_stack).copy()))
                    ctx.stack.push(i)
                    for j in func():
                        r.append(j)
                ctx.stack.push(r)
        elif desc == "outer product":
            a, b = ctx.stack.rmv(2)
            func = info
            if func != Void:
                x = listify(a)
                r = []
                old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
                if isinstance(a, list):
                    if isinstance(b, list):
                        for j in b:
                            r.append([])
                            for i in a:
                                ctx.stack = Stack(
                                    [i, j] + copy.deepcopy(list(old_stack).copy())
                                )
                                for k in func():
                                    r[-1].append(k)
                    else:
                        for i in a:
                            ctx.stack = Stack(
                                [i, b] + copy.deepcopy(list(old_stack).copy())
                            )
                            for k in func():
                                r.append(k)
                else:
                    if isinstance(b, list):
                        for i in b:
                            ctx.stack = Stack(
                                [a, i] + copy.deepcopy(list(old_stack).copy())
                            )
                            for k in func():
                                r.append(k)
                    else:
                        ctx.stack.push(b)
                        ctx.stack.push(a)
                        k = func()
                        if k:
                            r = k[-1]
                ctx.stack.push(r)
        elif desc == "single function filter":
            a = next(ctx.stack.rmv(1))
            func = info
            if func != Void:
                x = listify(a)
                r = []
                old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
                for i in x:
                    ctx.stack = Stack(copy.deepcopy(list(old_stack).copy()))
                    ctx.stack.push(i)
                    f = func()
                    if not f:
                        continue
                    if f[-1]:
                        r.append(i)
                ctx.stack.push(r)
        elif desc == "single function sort by":
            a = next(ctx.stack.rmv(1))
            func = info
            if func != Void:
                x = listify(a)
                sort_by = []
                old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
                for i in x:
                    ctx.stack = Stack(copy.deepcopy(list(old_stack).copy()))
                    ctx.stack.push(i)
                    f = func()
                    if not f:
                        sort_by.append((i, i))
                    else:
                        sort_by.append((i, f[-1]))
                try:
                    sorted_list = sorted(sort_by, key=lambda t: t[-1])
                    ctx.stack.push([p for p, q in sorted_list])
                except:
                    ctx.stack.push(x)
        elif desc == "single function group by":
            a = next(ctx.stack.rmv(1))
            func = info
            if func != Void:
                x = listify(a)
                group_by = []
                old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
                for i in x:
                    ctx.stack = Stack(copy.deepcopy(list(old_stack).copy()))
                    ctx.stack.push(i)
                    f = func()
                    if not f:
                        group_by.append((i, i))
                    else:
                        group_by.append((i, f[-1]))
                try:
                    d = []
                    for val, key in group_by:
                        for k, (i, j) in enumerate(d):
                            if key == i:
                                d[k][1].append(val)
                                break
                        else:
                            d.append((key, [val]))
                    ctx.stack.push([q for p, q in d])
                except:
                    ctx.stack.push(x)
        elif desc == "context variable":
            ctx.stack.push(n)
        elif desc == "iteration index":
            ctx.stack.push(iteration_index)
        elif desc == "get x":
            ctx.stack.push(vars_dict.get("x", 1))
        elif desc == "get y":
            ctx.stack.push(vars_dict.get("y", 2))
        elif desc == "set x":
            a = next(ctx.stack.rmv(1))
            vars_dict["x"] = a
        elif desc == "set y":
            a = next(ctx.stack.rmv(1))
            vars_dict["y"] = a
        elif desc == "set x without popping":
            a = (ctx.stack.copy() + ctx.other_il + [0])[0]
            vars_dict["x"] = a
        elif desc == "set y without popping":
            a = (ctx.stack.copy() + ctx.other_il + [0])[0]
            vars_dict["y"] = a
        elif desc == "apply to x":
            old_stack = copy.deepcopy(ctx.stack)
            ctx.stack.push(vars_dict.get("x", 1))
            for k in info():
                ctx.stack.push(k)
            vars_dict["x"] = next(ctx.stack.rmv(1))
            ctx.stack = copy.deepcopy(old_stack)
        elif desc == "apply to y":
            old_stack = copy.deepcopy(ctx.stack)
            ctx.stack.push(vars_dict.get("y", 2))
            for k in info():
                ctx.stack.push(k)
            vars_dict["y"] = next(ctx.stack.rmv(1))
            ctx.stack = copy.deepcopy(old_stack)
        elif desc == "get global array":
            ctx.stack.push(vars_dict.get("ga", []))
        elif desc == "add to global array":
            a = next(ctx.stack.rmv(1))
            ga = vars_dict.get("ga", [])
            if not isinstance(ga, list):
                vars_dict["ga"] = [ga, a]
            vars_dict["ga"] = ga + [a]
        elif desc == "stack":
            ctx.stack.push(list(ctx.stack).copy())
        elif desc == "constant":
            ctx.stack.push(info)
        elif desc == "callable constant":
            ctx.stack.push(info())
        elif desc == "codepage compression":
            ctx.stack.push(info)
        elif desc == "quit":
            raise TerminateProgramException()  # This will hopefully get caught and ignored
        elif desc == "next input":
            if ctx.other_il:
                ctx.stack.push(ctx.other_il[0])
                ctx.other_il = ctx.other_il[1:] + [ctx.other_il[0]]
        elif desc == "input list":
            ctx.stack.push(ctx.og_input_list)
        elif desc == "first input":
            try:
                ctx.stack.push(ctx.og_input_list[0])
            except:
                ctx.stack.push(ctx.og_input_list)
        elif desc == "second input":
            try:
                ctx.stack.push(ctx.og_input_list[1])
            except:
                ctx.stack.push(ctx.og_input_list)
        elif desc == "third input":
            try:
                ctx.stack.push(ctx.og_input_list[2])
            except:
                ctx.stack.push(ctx.og_input_list)
        elif desc == "third last input":
            try:
                ctx.stack.push(ctx.og_input_list[-3])
            except:
                ctx.stack.push(ctx.og_input_list)
        elif desc == "second last input":
            try:
                ctx.stack.push(ctx.og_input_list[-2])
            except:
                ctx.stack.push(ctx.og_input_list)
        elif desc == "last input":
            try:
                ctx.stack.push(ctx.og_input_list[-1])
            except:
                ctx.stack.push(ctx.og_input_list)
        elif desc == "print":
            print(next(ctx.stack.rmv(1)))
            ctx.implicit_print = False
        elif desc == "print without newline":
            print(next(ctx.stack.rmv(1)), end="")
            ctx.implicit_print = False
        elif desc == "print without popping":
            print((ctx.stack.copy() + ctx.other_il + [0])[0])
            ctx.implicit_print = False
        elif desc == "print each":
            for i in listify(next(ctx.stack.rmv(1))):
                print(i)
            ctx.implicit_print = False
        elif desc == "map":
            a = next(ctx.stack.rmv(1))
            x = listify(a)
            r = []
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            for i, j in enumerate(x):
                ctx.stack = Stack([j] + copy.deepcopy(old_stack))
                run(info, context=j, iteration_index=i)
                r.append(next(ctx.stack.rmv(1)))
            ctx.stack.push(r)
        elif desc == "filter":
            a = next(ctx.stack.rmv(1))
            x = listify(a)
            r = []
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            for i, j in enumerate(x):
                ctx.stack = Stack([j] + copy.deepcopy(old_stack))
                run(info, context=j, iteration_index=i)
                z = next(ctx.stack.rmv(1))
                if z:
                    r.append(j)
            ctx.stack.push(r)
        elif desc == "sort by":
            a = next(ctx.stack.rmv(1))
            x = listify(a)
            r = []
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            for i, j in enumerate(x):
                ctx.stack = Stack([j] + copy.deepcopy(old_stack))
                run(info, context=j, iteration_index=i)
                z = next(ctx.stack.rmv(1))
                r.append((j, z))
            try:
                sorted_list = sorted(r, key=lambda t: t[-1])
                ctx.stack.push([p for p, q in sorted_list])
            except:
                ctx.stack.push(x)
        elif desc == "group by":
            a = next(ctx.stack.rmv(1))
            x = listify(a)
            r = []
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            for i, j in enumerate(x):
                ctx.stack = Stack([j] + copy.deepcopy(old_stack))
                run(info, context=j, iteration_index=i)
                z = next(ctx.stack.rmv(1))
                r.append((j, z))
            try:
                d = []
                for val, key in r:
                    for k, (i, j) in enumerate(d):
                        if key == i:
                            d[k][1].append(val)
                            break
                    else:
                        d.append((key, [val]))
                ctx.stack.push([q for p, q in d])
            except:
                ctx.stack.push(x)
        elif desc == "fixed point":
            r = [Void]
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            i = 0
            while True:
                ctx.stack = Stack(copy.deepcopy(old_stack))
                run(info, context=r[-1], iteration_index=i)
                k = (ctx.stack + ctx.other_il + [0])[0]
                r.append(k)
                if r[-1] == r[-2]:
                    break
                i += 1
            ctx.stack.push(r[1:])
        elif desc == "first n integers":
            a = next(ctx.stack.rmv(1))
            try:
                x = int(a)
            except:
                x = 1
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            i = 1
            r = []
            while len(r) < x:
                ctx.stack = Stack(copy.deepcopy(old_stack))
                ctx.stack.push(i)
                run(info, context=i, iteration_index=i - 1)
                k = next(ctx.stack.rmv(1))
                if k:
                    r.append(i)
                i += 1
            ctx.stack.push(r)
        elif desc == "cumulative reduce by":
            a = next(ctx.stack.rmv(1))
            x = listify(a)
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            if x:
                r = [x.pop(0)]
                for i, j in enumerate(x):
                    ctx.stack = Stack(copy.deepcopy(old_stack))
                    ctx.stack.push(r[-1])
                    ctx.stack.push(j)
                    run(info, context=j, iteration_index=i)
                    r.append(next(ctx.stack.rmv(1)))
                ctx.stack.push(r)
            else:
                ctx.stack.push([])
        elif desc == "single function reduce by":
            a = next(ctx.stack.rmv(1))
            x = listify(a)
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            func = info
            if func != Void:
                if x:
                    r = [x.pop(0)]
                    for i, j in enumerate(x):
                        ctx.stack = Stack(copy.deepcopy(old_stack))
                        ctx.stack.push(r[-1])
                        ctx.stack.push(j)
                        for k in func():
                            r.append(k)
                    ctx.stack.push(r[-1])
                else:
                    ctx.stack.push([])
        elif desc == "single function right reduce by":
            a = next(ctx.stack.rmv(1))
            x = listify(a)[::-1]
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            func = info
            if func != Void:
                if x:
                    r = [x.pop(0)]
                    for i, j in enumerate(x):
                        ctx.stack = Stack(copy.deepcopy(old_stack))
                        ctx.stack.push(r[-1])
                        ctx.stack.push(j)
                        for k in func():
                            r.append(k)
                    ctx.stack.push(r[-1])
                else:
                    ctx.stack.push([])
        elif desc == "single function right cumulative reduce by":
            a = next(ctx.stack.rmv(1))
            x = listify(a)[::-1]
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            func = info
            if func != Void:
                if x:
                    r = [x.pop(0)]
                    for i, j in enumerate(x):
                        ctx.stack = Stack(copy.deepcopy(old_stack))
                        ctx.stack.push(r[-1])
                        ctx.stack.push(j)
                        for k in func():
                            r.append(k)
                    ctx.stack.push(r)
                else:
                    ctx.stack.push([])
        elif desc == "right reduce by":
            a = next(ctx.stack.rmv(1))
            x = listify(a)[::-1]
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            if x:
                r = [x.pop(0)]
                for i, j in enumerate(x):
                    ctx.stack = Stack(copy.deepcopy(old_stack))
                    ctx.stack.push(r[-1])
                    ctx.stack.push(j)
                    run(info, context=j, iteration_index=i)
                    r.append(next(ctx.stack.rmv(1)))
                ctx.stack.push(r[-1])
            else:
                ctx.stack.push([])
        elif desc == "for loop":
            a = next(ctx.stack.rmv(1))
            x = listify(a)
            for i, j in enumerate(x):
                if not isinstance(a, (int, float)):
                    ctx.stack.push(j)
                run(info, context=j, iteration_index=i)
        elif desc == "while loop":
            cond, body = info
            i = 0
            while True:
                old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
                run(cond, context=0, iteration_index=i)
                z = next(ctx.stack.rmv(1))
                ctx.stack = Stack(copy.deepcopy(old_stack))
                if not z:
                    break
                run(body, context=0, iteration_index=i)
                i += 1
        elif desc == "forever loop":
            i = 0
            while True:
                run(info, context=0, iteration_index=i)
                i += 1
        elif desc == "if statement":
            if_true, if_false = info
            a = next(ctx.stack.rmv(1))
            if a:
                run(if_true, context=0, iteration_index=1)
            else:
                run(if_false, context=0, iteration_index=0)
        elif desc == "execute without popping":
            if info != Void:
                values = info(pop=False)
                for value in values:
                    ctx.stack.push(value)
        elif desc == "pair apply":
            a = next(ctx.stack.rmv(1))
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            r = []
            f1, f2 = info
            ctx.stack.push(a)
            k = f1()
            if k:
                r.append(k[-1])
            ctx.stack = Stack(copy.deepcopy(old_stack))
            k = f2()
            if k:
                r.append(k[-1])
            ctx.stack = Stack(copy.deepcopy(old_stack))
            ctx.stack.push(r)
        elif desc == "recursive environment":
            a = next(ctx.stack.rmv(1))
            if isinstance(a, list):
                x = copy.deepcopy(a)
            else:
                x = [a]
            for i in x:
                print(i)
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            k = 0
            while True:
                ctx.stack = Stack(copy.deepcopy(list(old_stack).copy()))
                for j in x:
                    ctx.stack.push(j)
                run(info, context=([0] + x)[-1], iteration_index=k)
                y = next(ctx.stack.rmv(1))
                print(y)
                x.append(y)
                k += 1
        elif desc == "apply to every nth item":
            a = next(ctx.stack.rmv(1))
            try:
                a = int(a)
            except:
                try:
                    a = len(a)
                except:
                    a = 2
            b = listify(next(ctx.stack.rmv(1)))
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            r = []
            for i, j in enumerate(b):
                if i % a == 0:
                    ctx.stack = Stack(copy.deepcopy(list(old_stack).copy()))
                    ctx.stack.push(j)
                    for k in info():
                        r.append(k)
                else:
                    r.append(j)
            ctx.stack.push(r)
        elif desc == "rotate stack left":
            ctx.stack = Stack(rotate_left_once(ctx.stack))
        elif desc == "rotate stack right":
            ctx.stack = Stack(rotate_right_once(ctx.stack))
        elif desc == "reverse stack":
            ctx.stack = Stack(ctx.stack[::-1])
        elif desc == "adjacent group by":
            a = next(ctx.stack.rmv(1))
            x = listify(a)
            r = []
            old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
            for i, j in enumerate(x):
                ctx.stack = Stack([j] + copy.deepcopy(old_stack))
                run(info, context=j, iteration_index=i)
                z = next(ctx.stack.rmv(1))
                r.append((j, z))
            try:
                d = []
                last = None
                for val, key in r:
                    if key == last:
                        d[-1].append(val)
                    else:
                        d.append([val])
                    last = key
                ctx.stack.push(d)
            except:
                ctx.stack.push(x)
        elif desc == "single function adjacent group by":
            a = next(ctx.stack.rmv(1))
            func = info
            if func != Void:
                x = listify(a)
                group_by = []
                old_stack = Stack(copy.deepcopy(list(ctx.stack).copy()))
                for i in x:
                    ctx.stack = Stack(copy.deepcopy(list(old_stack).copy()))
                    ctx.stack.push(i)
                    f = func()
                    if not f:
                        group_by.append((i, i))
                    else:
                        group_by.append((i, f[-1]))
                try:
                    d = []
                    last = None
                    for val, key in group_by:
                        if key == last:
                            d[-1].append(val)
                        else:
                            d.append([val])
                        last = key
                    ctx.stack.push(d)
                except:
                    ctx.stack.push(x)
        else:
            if ctx.warnings:
                print("TRACEBACK: [UNRECOGNISED TOKEN]", file=sys.stderr)
                print(f"Got {chars!r} (tokenised to {desc!r})")
    return 0


def test(cod, inp=(), stk=(), warn=True):
    ctx.stack = Stack(stk)
    ctx.og_input_list = list(inp)
    ctx.other_il = list(inp)
    ctx.warnings = warn
    tokenised = tokenise(cod)[1]
    run(tokenised, context=0, iteration_index=0)
    print(ctx.stack)
    if ctx.implicit_print:
        print(ctx.stack[0])
