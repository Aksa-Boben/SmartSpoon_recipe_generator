# Smart Spoon - AI-Powered Recipe Generator

**Smart Spoon** is a GenAI-based web application that helps users generate delicious recipes using the ingredients they already have at home. 
It uses Retrieval-Augmented Generation (RAG) to either find matching recipes or generate new ones using AI.

---

## 👥 Team Members

- Adith Kurian Pulimalayil  
- Ahil Baby  
- Aksa Boben  
- Jacob Joji  
- Niveditha Shaji

---

## 📚 Table of Contents

- [Features](#features)
- [Folder Structure](#folder-structure)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Environment Variables](#environment-variables)
- [Run the App](#run-the-app)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

---

## Features

-  Search real recipes using FAISS and embeddings
-  Generate creative new recipes using LLaMA3 via Groq API
-  Uses SentenceTransformer for semantic search
-  Built with FastAPI, HTML, Tailwind CSS, and JavaScript
-  Clean UI with ingredient input and dynamic recipe output

---

## Folder Structure
project/
├── main.py # FastAPI app with routes
├── rag_recipe.py # Core recipe logic (RAG)
├── utils.py # Utilities: embeddings, FAISS, Groq
├── recipe_data.json # Recipe dataset
├── static/
│ └── style.css # Custom styles
├── templates/
│ └── index.html # Web frontend
├── .env # API keys (not uploaded)
├── requirements.txt # Python dependencies
└── README.md # Project overview


---

## How It Works

1. User types ingredients in the web page.
2. FastAPI receives the input and searches for similar recipes using FAISS.
3. If no good match is found, it uses LLaMA3 AI via Groq to generate a new recipe.
4. The recipe is displayed beautifully on the page.

---

## Technologies Used

- **FastAPI** – Web backend
- **FAISS** – Fast vector search for recipe matching
- **SentenceTransformer** – Embedding model for similarity
- **Groq + LLaMA3** – AI model for recipe generation
- **HTML, TailwindCSS, JavaScript** – Frontend UI
- **dotenv** – For securely loading API keys

---

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```
---

## Run the App
1. Install dependencies:
```bash
  pip install -r requirements.txt
```
2. Start the FastAPI server:
```bash
  uvicorn main:app --reload
```
3. Open your browser:
```bash
  http://localhost:8000
```
---

## Credits
- Developed during the GenAI Add-On Course by iSkew Learning
- Recipe embeddings powered by sentence-transformers
- Recipe generation by Groq's LLaMA3

---

## Acknowledgments
Thanks to my mentors, peers, and my college for encouraging this project.
