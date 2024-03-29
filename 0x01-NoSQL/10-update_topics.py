#!/usr/bin/env python3
"""
update a document in Python
"""
import pymongo


def update_topics(mongo_collection, name, topics):
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
