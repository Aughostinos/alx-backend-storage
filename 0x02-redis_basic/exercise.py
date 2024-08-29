#!/usr/bin/env python3
"""
Tasks
0. Writing strings to Redis
1. Reading from Redis and recovering original type
2. Incrementing values
"""
import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """count_calls decorator that takes a single
    method Callable argument and returns a Callable"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the call count in Redis"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


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


    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float, None]:
        """method that take a key string argument and an optional
        Callable argument named fn. This callable will be used to
        convert the data back to the desired format."""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data    


    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data from Redis as an integer"""
        return self.get(key, fn=int)


    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data from Redis as a string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))
    
    
    