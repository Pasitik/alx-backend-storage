#!/usr/bin/env python3
"""Module declares a redis class and methods"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    '''declares a Cache redis class'''
    def __init__(self):
        '''upon init to store an instance and flush'''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''takes a data argument and returns a string'''
        redkey = str(uuid4())
        self._redis.set(redkey, data)
        return redkey
