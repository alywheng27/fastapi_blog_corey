from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Aly Mama",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy to use and super fast!",
        "date_posted": "April 20, 2026"
    },
    {
        "id": 2,
        "author": "Bob Smith",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy to use and super fast!",
        "date_posted": "April 20, 2026"
    },
    {
        "id": 3,
        "author": "Bob Smith",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy to use and super fast!",
        "date_posted": "April 20, 2026"
    }
]

# response_class=HTMLResponse allows html
# include_in_schema=False hides the route from the docs


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts", response_class=HTMLResponse)
def get_posts():
    return posts
