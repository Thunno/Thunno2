"""
NOTE: This is just an experiment.

Each command in Thunno 2 has been assigned at least one token.
Using those tokens we can retrieve the original command.
"""

from thunno2.interpreter import commands
import sys


def get_command(token):
    for cmd, ovld in commands.items():
        if token.lower() in ovld.keywords:
            return cmd
    print(f"Couldn't find a command for token {token!r}", file=sys.stderr)
    sys.exit(0)


def transpile(code):
    r = ''
    for word in code.split():
        if word[:1] == '\\':
            r += word[1:]
        else:
            r += get_command(word)
    return r


def test():
    l = [token for cmd, ovld in commands.items() for token in ovld.keywords]
    for t in l:
        assert len(t) >= 2, f"Token {t!r} too short"
        assert l.count(t) == 1, f"Token {t!r} not unique"
        assert t == t.lower(), f"Token {t!r} not lowercase"
        assert t.replace('_', '').isalnum(), f"Token {t!r} invalid"
    print('[TOKENS]: Passed')


test()
