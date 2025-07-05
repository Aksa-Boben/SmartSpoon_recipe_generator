from utils import model, load_recipe_data, create_faiss_index, groq_client
import numpy as np

# Load recipes and FAISS index
recipes = load_recipe_data()
index, texts = create_faiss_index(recipes)

def ingredient_overlap_score(input_ingredients, recipe_ingredients):
    return len(set(input_ingredients).intersection(set(map(str.lower, recipe_ingredients))))

def generate_recipe_with_llama(user_ingredients: str):
    prompt = f"""
You are a professional chef. I have the following ingredients: {user_ingredients}.
Generate a unique and tasty recipe using most or all of these ingredients.
Include:
- Title
- Ingredients (as a list)
- Instructions (as clear steps)
"""
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful recipe assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500,
    )
    content = response.choices[0].message.content
    return {
        "title": "AI-Generated Recipe",
        "ingredients": [user_ingredients],
        "instructions": content
    }

def find_best_recipes(user_ingredients: str, top_k=5, min_overlap=2):  # set minimum match to 2
    input_ings = [i.strip().lower() for i in user_ingredients.split(",")]

    query_embedding = model.encode([user_ingredients])[0]
    D, I = index.search(np.array([query_embedding]).astype('float32'), top_k)

    results = []
    seen_titles = set()

    for i in I[0]:
        if i < len(recipes):
            recipe = recipes[i]
            title = recipe["title"]
            overlap = ingredient_overlap_score(input_ings, recipe["ingredients"])
            if overlap >= min_overlap and title not in seen_titles:
                results.append(recipe)
                seen_titles.add(title)

    if results:
        return results
    else:
        return [generate_recipe_with_llama(user_ingredients)]

