#!/usr/bin/env python3
"""
Task 9. Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    add_document = mongo_collection.insert_many(kwargs)
    return add_document.inserted_id