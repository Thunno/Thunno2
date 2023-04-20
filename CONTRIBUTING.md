# Contributing to Thunno 2

Although it has already been released, Thunno 2 is still very much a work in progress. You can contribute to Thunno 2 in the following ways:

### 1. Suggesting new commands

We are looking to add new commands into Thunno 2, and it would be much appreciated if you could suggest some new commands.

To suggest a command:
- ping me (`@TheThonnu`) in the [SE chatroom](https://chat.stackexchange.com/rooms/145278/thunno-2)
- or, submit a [new issue](https://github.com/Thunno/Thunno2/issues/new?assignees=&labels=enhancement%2C+request+command&template=command-request.md&title=) in the repository

### 2. Implementing new commands

This is by far the harder option. This would mean actually looking at the chaotic mess which is the Thunno 2 source code and trying to add more code in the right places.

If you do decide to do this though, you can follow these steps:
- fork your own copy of the repository
- add a helper function for your command into [`helpers.py`](https://github.com/Thunno/Thunno2/blob/main/src/thunno2/helpers.py)
- if you're feeling especially brave, suggest some test cases for your commands as well \
  (these will eventually be added to [`tests.py`](https://github.com/Thunno/Thunno2/blob/main/src/thunno2/tests.py))
- then, create a [pull request](https://github.com/Thunno/Thunno2/pulls), and we'll review your changes
- if we approve them, your code will get added to the main repository!
