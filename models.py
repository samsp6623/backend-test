from pydantic import BaseModel, HttpUrl, PastDatetime

class User(BaseModel):
    """
    A Class representing details of the Github User.
    """
    name: str
    type: str
    login: str
    html_url: HttpUrl
    bio: str
    public_repos: int
    public_gists: int
    followers: int
    following: int
    updated_at: PastDatetime

class IssueURL(BaseModel):
    """
    A class representing IssueURL.
    """
    url: HttpUrl

