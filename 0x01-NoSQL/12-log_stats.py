#!/usr/bin/env python3
"""
task 12. Log stats
"""
from pymongo import MongoClient


def log_stats():
    """ provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://localhost:27017/')
    nginx_collection = client.logs.nginx

    #first line: x logs where x is the number of documents
    logs_num = nginx_collection.count_documents({})
    print(f"{logs_num} logs")

    # documents number by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents(
            { "method": method }
        )
        print(f"\tmethod {method}: {method_count}")

    #one line with the number of documents with method=GET path=/status
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_check} status check")