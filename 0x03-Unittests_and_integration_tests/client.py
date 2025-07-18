#!/usr/bin/env python3

from utils import get_json


from typing import List
import requests

def get_json(url: str) -> dict:
    """Fetch JSON data from a given URL"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Client to interact with a GitHub organization."""

    def __init__(self, org_name: str) -> None:
        self.org_name = org_name

    @property
    def org(self) -> dict:
        """Get organization info"""
        return get_json(f"https://api.github.com/orgs/{self.org_name}")

    @property
    def _public_repos_url(self) -> str:
        """Get the URL of the public repos of the org"""
        return self.org.get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """Get list of public repo names, optionally filtered by license"""
        repos = get_json(self._public_repos_url)
        names = []
        for repo in repos:
            if license is None or self.has_license(repo, license):
                names.append(repo["name"])
        return names

    @staticmethod
    def has_license(repo: dict, license_key: str) -> bool:
        """Check if repo has the specified license"""
        return repo.get("license", {}).get("key") == license_key


