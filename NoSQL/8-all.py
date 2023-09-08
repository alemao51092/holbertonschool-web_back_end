#!/usr/bin/env python3
"""shebang"""


def list_all(mongo_collection):
    list_doc = []
    for doc in mongo_collection.find():
        list_doc.append(doc)
    return list_doc
