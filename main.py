from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


posts: list[dict] = [
    {
        "id": 1,
        "author": "Pavlo Leskovych",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "March 16, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "March 16, 2025",
    },
]

app = FastAPI(debug=False, title="Pavlo's Blog")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
async def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
async def get_posts():
    return posts
