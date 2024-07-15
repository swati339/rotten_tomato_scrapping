from setuptools import setup, find_packages

setup(
    name='rotten_tomatoes_scraper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
        'pytest',  
    ],
    entry_points={
        'console_scripts': [
            'scrape-rotten-tomatoes=scraper:main',
            'analyze-movies=analyze:process_movie_data',  
        ],
    },
)
