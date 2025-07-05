import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq OpenAI-compatible client
groq_client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_api_key,
)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def load_recipe_data():
    file_path = os.path.join(os.path.dirname(__file__), "recipe_data.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def create_recipe_embeddings(recipes):
    recipe_texts = [recipe["title"] + " " + " ".join(recipe["ingredients"]) for recipe in recipes]
    embeddings = model.encode(recipe_texts)
    return np.array(embeddings)

def create_faiss_index(recipes):
    embeddings = create_recipe_embeddings(recipes)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index, [recipe["title"] for recipe in recipes]