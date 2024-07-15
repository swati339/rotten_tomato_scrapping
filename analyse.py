# import json
# import re

# # Load JSON data from file
# with open('all_movies_data.json', 'r', encoding='utf-8') as f:
#     movie_data_list = json.load(f)

# structured_data = []

# for movie in movie_data_list:
#     title = movie['title']
#     score = movie['score']
#     synopsis = movie['synopsis']
    
#     match = re.search(r'Season\s(\d+)\s–\s(.+)', title)
#     if match:
#         season = match.group(1)
#         series_name = match.group(2)
#     else:
#         season = None
#         series_name = None
    
#     structured_data.append({
#         'title': title,
#         'season': season,
#         'series': series_name,
#         'score': score,
#         'synopsis': synopsis
#     })



# with open('series_seasons_data.json', 'w', encoding='utf-8') as f:
#     json.dump(structured_data, f, ensure_ascii=False, indent=4)

import json
import re

def process_movie_data(input_file, output_file):
    # Load JSON data from file
    with open(input_file, 'r', encoding='utf-8') as f:
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
            "title": title,
            "season": season,
            "series": series_name,
            "score": score,
            "synopsis": synopsis
        })

    # Save the structured data to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, ensure_ascii=False, indent=4)
