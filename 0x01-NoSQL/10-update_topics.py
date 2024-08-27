#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def update_topics(mongo_collection, name, topics):
    """ Changes  document based on the name """
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many({"name": name}, new_values)
