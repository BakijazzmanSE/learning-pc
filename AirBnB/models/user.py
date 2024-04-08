#!/usr/bin/python3
"""Import Modules Here """
from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
