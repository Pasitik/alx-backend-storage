#!/usr/bin/env python3
"""
update a document in Python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    update a documents into a collection
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                    "topics": topics
                }
        })
