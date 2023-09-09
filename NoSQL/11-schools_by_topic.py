#!/usr/bin/env python3
"""Task 11:
    Where can I learn python?"""


def schools_by_topic(mongo_collection, topic):
    """A function that returns the list of
    schools having a specific topic"""
    return mongo_collection.find({"topics": topic})
