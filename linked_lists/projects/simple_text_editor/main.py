import text_editor as txte
from os import system

def main():
    txt_editor = txte.TextEditor()

    move_to_left_cmmds = ['l', "left"]
    move_to_right_cmmds = ['r', "right"]
    insert_commands = ['i', "insert"]
    delete_commands = ['d', "delete"]
    quit_commands = ['q', "quit", 'e', "exit"]

    while True:

        system("clear")
        print(txt_editor)
        txt_editor.print_cursor()

        command = input("Command: ").lower()

        if command in move_to_left_cmmds:
            txt_editor.left()

        elif command in move_to_right_cmmds:
            txt_editor.right()

        elif command in insert_commands:
            char = input("character: ")
            txt_editor.insert(char)

        elif command in delete_commands:
            txt_editor.delete()

        elif command in quit_commands:
            break


if __name__ == "__main__":
    main()
