from typing import Union
from fastapi import FastAPI

app = FastAPI()


# TODO: eliminate file IO, load everything into memory
# TODO: use map<title_slug, problem_statement HTML>
@app.get("/statement/{title_slug}")
async def get_statement(title_slug: str):
    file_path = '../scraper/statements/'
    file_path += title_slug
    try:
        with open(file_path, 'r') as file:
            return {
                "statement": ''.join(file.readlines())
            }
    except:
        return {
            "error": "invalid title-slug provided"
        }

