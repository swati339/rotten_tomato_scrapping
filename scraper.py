import requests
from bs4 import BeautifulSoup
import json

def fetch_movie_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract movie title
    title_tag = soup.find('h1', class_='scoreboard__title')
    title = title_tag.text.strip() if title_tag else 'N/A'
    
    # Extract movie score
    score_tag = soup.find('span', class_='mop-ratings-wrap__percentage')
    score = score_tag.text.strip() if score_tag else 'N/A'
    
    # Extract movie synopsis
    synopsis_tag = soup.find('div', id='movieSynopsis')
    synopsis = synopsis_tag.text.strip() if synopsis_tag else 'N/A'
    
    return {
        'title': title,
        'score': score,
        'synopsis': synopsis,
    }

def main():
    url = input("Enter the Rotten Tomatoes movie URL: ")
    try:
        movie_data = fetch_movie_data(url)
        
        # Display movie data
        print("Movie Title:", movie_data['title'])
        print("Movie Score:", movie_data['score'])
        print("Movie Synopsis:", movie_data['synopsis'])
        
        # Save movie data to JSON file
        with open('movie_data.json', 'w', encoding='utf-8') as f:
            json.dump(movie_data, f, ensure_ascii=False, indent=4)
        
        print("Movie data has been saved to movie_data.json")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
