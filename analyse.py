# import json

# with open('all_movies_data.json', 'r', encoding='utf-8') as f:
#     movie_data_list = json.load(f)

# for movie in movie_data_list:
#     title = movie['title']
#     season= title.split('�')[-1].strip()  # Extract season string from title

#     if season in title:
#         print(f"Movie: {title}, Seasons: {season}")
#     else:
#         print()
#     #     print(f"Movie: {title}")
import json
import re

# Load JSON data from file
with open('all_movies_data.json', 'r', encoding='utf-8') as f:
    movie_data_list = json.load(f)

unique_titles = set()

for movie in movie_data_list:
    title = movie['title']
    
    if title not in unique_titles:
        unique_titles.add(title)
        
        match = re.search(r'Season\s(\d+)', title)
        if match:
            season = match.group(1)
        else:
            season = 'N/A'
        
        if season != 'N/A':
            print(f"Movie: {title}, Season: {season}")
        else:
            print(f"Movie: {title}, Seasons: N/A")
