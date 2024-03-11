#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ """

    __file__path = "file.json"
    __objects = {}

    def new(self, obj):
        """ """
        obj_class_name = obj.__class__.__name__
        Name_ID_key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[Name_ID_key] = obj

    def all(self):
        """
        return all objects
        """
        all_objects = FileStorage.__objects
        return all_objects

    def save(self):
        """
        serializes __objects to the JSON file
        """
        all_objects = FileStorage.__objects
        object_dict = {}
        for object in all_objects.keys():
            object_dict[object] = all_objects[object].to_dict()
        filePath = FileStorage.__file__path
        with open(filePath, "w", encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        all_objects = FileStorage.__objects
        filePath = FileStorage.__file__path
        if os.path.isfile(filePath):
            with open(filePath, "r", encoding="utf-8") as file:
                try:
                    object_dict = json.load(file)
                    for key, value in object_dict.items():
                        class_name, object_ID = key.split(".")

                        class_i = eval(class_name)
                        instance_i = class_i(**value)
                        all_objects[key] = instance_i
                except Exception:
                    pass
