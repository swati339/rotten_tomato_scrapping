import json
import re

def parse_series_and_season(title):
    match = re.search(r'Season\s(\d+)\s–\s(.+)', title)
    if match:
        season = match.group(1)
        series_name = match.group(2)
    else:
        match = re.search(r'Season\s(\d+)', title)
        if match:
            season = match.group(1)
            series_name = title
        else:
            season = None
            series_name = title
    return season, series_name


def process_movie_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        movie_data_list = json.load(f)
    
    unique_series = {}
    structured_data = []
    
    for movie in movie_data_list:
        title = movie['title']
        score = movie.get('score', None)
        synopsis = movie.get('synopsis', None)
        
        season, series_name = parse_series_and_season(title)
        
        structured_data.append({
            "title": title,
            "season": season,
            "series": series_name,
            "score": score,
            "synopsis": synopsis
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, ensure_ascii=False, indent=4)

