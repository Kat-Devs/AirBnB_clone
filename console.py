#!/usr/bin/python3
"""Module for HBNB command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for AirBnB project."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing if an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to JSON file, and print the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                storage.save()

    def do_all(self, arg):
        """Print all string representations of instances based or not on the class name."""
        objects = []
        if not arg:
            for key in storage.all():
                objects.append(str(storage.all()[key]))
            print(objects)
        elif arg not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        else:
            for key in storage.all():
                if key.split('.')[0] == arg:
                    objects.append(str(storage.all()[key]))
            print(objects)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in self.storage.all():
            print("** no instance found **")
            return
        obj = self.storage.all()[key]
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()