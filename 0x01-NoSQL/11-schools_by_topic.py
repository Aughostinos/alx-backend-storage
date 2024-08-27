#!/usr/bin/env python3
"""
task 11. Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """ a Python function that returns the
    list of school having a specific topic"""
    result = list(mongo_collection.find({ "topics": topic}))
    return result