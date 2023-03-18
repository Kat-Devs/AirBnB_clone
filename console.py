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

    def do_create(self, arg):
        """Creates a new instance of a BaseModel"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        try:
            cls = models.__dict__[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            cls = models.__dict__[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key = "{}.{}".format(cls.__name__, instance_id)
        if key in models.storage.all(cls):
            instance = models.storage.all(cls)[key]
            print(instance)
        else:
            print

if __name__ == '__main__':
    HBNBCommand().cmdloop()