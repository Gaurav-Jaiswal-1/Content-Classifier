import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Define base URL for anime list (e.g., MyAnimeList popular anime page)
base_url = 'https://animemangatoon.com/top-anime-and-k-drama-like-true-beauty/'

# Prepare empty lists to hold the scraped data
titles = []
descriptions = []
genres = []

# Function to scrape anime from a page
def scrape_anime(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all anime containers on the page
    anime_list = soup.find_all('div', class_='content-inner')

    for anime in anime_list:
        # Extract anime title
        title = anime.find('b').text.strip()
        titles.append(title)
        
        # Extract description (if available)
        description = anime.find('p', class_ = 'code-block-8').text.strip() if anime.find('p', class_ = 'code-block-8') else 'No description'
        descriptions.append(description)
        
        # Extract genre(s)
        # genres_list = []
        # genres_html = anime.find_all('span', class_='genre')
        # for genre in genres_html:
        #     genres_list.append(genre.text.strip())
        # genres.append(', '.join(genres_list))

# Iterate through several pages of anime
for page in range(1, 6):  # Scraping first 5 pages as an example
    page_url = f'{base_url}?limit={50 * (page - 1)}'  # Adjust URL for pagination
    scrape_anime(page_url)
    time.sleep(1)  # To avoid overloading the server

# Convert to a DataFrame for easier handling
anime_data = pd.DataFrame({
    'Title': titles,
    'Description': descriptions,
    'Genres': genres
})

# Save the data to a CSV file
anime_data.to_csv('anime_dataset5.csv', index=False)
print("Anime dataset saved as 'anime_dataset.csv'")
