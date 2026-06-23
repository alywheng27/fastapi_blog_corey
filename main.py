from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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


# @app.get("/", response_class=HTMLResponse, include_in_schema=False)
# @app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
# def home():
#     return f"<h1>{posts[0]['title']}</h1>"


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})


@app.get("/api/posts")
def get_posts():
    return posts
