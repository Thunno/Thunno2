"""An unordered, chaotic mess of helper functions"""


import copy
import itertools
import math
import random
import re
import string

from thunno2 import codepage
from thunno2 import canvas


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


def convert_all_to_string(func):
    def wrapper(*args, fn=func):
        return fn(*map(str, args))

    return wrapper


def try_int_conversion(func):
    def wrapper(*args, fn=func):
        try:
            return fn(*map(int, args))
        except:
            return [*args]

    return wrapper


def try_float_conversion(func):
    def wrapper(*args, fn=func):
        try:
            return fn(*map(float, args))
        except:
            return [*args]

    return wrapper


def try_number_conversion(func):
    def wrapper(*args, fn=func):
        new_args = []
        try:
            for a in args:
                if isinstance(a, int):
                    new_args.append(a)
                elif isinstance(a, str):
                    try:
                        new_args.append(int(a))
                    except:
                        new_args.append(float(a))
                elif isinstance(a, float):
                    new_args.append(a)
                else:
                    raise
        except:
            return args
        return fn(*new_args)

    return wrapper


def safe_max_len(*lsts):
    m = 0
    for lst in lsts:
        if isinstance(lst, list):
            if len(lst) > m:
                m = len(lst)
    return m


def first_non_none(l):
    for i in l:
        if i is not None:
            return i


def isalpha(s):
    return int(s.isalpha())


def number_to_base_digits(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def ntb(b, n):
    if b == 0:
        return [n]
    if b == 1:
        return n * [0]
    return number_to_base_digits(n, b)


def number_to_base(base, num):
    num, base = int(num), int(base)
    if base <= 0:
        return str(num)
    if base == 1:
        return num * "0"
    return number_to_base_digits(num, base)


def ntbs(b, n):
    r = number_to_base_digits(n, b)
    if b <= 64:
        digits = string.digits + string.ascii_uppercase + string.ascii_lowercase + "+/"
    else:
        digits = codepage.CODEPAGE * math.ceil(b / 256)
    return "".join(map(digits.__getitem__, r))


def to_custom_base_string(base, num):
    num = int(num)
    if len(base) == 0:
        return str(num)
    if len(base) == 1:
        return num * base
    return "".join(map(base.__getitem__, number_to_base_digits(num, len(base))))


def length_to_base(base, s):
    base = int(base)
    if base <= 0:
        return str(len(s))
    if base == 1:
        return len(s) * "0"
    return number_to_base_digits(len(s), base)


def length_custom_base_string(str2, str1):
    num = len(str1)
    if len(str2) == 0:
        return str(num)
    if len(str2) == 1:
        return num * "0"
    return "".join(map(str2.__getitem__, number_to_base_digits(len(str1), len(str2))))


def pass_(*args):
    return args[::-1]


def from_list_of_digits_2(num, base):
    r = 0
    for x, y in enumerate(reversed(num)):
        r += int(base) ** x * int(y)
    return r


def decompress(s, char):
    ci = codepage.CODEPAGE.index(char)
    indices = [i - (i > ci) for i in codepage.codepage_index(*s)]
    return from_list_of_digits_2(indices, 255)


def chr2(num):
    return chr(int(num))


def ord2(s):
    return [ord(c) for c in s]


def digits(num):
    return [int(d) for d in str(num) if d in "0123456789"]


def is_even(num):
    return int(num % 2 == 0)


def eval2(s):
    try:
        return eval(s)
    except:
        return 0


def factors(num):
    num = int(num)
    return [i for i in range(1, num + 1) if num % i == 0]


def substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


def max2(num):
    return max(int(d) for d in str(num) if d in "0123456789")


def max3(x):
    try:
        return max(x)
    except:
        return x


def from_hex(x):
    try:
        return int(str(x), 16)
    except:
        return x


def codepage_chr(num):
    return codepage.CODEPAGE[int(num) % 256]


def codepage_ord(s):
    return [*codepage.codepage_index(*s)]


def indexing_0(num, lst):
    if not lst:
        return lst
    return lst[int(num) % len(lst)]


def swapped_ind0(lst, num):
    if not lst:
        return lst
    return lst[int(num) % len(lst)]


def interleave_lst(lst1, lst2):
    if len(lst1) == len(lst2):
        r = []
        for i, j in zip(lst2, lst1):
            r.append(i)
            r.append(j)
        return r
    elif len(lst1) > len(lst2):
        r = []
        for i, j in zip(lst2, lst1):
            r.append(i)
            r.append(j)
        r.extend(lst1[len(lst2) :])
        return r
    else:
        r = []
        for i, j in zip(lst2, lst1):
            r.append(i)
            r.append(j)
        r.extend(lst2[len(lst1) :])
        return r


def interleave_str(s1, s2):
    if len(s1) == len(s2):
        r = ""
        for i, j in zip(s2, s1):
            r += i + j
        return r
    elif len(s1) > len(s2):
        r = ""
        for i, j in zip(s2, s1):
            r += i + j
        r += s1[len(s2) :]
        return r
    else:
        r = ""
        for i, j in zip(s2, s1):
            r += i + j
        r += s2[len(s1) :]
        return r


def binary_range(num1, num2):
    if num1 < num2:
        return binary_range(num2, num1)[::-1]
    return list(range(num2, num1 + 1))


def empty_join(iterable):
    if not isinstance(iterable, list):
        return str(iterable)
    return "".join(map(empty_join, iterable))


def safe_len(x):
    try:
        return len(x)
    except:
        return 1


def lowered_range(num):
    if num < 0:
        return [-i for i in lowered_range(-num)]
    return list(range(int(num)))


def min2(num):
    return min(int(d) for d in str(num) if d in "0123456789")


def min3(x):
    try:
        return min(x)
    except:
        return x


def safe_int(x):
    try:
        return int(x)
    except:
        return str(x)


def two_power(n):
    return 2**n


def is_prime(n):
    i = int(n)
    return int(i >= 2 and all(i % k for k in range(2, i)))


def slice1(num, lst):
    return lst[:: int(num)]


def slice2(lst, num):
    return lst[:: int(num)]


def not_equal(x, y):
    return int(x != y)


def one_range(num):
    if num < 0:
        return [-i for i in one_range(-num)]
    return list(range(1, int(num) + 1))


def digit_sum(num):
    return sum(int(d) for d in str(num) if d in "0123456789")


def it_sum(lst):
    if not lst:
        return 0
    if all(isinstance(item, (int, float)) for item in lst):
        return sum(lst)
    if all(isinstance(item, list) for item in lst):
        return sum(lst[1:], lst[0])
    return "".join(map(str, lst))


def uniquify_lst(lst):
    r = []
    for i in lst:
        if i not in r:
            r.append(i)
    return r


def uniquify_str(s):
    r = ""
    for c in s:
        if c not in r:
            r += c
    return r


def uniquify_num(num):
    return eval(uniquify_str(str(num)))


def indices_where_truthy(l):
    return [i for i, x in enumerate(l) if x]


def indices_where_truthy_num(n):
    return [i for i, x in enumerate(str(n)) if x in "123456789"]


def rot_13(s):
    r = ""
    for c in s:
        if ord("A") <= ord(c.upper()) <= ord("M"):
            r += chr(ord(c) + 13)
        elif ord("N") <= ord(c.upper()) <= ord("Z"):
            r += chr(ord(c) - 13)
        else:
            r += c
    return r


def wrap(x):
    return [x]


def zip2(l1, l2):
    return list(map(list, zip(l2, l1)))


def range_zip1(n1, n2):
    n1 = int(n1)
    return zip2(one_range(n1), [n2] * abs(n1))


def range_zip2(n, l):
    return zip2(one_range(int(n)), l)


def range_zip3(l, n):
    return zip2(l, one_range(int(n)))


def append(x, l):
    return l + [x]


def safe_index(x, y, e=-1):
    if y in x:
        return x.index(y)
    return e


def convert_from_base(base, num):
    if base <= 0:
        return num
    elif base == 1:
        return len(str(num))
    if base <= 64:
        digits = string.digits + string.ascii_uppercase + string.ascii_lowercase + "+/"
    else:
        digits = codepage.CODEPAGE * math.ceil(base / 256)
    return from_list_of_digits_2(
        list(map((lambda c: safe_index(digits, c, 0)), str(num))), base
    )


def convert_from_custom_base(base, num):
    return from_list_of_digits_2(
        list(map((lambda c: safe_index(base, c, 0)), str(num))), len(base)
    )


def nCr(r, n):
    n, r = int(n), int(r)
    f = math.factorial
    return f(n) // f(r) // f(n - r)


def string_count(x, y):
    if isinstance(x, list):
        return [string_count(i, y) for i in x]
    return str(y).count(str(x))


def list_count(x, y):
    if isinstance(x, list):
        return [list_count(i, y) for i in x]
    return y.count(x)


def duplicate(x):
    return x, x


def ten_power(n):
    return 10**n


def comma_split(s):
    return s.split(",")


def prime_factors(n):
    n = int(n)
    for i in range(2, n + 1):
        if is_prime(i) and n % i == 0:
            return [i] + prime_factors(n // i)
    return []


def case(s):
    r = []
    for c in s:
        if c.islower():
            r.append(0)
        elif c.isupper():
            r.append(1)
        else:
            r.append(-1)
    return r


def gcd(l):
    l = [int(i) for i in l if isinstance(i, (int, float)) or str(i).isdigit()]
    if not l:
        return 0
    for x in reversed(range(1, max(l))):
        if all(y % x == 0 for y in l):
            return x


def digits_gcd(n):
    return gcd([int(i) for i in str(n) if i in "0123456789"])


def ords_gcd(s):
    return gcd(list(map(ord, s)))


def head_extract(x):
    if not x:
        return x
    return x[1:], x[0]


def num_head_extract(n):
    r = ()
    for i in head_extract(str(n)):
        try:
            r += (eval(i),)
        except:
            r += (i,)
    return r


def num_ind0(x, y):
    s = str(y)[int(x) % len(str(y))]
    try:
        return int(s)
    except:
        return s


def length_ind0(x, y):
    return indexing_0(len(str(x)), y)


def vectorised_ind0(x, y):
    r = []
    for i in x:
        try:
            r.append(indexing_0(i, y))
        except:
            r.append(length_ind0(i, y))
    return r


def increment(num):
    return num + 1


def decrement(num):
    return num - 1


def str_increment(s):
    return "".join(chr(ord(c) + 1) for c in s)


def str_decrement(s):
    return "".join(chr(ord(c) - 1) for c in s)


def join(joiner, iterable):
    return str(joiner).join(map(str, iterable))


def num_join(j, n):
    return join(j, str(n))


def num_length(n):
    return len(str(n))


def mean(lst):
    l = []
    for i in lst:
        try:
            l.append(float(i))
        except:
            pass
    if not l:
        return 0
    return sum(l) / len(l)


def num_mean(n):
    return mean([int(i) for i in str(n) if i in "0123456789"])


def ord_mean(s):
    return mean(map(ord, s))


def str_rmv(x, y):
    return str(y).replace(str(x), "")


def num_rmv(x, y):
    try:
        return eval(str_rmv(x, y))
    except:
        return str_rmv(x, y)


def list_rmv(x, y):
    z = y.copy()
    while x in z:
        z.remove(x)
    return z


def swapped_list_rmv(x, y):
    return list_rmv(y, x)


def digit_product(num):
    return math.prod([int(i) for i in str(num) if i in "0123456789"])


def product(lst):
    l = []
    for i in lst:
        if isinstance(i, (int, float)):
            l.append(i)
        else:
            try:
                l.append(int(i))
            except:
                try:
                    l.append(float(i))
                except:
                    pass
    if not l:
        return 1
    return math.prod(l)


def ord_product(s):
    return math.prod(list(map(ord, s)))


def swapped_append(x, y):
    return append(y, x)


def _digits(x):
    if isinstance(x, (str, list)):
        return list(x)
    return [int(i) for i in str(x) if i in "0123456789"]


def append2(x, y):
    return _digits(y) + [x]


def string_replace(x, y, z):
    return str(z).replace(str(y), str(x))


def list_replace(x, y, z):
    return [x if i == y else i for i in z]


def digit_reverse(num):
    r = str(num)[::-1]
    try:
        try:
            return int(r)
        except:
            return eval(r)
    except:
        return r


def reverse(x):
    return x[::-1]


def swap(a, b):
    return a, b


def tail_extract(x):
    if not x:
        return x
    return x[:-1], x[-1]


def num_tail_extract(n):
    r = ()
    for i in tail_extract(str(n)):
        try:
            r += (eval(i),)
        except:
            r += (i,)
    return r


def remove_whitespace(s):
    return "".join(s.split())


def uninterleave(l):
    return [l[0::2], l[1::2]]


def num_uninterleave(n):
    return uninterleave(_digits(n))


def uninterleave_dump(l):
    return l[0::2], l[1::2]


def num_uninterleave_dump(n):
    return uninterleave_dump(_digits(n))


def bool2(x):
    return int(bool(x))


def isalphanum(s):
    return int(s.isalnum())


def any2(l):
    return int(any(l))


def from_binary(x):
    try:
        return int(str(x), 2)
    except:
        return x


def add(x, y):
    return y + x


def string_add(x, y):
    return str(y) + str(x)


def subtract(x, y):
    return y - x


def slice_start(s, n):
    return s[n:]


def slice_end(n, s):
    return s[:-n]


def strip(a, b):
    return b.strip([a])


def multiply(x, y):
    if isinstance(x, (str, list)):
        return x * int(y)
    elif isinstance(y, (str, list)):
        return int(x) * y
    return y * x


def string_cartesian_product(a, b):
    return ["".join(l) for l in itertools.product(b, a)]


def divide(x, y):
    return y / x


def split2(a, b):
    if a < 1:
        return b
    if not b:
        return [b] * a
    x, y = divmod(len(b), int(a))
    k = 0
    r = []
    while k < len(b):
        r.append(b[k : k + x + (y > 0)])
        k += x + (y > 0)
        if y > 0:
            y -= 1
    return r


def split1(a, b):
    return split2(b, a)


def split3(a, b):
    return b.split(a)


def exponentiate(x, y):
    return y**x


def append_first1(a, b):
    if not a:
        return " " * b
    while len(a) < b:
        a += a[0]
    return a


def append_first2(a, b):
    return append_first1(b, a)


def regex_findall(a, b):
    return list(re.findall(a, b))


def modulo(x, y):
    return y % x


def str_format(a, b):
    return str(b).replace("%", str(a))


def swapped_format(a, b):
    return str_format(b, a)


def integer_divide(x, y):
    return int(y // x)


def first_split1(a, b):
    s = split1(a, b)
    if s:
        return s[0]
    return s


def first_split2(a, b):
    s = split2(a, b)
    if s:
        return s[0]
    return s


def first_split3(a, b):
    s = split3(a, b)
    if s:
        return s[0]
    return s


def slice_start2(n, s):
    return s[n:]


def slice_end2(s, n):
    return s[:-n]


def swapped_subtract(x, y):
    return x - y


def strip2(a, b):
    return a.strip(b)


def split4(a, b):
    return a.split(b)


def swapped_divide(x, y):
    return x / y


def swapped_integer_divide(x, y):
    return int(x // y)


def last_split1(a, b):
    s = split1(a, b)
    if s:
        return s[-1]
    return s


def last_split2(a, b):
    s = split2(a, b)
    if s:
        return s[-1]
    return s


def last_split3(a, b):
    s = split3(a, b)
    if s:
        return s[-1]
    return s


def str_format2(a, b):
    return str(a).replace("%", str(b))


def swapped_modulo(x, y):
    return x % y


def swapped_exponentiate(x, y):
    return x**y


def prepend_last1(a, b):
    if not a:
        return " " * b
    while len(a) < b:
        a = a[-1] + a
    return a


def prepend_last2(a, b):
    return append_first1(b, a)


def swapped_regex_findall(a, b):
    return list(re.findall(b, a))


def equals(x, y):
    return int(y == x)


def less_than(x, y):
    return int(y < x)


def ord_less_than1(n, s):
    return [int(ord(x) < n) for x in s]


def ord_less_than2(s, n):
    return [int(n < ord(x)) for x in s]


def greater_than(x, y):
    return int(y > x)


def ord_greater_than1(n, s):
    return [int(ord(x) > n) for x in s]


def ord_greater_than2(s, n):
    return [int(n > ord(x)) for x in s]


def less_than_or_equal_to(x, y):
    return int(y <= x)


def ord_less_than_or_equal_to1(n, s):
    return [int(ord(x) <= n) for x in s]


def ord_less_than_or_equal_to2(s, n):
    return [int(n <= ord(x)) for x in s]


def greater_than_or_equal_to(x, y):
    return int(y >= x)


def ord_greater_than_or_equal_to1(n, s):
    return [int(ord(x) >= n) for x in s]


def ord_greater_than_or_equal_to2(s, n):
    return [int(n >= ord(x)) for x in s]


def logical_and(x, y):
    return y and x


def logical_or(x, y):
    return y or x


def logical_xor(x, y):
    return int(bool(y) ^ bool(x))


def logical_not(x):
    return int(not x)


def pair(x, y):
    return [y, x]


def is_divisible(x, y):
    try:
        return int(y % x == 0)
    except:
        return 0


def length_divisible1(s, n):
    return is_divisible(len(s), n)


def length_divisible2(n, s):
    return length_divisible1(s, n)


def length_divisible3(a, b):
    return is_divisible(len(a), len(b))


def zero_enumerate(l):
    return list(map(list, enumerate(l)))


def inclusive_zero_range(n):
    if n >= 0:
        return list(range(int(n) + 1))
    return [-i for i in range(abs(int(n)) + 1)]


def recursive_flatten(x):
    if isinstance(x, list):
        r = []
        for i in x:
            a = recursive_flatten(i)
            if isinstance(a, list):
                r += a
            else:
                r += (a,)
        return r
    return x


def dyadic_gcd(a, b):
    try:
        return math.gcd(abs(int(a)), abs(int(b)))
    except:
        return 1


def ordinal_gcd1(a, b):
    return [dyadic_gcd(ord(c), b) for c in a]


def ordinal_gcd2(a, b):
    return ordinal_gcd1(b, a)


def longest_common_substring(x, y):
    a, b = substrings(x), substrings(y)
    try:
        return max([i for i in a if i in b], key=len)
    except:
        return ""


def num_head(x):
    return int(str(x)[0])


def head(x):
    if not x:
        return x
    return x[0]


def num_tail(x):
    return int(str(x)[-1])


def tail(x):
    if not x:
        return x
    return x[-1]


def num_ind1(x, y):
    s = str(y)[~-int(x) % len(str(y))]
    try:
        return int(s)
    except:
        return s


def indexing_1(num, lst):
    if not lst:
        return lst
    return lst[~-int(num) % len(lst)]


def swapped_ind1(lst, num):
    if not lst:
        return lst
    return lst[~-int(num) % len(lst)]


def length_ind1(x, y):
    return indexing_1(len(str(x)), y)


def vectorised_ind1(x, y):
    r = []
    for i in x:
        try:
            r.append(indexing_1(i, y))
        except:
            r.append(length_ind1(i, y))
    return r


def ljust1(x, n, y):
    return str(y).ljust(abs(int(n)) or 1, (str(x) + " ")[0])


def ljust2(n, x, y):
    return str(y).ljust(abs(int(n)) or 1, (str(x) + " ")[0])


def ljust3(x, y, z):
    return str(z).ljust(len(y) or 1, (str(x) + " ")[0])


def mode(it):
    if not it:
        return it
    return max(it, key=it.count)


def num_mode(n):
    return mode(digits(n))


def negate(x):
    return -x


def rle(s):
    l = ""
    r = []
    for c in s:
        if c == l:
            r[-1] += 1
        else:
            r.append(1)
        l = c
    return r


def index_of(x, y):
    if isinstance(y, str):
        x = str(x)
    if x in y:
        return y.index(x)
    return -1


def swapped_index_of(x, y):
    return index_of(y, x)


def num_index_of(x, y):
    return index_of(x, digits(y))


def vectorised_index_of(x, y):
    r = []
    for i in x:
        if isinstance(y, (str, list)):
            r.append(index_of(i, y))
        else:
            r.append(num_index_of(i, y))
    return r


def cartesian_product(x, y):
    return list(map(list, itertools.product(y, x)))


def range_product1(n, y):
    return cartesian_product(list(one_range(n)), y)


def range_product2(x, n):
    return range_product1(n, x)


def range_product3(x, y):
    return cartesian_product(list(one_range(x)), list(one_range(y)))


def first_char_not_present(s, avoid=()):
    i = 0
    while 1:
        if chr(i) in avoid:
            continue
        if chr(i) not in s:
            return chr(i)
        i += 1


def recursive_replace(x, y, z):
    while y in z:
        z = z.replace(y, x)
    return z


def string_repr(s):
    r = repr(s)
    if r[0] == '"':
        return r
    f = first_char_not_present(r, "\\'\"")
    return (
        '"'
        + recursive_replace(f, "\\\\", r[1:-1])
        .replace("\\'", "'")
        .replace('"', '\\"')
        .replace(f, "\\\\")
        + '"'
    )


def list_repr(l):
    x = []
    for i in l:
        if isinstance(i, list):
            x.append(list_repr(i))
        elif isinstance(i, str):
            x.append(string_repr(i))
        else:
            x.append(str(i))
    return "[" + ", ".join(x) + "]"


def sort(l):
    return list(sorted(l))


def digits_sort(n):
    return eval("".join(str_sort(map(str, digits(n)))))


def str_sort(s):
    return "".join(sort(s))


def chunk1(x, y):
    return split2(x, one_range(y))


def chunk2(x, y):
    return split2(len(x), y)


def zip_self(l):
    return zip2(l, l)


def num_zip_self(n):
    return zip_self(one_range(n))


def triplicate(x):
    return x, x, x


def assign(c, b, a):
    if not a:
        return a
    if isinstance(a, list):
        a[int(b) % len(a)] = c
        return a
    else:
        a = list(a)
        a[b % len(a)] = c
        return "".join(map(str, a))


def swapped_assign(c, a, b):
    return assign(c, b, a)


def length_assign(c, b, a):
    return assign(c, len(b), a)


def num_assign(c, b, a):
    return assign(c, b, digits(a))


def vectorised_assign(c, b, a):
    for i in b:
        if isinstance(i, (str, list)):
            a = length_assign(c, i, a)
        else:
            a = assign(c, i, a)
    return a


def to_binary(n):
    if n < 0:
        return "-" + to_binary(abs(n))
    return bin(int(n))[2:]


def ord_bin(s):
    return [to_binary(ord(c)) for c in s]


def combinations1(n, x):
    if n > len(x):
        n = len(x)
    if n < 1:
        n = 1
    return list(map(list, itertools.combinations(x, n)))


def combinations2(x, n):
    return combinations1(n, x)


def combinations3(x, y):
    return combinations1(x, one_range(y))


def set_union(x, y):
    r = []
    for i in y:
        if i not in r:
            r.append(i)
    for j in x:
        if j not in r:
            r.append(j)
    return r


def from_list_of_digits(b, n):
    return from_list_of_digits_2(n, int(b))


def divmod2(x, y):
    return list(divmod(y, x))


def length_range(x):
    return one_range(len(x))


def exclusive_one_range(n):
    return one_range(n)[:-1]


def prime_factor_exponents(n):
    p = prime_factors(n)
    r = []
    for i in range(n + 1):
        if is_prime(i):
            r.append(p.count(i))
    x = r[::-1]
    for k, j in enumerate(x):
        if j:
            return x[k:][::-1]
    return []


def group_consecutive(l):
    last = None
    r = []
    for i in l:
        if i != last:
            r.append([i])
        else:
            r[-1].append(i)
        last = i
    if isinstance(l, str):
        return [*map("".join, r)]
    return r


def consecutive_digits(n):
    return group_consecutive(digits(n))


def num_head_remove(x):
    return int(str(x)[1:])


def head_remove(x):
    if not x:
        return x
    return x[1:]


def lcm(l):
    l = [int(i) for i in l if isinstance(i, (int, float)) or str(i).isdigit()]
    if not l:
        return 0
    n = 1
    while 1:
        if all(n % j == 0 for j in l):
            return n
        n += 1


def digits_lcm(n):
    return lcm([int(i) for i in str(n) if i in "0123456789"])


def ords_lcm(s):
    return lcm(list(map(ord, s)))


def median(lst):
    l = []
    for i in lst:
        if isinstance(i, (int, float)):
            l.append(i)
        else:
            try:
                l.append(int(i))
            except:
                try:
                    l.append(float(i))
                except:
                    pass
    if not l:
        return []
    if len(l) % 2:
        return sorted(l)[len(l) // 2]
    s = sorted(l)[len(l) // 2 - 1 : len(l) // 2 + 1]
    return mean(s)


def num_median(n):
    return median(digits(n))


def ord_median(s):
    return median(list(map(ord, s)))


def round_decimal_places(a, b):
    return round(b, int(a))


def range_intersection1(a, b):
    return [i for i in b if i in one_range(a)]


def range_intersection2(a, b):
    return [i for i in one_range(b) if i in a]


def set_intersection(a, b):
    return [i for i in b if i in a]


def permutations1(n, x):
    if n > len(x):
        n = len(x)
    if n < 1:
        n = 1
    return list(map(list, itertools.permutations(x, n)))


def permutations2(x, n):
    return permutations1(n, x)


def permutations3(x, y):
    return permutations1(x, one_range(y))


def set_difference(x, y):
    r = []
    for i in y:
        if i not in r:
            if i not in x:
                r.append(i)
    return r


def rjust1(x, n, y):
    return str(y).rjust(abs(int(n)) or 1, (str(x) + " ")[0])


def rjust2(n, x, y):
    return str(y).rjust(abs(int(n)) or 1, (str(x) + " ")[0])


def rjust3(x, y, z):
    return str(z).rjust(len(y) or 1, (str(x) + " ")[0])


def prefixes(l):
    r = []
    for i in range(1, len(l) + 1):
        r.append(l[:i])
    return r


def cumsum(l):
    if any(not isinstance(i, (int, float)) for i in l):
        if not all(isinstance(j, list) for j in l):
            l = [*map(str, l)]
    if not l:
        return []
    r = []
    for i in range(1, len(l) + 1):
        r.append(it_sum(l[:i]))
    return r


def numcumsum(n):
    return cumsum(digits(n))


def num_tail_remove(x):
    return int(str(x)[:-1])


def tail_remove(x):
    if not x:
        return x
    return x[:-1]


def chunk3(n, l):
    x, y = len(l), abs(int(n))
    return list(filter(bool, [l[i : i + y] for i in range(0, (x // y + 1) * y, y)]))


def chunk4(l, n):
    return chunk3(n, l)


def chunk5(x, y):
    return chunk3(x, one_range(y))


def chunk6(x, y):
    return chunk3(len(x), y)


def length_range_no_pop(l):
    return (l, one_range(len(l)))


def num_length_range(n):
    return n, one_range(len(str(n)))


def length_range_0(l):
    return (l, lowered_range(len(l)))


def num_length_range_0(n):
    return n, lowered_range(len(str(n)))


def character_multiply1(s, n):
    return "".join(c * n for c in s)


def character_multiply2(n, s):
    return character_multiply1(s, n)


def regex_split(x, y):
    return re.split(x, y)


def double(x):
    return x * 2


def exactly_not_equal(x, y):
    return int(y != x)


def to_hex(n):
    if n < 0:
        return "-" + to_hex(abs(n))
    return hex(int(n))[2:]


def ord_hex(s):
    return [to_hex(ord(c)) for c in s]


def reciprocal(n):
    return 1 / n


def remove_non_alphabets(s):
    return "".join(c for c in s if c.isalpha())


def num_bifurcate(n):
    return n, digit_reverse(n)


def bifurcate(x):
    return x, reverse(x)


def fallback_lcm(a, b):
    x, y = abs(int(a)), abs(int(b))
    return (x * y) // dyadic_gcd(x, y)


def dyadic_lcm(a, b):
    try:
        return math.lcm(abs(int(a)), abs(int(b)))
    except:
        try:
            return fallback_lcm(a, b)
        except:
            return 1


def ordinal_lcm1(a, b):
    return [dyadic_lcm(ord(c), b) for c in a]


def ordinal_lcm2(a, b):
    return ordinal_lcm1(b, a)


def ordinal_lcm3(a, b):
    return [dyadic_lcm(ord(x), ord(y)) for x, y in zip(a, b)]


def num_mirror(n):
    r = str(n) + str(n)[::-1]
    try:
        return eval(r)
    except:
        return r


def mirror(x):
    return x + x[::-1]


def str_transliterate(a, b, c):
    r = ""
    d = dict(zip(map(str, b), map(str, a)))
    for x in str(c):
        r += str(d.get(x, x))
    return r


def list_transliterate(a, b, c):
    r = []
    d = dict(zip(b, a))
    for x in c:
        r.append(d.get(x, x))
    return r


def str_transliterate_overload_1(a, b, c):
    r = ""
    d = dict(zip(str(b), map(str, a)))
    for x in str(c):
        r += str(d.get(x, x))
    return r


def list_transliterate_overload_1(a, b, c):
    r = []
    d = dict(zip(str(b), a))
    for x in c:
        r.append(d.get(x, x))
    return r


def str_transliterate_overload_2(a, b, c):
    r = ""
    d = dict(zip(map(str, b), str(a)))
    for x in str(c):
        r += str(d.get(x, x))
    return r


def list_transliterate_overload_2(a, b, c):
    r = []
    d = dict(zip(b, str(a)))
    for x in c:
        r.append(d.get(x, x))
    return r


def str_transliterate_overload_3(a, b, c):
    r = ""
    d = dict(zip(str(b), str(a)))
    for x in str(c):
        r += str(d.get(x, x))
    return r


def list_transliterate_overload_3(a, b, c):
    r = []
    d = dict(zip(str(b), str(a)))
    for x in c:
        r.append(d.get(x, x))
    return r


def combinations_with_replacement1(n, x):
    if n > len(x):
        n = len(x)
    if n < 1:
        n = 1
    return list(map(list, itertools.combinations_with_replacement(x, n)))


def combinations_with_replacement2(x, n):
    return combinations_with_replacement1(n, x)


def combinations_with_replacement3(x, y):
    return combinations_with_replacement1(x, one_range(y))


def combinations_with_replacement4(x, y):
    return combinations_with_replacement1(len(x), y)


def square(n):
    return n**2


def chunk_wrap_2(s):
    return chunk3(2, s)


def cube(n):
    return n**3


def chunk_wrap_3(s):
    return chunk3(3, s)


def fourth(n):
    return n**4


def chunk_wrap_4(s):
    return chunk3(4, s)


def fifth(n):
    return n**5


def chunk_wrap_5(s):
    return chunk3(5, s)


def halve(n):
    if n % 2 == 0:
        return n // 2
    return n / 2


def chunk_halve(s):
    return split1(s, 2)


def deltas(lst):
    l = []
    for i in lst:
        if isinstance(i, (int, float)):
            l.append(i)
        else:
            try:
                l.append(int(i))
            except:
                try:
                    l.append(float(i))
                except:
                    pass
    if not l:
        return []
    r = []
    for x, y in zip(l, l[1:]):
        r.append(y - x)
    return r


def digit_deltas(n):
    return deltas(digits(n))


def ord_deltas(s):
    return deltas(list(map(ord, s)))


def digits_wrap(n):
    return [digits(n)]


def list_wrap(s):
    return [[*s]]


def transpose(lst):
    l = []
    for i in lst:
        if isinstance(i, (list, str)):
            l.append(list(i))
        elif isinstance(i, (int, float)):
            l.append(digits(i))
    return list(map(list, zip(*l)))


def rotate_left(n, l):
    if not l:
        return l
    rot = int(n) % len(l)
    return l[rot:] + l[:rot]


def rotate_right(n, l):
    if not l:
        return l
    rot = int(n) % len(l)
    return l[-rot:] + l[:-rot]


def swapped_rotate_left(l, n):
    return rotate_left(n, l)


def swapped_rotate_right(l, n):
    return rotate_right(n, l)


def len_rotate_left(x, y):
    return rotate_left(len(x), y)


def len_rotate_right(x, y):
    return rotate_right(len(x), y)


def num_rotate_left(n, x):
    r = rotate_left(n, str(x))
    try:
        return eval(r)
    except:
        return r


def num_rotate_right(n, x):
    r = rotate_right(n, str(x))
    try:
        return eval(r)
    except:
        return r


def rotate_left_once(l):
    return rotate_left(1, l)


def rotate_right_once(l):
    return rotate_right(1, l)


def num_rotate_left_once(l):
    return num_rotate_left(1, l)


def num_rotate_right_once(l):
    return num_rotate_right(1, l)


def left_bit_shift(x, y):
    if x < 0:
        return right_bit_shift(-x, y)
    return int(y) << int(x)


def right_bit_shift(x, y):
    if x < 0:
        return left_bit_shift(-x, y)
    return int(y) >> int(x)


def uninterleave2(n, l):
    if not n:
        return l
    return [l[i::n] if i < len(l) else l * 0 for i in range(abs(int(n)))]


def num_uninterleave2(x, y):
    return uninterleave2(x, digits(y))


def swapped_uninterleave(l, n):
    return uninterleave2(n, l)


def len_uninterleave(x, y):
    return uninterleave2(len(x), y)


def num_to_alphabet(n):
    return chr(64 + (int(n) % 26))


def alphabet_to_num(s):
    return [
        ord(c) - 64 if "A" <= c <= "Z" else (ord(c) - 96 if "a" <= c <= "z" else 0)
        for c in s
    ]


def nPr(r, n):
    n, r = int(n), int(r)
    f = math.factorial
    return f(n) // f(n - r)


def string_contains(x, y):
    if isinstance(x, list):
        return [string_contains(i, y) for i in x]
    return int(str(x) in str(y))


def list_contains(x, y):
    if isinstance(x, list):
        return [list_contains(i, y) for i in x]
    return int(x in y)


def list_remove_at_index(n, l):
    if not l:
        return l
    x = l.copy()
    x.pop(int(n) % len(x))
    return x


def str_remove_at_index(n, s):
    return "".join(list_remove_at_index(n, [*str(s)]))


def swapped_list_remove_at_index(l, n):
    return list_remove_at_index(n, l)


def swapped_str_remove_at_index(s, n):
    return str_remove_at_index(n, s)


def unique_prime_factors(n):
    return uniquify_lst(prime_factors(n))


def palindromise(l):
    return l + l[:-1][::-1]


def num_palindromise(n):
    s = palindromise(str(n))
    try:
        return eval(s)
    except:
        return s


def recurse_integer_partitions(n, m=1):
    for i in range(m, n // 2 + 1):
        for part in recurse_integer_partitions(n - i, i):
            yield part + [i]
    yield [n]


def integer_partitions(n):
    n = int(n)
    l = [*recurse_integer_partitions(abs(n))]
    if n < 0:
        return [[-i for i in sl] for sl in l]
    return l


def newline_join(iterable):
    if not isinstance(iterable, list):
        return str(iterable)
    return "\n".join(map(empty_join, iterable))


def space_join(iterable):
    if not isinstance(iterable, list):
        return str(iterable)
    return " ".join(map(empty_join, iterable))


def prepend(x, l):
    return [x] + l


def swapped_prepend(l, x):
    return prepend(x, l)


def prepend2(x, y):
    return [x] + _digits(y)


def transpose_with_filler(f, l):
    matrix = [[*x] if isinstance(x, (list, str)) else digits(x) for x in l]
    transposed = itertools.zip_longest(*matrix, fillvalue=f)
    return list(map(list, transposed))


def swapped_transpose_with_filler(l, f):
    return transpose_with_filler(f, l)


def digits_wrap_2(x, y):
    return y, digits_wrap(x)


def list_wrap_2(x, y):
    return y, list_wrap(x)


def pop_(*_):
    return ()


def boolify(x):
    return int(bool(x))


def counts(l):
    r = []
    for i in uniquify_lst(l):
        r.append([i, l.count(i)])
    return r


def num_counts(n):
    return counts(digits(n))


def parity(n):
    return n % 2


def second_half(s):
    return chunk_halve(s)[-1]


def num_prefixes(n):
    return prefixes(digits(n))


def increment_twice(n):
    return n + 2


def grade_up(l):
    return [*map(lambda x: x[0], sorted(enumerate(l[:]), key=lambda x: x[-1]))]


def head_slice(n, l):
    return l[:n]


def num_head_slice(x, y):
    s = head_slice(x, str(y))
    try:
        return eval(s)
    except:
        return s


def swapped_head_slice(l, n):
    return head_slice(n, l)


def len_head_slice(x, y):
    return head_slice(len(x), y)


def tail_slice(n, l):
    return l[-n:]


def num_tail_slice(x, y):
    s = tail_slice(x, str(y))
    try:
        return eval(s)
    except:
        return s


def swapped_tail_slice(l, n):
    return tail_slice(n, l)


def len_tail_slice(x, y):
    return tail_slice(len(x), y)


def powerset(l):
    r = [l * 0]
    p = [[]]
    for i in l:
        n = [x + [i] for x in p]
        p += [s[:] for s in n]
        for j in n:
            r.append(j if not isinstance(l, str) else "".join(j))
    return r


def num_powerset(n):
    return powerset(one_range(n))


def randint(n):
    if n == 0:
        return 0
    return random.choice(one_range(n))


def randchoice(l):
    if not l:
        return l
    return random.choice(l)


def square_root(i):
    n = abs(i)
    x = math.sqrt(n)
    try:
        y = math.isqrt(n)
        if x == y:
            return y
        return x
    except:
        return x


def every_second_item(s):
    return s[::2]


def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


def sentence_case(s):
    r = ""
    b = True
    for c in s:
        if b:
            r += c.upper()
        else:
            r += c.lower()
        if c in "?!.":
            b = True
        elif c == " " and b == True:
            pass
        else:
            b = False
    return r


def sum_each(l):
    r = []
    for i in l:
        if isinstance(i, (list, str)):
            r.append(it_sum(i))
        else:
            r.append(digit_sum(i))
    return r


def all_equal(l):
    return int(len(uniquify_lst(l)) <= 1)


def num_all_equal(n):
    return all_equal(str(n))


def symmetric_set_difference(x, y):
    r = uniquify_lst([i for i in y if i not in x] + [j for j in x if j not in y])
    if (type(x), type(y)) == (str, str):
        return "".join(r)
    return r


def range_ssd1(x, y):
    return symmetric_set_difference(digits(x), digits(y))


def range_ssd2(n, x):
    if isinstance(x, str):
        return symmetric_set_difference(str(n), x)
    return symmetric_set_difference(digits(n), x)


def range_ssd3(x, n):
    if isinstance(x, str):
        return symmetric_set_difference(x, str(n))
    return symmetric_set_difference(x, digits(n))


def equals_one(x):
    return int(x == 1)


def enclose(l):
    return l + l[:1]


def num_enclose(n):
    s = enclose(str(n))
    try:
        return eval(s)
    except:
        return s


def add_digits1(l, x):
    return _digits(x) + l


def add_digits2(x, l):
    return l + _digits(x)


def add_digits3(x, y):
    return _digits(y) + _digits(x)


def corresponding_filter(x, y):
    r = []
    for i, j in zip(y, x):
        if j:
            r.append(i)
    if isinstance(y, str):
        return "".join(r)
    return r


def corresponding_digit_filter_1(x, y):
    return corresponding_filter(digits(x), digits(y))


def corresponding_digit_filter_2(n, l):
    return corresponding_filter(digits(n), l)


def corresponding_digit_filter_3(l, n):
    return corresponding_filter(l, digits(n))


def list_sort_uniquify(l):
    return sort(uniquify_lst(l))


def str_sort_uniquify(s):
    return str_sort(uniquify_str(s))


def num_sort_uniquify(n):
    return list_sort_uniquify(digits(n))


def to_roman_numerals(num):
    ret = ""
    if num < 0:
        num = -num
        ret += "-"
    symbols = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    for s, n in symbols.items():
        while num >= n:
            ret += s
            num -= n
    return ret


def from_roman_numerals(s):
    ret = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == "M":
            ret += 1000
        elif c == "D":
            ret += 500
        elif c == "L":
            ret += 50
        elif c == "V":
            ret += 5
        elif c == "C":
            i += 1
            if s[i] == "M":
                ret += 900
            else:
                ret += 100
                i -= 1
        elif c == "X":
            i += 1
            if s[i] == "C":
                ret += 90
            else:
                ret += 10
                i -= 1
        elif c == "I":
            i += 1
            if s[i] == "X":
                ret += 9
            else:
                ret += 1
                i -= 1
        i += 1
    return ret


def length_of_each(l):
    r = []
    for i in l:
        if isinstance(i, (int, float)):
            r.append(len(str(i)))
        else:
            r.append(len(i))
    return r


def complement(n):
    return 1 - n


def is_vowel(s):
    return [int(c.lower() in "aeiou") for c in s]


def islower(s):
    if not s:
        return 1
    return int(s.islower())


def cmp(x, y):
    return sign(y - x)


def zfill1(n, s):
    if n < 0:
        return zfill1(abs(n), s[::-1])[::-1]
    return s.zfill(n)


def zfill2(s, n):
    return zfill1(n, s)


def surround(x, y):
    return x + y + x


def digits_repeat1(n, x):
    return _digits(x) * int(n)


def digits_repeat2(x, n):
    return digits_repeat1(n, x)


def length_repeat1(x, y):
    if isinstance(y, (int, float)):
        y = str(y)
    return x * len(y)


def length_repeat2(x, y):
    if isinstance(x, (int, float)):
        y = str(x)
    return _digits(y) * len(x)


def shuffle(l):
    return random.sample(l, len(l))


def str_shuffle(s):
    return "".join(shuffle(s))


def range_shuffle(n):
    return shuffle(one_range(n))


def spaces(n):
    return int(n) * " "


def suffixes(l):
    r = []
    for i in range(1, len(l) + 1):
        r.append(l[-i:])
    return r


def triple_swap(a, b, c):
    return a, c, b


def cartesian_power(n, l):
    return list(map(list, itertools.product(*[l] * abs(int(n)))))


def swapped_cartesian_power(l, n):
    return cartesian_power(n, l)


def range_cartesian_power(x, y):
    return cartesian_power(x, one_range(y))


def head_remove_2(n, l):
    return l[n:]


def num_head_remove_2(x, y):
    s = head_remove_2(x, str(y))
    try:
        return eval(s)
    except:
        return s


def swapped_head_remove_2(l, n):
    return head_remove_2(n, l)


def len_head_remove_2(x, y):
    return head_remove_2(len(x), y)


def tail_remove_2(n, l):
    return l[:-n]


def num_tail_remove_2(x, y):
    s = tail_remove_2(x, str(y))
    try:
        return eval(s)
    except:
        return s


def swapped_tail_remove_2(l, n):
    return tail_remove_2(n, l)


def len_tail_remove_2(x, y):
    return tail_remove_2(len(x), y)


def reverse_each(l):
    r = []
    for i in l:
        if isinstance(i, (str, list)):
            r.append(i[::-1])
        else:
            s = str(i)[::-1]
            try:
                r.append(eval(s))
            except:
                r.append(s)
    return r


def listify(x):
    if isinstance(x, (list, str)):
        return list(copy.deepcopy(x))
    return one_range(x)


def replace_with_nothing(x, y):
    return y.replace(x, "")


def replace_with_nothing2(x, y):
    return x.replace(y, "")


def factorial(n):
    if n < 1:
        return 1
    return math.factorial(int(n))


def all_slices(s):
    if not s:
        return [[]]
    r = []
    for i in one_range(len(s)):
        for x in all_slices(s[i:]):
            r.append([s[:i]] + x)
    return r


def dump(x):
    return tuple(x)


def num_dump(n):
    return dump(digits(n))


def centre_list(x):
    l = [*map(str, x)]
    if not l:
        return ""
    max_len = safe_max_len(l)
    return newline_join([*map(lambda s, m=max_len: s.center(m), l)])


@convert_all_to_string
def brackets_are_balanced(s):
    brackets = dict(chunk_wrap_2("()[]{}<>"))
    l = []
    for c in s:
        if c in brackets.keys():
            l.append(brackets[c])
        elif c in brackets.values():
            if not l:
                return 0
            if l[-1] == c:
                l = tail_remove(l)
            else:
                return 0
    return logical_not(len(l))


@try_int_conversion
def nth_fibonacci_number(n):
    if n <= 0:
        return 0
    a = 0
    b = 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b


@try_float_conversion
def cosine(n):
    return math.cos(n)


@try_float_conversion
def sine(n):
    return math.sin(n)


@try_float_conversion
def tangent(n):
    return math.tan(n)


@try_float_conversion
def arc_cosine(n):
    return math.acos(n)


@try_float_conversion
def arc_sine(n):
    return math.asin(n)


@try_float_conversion
def arc_tangent(n):
    return math.atan(n)


@try_float_conversion
def degrees(n):
    return math.degrees(n)


@try_float_conversion
def radians(n):
    return math.radians(n)


@try_float_conversion
def exponent(n):
    return math.exp(n)


@try_int_conversion
def nth_prime(n):
    if n < 0:
        n = abs(n)
    i = 2
    while n:
        i += 1
        if is_prime(i):
            n -= 1
    return i


def main_diagonal(lst):
    l = [*map(_digits, lst)]
    if not l:
        return []
    r = []
    for i in range(min(len(l), min(map(len, l)))):
        r.append(l[i][i])
    return r


def anti_diagonal(lst):
    l = [*map(_digits, lst)]
    if not l:
        return []
    r = []
    m = min(len(l), min(map(len, l)))
    for i in range(m):
        r.append(l[i][m - i - 1])
    return r


def dot_product(x, y):
    r = []
    for i, j in zip(x, y):
        try:
            r.append(i * j)
        except:
            pass
    return it_sum(r)


def all_diagonals(lst):
    l = [*map(_digits, lst)]
    if not l:
        return []
    r = [[] for _ in range(len(l) + min(map(len, l)) - 1)]
    for i, x in enumerate(l):
        for j in range(min(map(len, l))):
            r[(j - i) % len(r)].append(x[j])
    return r


def all_anti_diagonals(lst):
    l = [*map(_digits, lst)]
    if not l:
        return []
    r = [[] for _ in range(len(l) + min(map(len, l)) - 1)]
    for i, x in enumerate(l):
        for j in range(min(map(len, l))):
            r[((-i) - j + min(len(l), min(map(len, l))) - 1) % len(r)].append(x[j])
    return r


def longest(l):
    if not l:
        return []
    return max(l, key=lambda x: len(_digits(x)))


def shortest(l):
    if not l:
        return []
    return min(l, key=lambda x: len(_digits(x)))


def dyadic_maximum(x, y):
    return max(y, x)


def dyadic_minimum(x, y):
    return min(y, x)


def string_dyadic_maximum(x, y):
    return x if str(x) > str(y) else y


def string_dyadic_minimum(x, y):
    return x if str(x) < str(y) else y


@try_int_conversion
def bitwise_and(x, y):
    return y & x


@try_int_conversion
def bitwise_or(x, y):
    return y | x


@try_int_conversion
def bitwise_xor(x, y):
    return y ^ x


@try_int_conversion
def bitwise_not(x):
    return ~x


def depth(lst, curr=0):
    if isinstance(lst, list):
        if not lst:
            return curr + 1
        return max(depth(i, curr + 1) for i in lst)
    return curr


def type_of(x):
    if isinstance(x, int):
        return 0
    if isinstance(x, float):
        return 1
    if isinstance(x, str):
        return 2
    if isinstance(x, list):
        return 3
    return -1


@try_float_conversion
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def extend_truncate(x, y):
    x = abs(int(x))
    if x == 0:
        return y * 0
    if not y:
        return y
    i = 0
    l = len(y)
    while x > len(y):
        y += y[(i % l) : (i % l) + 1]
        i += 1
    while x < len(y):
        y = y[:-1]
    return y


def swapped_extend_truncate(y, x):
    return extend_truncate(x, y)


def length_extend_truncate(x, y):
    return extend_truncate(len(x), y)


def num_extend_truncate(x, y):
    r = extend_truncate(x, str(y))
    try:
        return eval(r)
    except:
        return r


@try_float_conversion
def insignificant(x):
    return int(abs(x) <= 1)


def left_trim(x, l):
    r = l * 0
    for i, j in enumerate(l):
        if j != x:
            r = l[i:]
            break
    return r


def right_trim(x, l):
    return left_trim(x, l[::-1])[::-1]


def trim(x, l):
    return right_trim(x, left_trim(x, l))


def swapped_left_trim(l, x):
    return left_trim(x, l)


def swapped_right_trim(l, x):
    return right_trim(x, l)


def swapped_trim(l, x):
    return trim(x, l)


def str_left_trim(x, y):
    return str(y).lstrip(str(x))


def str_right_trim(x, y):
    return str(y).rstrip(str(x))


def str_trim(x, y):
    return str(y).strip(str(x))


def vectorised_left_trim(x, l):
    r = l * 0
    for i, j in enumerate(l):
        if j not in x:
            r = l[i:]
            break
    return r


def vectorised_right_trim(x, l):
    return vectorised_left_trim(x, l[::-1])[::-1]


def vectorised_trim(x, l):
    return vectorised_right_trim(x, vectorised_left_trim(x, l))


def connected_uniquify(l):
    return [x[0] for x in group_consecutive(l)]


def str_connected_uniquify(s):
    return "".join(connected_uniquify(s))


def num_connected_uniquify(n):
    return eval(str_connected_uniquify(str(n)))


def str_starts_with(x, y):
    return int(str(y).startswith(str(x)))


def str_ends_with(x, y):
    return int(str(y).endswith(str(x)))


def canvas_draw(dirs, text):
    l = []
    for i in dirs:
        try:
            j = int(i)
            if 0 <= j <= 7:
                l.append(j)
        except:
            pass
    canvas.canvas.draw(text, length_extend_truncate(text, l or [2]))
    return str(canvas.canvas)


def digits_canvas_draw(n, s):
    return canvas_draw(digits(n), s)


def swapped_canvas_draw(text, dirs):
    return canvas_draw(dirs, text)


def swapped_digits_canvas_draw(s, n):
    return digits_canvas_draw(n, s)


def blank_canvas_draw(dirs, text):
    l = []
    for i in dirs:
        try:
            j = int(i)
            if 0 <= j <= 7:
                l.append(j)
        except:
            pass
    temp_canvas = canvas.Canvas()
    temp_canvas.draw(text, length_extend_truncate(text, l or [2]))
    return str(temp_canvas)


def blank_digits_canvas_draw(n, s):
    return blank_canvas_draw(digits(n), s)


def blank_swapped_canvas_draw(text, dirs):
    return blank_canvas_draw(dirs, text)


def blank_swapped_digits_canvas_draw(s, n):
    return blank_digits_canvas_draw(n, s)


def clear_canvas():
    canvas.canvas.clear()
    return ()


def multidimensional_index(x, l):
    for i, j in enumerate(l):
        if j == x:
            return [i]
        elif isinstance(j, list):
            r = multidimensional_index(x, j)
            if r:
                return [i] + r
    return []


def swapped_multidimensional_index(l, x):
    return multidimensional_index(x, l)


def vectorised_multidimensional_index(x, l):
    if not isinstance(x, list):
        return multidimensional_index(x, l)
    return [*map(lambda i, y=l: vectorised_multidimensional_index(i, y), x)]


def absolute_difference(a, b):
    return abs(b - a)


@try_float_conversion
def logarithm(a, b):
    return math.log(b, a)


@try_float_conversion
def log10(a):
    return math.log10(a)


@try_float_conversion
def ln(a):
    return math.log(a)


@try_float_conversion
def log2(a):
    return math.log2(a)


def split_on(x, l):
    if isinstance(l, str):
        x = str(x)
    r = [l * 0]
    for i in l:
        if i == x:
            r.append(l * 0)
        else:
            r[-1] += [i] if isinstance(l, list) else i
    return r


def num_split_on(x, y):
    return split_on(x, _digits(y))


def swapped_split_on(l, x):
    return split_on(x, l)


def perfect_nth(n, a):
    if isinstance(a, float):
        if not str(a).endswith(".0"):
            return 0
        a = int(a)
    n = int(n)
    if n <= 0:
        return 0
    if n == 1:
        return 1
    l = [i**n for i in inclusive_zero_range(abs(a))]
    return int(a in l)


@try_number_conversion
def perfect_square(a):
    return perfect_nth(2, a)


@try_number_conversion
def perfect_cube(a):
    return perfect_nth(3, a)


@try_number_conversion
def perfect_fourth(a):
    return perfect_nth(4, a)


@try_number_conversion
def perfect_fifth(a):
    return perfect_nth(5, a)
