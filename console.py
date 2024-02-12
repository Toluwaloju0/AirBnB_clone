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
        if len(sys.argv) == 2:
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return
        model = BaseModel()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
