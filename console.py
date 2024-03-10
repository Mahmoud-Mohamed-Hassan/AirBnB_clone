#!/usr/bin/python3
"""cmd module to make command interpreter"""


import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """

    prompt = "(hbnb) "
    list_of_classes = ["BaseModel", "User",
                       "City", "State", "Amenity", "Review", "Place"]
    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True

    def help_quit(self, arg):
        """ """
        print("quit command to exit the program")

    def do_create(self, arg):
        """Creates a new instance"""

        if arg:
            if arg not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            else:
                instance = eval(f"{arg}()")
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, linee):
        """Prints the string representation of \
            an instance based on the class name and id"""

        if linee:
            list_linee = linee.split(" ")
            if list_linee[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_linee) == 1:
                print("** instance id missing **")
            elif list_linee[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_linee[0]}.{list_linee[1]}" == key:
                        print(value)
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")
    def do_destroy(self, linee):
        """Deletes an instance based on the class name and id"""

        if linee:
            list_linee = linee.split(" ")
            if list_linee[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_linee) == 1:
                print("** instance id missing **")
            elif list_linee[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_linee[0]}.{list_linee[1]}" == key:
                        del dic[key]
                        storage.save()
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")
            
    def do_all(self, linee):
        """Prints all string representation of all\
            instances based or not on the class name"""

        new_listt = []
        dic = storage.all()
        for value in dic.values():
            new_listt.append(str(value))
        if linee:
            if linee not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            else:
                print(new_listt)
        else:
            print(new_listt)
            
    def do_update(self, linee):
        """Updates an instance based on the class name and id"""

        list_linee = linee.split(" ")
        if linee:
            list_linee = linee.split(" ")
            if list_linee[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_linee) == 1:
                print("** instance id missing **")
            elif list_linee[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_linee[0]}.{list_linee[1]}" == key:
                        if len(list_linee) == 2:
                            print("** attribute name missing **")
                            flag = 1
                        elif len(list_linee) == 3:
                            print("** value missing **")
                            flag = 1
                        else:
                            if list_linee[3][0] == '"':
                                atr_value = list_linee[3][1:-1]
                            else:
                                if list_linee[3].isdigit():
                                    atr_value = int(list_linee[3])
                                else:
                                    atr_value = list_linee[3]
                            setattr(value, list_linee[2], atr_value)
                            storage.save()
                            flag = 1
                            break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
