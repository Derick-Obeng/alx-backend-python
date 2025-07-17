#!/usr/bin/env python3
"""Utility functions for nested access, HTTP requests, and memoization"""

import requests
from typing import Mapping, Any, Sequence, Callable


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a value in a nested map with a sequence of keys"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> dict:
    """GET JSON content from a URL"""
    res = requests.get(url)
    return res.json()


def memoize(method: Callable) -> Callable:
    """Decorator to memoize method results"""
    attr_name = "_{}".format(method.__name__)

    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return wrapper
