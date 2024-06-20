from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import random 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    result = random.choice(omikuji_list)  
    return {"result": result}

@app.get("/index", response_class=HTMLResponse)
def index():
    html_content = """
    <html>
        <head>
            <title>My Home Page</title>
        </head>
        <body>
            <h1>Welcome to My Home Page!</h1>
            <p>This is a simple HTML page served by FastAPI.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present: str = Form(...)):
    return {"response": f"Thank you for the {present}! Here is your gift: Candy."}
