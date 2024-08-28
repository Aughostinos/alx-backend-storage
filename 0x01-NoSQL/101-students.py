#!/usr/bin/env python3
"""
task 14. Top students
"""


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    j_students = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": { "$avg": "$topics.score"}
            }
        },
        { "$sort": { "averageScore": -1 }}
    ]
    return list(mongo_collection.aggregate(j_students))