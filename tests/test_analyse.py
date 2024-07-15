import json
import os
from analyse import process_movie_data

def test_process_movie_data():
    sample_input_path = 'all_movies_data.json'
    expected_output_path = 'series_seasons_data.json'

    with open(sample_input_path, 'r', encoding='utf-8') as f:
        sample_data = json.load(f)
    
    with open(expected_output_path, 'r', encoding='utf-8') as f:
        expected_output = json.load(f)

    process_movie_data(sample_input_path, 'temp_output.json')

    with open('temp_output.json', 'r', encoding='utf-8') as f:
        output_data = json.load(f)

    os.remove('temp_output.json')

    assert output_data == expected_output
