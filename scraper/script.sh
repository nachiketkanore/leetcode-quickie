cat all-problems-response.json | grep titleSlug | awk '{print $2}' > title-slugs
grep all-problems-response.json titleSlug
