"""
NOTE: This is just an experiment.

Each command in Thunno 2 has been assigned at least one token.
Using those tokens we can retrieve the original command.
"""

from thunno2.interpreter import commands
from thunno2.commands import (
    string_digraphs,
    list_digraphs,
    random_digraphs_1,
    random_digraphs_2,
)
import sys


def get_command(token):
    for tokens, cmd in full_list:
        if token.lower() == tokens:
            return cmd
    print(f"Couldn't find a command for token {token!r}", file=sys.stderr)
    sys.exit(0)


def transpile(code):
    r = ""
    for word in code.split():
        if word[:1] == "\\":
            r += word[1:]
        elif word.isdigit():
            r += word
        elif word == "":
            r += " "
        else:
            r += get_command(word)
    return r


def test():
    tokens_list = [x for x, y in full_list]
    for t, _ in full_list:
        assert (
            tokens_list.count(t) == 1
        ), f"Token {t!r} not unique (used {tokens_list.count(t)} times)"
        assert t == t.lower(), f"Token {t!r} not lowercase"
        assert t.replace("_", "").isalnum(), f"Token {t!r} invalid"
    print("[TOKENS]: Passed")


other_tokens = {
    '"': ("string_literal",),
    "'": ("one_character",),
    "`": ("two_characters",),
    "ʋ": ("three_characters",),
    "“": ("lowercase_string_compression",),
    "”": ("title_case_string_compression",),
    "‘": ("lowercase_dictionary_compression",),
    "’": ("title_case_dictionary_compression",),
    "»": ("integer_compression",),
    "«": ("small_integer_compression",),
    "¿": ("integer_list_compression",),
    "[": ("open_list_literal", "open_list", "list"),
    "]": ("close_list_literal", "close_list", "end_list"),
    "#": ("comment",),
    " ": ("nop",),
    "¡": ("get_veriable",),
    "!": ("set_variable",),
    "ı": ("map",),
    "€": ("single_function_map",),
    "æ": ("filter",),
    "œ": ("single_function_filter",),
    "Þ": ("sort_by",),
    "þ": ("single_function_sort_by",),
    "Ñ": ("group_by",),
    "ñ": ("single_function_group_by",),
    "ȷ": ("outer_product",),
    "¥": ("fixed_point",),
    "{": ("open_for_loop",),
    "}": ("close_for_loop",),
    "(": ("open_while_loop",),
    ")": ("close_while_loop",),
    "⁽": ("open_forever_loop",),
    "⁾": ("close_forever_loop",),
    "?": ("if_statement", "if"),
    ":": ("else_statement", "else"),
    ";": ("close_statement",),
    "ç": ("pair_apply",),
    "n": ("context_variable",),
    "ṅ": ("iteration_index",),
    "x": ("get_x",),
    "y": ("get_y",),
    "X": ("set_x",),
    "Y": ("set_y",),
    "Ẋ": ("set_x_without_popping",),
    "Ẏ": ("set_y_without_popping",),
    "ẋ": ("apply_to_x",),
    "ẏ": ("apply_to_y",),
    "Ȥ": ("get_global_array",),
    "ȥ": ("add_to_global_array",),
    "K": ("stack",),
    "ṇ": ("codepage_compression",),
    "q": ("quit",),
    "$": ("next_input",),
    "¤": ("input_list",),
    "°": ("first_input",),
    "¹": ("second_input",),
    "⁶": ("third_input",),
    "⁷": ("third_last_input",),
    "⁸": ("second_last_input",),
    "⁹": ("last_input",),
    "£": ("print",),
    "¢": ("print_without_newline",),
    "ß": ("print_without_popping",),
    "Ƙ": ("first_n_integers",),
    "Ʋ": ("cumulative_reduce_by",),
    "Ɓ": ("execute_without_popping",),
    "µµ": ("recursive_environment",),
    "µƲ": ("single_function_reduce_by",),
    "µɼ": ("single_function_right_reduce_by",),
    "µƇ": ("single_function_right_cumulative_reduce_by",),
    "µʋ": ("right_reduce_by",),
    "µ€": ("apply_to_every_nth_item",),
    "µ«": ("rotate_stack_left",),
    "µ»": ("rotate_stack_right",),
    "µ!": ("reverse_stack",),
    "µÑ": ("adjacent_group_by",),
    "µñ": ("single_function_adjacent_group_by",),
}


full_list = (
    [(token, cmd) for cmd, ovld in commands.items() for token in ovld.keywords]
    + [
        (token, "ø" + cmd)
        for cmd, ovld in string_digraphs.items()
        for token in ovld.keywords
    ]
    + [
        (token, "Ø" + cmd)
        for cmd, ovld in list_digraphs.items()
        for token in ovld.keywords
    ]
    + [
        (token, "Æ" + cmd)
        for cmd, ovld in random_digraphs_1.items()
        for token in ovld.keywords
    ]
    + [
        (token, "µ" + cmd)
        for cmd, ovld in random_digraphs_2.items()
        for token in ovld.keywords
    ]
    + [(val, key) for key, vals in other_tokens.items() for val in vals]
)
