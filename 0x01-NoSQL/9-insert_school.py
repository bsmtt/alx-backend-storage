#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

def insert_school(mongo_collection, **kwargs):
    """ insert and return _id """
    id = mongo_collection.insert(kwargs)
    return id;
