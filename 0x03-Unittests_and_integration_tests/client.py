#!/usr/bin/env python3

from utils import get_json

class GithubOrgClient:
    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        return get_json(f"https://api.github.com/orgs/{self.org_name}")
