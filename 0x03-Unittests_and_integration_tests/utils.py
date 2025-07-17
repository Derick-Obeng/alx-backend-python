#!/usr/bin/env python3

def access_nested_map():
    return None

# utils.py
import requests

def get_json(url: str) -> dict:
    """GET JSON content from a URL"""
    res = requests.get(url)
    return res.json()


def memoize():
    return None