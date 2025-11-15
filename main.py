from fastapi import FastAPI, Query
import random
from scraper import scrape_reedsy_prompts

app = FastAPI(
    title="Prompt API",
    description="Returns random creative writing prompts by category.",
    version="2.0"
)

# Scrape once at startup (you can also schedule this weekly later)
print("Scraping prompts... please wait...")
PROMPTS_BY_CATEGORY = scrape_reedsy_prompts()
print(f"Loaded {sum(len(v) for v in PROMPTS_BY_CATEGORY.values())} prompts.")

@app.get("/")
def home():
    return {
        "message": "Welcome to the Prompt API! Use /random?category=Romance or /categories",
        "total_prompts": sum(len(v) for v in PROMPTS_BY_CATEGORY.values()),
        "categories": list(PROMPTS_BY_CATEGORY.keys())
    }

@app.get("/categories")
def get_categories():
    """List available categories"""
    return {"categories": list(PROMPTS_BY_CATEGORY.keys())}

@app.get("/random")
def get_random_prompt(category: str = Query(None, description="Category name (optional)")):
    """Get a random prompt from a category, or any if none specified."""
    if category:
        category = category.strip().title()
        if category not in PROMPTS_BY_CATEGORY:
            return {"error": f"Category '{category}' not found. Try one from /categories."}
        prompt = random.choice(PROMPTS_BY_CATEGORY[category])
        return {"category": category, "prompt": prompt}
    else:
        # Pick a random category and then a random prompt
        cat = random.choice(list(PROMPTS_BY_CATEGORY.keys()))
        prompt = random.choice(PROMPTS_BY_CATEGORY[cat])
        return {"category": cat, "prompt": prompt}
