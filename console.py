#!/usr/bin/python3

"""Module that defines HBNBCommand Class"""

import cmd

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

validObjects = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class HBNBCommand(cmd.Cmd):

    """Implementation of HBNBCommand class"""

    prompt = "(hbnb) "
    doc_header = "Documented commands (type help <topic>):"

    def do_EOF(self, line):
        """
    Handles the end of file condition
        """
        print()
        return True

    def do_quit(self, line):
        """
    Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """
    Creates a new instance of the object that
    is passed as an argument
        """
        args = line.split()
        if len(args) > 0:
            if args[0] not in validObjects:
                print("** class doesn't exist **")
            else:
                obj = validObjects[args[0]]()
                obj.save()
                print(obj.id)

        else:
            print("** class name missing **")

    def do_show(self, line):
        """
    Show the object that is passed as an arg
    that have to be writed in the next way:
    <ClassName> <Object id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] not in validObjects:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                str_to_search = args[0] + "." + args[1]
                if str_to_search not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[str_to_search])

    def do_destroy(self, line):
        """
    Deletes the object that is passed as an arg
    that have to be writed in the next way:
    <ClassName> <Object id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] not in validObjects:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                str_to_search = args[0] + "." + args[1]
                if str_to_search not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[str_to_search]
                    storage.save()

    def do_all(self, line):
        """
    Shows all objects of a class if a class name is passed
    otherwise shows all the Objects.
        """
        args = line.split()
        if len(args) > 0:
            if args[0] not in validObjects:
                print("** class doesn't exist **")
            else:
                filtered_list = []
                for k, v in storage.all().items():
                    if k.startswith(args[0]):
                        filtered_list.append(v.__str__())
                print(filtered_list)
        else:
            filtered_list = list(v.__str__() for v in storage.all().values())
            print(filtered_list)

    def do_update(self, line):
        """
    Updates an instance of a class with the next sintax
    update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] not in validObjects:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                str_to_search = args[0] + "." + args[1]
                if str_to_search not in storage.all().keys():
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    argUpdate = args[3]

                    if argUpdate.startswith('"') and argUpdate.endswith('"'):
                        argUpdate = str(argUpdate)
                    elif argUpdate.isalnum() and argUpdate.find('.') == -1:
                        argUpdate = int(argUpdate)
                    else:
                        argUpdate = float(argUpdate)

                    objToUpdate = storage.all()[str_to_search]
                    objToUpdate.__setattr__(args[2], argUpdate)
                    objToUpdate.save()

    def do_emptyline(self):
        """Handles the empty line
        """
        pass


if __name__ == '__main__':
    """Main loop of the console"""
    HBNBCommand().cmdloop()
