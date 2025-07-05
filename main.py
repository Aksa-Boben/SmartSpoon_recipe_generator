from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from rag_recipe import find_best_recipes

app = FastAPI()

# Serve static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tell FastAPI where our HTML templates are
templates = Jinja2Templates(directory="templates")

# Define data model
class IngredientsInput(BaseModel):
    ingredients: str

# Route for home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route for recipe generation
@app.post("/generate")
async def generate_recipe(data: IngredientsInput):
    results = find_best_recipes(data.ingredients)
    return {"recipes": results}
