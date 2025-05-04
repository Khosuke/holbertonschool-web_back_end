#!/usr/bin/env python3
"""
This module provide one function that inserts a new 
document in a collection based on kwargs
"""

from typing import Collection, Dict, Any


def insert_school(mongo_collection: Collection, **kwargs: Dict[str, Any]) -> Any:
    """
    Inserts a new document into the specified MongoDB collection
    Args:
        mongo_collection (Collection): The PyMongo collection object
        **kwargs: Arbitrary keyword arguments representing the document fields
    Returns:
        The _id of the newly inserted document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
