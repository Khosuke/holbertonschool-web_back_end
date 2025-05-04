#!/usr/bin/env python3
"""
This script connects to a local MongoDB instance and analyzes logs
stored in the 'nginx' collection of the 'logs' database.

It prints:
- The total number of logs
- The count of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
- The number of logs that are 'GET' requests to the '/status' path
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}

    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        method_counts[method] = count

    nb_logs = nginx_collection.count_documents({})
    print(f"{nb_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    nb_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{nb_status} status check")
