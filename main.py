from fastapi import FastAPI
import random

app = FastAPI(
    title="Prompt API",
    description="Returns random creative writing prompts. Free to use.",
    version='1.0',
)

# Example data
prompts = [
    "Write a story about a talking tree.",
    "Invent a new superhero with strange power.",
    "Describe your dream vacation.",
    "Write about a world where gravity stops for one day.",
    "Imagine if animals could vote-what happens next?",
]

@app.get("/")
def home():
    return {"message": "Welcome to the Prompt Savont API. Visit /random to get a prompt"}

@app.get("/random")
def get_random_prompt():
    return {"prompt": random.choice(prompts)}