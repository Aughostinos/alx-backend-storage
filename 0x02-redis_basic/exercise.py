#!/usr/bin/env python3
"""
Tasks:
0. Writing strings to Redis
1. Reading from Redis and recovering original type
2. Incrementing values
3. Storing lists
4. Retrieving lists
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


def call_history(method: Callable) -> Callable:
    """call_history decorator that stores the history"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that stores input and output history in Redis."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # store input
        self._redis.rpush(input_key, str(args))
        # execute original method
        output = method(self, *args, **kwargs)
        # store output
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls to a particular method."""
    qualname = method.__qualname__

    # Retrieve inputs and outputs from Redis
    inputs_key = f"{qualname}:inputs"
    outputs_key = f"{qualname}:outputs"

    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = method.__self__._redis.lrange(outputs_key, 0, -1)

    # Display the history of the calls
    print(f"{qualname} was called {len(inputs)} times:")
    for input_, output in zip(inputs, outputs):
        print(f"{qualname}(*{input_.decode('utf-8')}) -> "
              f"{output.decode('utf-8')}")


class Cache:
    """Cache class to store data in Redis."""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the given data in Redis with a randomly generated key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and optionally convert it using the provided function."""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data from Redis as an integer."""
        return self.get(key, fn=int)

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data from Redis as a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))
