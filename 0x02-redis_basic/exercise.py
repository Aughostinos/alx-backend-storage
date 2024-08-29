#!/usr/bin/env python3
"""Task 0. Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """cache class to store data in redis"""


    def __init__(self):
        """store an instance of the Redis client
        as a private variable named _redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """The method should generate a random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key