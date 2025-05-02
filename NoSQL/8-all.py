#!/usr/bin/env python3
"""
This module provide one function that
list all document in a MongoDB collection
"""

from typing import Collection, List


def list_all(mongo_collection: Collection) -> List:
    """
    Lists all documents in a MongoDB collection
    Args:
        mongo_collection: The PyMongo collection object
    Returns:
        List of documents in the collection
        Returns an empty list if no documents are found
    """
    return list(mongo_collection.find())
