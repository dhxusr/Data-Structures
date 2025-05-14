
"""
A simple text editor that stores and displays a string of character using the positional list ADT, together
with a cursor object that highlights a position in this string. A simple interface is to print the string and
then to use a second line of output to underline the position of the cursor.


Text editor:
- left: move the cursor left one character (do nothing if at beginning).
- right: move the cursor right one character (do nothing if at end).
- insert c: Insert the character c just after the cursor.
- delete: delete the character at the position of the cursor (do nothing at end).
- print: print the characters in the editor and print the cursor.

Cursor:
- keep a position as its current position.
"""

from __future__ import annotations
from dataclasses import dataclass
from positional_list import Position, PositionalList


class TextEditor:


    @dataclass
    class Cursor:
        position: Position | None = None


    def __init__(self) -> None:

        self._string = PositionalList()
        self._cursor = self.Cursor()

    def __str__(self) -> str:

        string = "".join(
            char for char in self._string
        )
        return string


    def _move_cursor(self, side: str) -> None:
        """Move the cursor to left or right."""

        if (self._cursor.position is None or
            self._cursor.position == self._string.first() and side == "left" or
            self._cursor.position == self._string.last() and side == "right"):
            return

        if side == "left":
            self._cursor.position = self._string.before(self._cursor.position)

        if side == "right":
            self._cursor.position = self._string.after(self._cursor.position)


    def print_cursor(self):
        """return a string with '-' below the character at the position of the cursor."""

        if not self._string.is_empty():

            current_position = self._string.first()
            while current_position != self._cursor.position:
                print(' ', end='')
                current_position = self._string.after(current_position)

        print('-')

        
    def left(self):
        """Move the cursor one position to the left."""    

        self._move_cursor("left")


    def right(self):
        """Move the cursor one position to the right."""

        self._move_cursor("right")


    def insert(self, char):
        """Insert char just after the position of the cursor.
        move the cursor to the position of the new character."""

        if self._cursor.position is None:
            self._cursor.position = self._string.add_first(char)

        else:
            self._cursor.position = self._string.add_after(
                                        self._cursor.position,
                                        char
                                    )


    def delete(self):
        """Delete the character at cursor's position.
        move the cursor one position to the left."""

        if self._string.is_empty():
            return

        position_to_delete = self._cursor.position
        self._move_cursor("left")
        self._string.delete(position_to_delete)

        try:
            #validate position to know if the deleted element was the first.
            # if the element to delete is the first, move_cursor method doesn't move the cursor
            # delete method of the Positional List deprecates the position.
            self._string._validate_position(self._cursor.position)

        except ValueError:
            # if the string is empty. first is None
            self._cursor.position = self._string.first()
