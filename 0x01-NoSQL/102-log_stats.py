#!/usr/bin/env python3
"""
task 15. Log stats - new version
"""


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

    # top 10 Ips
    print("IPs:")
    ips = [
        { "$group": {"_id": "$ip", "count": {"$sum": 1 }}},
        { "$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_10_ips = nginx_collection.aggregate(ips)
    for ip in top_10_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()