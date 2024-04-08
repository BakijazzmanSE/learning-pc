#!/usr/bin/env python3
"""Importy modules here"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

class FileStorage():
    """serialition of the dictionary from the basemodel"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with the key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """save the iso format copy to the file """
        with open (self.__file_path, "w", encoding="utf-8") as f:
            string = {k : v.to_dict() for k, v in self.__objects.items()}
            json.dump(string, f)

    def reload(self):   
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    self.new(eval(f"{cls_name}")(**o))
        except FileNotFoundError:
            return

