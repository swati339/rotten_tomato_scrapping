import json
import re

# Load JSON data from file
with open('all_movies_data.json', 'r', encoding='utf-8') as f:
    movie_data_list = json.load(f)

unique_titles = set()
unique_series = {}

for movie in movie_data_list:
    title = movie['title']
    
    if title not in unique_titles:
        unique_titles.add(title)
        
        match = re.search(r'Season\s(\d+)\s–\s(.+)', title)
        if match:
            season = match.group(1)
            series_name = match.group(2)
        else:
            season = 'N/A'
            series_name = title
        
        if series_name not in unique_series:
            unique_series[series_name] = set()
        
        if season != 'N/A':
            unique_series[series_name].add(season)

for series, seasons in unique_series.items():
    if seasons:
        seasons_list = ', '.join(sorted(seasons))
        print(f"Series: {series}, Seasons: {seasons_list}")
    else:
        print(f"Series: {series}, Seasons: N/A")

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
        season = 'N/A'
        series_name = title
    
    structured_data.append({
        'title': title,
        'season': season,
        'series': series_name,
        'score': score,
        'synopsis': synopsis
    })



with open('series_seasons_data.json', 'w', encoding='utf-8') as f:
    json.dump(structured_data, f, ensure_ascii=False, indent=4)