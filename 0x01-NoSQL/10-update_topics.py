#!/usr/bin/env python3
"""
Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a schooldocument based on the name
    
    args:
        mongo_collection
        name
        topics
    return:
        The number of documents modified.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
