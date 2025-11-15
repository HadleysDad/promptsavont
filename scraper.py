import requests
from bs4 import BeautifulSoup

def scrape_reedsy_prompts():
    """
    Scrapes prompts from Reedsy website and groups them by category.
    Returns a dictionary like: {"Romance": [...], "Sci-Fi": [...], ...}
    """
    url = "https://blog.reedsy.com/creative-writing-prompts/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {}

    # Find all category sections
    categories = soup.find_all("section", class_="prompts__group")

    for cat in categories:
        category_title = cat.find("h2").text.strip()
        prompts = [li.text.strip() for li in cat.find_all("li")]
        data[category_title] = prompts

    return data
