#!/usr/bin/env python3
"""
This module provides a function to retrieve all documents from a
MongoDB collection where a specific topic is listed in the 'topics' field.
"""

from typing import Collection


def schools_by_topic(mongo_collection: Collection, topic: str) -> Collection:
    """
    Retrieves all documents in the given MongoDB collection that include
    the specified topic in their 'topics' list field
    Args:
        mongo_collection (Collection): The PyMongo collection object
        topic (str): The topic to search for in the 'topics' field
    Returns:
        Cursor: A MongoDB cursor pointing to the matching documents
    """
    return mongo_collection.find({"topics": topic})
