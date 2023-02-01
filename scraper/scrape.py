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

    headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate, br',
      'content-type': 'application/json',
      'x-csrftoken': 'xsfGoCtyOHoWgEQmDrOgse2GiJ0mqT1GzFsFH92va9nosWWXQBhj0usEn5qvRz35',
      'authorization': '',
      'random-uuid': '972642fe-0975-f04e-3706-b839c65b5962',
      'Origin': 'https://leetcode.com',
      'Connection': 'keep-alive',
      # 'Referer': 'https://leetcode.com/problems/odd-even-jump/',
      'Cookie': cookie,
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'TE': 'trailers'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

# TODO: iterate over all title slugs and scrape the data
# for idx, title_slug in enumerate(['odd-even-jump', 'split-array-with-same-average']):
#     print(idx)
#     print(get_problem_data(title_slug))

# TODO: serialize response into a well define structure
