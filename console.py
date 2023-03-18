#!/usr/bin/python3
"""Defines the HBNBCommand class."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
