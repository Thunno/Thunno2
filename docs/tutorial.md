# Thunno 2 tutorial

## 1. The stack

Thunno 2's "stack" is just a list of items which have been referenced in the program. You can push items to the stack, or pop items from the stack. <!-- You can even rotate and reverse the stack! 
 TODO -->

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

List work just like in Python. Anything between a `[` and `]` is pushed as a list.

For example:

* `[1,2,3,4]` pushes [1, 2, 3, 4]
* `['abc', 123, "def"]` pushes ['abc', 123, 'def']

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
