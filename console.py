#!/usr/bin/python3
"""A module which serves as the command intepreter"""

import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """A class of the command line"""

    prompt = '(hbnb)'

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """A function To handle the EOF action
        Args:
            line: a system default variable
        """

        return True

    def do_quit(self, arg):
        'To close the shell'
        quit()
        return True

    def do_create(self, line):
        'To create a new class of BaseModel'
        if not line:
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return
        model = BaseModel()
        model.save()
        print(model.id)

    def do_show(self, line):
        'Prints the string representation of an instance based \
        on the class name and id'
        if not line:
            print('** class name missing **')
            return
        line = line.split()
        if line[0] != 'BaseModel':
            print('** class doesn\'t exist **')
            return
        if not line[1]:
            print("** instance id missing **")
            return
        my_dict = strorage.all()
        for key in my_dict:
            a = key.split('.')
            if a[1] == line[1]:
                print(a[0])
                return
            continue
        print("** no instance found **")

    def do_destroy(self, line):
        if not line:
            print('** class name missing **')
            return
        line = line.split()
        if line[0] != 'BaseModel':
            print('** class doesn\'t exist **')
            return
        if not line[1]:
            print("** instance id missing **")
            return
        my_dict = strorage.all()
        for key in my_dict:
            a = key.split('.')
            if a[1] == line[1]:
                del (key)
                return
            continue
        print("** no instance found **")
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
