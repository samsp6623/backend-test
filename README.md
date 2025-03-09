# Github API Integration

## Task

Build an API that connects to the GitHub API to show your GitHub activity log. Add it to your portfolio website at a new route /github.

## Endpoints

   - GET /github → Show your data, like number of followers, number of following, list of your personal repositories, etc.

   - GET /github/{repo-name} → Show data about that particular project.

   - POST /github/{repo-name}/issues → Take in the title and body, create an issue in the repo, and return the GitHub issue URL.


## Requirements

   - You can just return a JSON that can be pretty-printed in the browser. UI is NOT needed.

   - Deploy the API online. You can use Vercel, Netlify, Cloudflare, Heroku, Render, etc.
