from thunno2 import interpreter, commands, helpers
import re


def process_input_flags(flags, inputs):
    if "w" in flags:
        commands.ctx.warnings = True

    if "W" in flags:
        inputs = [inputs]
    else:
        inputs = inputs.splitlines()

    if "E" not in flags:
        new_input = []
        for inp in inputs:
            try:
                x = eval(inp)
                if type(x) in (int, float, str, list):
                    new_input.append(x)
                elif isinstance(x, bool):
                    new_input.append(int(x))
                elif isinstance(x, (set, tuple)):
                    new_input.append(list(x))
                elif isinstance(x, dict):
                    new_input.append(list(map(list, x.items())))
                else:
                    new_input.append(inp)
            except:
                new_input.append(inp)
        inputs = new_input[:]

    for flag in flags:
        if flag == "Z":
            commands.ctx.stack.push(0)
        elif flag == "T":
            commands.ctx.stack.push(10)
        elif flag == "H":
            commands.ctx.stack.push(100)

    if "B" in flags:
        new_input = []
        for inp in inputs:
            if isinstance(inp, str):
                new_input.append([ord(c) for c in inp])
            else:
                new_input.append(inp)
        inputs = new_input[:]

    if "+" in flags:
        new_input = []
        for inp in inputs:
            if isinstance(inp, (int, float)):
                new_input.append(inp + flags.count("+"))
            else:
                new_input.append(inp)
        inputs = new_input[:]

    if "-" in flags:
        new_input = []
        for inp in inputs:
            if isinstance(inp, (int, float)):
                new_input.append(inp - flags.count("-"))
            else:
                new_input.append(inp)
        inputs = new_input[:]

    if "c" in flags:
        commands.ctx.vyxal_mode = True

    return inputs


def process_output_flags(flags, do_print=True):
    for flag in flags:
        if "J" == flag:
            commands.ctx.stack.push(helpers.empty_join(next(commands.ctx.stack.rmv(1))))

        if "j" == flag:
            commands.ctx.stack.push(helpers.empty_join(list(commands.ctx.stack)))

        if "N" == flag:
            commands.ctx.stack.push(
                helpers.newline_join(next(commands.ctx.stack.rmv(1)))
            )

        if "n" == flag:
            commands.ctx.stack.push(helpers.newline_join(list(commands.ctx.stack)))

        if "Ṡ" == flag:
            commands.ctx.stack.push(helpers.space_join(next(commands.ctx.stack.rmv(1))))

        if "ṡ" == flag:
            commands.ctx.stack.push(helpers.space_join(list(commands.ctx.stack)))

        if "S" == flag:
            commands.ctx.stack.push(commands.commands["S"]()[0])

        if "s" == flag:
            commands.ctx.stack.push(helpers.it_sum(commands.ctx.stack))

        if "L" == flag:
            commands.ctx.stack.push(commands.commands["l"]()[0])

        if "l" == flag:
            commands.ctx.stack.push(len(commands.ctx.stack))

        if "h" == flag:
            commands.ctx.stack.push(commands.commands["h"]()[0])

        if "t" == flag:
            commands.ctx.stack.push(commands.commands["t"]()[0])

        if "B" == flag:
            x = (commands.ctx.stack + commands.ctx.other_il + [0])[0]
            if isinstance(x, list):
                r = ""
                for i in x:
                    try:
                        r += chr(int(i))
                    except:
                        pass
                commands.ctx.stack.push(r)

        if "G" == flag:
            commands.ctx.stack.push(commands.commands["G"]()[0])

        if "M" == flag:
            commands.ctx.stack.push(commands.commands["M"]()[0])

        if "b" == flag:
            commands.ctx.stack.push(commands.commands["ɓ"]()[0])

        if "!" == flag:
            commands.ctx.stack.push(commands.commands["¬"]()[0])

        if "Ḷ" == flag:
            a = next(commands.ctx.stack.rmv(1))
            if isinstance(a, str):
                commands.ctx.stack.push(a.upper())
            else:
                commands.ctx.stack.push(a)

        if "Ṭ" == flag:
            a = next(commands.ctx.stack.rmv(1))
            if isinstance(a, str):
                commands.ctx.stack.push(a.title())
            else:
                commands.ctx.stack.push(a)

        if "Ụ" == flag:
            a = next(commands.ctx.stack.rmv(1))
            if isinstance(a, str):
                commands.ctx.stack.push(a.upper())
            else:
                commands.ctx.stack.push(a)

    if do_print:
        do_printing(flags)


def do_printing(flags):
    if (commands.ctx.implicit_print or ("O" in flags)) and not ("o" in flags):
        print(next(commands.ctx.stack.rmv(1)))


def run(flags, code, inputs):
    if "V" in flags:
        new_flags = "".join(f for f in flags if f != "V")
        for line in inputs.splitlines():
            try:
                x = eval(line)
                if isinstance(x, tuple):
                    new_inputs = process_input_flags(new_flags, "\n".join(map(repr, x)))
                else:
                    new_inputs = [x]
            except:
                new_inputs = [line]
            commands.ctx.og_input_list = new_inputs.copy()
            commands.ctx.other_il = new_inputs.copy()
            print(line, "--> ", end="")
            interpreter.run(code, context=0, iteration_index=0)
            process_output_flags(new_flags)
        return None

    elif "C" in flags:
        new_flags = "".join(f for f in flags if f != "C")
        for l in inputs.splitlines():
            m = re.match(r"(.+) ?(?:=>|-+>) ?(.+)", l)
            try:
                line, output = m[1], m[2]
                try:
                    x = eval(line)
                    if isinstance(x, tuple):
                        new_inputs = process_input_flags(
                            new_flags, "\n".join(map(repr, x))
                        )
                    else:
                        new_inputs = [x]
                except:
                    new_inputs = [line]
                try:
                    expected = process_input_flags("", output)[0]
                except:
                    expected = output.strip()
            except Exception as e:
                print(f"FAIL ❌ (Got error {e})")
                continue
            commands.ctx.og_input_list = new_inputs.copy()
            commands.ctx.other_il = new_inputs.copy()
            commands.ctx.stack = commands.Stack()
            print(line, "--> ", end="")
            interpreter.run(code, context=0, iteration_index=0)
            process_output_flags(new_flags, False)
            actual_output = next(commands.ctx.stack.rmv(1))
            print(actual_output, end="\t")
            if actual_output == expected:
                print("PASS ✅")
            else:
                print(f"FAIL ❌ (Expected {expected})")
        return None

    inputs = process_input_flags(flags, inputs)
    commands.ctx.og_input_list = inputs.copy()
    commands.ctx.other_il = inputs.copy()
    interpreter.run(code, context=0, iteration_index=0)
    process_output_flags(flags)
