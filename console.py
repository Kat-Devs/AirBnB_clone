#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


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

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()