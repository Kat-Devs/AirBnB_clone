#!/usr/bin/python3
'''
Entry point for HBNBCommand intepreter
'''

import cmd
from models import *
from models.base_model import BaseModel
from models import storage

class_dict = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):
    '''
    Command Intepreter Class
    '''
    prompt = '(hbnb) '

    def do_quit(self, args):
        '''Quit command to exit program'''
        return True
    
    def do_EOF(self, args):
        '''EOF command to exit the program'''
        print()
        return True
    
    def emptyline(self):
        '''Do nothing on empty line'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel'''
        if not arg:
            print('** class name missing **')
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in class_dict:
            print('** class does not exist **')
            return
        instance = class_dict[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        '''Prints string representation of an instance'''
        if not arg:
            print("** class doesn't exist **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing')
            return
        instance_id = args[1]
        key = f'{class_name}.{instance_id}'
        instances = storage.all()
        if key not in instances:
            print('** no instance found **')
            return
        print(instances[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if len(args) == 0:
            instances = storage.all()
        else:
            class_name = args[0]
            if class_name not in class_dict:
                print("** class doesn't exist **")
                return
            instances = storage.all(class_name)
        print([str(instance) for instance in instances.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

if __name__ == '__main__':
    HBNBCommand().cmdloop()