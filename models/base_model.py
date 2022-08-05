#!/usr/bin/python3
"""Contains the Base class for the AirBnB clone console"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Class for base model"""

    def __init__(self, *args, **kwargs):
        """Takes args and kwargs
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute \
            updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all \
            keys/values of __dict__ of the instance: """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
