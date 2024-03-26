#!/usr/bin/env python3
"""
Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a
    collection based on kwargs

    args:
        mongo_collection
        **kwargs
    return:
        The _id of the newly inserted document.
    """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
