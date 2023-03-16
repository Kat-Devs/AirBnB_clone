#!/usr/bin/python3
'''
HBNBCommand intepreter
'''

import cmd


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
        return True
    
    def emptyline(self):
        '''Do nothing on empty line'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()