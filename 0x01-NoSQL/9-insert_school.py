#!/usr/bin/env python3
"""
Task 9
"""


def insert_school(mongo_collection, **kwargs):
    """ unction that inserts a new document in a collection based on kwargs"""
    document_id = mongo_collection.insert(kwargs)
    return document_id
