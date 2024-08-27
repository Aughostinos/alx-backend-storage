#!/usr/bin/env python3
"""
Task 8. List all documents in Python
"""

def list_all(mongo_collection):
    """Lists all documents in a collection."""
    documents = list(mongo_collection.find())
    return documents
