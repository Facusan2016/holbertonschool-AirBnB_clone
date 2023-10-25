#!/usr/bin/python3

"""Module that defines HBNBCommand Class"""

import cmd


class HBNBCommand(cmd.Cmd):

    """Implementation of HBNBCommand class"""

    prompt = "(hbnb) "
    doc_header = "Documented commands (type help <topic>):"

    def do_EOF(self, line):
        """Handles the end of file condition
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Handles the empty line
        """
        pass


if __name__ == '__main__':
    """Main loop of the console"""
    HBNBCommand().cmdloop()
