#!/usr/bin/python3

"""FileStorage class declaration"""

import json

class FileStorage():

    """Declaration of base class"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Method that returns all the objects"""
        return self.__objects

    def new(self, obj):
        """Method that adds a new object to the objects dict"""
        self.all()[f"{type(obj).__name__}.{obj.id}"] = obj
    
    def save(self):
        """Method that serializes the objects dict and dumps it"""
        with open(self.__file_path, "w") as f:
            obj_dict_repr = {}
            for k, obj in self.all().items():
                obj_dict_repr[k] = obj.to_dict()
            json.dump(obj_dict_repr, f, indent=4)
    
    def reload(self):
        """Method that reloads the serialized objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                from models.amenity import Amenity
                from models.base_model import BaseModel
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User

                correspondences = {
                    "Amenity" : Amenity,
                    "BaseModel" : BaseModel,
                    "City" : City,
                    "Place" : Place,
                    "Review" : Review,
                    "State" : State,
                    "User" : User
                }

                for key, obj in obj_dict.items():
                    correct_class = correspondences[obj['__class__']]
                    self.new(correct_class(**obj))

        except FileNotFoundError:
            pass
