with open('title-slugs', 'r') as file:
    title_slugs = file.readlines()
title_slugs = [slug.strip() for slug in title_slugs]
print(title_slugs)

import os
for title_slug in title_slugs:
    print(title_slug)
    os.system(f'jq -r ".data.question.content" statements/{title_slug} > tmp && cp tmp statements/{title_slug}')
    # break
    # os.system(f'jq . statements/{title_slug} > tmp && cp tmp statements/{title_slug}')
