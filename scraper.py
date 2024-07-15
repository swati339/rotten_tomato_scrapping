import requests
from bs4 import BeautifulSoup
import json

def fetch_movie_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract movie title
    title_tag = soup.find( 'h1', class_="unset")
    title = title_tag.text.strip() if title_tag else 'N/A'
    
    # Extract movie score
    score_tag = soup.find('rt-text', size="1.375")
    score = score_tag.text.strip() if score_tag else 'N/A'
    
    # Extract movie synopsis
    synopsis_tag = soup.find( 'drawer-more',slot="description")
    synopsis = synopsis_tag.text.strip() if synopsis_tag else 'N/A'
    
    return {
        'title': title,
        'score': score,
        'synopsis': synopsis,
    }

def main():
    movie_urls = [
        # Add your Rotten Tomatoes movie URLs here
        'https://www.rottentomatoes.com/tv/sunny/s01',
        'https://www.rottentomatoes.com/tv/sausage_party_foodtopia/s01',
        'https://www.rottentomatoes.com/tv/vikings_valhalla/s03',
        'https://www.rottentomatoes.com/tv/mastermind_to_think_like_a_killer/s01',
        'https://www.rottentomatoes.com/tv/the_serpent_queen/s02',
        'https://www.rottentomatoes.com/tv/me/s01',
        'https://www.rottentomatoes.com/tv/the_bachelorette/s21',
        'https://www.rottentomatoes.com/tv/all_american_homecoming/s03',
        'https://www.rottentomatoes.com/m/the_bikeriders',
        'https://www.rottentomatoes.com/tv/star_wars_the_acolyte/s01',
        'https://www.rottentomatoes.com/tv/all_american_homecoming/s03',
        'https://www.rottentomatoes.com/tv/all_american_homecoming/s03'

        
    ]
    
    movie_data_list = []
    
    for url in movie_urls:
        try:
            movie_data = fetch_movie_data(url)
            movie_data_list.append(movie_data)
            print(f"Scraped data for {movie_data['title']}")
        except Exception as e:
            print(f"Failed to scrape {url}: {str(e)}")
    
    # Save movie data to JSON file
    with open('all_movies_data.json', 'w', encoding='utf-8') as f:
        json.dump(movie_data_list, f, ensure_ascii=False, indent=4)
    
    print("All movie data has been saved to all_movies_data.json")

if __name__ == "__main__":
    main()
