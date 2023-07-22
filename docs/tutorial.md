# Thunno 2 tutorial

## 1. The stack

Thunno 2's "stack" is just a list of items which have been referenced in the program. You can push items to the stack, or pop items from the stack. You can even rotate and reverse the stack!

## 2. Numbers

To push a number to the stack, just write it.

For example:

* `1` pushes 1
* `1.23` pushes 1.23
* `.456` pushes 0.456

## 3. Mathematical operations

Thunno 2 has normal mathematical operations: `+`, `-`, `×`, `/`.

These go **after** the operands.

For example:

* `1 2+` pushes 3
* `4.56 1-` pushes 3.56
* `12 3×` pushes 36
* `20 4/` pushes 5

(Note that there needs to be a space between two numbers so the interpreter knows they are separate from each other.)

## 4. Strings

Strings in Thunno 2 start and end with double quotes (`"`). You can include double quotes inside strings as long as they have a backslash (`\`) before them.

For example:

* `"abc"` pushes abc
* `"\"Thunno\""` pushes "Thunno"

Strings can be concatenated using `+`. A string can be concatenated to another string, or a number:

* `"abc""def"+` pushes abcdef
* `123"abc"+` pushes 123abc

## 5. Lists

Anything between a `[` and `]` is pushed as a list. Elements are separated by `;` and are evaluated as Thunno 2 code.

For example:

* `[1;2;3;4]` pushes [1, 2, 3, 4]
* `["abc"; 123.456; 'x]` pushes ["abc", 123, "x"]
* `[1; [2; [3; [4]]]]` pushes [1, [2, [3, [4]]]]

## 6. Vectorisation

Thunno 2 can do operations on lists without needing loops. This is called "vectorisation".

For example:

* `[1, 2, 3] 2 +` pushes [3, 4, 5]
* `10 [1, 2, 5, 10] /` pushes [10.0, 5.0, 2.0, 1.0]

This works with lists on both sides as well:

* `[1, 2, 3] [4, 5, 6] +` pushes [5, 7, 9]
* `[2, 3, 4] [10, 20, 30] ×` pushes [20, 60, 120]

And nested lists:

* `[50, [100, [200], 400], 800] 10 -` pushes [40, [90, [190], 390], 790]
* `[[[[[10], 11], 12], 13], 14] [[1, 2], 3] +` pushes [[[[[11], 12], 13], 15, 17]]

## 7. Input

If you were asked to write a Thunno 2 program to take two inputs, add them together, and print the result, you might write something like this:

```python
$$+£
```

Explanation:

```python
$     # Push first input
 $    # Push second input
  +   # Add them together
   £  # Print the result
```

But Thunno 2 has implicit input, meaning that the `$`s can be omitted:

```python
+£
```

Explanation:

```python
    # Implicit inputs pushed to the stack
+   # Add them together
 £  # Print the result
```

## 8. Output

Thunno 2 also has implicit output, meaning that the last thing pushed to the stack is output automatically at the end, so the `£` is not necessary:

```python
+
```

Explanation:

```python
   # Implicit inputs pushed to the stack
+  # Add them together
   # Implicit output of the result
```

Note that if you use explicit printing (`£`), the implicit output will be disabled.

## 9. Overloading

Thunno 2 uses type overloading, which means that some commands behave differently when passed different types. For example, the [`C` command](https://github.com/Thunno/Thunno2/blob/main/docs/commands.md#c-chr--ord) is `chr` when given a number and `ord` when given a string. All overloads are documented in [`commands.md`](https://github.com/Thunno/Thunno2/blob/main/docs/commands.md).

## 10. Loops (1)

While vectorisation will help you with lists, it won't be what you need all the time. So, Thunno 2 has FOR, WHILE, FOREVER, and MAP loops.

A `for` loop looks like this:

```
{ CODE }
```

A `while` loop looks like this:

```
( CONDITION ; BODY )
```

A `forever` loop looks like this:

```
⁽ CODE ⁾
```

A `map` loop looks like this:

```
ı CODE ;
```

## 11. Loops (2)

Alright, but what do those loops actually do?

A `for` loop can do two different things:

* If given a string or a list, it executes `CODE` with each item of that string or list
* If given a number, it executes `CODE` that many times

A `while` loop does this:

* Until `CONDITION` returns False, execute `BODY`

A `forever` loop does this:

* Forever, execute `CODE`

A `map` loop does this:

* For each item of the given object, it executes `CODE` and collects all the results in a list

(Note: if given a number, `map` will convert it to a range.)

## 12. Other structures (1)

This is `filter`:
  
* <pre><code>æ CONDITION ;</code></pre>

* This only keeps items from the given object if `CONDITION` returns True.

This is `sort by`:

* <pre><code>Þ CODE ;</code></pre>

* This sorts the object by the result of `CODE`.

This is `group by`:

* <pre><code>Ñ CODE ;</code></pre>

* This groups items of the object for which `CODE` has the same result together.

## 13. Other structures (2)

`filter`, `sort by`, and `group by` all also have single-function versions. They take only one command and require no closing delimiter.

They are `œ`, `þ`, and `ñ` respectively.

## 14. Challenges

You are now ready for your first Thunno 2 challenge!

*(Challenges coming soon)*