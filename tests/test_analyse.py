# import json
# import os
# import analyse
# from analyse import parse_series_and_season
# from analyse import process_movie_data, parse_series_and_season
# import pytest

# def test_process_movie_data():
#     sample_input_path = 'all_movies_data.json'
#     expected_output_path = 'series_seasons_data.json'

#     with open(sample_input_path, 'r', encoding='utf-8') as f:
#         sample_data = json.load(f)
    
#     with open(expected_output_path, 'r', encoding='utf-8') as f:
#         expected_output = json.load(f)

#     process_movie_data(sample_input_path, 'temp_output.json')

#     with open('temp_output.json', 'r', encoding='utf-8') as f:
#         output_data = json.load(f)

#     os.remove('temp_output.json')

    # assert output_data == expected_output

# import sys
# import os
# import json
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from analyse import process_movie_data, parse_series_and_season
#@pytest.fixature
# def test_parse_series_and_season():
#     res = parse_series_and_season("Season 3 – Vikings: Valhalla")
#     assert res == ('3', 'Vikings: Valhalla')

# def test_process_movie_data():
#     # Load sample input data from JSON file
#     with open('all_movies_data.json', 'r', encoding='utf-8') as f:
#         sample_data = json.load(f)
    
#     # Process the sample data
#     output_data = process_movie_data(sample_data)

#     # Basic checks for the output data
#     assert isinstance(output_data, list)
#     assert all(isinstance(item, dict) for item in output_data)
#     assert all('title' in item for item in output_data)
#     assert all('season' in item for item in output_data)
#     assert all('series' in item for item in output_data)
#     assert all('score' in item for item in output_data)
#     assert all('synopsis' in item for item in output_data)

#     non_null_season_series_count = sum(
#         1 for item in output_data if item['season'] and item['series']
#     )
#     assert non_null_season_series_count >= len(output_data) // 2


import json
import os
from analyse import process_movie_data, parse_series_and_season

def test_parse_series_and_season():
    res = parse_series_and_season("Season 3 – Vikings: Valhalla")
    assert res == ('3', 'Vikings: Valhalla')

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
        1 for item in output_data if item['season'] != 'N/A' and item['series'] != 'N/A'
    )
    assert non_null_season_series_count >= len(output_data) // 2

    os.remove(output_file)
