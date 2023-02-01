import requests
import json

def get_problem_data(title_slug = 'odd-even-jump'):

    url = "https://leetcode.com/graphql/"

    payload = json.dumps({
      "query": "\n    query questionContent($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    content\n    mysqlSchemas\n  }\n}\n    ",
      "variables": {
        "titleSlug": title_slug
      }
    })

# storing cookie in a env file
    cookie = ''
    with open('.env', 'r') as file:
        cookie = file.read().rstrip()

    # (done) TODO: remove unnnecessary headers
    headers = {
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate, br',
      'content-type': 'application/json',
      'authorization': '',
      'Origin': 'https://leetcode.com',
      'Connection': 'keep-alive',
      'Cookie': cookie,
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'TE': 'trailers'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

with open('title-slugs', 'r') as file:
    title_slugs = file.readlines()
title_slugs = [slug.strip() for slug in title_slugs]
print(title_slugs)

# generate problem statement files (to be done once)
# TODO: add check to skip if already exists
for title_slug in title_slugs:
    print(f'{title_slug}')
    response = get_problem_data(title_slug)
    print(response.text)
    if response.status_code == 200:
        with open(f'statements/{title_slug}', 'w') as file:
            file.write(response.text)
        print(f'successfully written problem statement for {title_slug}')
    else:
        print(f'failed to get problem statement for {title_slug}')

# (done) TODO: iterate over all title slugs and scrape the data

# TODO: serialize response into a well define structure
