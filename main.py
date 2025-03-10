import os
import json
import requests
from typing import Annotated
from models import User, IssueURL
from fastapi import FastAPI

app = FastAPI()

GITHUB_TOKEN: str = os.environ.get("GITHUB_TOKEN", None)

if GITHUB_TOKEN is None:
    raise Exception("Please provide GITHUB_TOKEN")

BASE_URL = "https://api.github.com"


def get_data(
    endpoint: str, data = None, method = "GET"
):
    """A Generic function to make call to Github and fetch user relaed data."""
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        # "Accept": "application/vnd.github+json",
        "Accept": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if method == "GET":
        resp = requests.get(BASE_URL + endpoint, data=data, headers=headers)
    elif method == "POST":
        headers.update({"Content-Type": "application/json"})
        url = BASE_URL + endpoint
        resp = requests.post(url, data=json.dumps(data), headers=headers)
    return resp.json()


@app.get("/github", response_model=User)
def read_root():
    data = get_data("/user")
    return data


@app.get("/github/{repo_name}")
def read_item(repo_name: Annotated[str, True]):
    data = get_data(f"/repos/samsp6623/{repo_name}")
    return data


@app.post("/github/{repo_name}/issues", response_model=IssueURL)
def post_item(title: str, body: str, repo_name: Annotated[str, True]):
    output = get_data(
        f"/repos/samsp6623/{repo_name}/issues",
        method="POST",
        data={"title": title, "body": body},
    )
    return output
