import json
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def analyse_data(data):
    for movies in data:
        movie_data = movies.get('movie_name', 'N/A')
        seasons = movies.get('seasons', [])
        num_seasons = len(seasons)
        
        print(f"Movie: {movie_name}")
        print(f"Number of Seasons: {num_seasons}")
        
        for season in seasons:
            title = season.get('title', 'N/A')
            score = season.get('score', 'N/A')
            synopsis = season.get('synopsis', 'N/A')
            
            print(f"  Season Title: {title}")
            print(f"  Score: {score}")
            print(f"  Synopsis: {synopsis}")
        print("\n")

def main():
    filename = 'all_movies_data.json'
    data = load_data(filename)
    analyse_data(data)

if __name__ == "__main__":
    main()