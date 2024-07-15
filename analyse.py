# import json

# with open('all_movies_data.json', 'r', encoding='utf-8') as f:
#     movie_data_list = json.load(f)

# for movie in movie_data_list:
#     title = movie['title']
#     season= title.split('�')[-1].strip()  # Extract season string from title

#     # Check if season_string is not 'N/A'
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

# Initialize a set to store unique titles
unique_titles = set()

# Iterate through each movie data
for movie in movie_data_list:
    title = movie['title']
    
    # Check if title is already in the set
    if title not in unique_titles:
        unique_titles.add(title)
        
        # Extract season number from title
        match = re.search(r'Season\s(\d+)', title)
        if match:
            season = match.group(1)
        else:
            season = 'N/A'
        
        # Print the movie title and season if season is not 'N/A'
        if season != 'N/A':
            print(f"Movie: {title}, Season: {season}")
        else:
            print(f"Movie: {title}, Seasons: N/A")
