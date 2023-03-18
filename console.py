#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import shlex
import models



class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not args:
            print("** class name missing **")
            return
        try:
            cls = getattr(models, args)
        except AttributeError:
            print("** class doesn't exist **")
            return
        instance = cls()
        instance.save()
        print(instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()