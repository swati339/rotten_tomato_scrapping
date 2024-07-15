import json
from collections import defaultdict

def load_data(filename):
    """Load data from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def analyze_data(data):
    """Analyze and print the movie data."""
    series_seasons = defaultdict(set)
    
    for movie in data:
        title = movie.get('title', 'N/A')
        season = movie.get('season', 'N/A')
        series_seasons[title].add(season)
    
    for title, seasons in series_seasons.items():
        print(f"Series: {title}")
        print(f"Total Seasons: {len(seasons)}")
        print(f"Seasons: {', '.join(sorted(seasons))}")
        print("\n")

def main():
    filename = 'all_movies_data.json'
    data = load_data(filename)
    analyze_data(data)

if __name__ == "__main__":
    main()
