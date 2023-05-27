from thunno2 import lexer, version, flags, tokens, autoexplanation, codepage
import sys, time


def from_terminal():
    print("Thunno", version.THUNNO_VERSION, "interpreter\n")
    print("\nFlags:")
    flags_list = input()
    code = ""
    print("\nHeader:")
    inp = input()
    while inp:
        code += inp + "\n"
        inp = input()
    print("\nCode:")
    inp = input()
    while inp:
        code += inp + "\n"
        inp = input()
    print("\nFooter:")
    inp = input()
    while inp:
        code += inp + "\n"
        inp = input()
    inputs = ""
    print("\nInput:")
    inp = input()
    while inp:
        inputs += inp + "\n"
        inp = input()
    if "U" in flags_list:
        code = codepage.utf8_to_thunno2(code)
    if "." in "".join(flags_list):
        start_time = time.time()
    if "v" in flags_list:
        transpiled = tokens.transpile(code)
        print("\nTranspiled:")
        print(transpiled)
        print()
        _, tokenised = lexer.tokenise(transpiled)
    else:
        _, tokenised = lexer.tokenise(code)
    if "." in "".join(flags_list):
        lexed_time = time.time()
    if "e" in flags_list:
        print(
            "\nExplanation:\n\n"
            + autoexplanation.auto_explain(tokenised, tkn=False)
            + "\n"
        )
    print("\nOutput:")
    flags.run(flags_list, tokenised, inputs)
    if "." in "".join(flags_list):
        end_time = time.time()
        times = [
            (lexed_time - start_time) * 1000,
            (end_time - lexed_time) * 1000,
            (end_time - start_time) * 1000,
        ]
        print("\nTimings:")
        print(f"Lexer: {times[0]:.3f}ms")
        print(f"Program: {times[1]:.3f}ms")
        print(f"Total: {times[2]:.3f}ms\n")


def from_cmdline():
    args = sys.argv[1:]
    if not args:
        from_terminal()
        return None
    filename = args[0]
    flags_list = args[1:]
    sys.stderr.write("Thunno, v" + version.THUNNO_VERSION + "\n")
    try:
        with open(filename) as f:
            code = f.read()
            if "U" in "".join(flags_list):
                code = codepage.utf8_to_thunno2(code)
            if "." in "".join(flags_list):
                start_time = time.time()
            if "v" in "".join(flags_list):
                transpiled = tokens.transpile(code)
                print("Transpiled:", transpiled, file=sys.stderr)
                _, tokenised = lexer.tokenise(transpiled)
            else:
                _, tokenised = lexer.tokenise(code)
            if "." in "".join(flags_list):
                lexed_time = time.time()
            if "e" in "".join(flags_list):
                sys.stderr.write(
                    "\nExplanation:\n\n"
                    + autoexplanation.auto_explain(tokenised, tkn=False)
                    + "\n"
                )
            flags.run("".join(flags_list), tokenised, sys.stdin.read())
            if "." in "".join(flags_list):
                end_time = time.time()
                times = [
                    (lexed_time - start_time) * 1000,
                    (end_time - lexed_time) * 1000,
                    (end_time - start_time) * 1000,
                ]
                sys.stderr.write(
                    f"\nTimings:\nLexer: {times[0]:.3f}ms\nProgram: {times[1]:.3f}ms\nTotal: {times[2]:.3f}ms\n"
                )
    except Exception as E:
        sys.stderr.write("An error occurred: " + repr(E))
