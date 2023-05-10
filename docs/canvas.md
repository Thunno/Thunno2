# Thunno 2 Canvas

<sup><sub><i>(Inspired by [05AB1E's](https://codegolf.stackexchange.com/a/175520/114446) 
and [Vyxal's](https://github.com/Vyxal/Vyxal/blob/main/documents/specs/Canvas.md) canvases.)</i></sup></sub>

The Canvas takes a string of text and a list of directions. These are the directions:

$$
\begin{array}{l}
    7 & & 0 & & 1 \\
      & \nwarrow & \uparrow & \nearrow & \\
    6 & \leftarrow & \bullet & \rightarrow & 2 \\
      & \swarrow & \downarrow & \searrow & \\
    5 & & 4 & & 3
\end{array}
$$

<sup><sub><i>(MathJax stolen from [this answer](https://codegolf.stackexchange.com/a/181844/114446)
on Code Golf Stack Exchange)</i></sup></sub>

* The canvas is essentially a list of lines of text. It starts out empty, but expands as needed.

* For each character, you provide a direction to move before adding that character to the canvas.

* There is only one canvas. You can add to it with the `ø^` command, and clear it with the `øv` command.

The canvas command (`ø^`) takes two arguments:

* a string of text
* a list of integer directions \
  (this can also be an integer which is interpreted as a digit list)