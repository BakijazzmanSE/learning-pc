#!/usr/bin/python3
"""import modules here """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """command line intereaction """

    prompt = "HBNB "
    __classes = ["BaseModel",
                 "User", 
                 "State", 
                 "City", 
                 "Place", 
                 "Amenity", 
                 "Review"
                 ]

    def do_quit(self, arg):
        """quit function for the console
        """
        return True
    def do_EOF(self, arg):
        """ Ctrl D quits the console
        """
        return True
    def emptyline(self):
        """action when no command is entered """
        return
    def do_create(self, arg):
        """creats a new instance of base model and saves it as a json file
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** Class does not exist **")
        else:
            new_object = eval(f'{args[0]}')()
            print(new_object.id)

    def do_show(self, arg):
        """show all classes of the arguement given"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesnt exist **")
        elif len(args) == 1:
            print("** Instance Id Missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** instance not found **")
        else:
            db = storage.all()
            print(db[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("**class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesnt exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** Instance Not Found **")
        else:
            db = storage.all()
            key = f"{args[0]}.{args[1]}"
            del db[key]
            print(f"** deleted {key} from database **")
        storage.save()

    def do_all(self, arg):
        args = arg.split()
        if len(args) == 0:
            for value in storage.all().values():
                print(str(value))
        elif args[0] not in self.__classes:
            print("** class doesnt exist **")
        else:
            db = storage.all()
            key =  f"{args[0]}"
            for k, v in db.items():
                if k.startswith(key):
                    print(str(v))
    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesnt exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_class = args[0]
            obj_id = args[1]
            key = f"{obj_class}.{obj_id}"
            obj = storage.all()[key]
            attr_name = args[2]
            attr_value = args[3]
            if attr_value[0] == '"':
                attr_value = attr_value[1:-1]

            if hasattr(obj, attr_name):
                type_ = type(getattr(obj, attr_name))
                if type_ in [str, float, int]:
                    attr_value = type_(attr_value)
                    setattr(obj, attr_name, attr_value)
            else:
                setattr(obj, attr_name, attr_value)
            storage.save()





if __name__ == "__main__":
    HBNBCommand().cmdloop()

