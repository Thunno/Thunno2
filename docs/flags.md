# List of flags in Thunno 2

| Flag | Description                                    |
|------|------------------------------------------------|
| `w`  | Enable warnings                                |
| `v`  | Enable verbose mode (tokens)                   |
| `V`  | Verify all test cases                          |
| `C`  | Confirm all test cases                         |
| `e`  | Auto-explain the code (experimental)           |
| `c`  | Auto-fill stack with context rather than input |
| `r`  | Use reversed arguments                         |
| `d`  | Don't pop anything from the stack              |
| `W`  | Take input as one multi-line string            |
| `E`  | Don't evaluate the inputs                      |
| `U`  | Read in code as UTF-8, not Thunno 2 encoding   |
| `Z`  | Preset top of stack to `0`                     |
| `T`  | Preset top of stack to `10`                    |
| `H`  | Preset top of stack to `100`                   |
| `B`  | Convert strings to byte arrays                 |
| `ḃ`  | Convert integers to binary                     |
| `+`  | Increment all input numbers by one             |
| `-`  | Decrement all input numbers by one             |
| `J`  | Join top of stack by nothing at the end        |
| `j`  | Join stack by nothing at the end               |
| `N`  | Join top of stack by newlines at the end       |
| `n`  | Join stack by newlines at the end              |
| `Ṡ`  | Join top of stack by spaces at the end         |
| `ṡ`  | Join stack by spaces at the end                |
| `S`  | Sum top of stack at the end                    |
| `s`  | Sum stack at the end                           |
| `P`  | Push product of top of stack at the end        |
| `p`  | Push product of stack at the end               |
| `L`  | Push length of top of stack at the end         |
| `l`  | Push length of stack at the end                |
| `h`  | Push first item of top of stack at the end     |
| `t`  | Push last item of top of stack at the end      |
| `G`  | Push maximum of top of stack at the end        |
| `M`  | Push minimum of top of stack at the end        |
| `b`  | Boolify top of stack at the end                |
| `!`  | Push logical not of top of stack at the end    |
| `Ḷ`  | Push lowercase of top of stack at the end      |
| `Ṭ`  | Push title case of top of stack at the end     |
| `Ụ`  | Push uppercase of top of stack at the end      |
| `O`  | Force implicit output at the end               |
| `o`  | Disable implicit output at the end             |
| `.`  | Output timings at the end                      |