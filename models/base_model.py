#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        ISO_time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:  # takes kwargs from dict
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, ISO_time_format))
                else:  # kwargs is id
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        """ """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.created_at.isoformat()

        return instance_dict

    def __str__(self):
        """ """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
