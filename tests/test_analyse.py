import json
import os
from analyse import process_movie_data, parse_series_and_season

def test_parse_series_and_season():
    res = parse_series_and_season("Season 3 – Vikings: Valhalla")
    assert res == ('3', 'Vikings: Valhalla')
    
    res = parse_series_and_season("Vikings: Valhalla") #wiht no season info
    assert res == (None, 'Vikings: Valhalla')
    
    res = parse_series_and_season("Season3-Vikings:Valhalla") #with wrong info
    assert res == (None, 'Season3-Vikings:Valhalla')
    
    res = parse_series_and_season("Season 2") #with title name only
    assert res == ('2', 'Season 2')

def test_process_movie_data():
    with open('all_movies_data.json', 'r', encoding='utf-8') as f:
        sample_data = json.load(f)
    
    output_file = 'test_output.json'

    process_movie_data('all_movies_data.json', output_file)

    with open(output_file, 'r', encoding='utf-8') as f:
        output_data = json.load(f)

    assert isinstance(output_data, list)
    assert all(isinstance(item, dict) for item in output_data)
    assert all('title' in item for item in output_data)
    assert all('season' in item for item in output_data)
    assert all('series' in item for item in output_data)
    assert all('score' in item for item in output_data)
    assert all('synopsis' in item for item in output_data)

    non_null_season_series_count = sum(
        1 for item in output_data if item['season'] is not None and item['series'] is not None
    )
    assert non_null_season_series_count >= len(output_data) // 2

    os.remove(output_file)

if __name__ == "__main__":
    test_parse_series_and_season()
    test_process_movie_data()
