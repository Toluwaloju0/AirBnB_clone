#!/usr/bin/python3
"""A module which serves as the command intepreter"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage
import json


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
        if len(line) != 2:
            print("** instance id missing **")
            return
        my_dict = storage.all()
        for key in my_dict.keys():
            a = key.split('.')
            if line[1] == a[1]:
                print(my_dict[key])
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
        if len(line) != 2:
            print("** instance id missing **")
            return
        my_dict = {}
        with open("file.json", mode='r', encoding='utf-8') as a:
            my_dict = json.loads(a.read())
        for key in my_dict.keys():
            a = key.split('.')
            if a[1] == line[1]:
                del (my_dict[key])
                with open("file.json", mode='w', encoding='utf-8') as a:
                    a.write(json.dumps(my_dict))
                storage.reload()
                return
            continue
        print("** no instance found **")

    def do_all(self, line):
        if len(line) == 0 or line == "BaseModel":
            my_dict = storage.all()
            for key in my_dict.keys():
                print(my_dict[key])
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
