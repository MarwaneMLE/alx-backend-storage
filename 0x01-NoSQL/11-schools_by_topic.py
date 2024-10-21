#!/usr/bin/env python3
""" task 11. Where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [doc for doc in documents]
    return list_docs
