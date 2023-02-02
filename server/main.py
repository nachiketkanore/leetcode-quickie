from os.path import isfile
from fastapi import FastAPI
import random

app = FastAPI()

# items needed to be computed once at startup
title_slugs: list[str] = []
problem_statements = {}
solutions = {}

@app.on_event("startup")
async def preprocess():

    # bringing all title-slugs
    with open('../scraper/title-slugs', 'r') as file:
        for line in file.readlines():
            title_slugs.append(line.strip())

    # bringing all problem statements
    for title_slug in title_slugs:
        file_path = f'../scraper/statements/{title_slug}'
        if isfile(file_path):
            with open(file_path, 'r') as file:
                problem_statements[title_slug] = ''.join(file.readlines())

    # bringing all solutions
    for title_slug in title_slugs:
        file_path = f'../scraper/solutions/{title_slug}'
        if isfile(file_path):
            with open(file_path, 'r') as file:
                solutions[title_slug] = ''.join(file.readlines())

    # shuffling title_slugs list
    random.shuffle(title_slugs)



@app.get("/all-slugs")
async def get_all_problem_statements() -> list[str]:
    return title_slugs

@app.get("/statement/{title_slug}")
async def get_statement(title_slug: str) -> str:
    if title_slug in problem_statements.keys():
        return problem_statements[title_slug]
    return f'problem with title-slug `{title_slug}` does not exists'

@app.get("/solution/{title_slug}")
async def get_solution(title_slug: str):
    if title_slug in solutions.keys():
        return solutions[title_slug]
    return f'solution for {title_slug} not created yet'

@app.get("/next-problem-slug")
async def get_random_problem() -> str:
    idx = random.randint(0, len(title_slugs) - 1)
    return title_slugs[idx]

