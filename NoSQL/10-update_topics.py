#!/usr/bin/env python3
"""
This module provides a function to update the 'topics' field
for all documents in a MongoDB collection matching a given name
"""

from typing import Collection, List


def update_topics(mongo_collection: Collection,
                  name: str, topics: List[str]) -> Collection:
    """
    Updates the 'topics' field of all documents with the specified name
    Args:
        mongo_collection: The PyMongo collection object
        name (str): The name to match in the collection
        topics (list): The list of topics to assign to the matched documents
    Returns:
        UpdateResult: The result of the update operation
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
