---
title: Commands
slug: commands
---

# `"` (String literal)

Tokens: `string_literal`

Start a string literal. Anything between the two `"`s is evaluated as a Python string and pushed to the stack.

---

# `'` (One-character string literal)

Tokens: `one_character`

Push the next character as a string to the stack.

---

# <code>`</code> (Two-character string literal)

Tokens: `two_characters`

Push the next two characters as a string to the stack.

---

# `ʋ` (Three-character string literal)

Tokens: `three_characters`

Push the next three characters as a string to the stack.

---

# `“` (Lowercase string compression)

Tokens: `lowercase_string_compression`

Decompress the characters between the two `“`s as lowercase characters. Use [this program](https://ato.pxeger.com/run?1=PZLbUxNJGMWrfMxf0V4nkwygKF7Q0WWVZW_e7yLGhEzC7CaT7GQi4K5WBhEUvEKVgNcASSgFEZBL9wxiVc9kKuFh3923r_-SnRD1qau_Pud3TnX3i0KyW-tIKNn_Nv179OSx5lNNLc0IiYjjODpOJ-gkzdE8LdC3dIbO0iX6iX5mPTNWn9VvPbGeWiPWaHHIem29sQrWlDVnz5dWrHlrxcLFYWsNbd6yddv2HZyX9_mFmtq6nbvqd-9p2Ltv_4HGg4fEw0d-aPrx6LHmn1p-_uXX334_fuLkqdNnzp47f-HipctXWq-2XQtcD4baw1Ik2iH_8WcsriSSf6kpLX2js6v75t__3LpNl92Snu-l_dXSc5TQBfqR6YtMX2L6MtNXmI6ZTphuMN1k-irTPzF9zdGdfmfAeeoMO6NsftZ55eScGWehlCsPO_fKI85QOVsuOGPl-fKCk1_PllfXe5z364OlPBhZwL2AH4CBAefAHAC8AHgZSA-QPjAfAHkOZALIDJg5IGtg3ANzEYyhUgFwj-2qB-xngF_bLmbCnrM_A8kA6S3NAnkGZBRIFsg7MPrAGADjUdEEYxzwXcAPwSCA82AOAv4IeAXIHSD9YD4E8gLIJJD3dMrqBeM-mEtgDJemAN-xXe2gPQL4je1CJotukA7kbukDkBEgY0DGgUyD0Q_GIBiPi6t0mposM8oyYyzzqnK7cjyZUDWU0lRZiXpCIoc4f3VTG0y1y3IgluiU1PZgSvK4L4UiXkUI8Y0epIo7PSiSUFGX0I1kBUlKOi6pQU3yKq2NjTW72ioipPrFkM_X5ZMVzdvNuy5JS6sKUjdY0W-ssNja5kGdHXJMQkrFFvaLFYeCtqMQL7gDpa5ODH23h6sJ-bQWqdn_5XJSrYg5lnnJCb54MOn99mNqA4GopMmaFA8EhKg34m3dOA7VykpY6hJkJZnWvDzfJtTv44X6hgaeF6qUlJQUOY6vBmS_LtMdUiyWQJ0JNRaujv4H) to compress a lowercase string.

---

# `”` (Title case string compression)

Tokens: `title_case_string_compression`

Decompress the characters between the two `”`s as title case characters. Use [this program](https://ato.pxeger.com/run?1=PZLbUxNJGMWrfMxf0V4nkwygKF7Q0WWVZW_e7yLGhEzC7CaT7GQi4K5WBhEUvEKVgNcASSgFEZBL9wxiVc9kKuFh3923r_-SnRD1qau_Pud3TnX3i0KyW-tIKNn_Nv179OSx5lNNLc0IiYjjODpOJ-gkzdE8LdC3dIbO0iX6iX5mPTNWn9VvPbGeWiPWaHHIem29sQrWlDVnz5dWrHlrxcLFYWsNbd6yddv2HZyX9_mFmtq6nbvqd-9p2Ltv_4HGg4fEw0d-aPrx6LHmn1p-_uXX334_fuLkqdNnzp47f-HipctXWq-2XQtcD4baw1Ik2iH_8WcsriSSf6kpLX2js6v75t__3LpNl92Snu-l_dXSc5TQBfqR6YtMX2L6MtNXmI6ZTphuMN1k-irTPzF9zdGdfmfAeeoMO6NsftZ55eScGWehlCsPO_fKI85QOVsuOGPl-fKCk1_PllfXe5z364OlPBhZwL2AH4CBAefAHAC8AHgZSA-QPjAfAHkOZALIDJg5IGtg3ANzEYyhUgFwj-2qB-xngF_bLmbCnrM_A8kA6S3NAnkGZBRIFsg7MPrAGADjUdEEYxzwXcAPwSCA82AOAv4IeAXIHSD9YD4E8gLIJJD3dMrqBeM-mEtgDJemAN-xXe2gPQL4je1CJotukA7kbukDkBEgY0DGgUyD0Q_GIBiPi6t0mposM8oyYyzzqnK7cjyZUDWU0lRZiXpCIoc4f3VTG0y1y3IgluiU1PZgSvK4L4UiXkUI8Y0epIo7PSiSUFGX0I1kBUlKOi6pQU3yKq2NjTW72ioipPrFkM_X5ZMVzdvNuy5JS6sKUjdY0W-ssNja5kGdHXJMQkrFFvaLFYeCtqMQL7gDpa5ODH23h6sJ-bQWqdn_5XJSrYg5lnnJCb54MOn99mNqA4GopMmaFA8EhKg34m3dOA7VykpY6hJkJZnWvDzfJtTv44X6hgaeF6qUlJQUOY6vBmS_LtMdUiyWQJ0JNRaujv4H) to compress a lowercase string.

---

# `‘` (Lowercase dictionary string compression)

Tokens: `lowercase_dictionary_compression`

Decompress the characters between the two `‘`s as lowercase characters using the dictionary. Only words in the dictionary can be compressed. Characters which are alphanumeric or in `.,!?:\"'% ()` are not decompressed.

---

# `’` (Title case dictionary string compression)

Tokens: `title_case_dictionary_compression`

Decompress the characters between the two `’`s as title case characters using the dictionary. Only words in the dictionary can be compressed. Characters which are alphanumeric or in `.,!?:\"'% ()` are not decompressed.

---

# `»` (Integer compression)

Tokens: `integer_compression`

Decompress the characters between the two `»`s as an integer. Use [this program](https://ato.pxeger.com/run?1=PVJrUxJhFJ7pI79iu9iC4rUso6jMW3ftbpmRBCKlK-mS2W1YvGCglTIjmKmogJOiCV54310vM-8uO-A_qG_n_SWtWX05Z84zz3nOM-ecybirl2_r5CK_DjVW1VfXNFTW1TCMmWFZlsySOTJPoiRG4uQ7SZAVskG2yS71JuRB2Sd_kUflkBzOjMnT8owclxfkVSWZTctJOS2jTFDeYQ4fOXos7zirN-QXGAuLiktKy06cLD91uuKM6ew58_kLFysvVVXX1NZdvnL12vUbN-sbbt2-c_fe_QeNDx81PW5-YnnaYn1ms7c62pzPX7R3cJ2ul13dvPtVz-veN2_fvf9ANjWTuv-mCw5MrxJMUmSNCutU2KDCJhXSVEBUwFQQqSBRYYsK21TYUQXVp_rVUTWohmlyRZ1So2pCTWWjuaA6lAupY7lILq5O5JK5lBrbi-S29rzq8l4gGwMxAqgf0DCICFAUJD-gFKBNwF7AgyANA_4KeA5wAqQo4B0Qh0BaB3EsGwfkVTS2XxkHNK1oMnPKqrIL2AO4P7sCeBxwGHAE8CKIgyD6QfyUkUCcBTQAaAREDCgGUgDQGqA04D7APpBGAE8Cnge8TBbkfhA_grQBYjC7AKhP0bgBJQRoRtFE5jPaIAHwQPYH4BDgCcCzgJdA9IEYAPFzZossUU-Yeiao5xv1TO2vV9s_49BzRqvBpGNs5qZmHdPT5my3M5xWM7YCs5Pj9RyTx1gNRg3giovNVh3TZefdXRxjazKZCkubY26-tbDiZ62ra5_MEok15ne0uPT_TldksTjsvJO3d1gsRod-n-TkXG5ebzAYy8rLtfinp9vuMrOs4UAt8jct_v-pkgPkNw) to compress an integer.

---

# `«` (Small integer compression)

Tokens: `small_integer_compression`

Decompress the next two characters after `«` as an integer. Use [this program](https://ato.pxeger.com/run?1=PZJpU9NQFIZn_NhfERdMYgtIFcVKVQTEFXBHESuVAMWS1jYVUXQadllUYIZFBAq0ZZSC7NybsMzcpJmWf6Dfzv0lBhn8dOaceeY977znjMf9zVK9T4z8OVJRWFZUXF5QUswwToZlWTJNZsgsiZIYiZMfJEEWyTrZJru0NaF1al3aV21AG9FGk4PapDalxbU5bUlfTm1qy9qmhpJD2g5z9NjxExknWY4_ZbVlZmWfzrGfOZt77nzeBcfFfOely1cKrhYWFV8ruX7j5q3bd0rLyu_eu__g4aPHFU-eVj6reu56Ue1-WSPU1tV7Gl55G0Wf_3UgKIXeNL1tfve-5cNHsmGatPw3bT0wvUQwWSGrVF6j8jqVN6i8SWVEZUxlhcoqlbeovE3lHUM2uoweY8AYMkbp8qIxYUSNhLGSiqaHjO70iDGYjqTjxlh6Ob1ixPYi6a29VmNhrzcVAyUCqB1QHygIUBTUHkArgDYAtwLuBLUP8DfAM4AToEYB74DSDeoaKIOpOKBW3aR79GFAk7opM6Mv6buAw4DbU4uAhwGPAo4A_glKJyg9oHxOqqBMA-oA1A8KBhQDtRfQKqBNwG2Au0DtBzwOeBbwApnT2kH5BOo6KEOpOUBtusn26iOApnRTZDZpLpIBd6R-AR4BPAZ4GvA8KF2g9ILyJblFVBoepeExGv5OwxP78Zr5M3WcaHPzDgtT46yssjBN9R6vwIhmz9RYnR5R4kQmg3HzNnMgZmc73RYmIEihgMjUVDocmTlVsZBUm5n3uyXoZNmsBp9H5Bqr_dzh4bJcrjpB8khCo8tlq-P29TyiPyRxPG-z5-byPG_x1DJeQeSCfL7T7vAH9hGWzLPWYFagIRSUOLvNfFbWBAVvUDgESn0S4_cFgx63V2D5Aw-Rw_LvCw-avw) to compress a small integer.

---

# `¿` (Integer list compression)

Tokens: `integer_list_compression`

Decompress the characters between the two `¿`s as an integer list. Use [this program](https://ato.pxeger.com/run?1=RZJpU9NQFIZn_NhfEdc0bdipCxoVAXcF9wWxUptCVUItqYDbNKwKrjBDiwgWaMsoi4BQ7k0QZ27STMs_0G_n_hJTEPx0Zs553-e8c88dSQba5cZmKfZnR6qiurKqpvxUFcMIDMuyZJxMkEkSJwmSJF_JDJkjy-Qn7ZjRe_Re_YP-UY_o0fSAPqZ_0ZP6lD5vLGRW9AV9RUfpQX2N2blr9569-1g753DyefkFhUXFJaWu_QcOHio7fEQ4eux4-YmKyqqTp06fOXvu_IWL1TWXLl-5eu36jZu3btfeqbvrvlfvue8VfQ2N_gcPHzVJzYHHwRY59KS1rf3ps-cvXpKUFdG2Hdm5GXmeYLJIflBliSrLVElRZYUqiCqYKipVNKqsUuUnVdZMxew1-8yP5qAZpQtz5qgZN2fMxUw8O2i-ykbMgWwsmzSHswvZRTOxHsuurneYs-v9mQSoMUBdgN6AigDFQesDtAgoBbgDcA9obwB_AjwBeAa0OOA1UF-BtgTqQCYJqMOw1H3GEKAxw8JMGPPGL8BhwF2ZOcBDgKOAY4C_gdoDah-o79IaqOOAugG9BRUDSoDWD-gHoBXAnYB7QXsLeATwJOBZMqV3gfoatGVQBzNTgDoNS9tvRAB9MSzIZNpapADuznwHHAE8DHgc8DSovaD2g_o-vUqmiUbDURoepuHPNDyae2CPwP4_XF4-z9qsmzA-u8R7uDIbExQKbYyvOci08e2MX2JEKdQkButl0S7VlpXlFdXlREzQKXgcjjaHX5Lt7ZzlEuVQUGKCG6yGLZZXqK2zMa2N_kciI-VsXqeQc0jMXsbD8VZDKigQPNt27-aGREj25R38fSMQzIlZ8ovlHU31AfvW18h3uxtE2S-LTW4332D32Ws3xp58v-QV23i_FAjJdo6r44tcHF_scnEcvwFpEQMCy3Kb-Ni_Ml3IF_HFfAlfyrs2W38B) to compress an integer list. These characters can be compressed: `0123456789-.,`.

---

# `[` (Open list literal)

Tokens: `open_list_literal`, `open_list`, `list`

Start a list literal. Anything between `[` and `]` is evaluated as a Python list and pushed to the stack.

---

# `]` (Close list literal)

Tokens: `close_list_literal`, `close_list`, `end_list`

End a list literal. Anything between `[` and `]` is evaluated as a Python list and pushed to the stack.

---

# `#` (Single character comment)

Tokens: `comment`

Comment out the next character.

---

# `#⎵` (Single line comment)

Comment out anything up to the next newline or `¶` character. (Note: `⎵` is a space)

---

# `#{` (Block comment)

Comment out anything up to the next `}#`.

---

# <code>&nbsp;</code> (NOP)

Tokens: `nop`

Ignored by the interpreter.

---

# `¡` (Get variable)

Tokens: `get_variable`

Get the variable corresponding to the next character. Example usage: `¡Q` gets the value of the variable `Q`.

---

# `!` (Set variable)

Tokens: `set_variable`

Store `a` in the variable corresponding to the next character. Example usage: `!Q` sets the variable `Q` to the value of `a`.

---

# `ı` (Map)

Tokens: `map`

Usage: `ı CODE ;`. Map `CODE` over the elements of `a`.

---

# `€` (Single function map)

Tokens: `single_function_map`

Map the next command over the elements of `a`.

---

# `æ` (Filter)

Tokens: `filter`

Usage: `æ CODE ;`. Filter the elements of `a` by `CODE`.

---

# `œ` (Single function filter)

Tokens: `single_function_filter`

Filter `a` by the next command.

---

# `Þ` (Sort by)

Tokens: `sort_by`

Usage: `Þ CODE ;`. Sort `a` by the result of `CODE`.

---

# `þ` (Single function sort by)

Tokens: `single_function_sort_by`

Sort `a` by the next command.

---

# `Ñ` (Group by)

Tokens: `group_by`

Usage: `Ñ CODE ;`. Group `a` by the result of `CODE`

---

# `ñ` (Single function group by)

Tokens: `single_function_group_by`

Group `a` by the next command

---

# `ȷ` (Outer product)

Tokens: `outer_product`

Vectorise the next command over both `a` and `b`.

---

# `¥` (Fixed point)

Tokens: `fixed_point`

Usage: `¥ CODE ;`. Apply `CODE` until the results reach a fixed point

---

# `{` (Open FOR loop)

Tokens: `open_for_loop`

Usage: `{ CODE }`. Apply `CODE` to each element of `a`

---

# `}` (Close FOR loop)

Tokens: `close_for_loop`

Close a `FOR` loop.

---

# `(` (Open WHILE loop)

Tokens: `open_while_loop`

Usage: `( CONDITION ; BODY )`. While `CONDITION` is true, run `BODY`

---

# `)` (Close WHILE loop)

Tokens: `close_while_loop`

Close a `WHILE` loop.

---

# `⁽` (Open FOREVER loop)

Tokens: `open_forever_loop`

Usage: `⁽ CODE ⁾`. Execute `CODE` forever

---

# `⁾` (Close FOREVER loop)

Tokens: `close_forever_loop`

Close a `FOREVER` loop.

---

# `?` (IF statement)

Tokens: `if_statement`

Usage: `CONDITION ? IF_TRUE : IF_FALSE ;`. If `CONDITION` is true, execute `IF_TRUE`. Otherwise, execute `IF_FALSE`

---

# `:` (ELSE statement)

Tokens: `else_statement`

Used in conjunction with `IF` statements.

---

# `;` (Close statement)

Tokens: `close_statement`

Used to close statements like mapping loops or `IF` statements.

---

# `Ç` (Two function map)

Tokens: `two_function_map`

Map the next two commands over the elements of `a`.

---

# `ç` (Pair apply)

Tokens: `pair_apply`

Apply the next two commands to `a` and push both results in a list.

---

# `Ð` (Triplicate)

Tokens: `triplicate`

`any a`: push `a`, `a`, `a`

---

# `A` (Absolute value / Is alpha)

Tokens: `abs`,`absolute`,`isalpha`,`is_alpha`

- `num a`: push `abs(a)`
- `str a`: push `a.isalpha()`

---

# `B` (Convert to base)

Tokens: `to_base`,`from_decimal`

- `num a`, `num b`: convert `b` to base `a`
- `str a`, `num b`: convert `b` to custom base string `a`
- `num a`, `str b`: convert `len(b)` to base `a`
- `str a`, `str b`: convert `len(b)` to custom base string `a`

---

# `C` (Chr / Ord)

Tokens: `chr`,`character`,`ord`,`ordinal`

- `num a`: push `chr(a)`
- `str a`: push `ord(a)`

---

# `D` (Duplicate)

Tokens: `dup`,`duplicate`

- `any a`: push `a`, `a`

---

# `E` (Is even / Eval)

Tokens: `even`,`is_even`,`eval`

- `num a`: push `a % 2 == 0`
- `str a`: push `eval(a)`

---

# `F` (Factors / Substrings)

Tokens: `factors`,`substrings`

- `num a`: factors of `a`
- `str a`: substrings of `a`

---

# `G` (Maximum)

Tokens: `max`,`maximum`,`greatest`

- `num a`: maximum digit of `a`
- `str a`: character with maximum ordinal in `a`
- `lst a`: maximum value in `a`

---

# `H` (Convert from hexadecimal)

Tokens: `from_hex`,`from_hexadecimal`

- `any a`: push `int(a, 16)`

---

# `I` (Inclusive range / Slicing / Interleave)

Tokens: `inclusive_range`,`slice`,`interleave`

- `num a`, `num b`: push `[a, a+1, ..., b]`
- `str/lst a`, `num b`: push `a[::b]`
- `num a`, `str/lst b`: push `b[::a]`
- `str/lst a`, `str/lst b`: interleave `a` and `b`

---

# `J` (Join)

Tokens: `empty_join`,`str`

- `any a`: push `''.join(a)`

---

# `K` (Push the stack)

Tokens: `stack`

Push the stack without popping any items

---

# `L` (Lowered range / Lowercase)

Tokens: `lowered_range`,`zero_range`,`lower`,`lowercase`

- `num a`: push `[0, 1, ..., a-1]`
- `str a`: push `a.lower()`

---

# `M` (Minimum)

Tokens: `min`,`minimum`

- `num a`: minimum digit of `a`
- `str a`: character with minimum ordinal in `a`
- `lst a`: minimum value in `a`

---

# `N` (Cast to integer)

Tokens: `int`,`integer`

- `any a`: push `int(a)`

---

# `O` (Two power / Split by spaces)

Tokens: `two_power`,`space_split`

- `num a`: push `2 ** a`
- `str a`: push `a.split(' ')`

---

# `P` (Prime check / Swap case)

Tokens: `prime`,`is_prime`,`swapcase`

- `num a`: is `a` prime?
- `str a`: push `a.swapcase()`

---

# `Q` (Not equal to)

Tokens: `not_equal`,`inequality`

- `any a, any b`: push `b != a`

---

# `R` (One-based range / Uppercase)

Tokens: `one_range`,`range`,`upper`,`uppercase`

- `num a`: push `[1, 2, ..., a]`
- `str a`: push `a.upper()`

---

# `S` (Sum)

Tokens: `sum`

- `num a`: digit sum of `a`
- `str/lst a`: push `sum(a)`

---

# `T` (Ten)

Tokens: `ten`

Push `10` to the stack.

---

# `U` (Uniquify)

Tokens: `uniquify`

- `num a`: unique digits of `a`
- `str a`: unique characters of `a`
- `lst a`: unique elements of `a`

---

# `V` (Truthy indices / Round / ROT-13)

Tokens: `where_truthy`,`rot13`

- `num a`: round `a`
- `str a`: encode `a` using ROT-13
- `lst a`: indices where the element is truthy

---

# `W` (Wrap)

Tokens: `wrap`

- `any a`: push `[a]`

---

# `X` (Store in x)

Tokens: `set_x`

- `any a`: store `a` in variable `x`

---

# `Y` (Store in y)

Tokens: `set_y`

- `any a`: store `a` in variable `y`

---

# `Z` (Zip)

Tokens: `zip`

- `num a`, `num b`: push `[[b, 1], [b, 2], ..., [b, a]]`
- `num a`, `str/lst b`: zip `b` with `[1, 2, ..., a]`
- `str/lst a`, `num b`: zip `[1, 2, ..., b]` with `a`
- `str/lst a`, `str/lst b`: zip `b` with `a`

---

# `a` (Append)

Tokens: `append`

- `any a`, `any b`: append `a` to `b`

---

# `b` (From base)

Tokens: `from_base`,`to_decimal`

- `num a`, `num/str b`: convert `b` from base `a`
- `str a`, `num/str b`: convert `b` from custom base string `a`

---

# `c` (Count / nCr)

Tokens: `ncr`,`count`

- `num a`, `num b`: push `nCr(b, a)`
- `any a`, `str/lst b`: push `b.count(a)`

---

# `d` (Digits / Characters)

Tokens: `digits`,`characters`,`chars`

- `num a`: digits of `a`
- `str a`: characters of `a`

---

# `e` (Ten power / Comma split)

Tokens: `ten_power`,`comma_split`

- `num a`: push `10 ** a`
- `str a`: push `a.split(',')`

---

# `f` (Prime factors / Case)

Tokens: `prime_factors`,`case`

- `num a`: prime factors of `a`
- `str a`: case of each character of `a` (`1` = uppercase, `0` = lowercase, `-1` = non-alphabetic)

---

# `g` (GCD)

Tokens: `gcd`,`greatest_common_divisor`

- `num a`: GCD of the digits of `a`
- `str a`: GCD of the `ord`s of `a`
- `lst a`: GCD of the numbers in `a`

---

# `h` (Head)

Tokens: `head`,`first`

- `any a`: push `a[0]`

---

# `i` (Indexing)

Tokens: `indexing`,`zero_indexing`

- `num a`, `any b`: push `b[a]` (0-based, modular)
- `any a`, `num b`: push `a[b]` (0-based, modular)

---

# `j` (Join)

Tokens: `join`

- `any a`, `any b`: push `a.join(b)`

---

# `k` (Constant digraphs)

| Command | Constant                                                               |
| ------- | ---------------------------------------------------------------------- |
| `kA`    | Uppercase alphabet: `[A-Z]`                                            |
| `kB`    | `'Buzz'`                                                               |
| `kC`    | Thunno 2 Codepage                                                      |
| `kD`    | Digits: `[0-9]`                                                        |
| `kE`    | Euler's Number: `2.718281828459045`                                    |
| `kF`    | `'Fizz'`                                                               |
| `kG`    | Golden ratio: `1.618033988749895`                                      |
| `kH`    | `'Hello, World!'`                                                      |
| `kI`    | Current microseconds                                                   |
| `kJ`    | Current seconds                                                        |
| `kK`    | Current minutes                                                        |
| `kL`    | Current hour                                                           |
| `kM`    | Current day                                                            |
| `kN`    | Current month                                                          |
| `kO`    | Current year                                                           |
| `kP`    | Pi: `3.141592653589793`                                                |
| `kQ`    | Current time (`YYYY-MM-DD HH:mm:ss`)                                   |
| `kR`    | Brackets: `'()[]{}'`                                                   |
| `kS`    | Open brackets: `'([{'`                                                 |
| `kT`    | Close brackets: `')]}'`                                                |
| `kU`    | Open brackets with angled brackets:`'([{<'`                            |
| `kV`    | Close brackets with angled brackets: `')]}>'`                          |
| `kW`    | Uppercase vowels: `'AEIOU'`                                            |
| `kX`    | Uppercase consonants: `'BCDFGHJKLMNPQRSTVWXYZ'`                        |
| `kY`    | Uppercase vowels with `Y`: `'AEIOUY'`                                  |
| `kZ`    | Uppercase consonants without `Y`: `'BCDFGHJKLMNPQRSTVWXZ'`             |
| `ka`    | Lowercase + uppercase alphabet: `[a-zA-Z]`                             |
| `kb`    | `'buzz'`                                                               |
| `kc`    | Printable ASCII characters                                             |
| `kd`    | Binary digits: `'01'`                                                  |
| `ke`    | Octal digits: `[0-7]`                                                  |
| `kf`    | Hexadecimal digits: `[0-9A-F]`                                         |
| `kg`    | `['Fizz', 'Buzz']`                                                     |
| `kh`    | `'Hello World'`                                                        |
| `ki`    | `16`                                                                   |
| `kj`    | `32`                                                                   |
| `kk`    | `64`                                                                   |
| `kl`    | `128`                                                                  |
| `km`    | `256`                                                                  |
| `kn`    | `512`                                                                  |
| `ko`    | `1024`                                                                 |
| `kp`    | `2048`                                                                 |
| `kq`    | `4096`                                                                 |
| `kr`    | `8192`                                                                 |
| `ks`    | `16384`                                                                |
| `kt`    | `32768`                                                                |
| `ku`    | `65536`                                                                |
| `kv`    | `["qwertyuiop", "asdfghjkl", "zxcvbnm"]`                               |
| `kw`    | Lowercase vowels: `'aeiou'`                                            |
| `kx`    | Lowercase consonants: `'bcdfghjklmnpqrstvwxyz'`                        |
| `ky`    | Lowercase vowels with `y`: `'aeiouy'`                                  |
| `kz`    | Lowercase consonants without `y`: `'bcdfghjklmnpqrstvwxz'`             |
| `k1`    | `10**3`                                                                |
| `k2`    | `10**4`                                                                |
| `k3`    | `10**5`                                                                |
| `k4`    | `10**6`                                                                |
| `k5`    | `10**7`                                                                |
| `k6`    | `10**8`                                                                |
| `k7`    | `10**9`                                                                |
| `k8`    | `10**10`                                                               |
| `k9`    | `10**11`                                                               |
| `k0`    | `10**12`                                                               |
| `k!`    | Thunno Version                                                         |
| `k"`    | `[0, 0]`                                                               |
| `k#`    | `[0, 1]`                                                               |
| `k$`    | `[0, -1]`                                                              |
| `k%`    | `[1, 0]`                                                               |
| `k&`    | `[1, 1]`                                                               |
| `k'`    | `[1, -1]`                                                              |
| `k(`    | `[-1, 0]`                                                              |
| `k)`    | `[-1, 1]`                                                              |
| `k*`    | `[-1, -1]`                                                             |
| `k+`    | `[3, 5]`                                                               |
| `kȦ`    | Alphanumeric characters: `[a-zA-Z0-9]`                                 |
| `kḂ`    | Base digits: `[0-9A-Za-z]`                                             |
| `kĊ`    | Alphanumeric characters + underscore: `[a-zA-Z0-9_]`                   |
| `kḊ`    | Reversed uppercase alphabet: `[Z-A]`                                   |
| `kĖ`    | Reversed lowercase + uppercase alphabet: `[z-aZ-A]`                    |
| `kḞ`    | Reversed alphanumeric characters + underscore: `[z-aZ-A9-0_]`          |
| `kĠ`    | Uppercase + lowercase alphabet: `[A-Za-z]`                             |
| `kḢ`    | Reversed uppercase + lowercase alphabet: `[Z-Az-a]`                    |
| `kİ`    | Reversed alphanumeric characters: `[z-aZ-A9-0]`                        |
| `kĿ`    | Alphanumeric characters: `[A-Za-z0-9]`                                 |
| `kṀ`    | Reversed alphanumeric characters: `[Z-Az-a9-0]`                        |
| `kṄ`    | Reversed digits: `[9-0]`                                               |
| `kȮ`    | Printable ASCII characters including newline                           |
| `kṖ`    | Punctuation: `'!"`<code>#$%&\\'()\*+,-./:;<=>?@[\\\\]^\_`{\|}~'</code> |
| `kṘ`    | `'http://'`                                                            |
| `kṠ`    | `'http://www.'`                                                        |
| `kṪ`    | `'https://www.'`                                                       |
| `kẆ`    | Whitespace: `' \t\n\r\x0b\x0c'`                                        |
| `kẊ`    | Bracket pairs: `['()', '[]', '{}', '<>']`                              |
| `kẎ`    | Nested brackets: `'([{<>}])'`                                          |
| `kŻ`    | Brainf\*ck commands: `'[]<>-+.,'`                                      |

---

# `l` (Length)

Tokens: `len`,`length`

- `any a`: push `len(a)`

---

# `m` (Mean)

Tokens: `mean`,`avg`,`average`

- `num a`: mean of the digits of `a`
- `str a`: mean `ord` of `a`
- `lst a`: mean of the numbers in `a`

---

# `n` (Loop variable)

Tokens: `context_variable`

Reserved for the value of the loop. Defaults to 0.

---

# `o` (Remove)

Tokens: `rmv`,`remove`

- `any a`, `any b`: push `b` without `a`

---

# `p` (Product)

Tokens: `product`,`prod`

- `num a`: digital product of `a`
- `str a`: product of the `ord`s of `a`
- `lst a`: product of the numbers in `a`

---

# `q` (Quit)

Tokens: `quit`

Terminate the program.

---

# `r` (Reverse)

Tokens: `reverse`

- `any a`: reverse `a`

---

# `s` (Swap)

Tokens: `swap`

- `any a`, `any b`: push `b`, `a`

---

# `t` (Tail)

Tokens: `tail`,`last`

- `any a`: push `a[-1]`

---

# `u` (Minus one)

Tokens: `negative_one`

Push `-1` to the stack.

---

# `v` (Replace)

Tokens: `replace`

- `any a`, `any b`, `any c`: replace all `b`s with `a` in `c`

---

# `w` (Factorial / Remove whitespace)

Tokens: `factorial`,`remove_whitespace`

- `num a`: factorial of `a`
- `str a`: remove whitespace from `a`

---

# `x` (Push `x`)

Tokens: `get_x`

Push the variable `x` to the stack.

---

# `y` (Push `y`)

Tokens: `get_y`

Push the variable `y` to the stack.

---

# `z` (Uninterleave)

Tokens: `uninterleave`

- `any a`: push `[a[0::2], a[1::2]]`

---

# `0` (Literal digit `0`)

Used in numeric literals

---

# `1` (Literal digit `1`)

Used in numeric literals

---

# `2` (Literal digit `2`)

Used in numeric literals

---

# `3` (Literal digit `3`)

Used in numeric literals

---

# `4` (Literal digit `4`)

Used in numeric literals

---

# `5` (Literal digit `5`)

Used in numeric literals

---

# `6` (Literal digit `6`)

Used in numeric literals

---

# `7` (Literal digit `7`)

Used in numeric literals

---

# `8` (Literal digit `8`)

Used in numeric literals

---

# `9` (Literal digit `9`)

Used in numeric literals

---

# `.` (One half)

Push `0.5` to the stack

---

# `Ȧ` (Any / Is alpha-num)

Tokens: `any`,`is_alphanum`,`is_alpha_num`

- `num a`: push `a != 0`
- `str a`: push `a.isalnum()`
- `lst a`: push `any(a)`

---

# `Ḃ` (Convert from binary)

Tokens: `from_binary`

- `any a`: push `int(a, 2)`

---

# `Ċ` (Codepage Chr / Ord)

Tokens: `codepage_chr`,`codepage_character`,`codepage_ord`,`codepage_ordinal`

- `num a`: `chr(a)` using Thunno 2 codepage
- `str a`: `ord(a)` using Thunno 2 codepage

---

# `Ḋ` (Is divisible)

Tokens: `divisible`,`is_divisible`

- `any a`, `any b`: push `b % a == 0`

---

# `Ė` (Enumerate / Inclusive zero range)

Tokens: `enumerate`,`inclusive_zero_range`

- `num a`: push `[0, 1, ..., a]`
- `str/lst a`: push `[[0, a[0]], [1, a[1]], ...]`

---

# `Ḟ` (Flatten)

Tokens: `flatten`,`recursive_flatten`

- `any a`: recursively flatten `a`

---

# `Ġ` (Dyadic GCD)

Tokens: `dyadic_gcd`

- `num a`, `num b`: push `gcd(a, b)`
- `num a`, `str b`: push `gcd(a, ord(b))`
- `str a`, `num b`: push `gcd(ord(a), b)`
- `str a`, `str b`: longest common substring of `a` and `b`

---

# `Ḣ` (Head extract)

Tokens: `head_extract`

- `any a`: push `a[0]`, `a[1:]`

---

# `İ` (One-based indexing)

Tokens: `one_indexing`

- `num a`, `any b`: push `b[a]` (1-based, modular)
- `any a`, `num b`: push `a[b]` (1-based, modular)

---

# `Ŀ` (Left justify)

Tokens: `ljust`,`left_justify`

- `num a`, `any b`, `any c`: push `c.ljust(a, b)`
- `any a`, `num b`, `any c`: push `c.ljust(b, a)`

---

# `Ṁ` (Mode)

Tokens: `mode`,`most_common_element`

- `any a`: most common element of `a`

---

# `Ṅ` (Negate / Run length encoding)

Tokens: `negate`,`neg`,`rle`,`run_length_encode`

- `num a`: push `-a`
- `str a`: run-length encode `a`

---

# `Ȯ` (Index of)

Tokens: `index_of`,`find`

- `any a`, `any b`: push `b.index(a)`

---

# `Ṗ` (Cartesian product)

Tokens: `cartesian_product`

- `any a`, `any b`: cartesian product of `a` and `b`

---

# `Ṙ` (Repr)

Tokens: `repr`

- `any a`: push `repr(a)`

---

# `Ṡ` (Sort)

Tokens: `sort`

- `any a`: push `sorted(a)`

---

# `Ṫ` (Tail extract)

Tokens: `tail_extract`

- `any a`: push `a[-1]`, `a[:-1]`

---

# `Ẇ` (Chunk)

Tokens: `chunk`,`chunk_split`

- `num a`, `any b`: split `b` into `a` chunks
- `any a`, `num b`: split `a` into `b` chunks

---

# `Ẋ` (Store in x without popping)

Tokens: `set_x_without_popping`

- `any a`: store `a` in variable `x` without popping `a` from the stack

---

# `Ẏ` (Store in y without popping)

Tokens: `set_y_without_popping`

- `any a`: store `a` in variable `y` without popping `a` from the stack

---

# `Ż` (Length range)

Tokens: `zero_length_range`

- `any a`: push `[0, 1, ..., len(a) - 1]` without popping `a`

---

# `,` (Pair)

Tokens: `pair`

- `any a`, `any b`: push `[b, a]`

---

# `£` (Print)

Tokens: `print`

- `any a`: print `a` with a trailing newline

---

# `⁺` (Increment)

Tokens: `increment`,`incr`,`plus_one`

- `any a`: push `a + 1`

---

# `⁻` (Decrement)

Tokens: `decrement`,`decr`,`minus_one`

- `any a`: push `a - 1`

---

# `⁼` (Exactly equal)

Tokens: `exactly_equal`,`exactly_equals`

- `any a`, `any b`: push `b == a`

---

# `+` (Addition)

Tokens: `add`,`plus`

- `num a`, `num b`: push `b + a`
- `num a`, `str b`: push `b + str(a)`
- `str a`, `num b`: push `str(b) + a`
- `str a`, `str b`: push `b + a`

---

# `-` (Subtraction)

Tokens: `subtract`,`minus`

- `num a`, `num b`: push `b - a`
- `num a`, `str b`: push `b[:-a]`
- `str a`, `num b`: push `b[a:]`
- `str a`, `str b`: push `b.replace(a, '')`

---

# `×` (Multiplication)

Tokens: `multiply`,`times`

- `num a`, `num b`: push `b * a`
- `num a`, `str b`: push `b * a`
- `str a`, `num b`: push `b * a`
- `str a`, `str b`: cartesian product of `a` and `b`

---

# `/` (Division)

Tokens: `divide`,`split`

- `num a`, `num b`: push `b / a`
- `num a`, `str b`: split `b` into `a` pieces
- `str a`, `num b`: split `a` into `b` pieces
- `str a`, `str b`: push `b.split(a)`

---

# `*` (Exponentiation)

Tokens: `exponentiate`,`power`,`pow`,`regex`,`findall`

- `num a`, `num b`: push `b ** a`
- `num a`, `str b`: append `b[0]` to `b` until `b` is length `a`
- `str a`, `num b`: append `a[0]` to `a` until `a` is length `b`
- `str a`, `str b`: regex findall (`a` = pattern, `b` = search string)

---

# `%` (Modulo)

Tokens: `modulo`,`mod`,`format`

- `num a`, `num b`: push `b % a`
- `num a`, `str b`: replace `%`s in `b` with `a`
- `str a`, `num b`: replace `%`s in `a` with `b`
- `str a`, `str b`: replace `%`s in `b` with `a`

---

# `÷` (Integer division)

Tokens: `floor_divide`,`integer_divide`

- `num a`, `num b`: push `b // a`
- `num a`, `str b`: first item of `b` split into `a` pieces
- `str a`, `num b`: first item of `a` split into `b` pieces
- `str a`, `str b`: first item of `b.split(a)`

---

# `_` (Swapped subtraction)

Tokens: `swapped_subtract`,`swapped_minus`

- `num a`, `num b`: push `a - b`
- `num a`, `str b`: push `b[a:]`
- `str a`, `num b`: push `b[:-a]`
- `str a`, `str b`: push `a.replace(b, '')`

---

# `\` (Swapped division)

Tokens: `swapped_divide`,`swapped_split`

- `num a`, `num b`: push `a / b`
- `num a`, `str b`: split `b` into `a` pieces
- `str a`, `num b`: split `a` into `b` pieces
- `str a`, `str b`: push `a.split(b)`

---

# `@` (Swapped exponentiation)

Tokens: `swapped_exponentiate`,`swapped_pow`,`swapped_findall`,`swapped_regex`

- `num a`, `num b`: push `a ** b`
- `num a`, `str b`: prepend `b[-1]` to `b` until `b` is length `a`
- `str a`, `num b`: prepend `a[-1]` to `a` until `a` is length `b`
- `str a`, `str b`: regex findall (`a` = search string, `b` = pattern)

---

# `Œ` (Swapped modulo)

Tokens: `swapped_modulo`,`swapped_mod`,`swapped_format`

- `num a`, `num b`: push `a % b`
- `num a`, `str b`: replace `%`s in `b` with `a`
- `str a`, `num b`: replace `%`s in `a` with `b`
- `str a`, `str b`: replace `%`s in `a` with `b`

---

# `¦` (Swapped integer division)

Tokens: `swapped_floor_divide`,`swapped_integer_divide`

- `num a`, `num b`: push `a // b`
- `num a`, `str b`: last item of `b` split into `a` pieces
- `str a`, `num b`: last item of `a` split into `b` pieces
- `str a`, `str b`: last item of `b.split(a)`

---

# `=` (Equal to)

Tokens: `equal`,`equals`

- `any a`, `any b`: push `b == a`

---

# `<` (Less than)

Tokens: `less_than`

- `any a`, `any b`: push `b < a`

---

# `>` (Greater than)

Tokens: `greater_than`

- `any a`, `any b`: push `b > a`

---

# `©` (Less than or equal to)

Tokens: `less_than_or_equal_to`

- `any a`, `any b`: push `b <= a`

---

# `®` (Greater than or equal to)

Tokens: `greater_than_or_equal_to`

- `any a`, `any b`: push `b >= a`

---

# `&` (Logical AND)

Tokens: `and`,`logical_and`

- `any a`, `any b`: push `b and a`

---

# `|` (Logical OR)

Tokens: `or`, `logical_or`

- `any a`, `any b`: push `b or a`

---

# `^` (Logical XOR)

Tokens: `xor`,`logical_xor`

- `any a`, `any b`: push `b ^ a`

---

# `~` (Logical NOT)

Tokens: `not`,`logical_not`

- `any a`: push `not a`

---

# `$` (Next input)

Tokens: `next_input`

Push the next input from the input list.

---

# `¤` (Input list)

Tokens: `input_list`

Push all the inputs in a list.

---

# `ð` (Space)

Tokens: `space`

Push a space to the stack.

---

# `¢` (Print without a newline)

Tokens: `print_without_newline`

- `any a`: print `a` without a trailing newline

---

# `ß` (Print without popping)

Tokens: `print_without_popping`

- `any a`: print `a` without popping

---

# `¶` (Newline)

Tokens: `newline`

Push `\n` to the stack.

---

# `¬` (Non-vectorised logical NOT)

Tokens: `non_vectorised_not`,`non_vectorised_logical_not`

- `any a`: push `not a`

---

# `§` (Dyadic maximum)

Tokens: `dyadic_maximum`

- `any a`, `any b`: push `max([a, b])`

---

# `½` (Halve)

Tokens: `halve`

- `num a`: push `a / 2`
- `str a`: split `a` into two pieces

---

# `ȧ` (Assign)

Tokens: `assign`

- `any a`, `num b`, `any c`: `c[b] = a` (0-based, modular)
- `any a`, `any b`, `num c`: `b[c] = a` (0-based, modular)

---

# `ḃ` (Binary)

Tokens: `bin`,`binary`,`to_binary`

- `any a`: push `bin(a)`

---

# `ċ` (Combinations / Set union)

Tokens: `combinations`,`union`

- `num a`, `any b`: list of all combinations of `b` with length `a`
- `any a`, `num b`: list of all combinations of `a` with length `b`
- `str/lst a`, `str/lst b`: merge `b` and `a` and remove duplicates

---

# `ḋ` (Divmod / From list of digits)

Tokens: `divmod`,`from_digits`

- `num a`, `num b`: push `[b // a, b % a]`
- `num a`, `lst b`: convert `b` from a list of digits in base `a`
- `lst a`, `num b`: convert `a` from a list of digits in base `b`

---

# `ė` (Exclusive one range / Length range)

Tokens: `length_range`,`exclusive_one_range`

- `num a`: push `[1, 2, ..., a-1]`
- `str/lst a`: push `[1, 2, ..., len(a)]`

---

# `ḟ` (Prime factor exponents / Title case)

Tokens: `prime_factor_exponents`,`title`,`title_case`

- `num a`: exponents of the prime factorisation of `a`
- `str a`: push `a.title()`

---

# `ġ` (Group consecutive)

Tokens: `group_consecutive`

- `any a`: group consecutive elements of `a`

---

# `ḣ` (Head remove)

Tokens: `head_remove`

- `any a`: push `a[1:]`

---

# `ŀ` (LCM)

Tokens: `lcm`,`lowest_common_multiple`

- `num a`: LCM of the digits of `a`
- `str a`: LCM of the `ord`s of `a`
- `lst a`: LCM of the numbers in `a`

---

# `ṁ` (Median)

Tokens: `median`

- `any a`: middle item of `a` when sorted

---

# `ṅ` (Iteration index)

Tokens: `iteration_index`

Reserved for the index of the loop. Defaults to 0.

---

# `ȯ` (Set intersection / Round)

Tokens: `set_intersection`,`round_dps`

- `num a`, `num b`: round `b` to `a` decimal places
- `any a`, `any b`: elements from `b` which are also in `a`

---

# `ṗ` (Permutations / Set difference)

Tokens: `permutations`,`set_difference`

- `num a`, `any b`: list of all permutations of `b` with length `a`
- `any a`, `num b`: list of all permutations of `a` with length `b`
- `str/lst a`, `str/lst b`: elements of `b` which aren't in `a`

---

# `ṙ` (Right justify)

Tokens: `rjust`,`right_justify`

- `num a`, `any b`, `any c`: push `c.rjust(a, b)`
- `any a`, `num b`, `any c`: push `c.rjust(b, a)`

---

# `ṫ` (Tail remove)

Tokens: `tail_remove`

- `any a`: push `a[:-1]`

---

# `ṡ` (Cumulative sums)

Tokens: `cumsum`,`cumulative_sums`

- `any a`: push `[a[0], a[0] + a[1], a[0] + a[1] + a[2], ...]`

---

# `ẇ` (Chunk wrap)

Tokens: `chunk_wrap`,`split_chunk`

- `num a`, `any b`: split `b` into chunks of length `a`
- `any a`, `num b`: split `a` into chunks of length `b`

---

# `ẋ` (Apply to x)

Tokens: `apply_to_x`

Apply the next command to `x`.

---

# `ẏ` (Apply to y)

Tokens: `apply_to_y`

Apply the next command to `y`.

---

# `ż` (Length range)

Tokens: `length_range_no_pop`

- `any a`: push `[1, 2, ..., len(a)]` without popping `a`

---

# `Ạ` (Lowercase alphabet)

Tokens: `alphabet`,`lowercase_alphabet`

Push `abcdefghijklmnopqrstuvwxyz` to the stack

---

# `Ḅ` (Base conversion / Character multiply / Regex split)

Tokens: `to_base_string`,`character_multiply`,`regex_split`

- `num a`, `num b`: convert `b` to a string in base `a`
- `num a`, `str b`: repeat each character in `b` `a` times
- `str a`, `num b`: repeat each character in `a` `b` times
- `str a`, `str b`: regex split (`a` = pattern, `b` = search string)

---

# `Ḍ` (Double)

Tokens: `double`

- `any a`: push `a * 2`

---

# `Ẹ` (Dump onto stack)

Tokens: `dump`

- `any a`: push each item of `a` to the stack

---

# `Ḥ` (Hexadecimal)

Tokens: `hex`,`hexadecimal`,`to_hexadecimal`

- `any a`: push `hex(a)`

---

# `Ị` (Reciprocal / Remove non-alphabets)

Tokens: `reciprocal`,`inverse`,`filter_isalpha`,`only_alphabetic`

- `num a`: push `1 / a`
- `str a`: remove non-alphabets from `a`

---

# `Ḳ` (Bifurcate)

Tokens: `bifurcate`

- `any a`: push `reversed(a)` without popping `a`

---

# `Ḷ` (Dyadic LCM)

Tokens: `dyadic_lcm`

- `num a`, `num b`: push `lcm(a, b)`
- `num a`, `str b`: push `lcm(a, ord(b))`
- `str a`, `num b`: push `lcm(ord(a), b)`
- `str a`, `str b`: push `lcm(ord(a), ord(b))`

---

# `Ṃ` (Mirror)

Tokens: `mirror`

- `any a`: push `a + reversed(a)`

---

# `Ṇ` (Transliterate)

Tokens: `transliterate`

- `any a`, `any b`, `any c`: transliterate `c` from `b` to `a`

---

# `Ọ` (Dyadic minimum)

Tokens: `dyadic_minimum`

- `any a`, `any b`: push `min([a, b])`

---

# `Ṛ` (Combinations with replacement)

Tokens: `combinations_with_replacement`

- `num a`, `any b`: list of all combinations with replacement of `b` with length `a`
- `any a`, `num b`: list of all combinations with replacement of `a` with length `b`

---

# `Ṣ` (Forward differences)

Tokens: `deltas`,`forward_differences`

- `any a`: push `[a[1] - a[0], a[2] - a[1], ...]`

---

# `Ṭ` (Transpose)

Tokens: `transpose`

- `any a`: transpose `a`

---

# `Ụ` (Rotate left once)

Tokens: `rotate_left_once`

- `any a`: rotate `a` left by one place

---

# `Ṿ` (Rotate right once)

Tokens: `rotate_right_once`

- `any a`: rotate `a` right by one place

---

# `Ẉ` (Uninterleave)

Tokens: `uninterleave_into_pieces`

- `num a`, `any b`: push `[b[0::a], b[1::a], ...]`
- `any a`, `num b`: push `[a[0::b], a[1::b], ...]`

---

# `Ỵ` (Rotate left / Left bit shift)

Tokens: `rotate_left`,`left_bit_shift`

- `num a`, `num b`: push `b << a`
- `num a`, `any b`: rotate `b` left by `a` places
- `any a`, `num b`: rotate `a` left by `b` places

---

# `Ẓ` (Rotate right / Right bit shift)

Tokens: `rotate_right`,`right_bit_shift`

- `num a`, `num b`: push `b >> a`
- `num a`, `any b`: rotate `b` right by `a` places
- `any a`, `num b`: rotate `a` right by `b` places

---

# `Ä` (Number to alphabet / Alphabet to number)

Tokens: `num_to_alphabet`,`alphabet_to_num`

- `num a`: `a`th letter of the alphabet
- `str a`: index of `a` in the alphabet

---

# `°` (First input)

Tokens: `first_input`

Push the first input to the stack.

---

# `¹` (Second input)

Tokens: `second_input`

Push the second input to the stack.

---

# `²` (Square)

Tokens: `square`

- `num a`: push `a ** 2`
- `str a`: split `a` into chunks of length 2

---

# `³` (Cube)

Tokens: `cube`

- `num a`: push `a ** 3`
- `str a`: split `a` into chunks of length 3

---

# `⁴` (Fourth power)

Tokens: `fourth`,`fourth_power`

- `num a`: push `a ** 4`
- `str a`: split `a` into chunks of length 4

---

# `⁵` (Fifth power)

Tokens: `fifth`,`fifth_power`

- `num a`: push `a ** 5`
- `str a`: split `a` into chunks of length 5

---

# `⁶` (Third input)

Tokens: `third_input`

Push the third input to the stack.

---

# `⁷` (Third last input)

Tokens: `third_last_input`

Push the third last input to the stack.

---

# `⁸` (Second last input)

Tokens: `second_last_input`

Push the second last input to the stack.

---

# `⁹` (Last input)

Tokens: `last_input`

Push the last input to the stack.

---

# `Ɓ` (Execute without popping)

Tokens: `execute_without_popping`

Run the next command without popping any items from the stack.

---

# `Ƈ` (Contains / nPr)

Tokens: `npr`,`contains`

- `num a`, `num b`: push `nPr(b, a)`
- `any a`, `str/lst b`: push `a in b`

---

# `Ɗ` (Drop at index)

Tokens: `drop_at_index`,`remove_at_index`

- `any a`, `any b`: remove the item at index `a` from `b`

---

# `Ƒ` (Unique prime factors / Substrings / Sublists)

Tokens: `unique_prime_factors`,`sublists`

- `num a`: unique prime factors of `a`
- `str a`: substrings of `a`
- `lst a`: sublists of `a`

---

# `Ɠ` (Sixteen)

Tokens: `sixteen`

Push `16` to the stack.

---

# `Ƙ` (First n integers)

Tokens: `first_n_integers`

Usage: `Ƙ CODE ;`. Push the first `a` positive integers where the result of `CODE` is true.

---

# `Ɱ` (Palindromise)

Tokens: `palindromise`

- `any a`: push `a + a[:-1][::-1]`

---

# `Ɲ` (Integer partitions / Join by newlines)

Tokens: `integer_partitions`,`newline_join`,`join_by_newlines`

- `num a`: integer partitions of `a`
- `lst a`: push `'\n'.join(a)`

---

# `Ƥ` (Prepend)

Tokens: `prepend`

- `any a`, `any b`: prepend `a` to `b`

---

# `Ƭ` (Transpose with filler)

Tokens: `transpose_with_filler`

- `any a`, `any b`: transpose `b`, using `a` as a fill value

---

# `Ʋ` (Cumulative reduce by)

Tokens: `cumulative_reduce_by`

Usage: `Ʋ CODE ;`. Cumulative reduce (scanl) `a` by `CODE`

---

# `Ȥ` (Push global array)

Tokens: `get_global_array`

Push the global array to the stack.

---

# `ɓ` (Boolify)

Tokens: `boolify`

- `any a`: push `bool(a)`

---

# `ƈ` (Counts)

Tokens: `counts`

- `any a`: push a list of `[item, count]` for each item in `a`

---

# `ɗ` (Parity / Second half)

Tokens: `parity`,`second_half`

- `num a`: push `a % 2`
- `str a`: second half of `a`

---

# `ƒ` (Prefixes)

Tokens: `prefixes`

- `any a`: push `[a[:1], a[:2], ..., a[:]]`

---

# `ɠ` (Two hundred and fifty-six)

Tokens: `two_fifty_six`,`two_hundred_fifty_six`

Push `256` to the stack.

---

# `ɦ` (One hundred)

Tokens: `hundred`,`one_hundred`

Push `100` to the stack.

---

# `ƙ` (Grade up / Increment twice)

Tokens: `grade_up`,`increment_twice`

- `num a`: push `a + 2`
- `str/lst a`: indices that will sort `a` in ascending order

---

# `ɱ` (Head slice)

Tokens: `head_slice`

- `num a`, `any b`: push `b[:a]` (first `a` items of `b`)
- `any a`, `num b`: push `a[:b]` (first `b` items of `a`)

---

# `ɲ` (Tail slice)

Tokens: `tail_slice`

- `num a`, `any b`: push `b[-a:]` (last `a` items of `b`)
- `any a`, `num b`: push `a[-b:]` (last `b` items of `a`)

---

# `ƥ` (Pop)

Tokens: `pop`

Pop `a` from the stack.

---

# `ʠ` (Powerset)

Tokens: `powerset`

- `any a`: all combinations of `a`, including the empty one

---

# `ɼ` (Random choice)

Tokens: `random`,`random_choice`,`randint`

- `num a`: random element of `[1, 2, ..., a]`
- `str/lst a`: random element of `a`

---

# `ʂ` (Sum each / Sign / Sentence case)

Tokens: `sign`,`sentence_case`,`sum_each`

- `num a`: push `-1` if `a < 0`, `0` if `a == 0`, `1` if `a > 0`
- `str a`: convert `a` to sentence case
- `lst a`: sum each element of `a`

---

# `ƭ` (Square root)

Tokens: `square_root`,`every_second_item`

- `num a`: square root of `a`
- `str a`: every second character of `a`

---

# `ȥ` (Add to global array)

Tokens: `add_to_global_array`

- `any a`: add `a` to the global array

---

# `ạ` (All equal)

Tokens: `all_equal`

- `any a`: are all the elements of `a` equal?

---

# `ḅ` (Equals one)

Tokens: `equals_one`

- `any a`: push `a == 1`

---

# `ḍ` (Symmetric set difference)

Tokens: `symmetric_set_difference`

- `any a`, `any b`: uncommon elements of `b` and `a`

---

# `ẹ` (Enclose)

Tokens: `enclose`

- `any a`: append `a[0]` to `a`

---

# `ḥ` (Concatenate)

Tokens: `concatenate`,`merge`

- `any a`, `any b`: concatenate `b` with `a`

---

# `ị` (Corresponding filter)

Tokens: `corresponding_filter`

- `any a`, `any b`: filter `b` by the corresponding elements of `a`

---

# `ḳ` (Sorted uniquify)

Tokens: `sorted_uniquify`

- `any a`: uniquify and sort `a`

---

# `ḷ` (Length of each / Complement / Is lower)

Tokens: `length_of_each`,`complement`,`is_lower`

- `num a`: push `1 - a`
- `str a`: is `a` all lowercase?
- `lst a`: lengths of each element of `a`

---

# `ṃ` (Ceil / Is vowel / Reverse each)

Tokens: `ceil`,`is_vowel`,`reverse_each`

- `num a`: push `ceil(a)`
- `str a`: is `a` a vowel?
- `lst a`: reverse each element of `a`

---

# `ṇ` (Codepage integer compression)

Tokens: `codepage_compression`

Push the index of the next character of the codepage + 101

---

# `ọ` (Repeat)

Tokens: `repeat`

- `num a`, `any b`: repeat `b` `a` times
- `any a`, `num b`: repeat `a` `b` times

---

# `ṛ` (Compare / Zfill / Surround)

Tokens: `compare`,`cmp`,`zfill`,`surround`

- `num a`, `num b`: push `1` if `b > a`, `0` if `b == a`, `-1` if `b < a`
- `num a`, `str b`: push `b.zfill(a)`
- `str a`, `str b`: push `a.zfill(b)`
- `str a`, `str b`: push `a + b + a`

---

# `ṣ` (Suffixes / Spaces)

Tokens: `suffixes`,`spaces`

- `num a`: push `a * ' '`
- `str/lst a`: push `[a[-1:], a[-2:], ..., a[:]]`

---

# `ṭ` (Triple swap)

Tokens: `triple_swap`

- `any a`, `any b`, `any c`: move `a` below `b` and `c`

---

# `ẉ` (Cartesian power)

Tokens: `cartesian_power`

- `num a`, `any b`: `b` raised to the `a`th cartesian power
- `any a`, `num b`: `a` raised to the `b`th cartesian power

---

# `ỵ` (Head remove)

Tokens: `head_remove_many`

- `num a`, `any b`: remove the first `a` elements of `b`
- `any a`, `num b`: remove the first `b` elements of `a`

---

# `ẓ` (Tail remove)

Tokens: `tail_remove_many`

- `num a`, `any b`: remove the last `a` elements of `b`
- `any a`, `num b`: remove the last `b` elements of `a`

---

# `øB` (Brackets are balanced)

Tokens: `balanced_brackets`,`brackets_are_balanced`

- `any a`: are the brackets balanced in `a`?

---

# `øD` (Optimal dictionary compression)

Tokens: `optimal_dictionary_compression`

- `any a`: optimally dictionary compress `a`

---

# `øv` (Global canvas draw)

- `any a`, `any b`: draw `b` on the global canvas using `a` as directions. \
  See [`docs/canvas.md`](https://github.com/Thunno/Thunno2/blob/main/docs/canvas.md) for more.

---

# `øV` (Blank canvas draw)

- `any a`, `any b`: draw `b` on a blank canvas using `a` as directions. \
  See [`docs/canvas.md`](https://github.com/Thunno/Thunno2/blob/main/docs/canvas.md) for more.

---

# `ø^` (Clear global canvas)

Clear the global canvas. See [`docs/canvas.md`](https://github.com/Thunno/Thunno2/blob/main/docs/canvas.md) for more.

---

# `ø<` (Starts with)

- `any a`, `any b`: does `b` start with `a`?

---

# `ø>` (Ends with)

- `any a`, `any b`: does `b` end with `a`?

---

# `ØC` (Center)

Tokens: `center`,`centre`

- `any a`: center `a`

---

# `ØD` (Depth)

Tokens: `depth`

- `any a`: maximum depth of `a`

---

# `ØE` (Extend/truncate to length)

Tokens: `extend`,`truncate`,`extend_truncate`,`extend_to_length`,`truncate_to_length`

- `num a`, `any b`: extend/truncate `b` to length `a`
- `any a`, `num b`: extend/truncate `a` to length `b`

---

# `ØG` (Longest element)

Tokens: `longest`

- `any a`: longest element of `a`

---

# `ØM` (Shortest element)

Tokens: `shortest`

- `any a`: shortest element of `a`

---

# `Ø.` (Dot product)

Tokens: `dot_product`

- `any a`, `any b`: dot product of `a` and `b`

---

# <code>Ø\\</code> (Main diagonal)

- `any a`: main diagonal of `a`

---

# `Ø/` (Main anti-diagonal)

Tokens: `anti_diagonal`

- `any a`: main anti-diagonal of `a`

---

# `Ø“` (All diagonals)

Tokens: `all_diagonals`

- `any a`: all diagonals of `a`

---

# `Ø”` (All anti-diagonals)

Tokens: `all_anti_diagonals`

- `any a`: all anti-diagonals of `a`

---

# `ÆC` (Cosine)

Tokens: `cosine`,`cos`

- `any a`: push `cos(a)`

---

# `ÆD` (Degrees)

Tokens: `degrees`

- `any a`: push `degrees(a)`

---

# `ÆE` (Exponent)

Tokens: `exponent`

- `any a`: push `exp(a)`

---

# `ÆF` (nth Fibonacci number)

Tokens: `nth_fibonacci_number`

- `any a`: `n`th Fibonacci number

---

# `ÆH` (Hypotenuse)

Tokens: `hypot`,`hypotenuse`

- `any a`, `any b`: push `sqrt(a**2 + b**2)`

---

# `ÆI` (Insignificant)

Tokens: `insignificant`

- `any a`: push `abs(a) <= 1`

---

# `ÆP` (nth prime number)

Tokens: `nth_prime`

- `any a`: `n`th prime number

---

# `ÆR` (Radians)

Tokens: `radians`

- `any a`: push `radians(a)`

---

# `ÆS` (Sine)

Tokens: `sine`,`sin`

- `any a`: push `sin(a)`

---

# `ÆT` (Tangent)

Tokens: `tangent`,`tan`

- `any a`: push `tan(a)`

---

# `Æc` (Inverse cosine)

Tokens: `arc_cosine`,`arccos`

- `any a`: push `arccos(a)`

---

# `Æs` (Inverse sine)

Tokens: `arc_sine`,`arcsin`

- `any a`: push `arcsin(a)`

---

# `Æt` (Inverse tangent)

Tokens: `arc_tangent`,`arctan`

- `any a`: push `arctan(a)`

---

# `Æ&` (Bitwise AND)

Tokens: `bitwise_and`

- `any a`, `any b`: push `b & a`

---

# `Æ|` (Bitwise OR)

Tokens: `bitwise_or`

- `any a`, `any b`: push `b | a`

---

# `Æ^` (Bitwise XOR)

Tokens: `bitwise_xor`

- `any a`, `any b`: push `b ^ a`

---

# `Æ~` (Bitwise NOT)

Tokens: `bitwise_not`

- `any a`: push `~a`

---

# `µR` (To Roman numerals / From Roman numerals)

Tokens: `roman_numerals`

- `num a`: convert `a` to Roman numerals
- `str a`: convert `a` from Roman numerals

---

# `µT` (Type)

Tokens: `type`

- `num a`: push `0` if int, `1` if float
- `str a`: push `2`
- `lst a`: push `3`

---

# `µU` (Connected uniquify)

Tokens: `connected_uniquify`

- `any a`: connected uniquify `a`

---

# `µr` (Random shuffle)

Tokens: `random_shuffle`

- `any a`: random permutation of `a`

---

# `µv` (Trim)

Tokens: `trim`

- `any a`, `any b`: remove `a` from both sides of `b`

---

# `µ<` (Left trim)

Tokens: `left_trim`

- `any a`, `any b`: remove `a` from the left side of `b`

---

# `µ>` (Right trim)

Tokens: `right_trim`

- `any a`, `any b`: remove `a` from the right side of `b`

---

# `µµ` (Recursive environment)

Tokens: `recursive_environment`

Usage: `µµ CODE ;`. Start recursive list generation, executing `CODE` to get each successive item in the sequence.

---

# `µ£` (Print each)

- `any a`: print each item of `a`

---

# `µ&` (Non-vectorised logical AND)

Tokens: `non_vectorised_and`,`non_vectorised_logical_and`

- `any a`, `any b`: push `b and a`

---

# `µ|` (Non-vectorised logical OR)

Tokens: `non_vectorised_or`,`non_vectorised_logical_or`

- `any a`, `any b`: push `b or a`

---

# `µ^` (Non-vectorised logical XOR)

Tokens: `non_vectorised_xor`,`non_vectorised_logical_xor`

- `any a`, `any b`: push `b ^ a`

---

# `µƲ` (Single function reduce by)

Tokens: `single_function_reduce_by`

Reduce (foldl) the elements of `a` by the next command.

---

# `µɼ` (Single function right reduce by)

Tokens: `single_function_right_reduce_by`

Right reduce (foldr) the elements of `a` by the next command.

---

# `µƇ` (Single function right cumulative reduce by)

Tokens: `single_function_right_cumulative_reduce_by`

Right cumulative reduce (scanr) the elements of `a` by the next command.

---

# `µʋ` (Right reduce by)

Tokens: `right_reduce_by`

Usage: `Ʋ CODE ;`. Right reduce (foldr) `a` by `CODE`

---
