import json
import re

# Load JSON data from file
with open('all_movies_data.json', 'r', encoding='utf-8') as f:
    movie_data_list = json.load(f)

structured_data = []

for movie in movie_data_list:
    title = movie['title']
    score = movie['score']
    synopsis = movie['synopsis']
    
    match = re.search(r'Season\s(\d+)\s–\s(.+)', title)
    if match:
        season = match.group(1)
        series_name = match.group(2)
    else:
        season = None
        series_name = None
    
    structured_data.append({
        'title': title,
        'season': season,
        'series': series_name,
        'score': score,
        'synopsis': synopsis
    })



with open('series_seasons_data.json', 'w', encoding='utf-8') as f:
    json.dump(structured_data, f, ensure_ascii=False, indent=4)