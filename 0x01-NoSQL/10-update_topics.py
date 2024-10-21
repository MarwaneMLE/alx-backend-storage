#!/usr/bin/env python3
"""
Task: 10. Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)