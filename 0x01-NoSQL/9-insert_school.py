#!/usr/bin/env python3
"""
Task 9. Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """a Python function that inserts a new document
    in a collection based on kwargs"""
    add_document = mongo_collection.insert_one(kwargs)
    return add_document.inserted_id
