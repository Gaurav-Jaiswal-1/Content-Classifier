import requests
import re
import csv
from bs4 import BeautifulSoup
import pandas as pd


url=r"https://animemangatoon.com/top-anime-and-k-drama-like-true-beauty/"
r=requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')



# Initialize lists for headings and paragraphs
headings_and_paragraphs = []
headings = []
paragraphs1 = []

# Loop through all heading elements
for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    heading = element.text
    paragraphs = []

    # Loop through the siblings, but stop if another heading is found
    for sibling in element.find_next_siblings():
        # If the sibling is another heading, stop collecting paragraphs
        if sibling.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            break
        # Otherwise, collect paragraphs
        if sibling.name == 'p':
            paragraphs.append(sibling.text)

    # Append the heading and paragraphs as a tuple
    headings_and_paragraphs.append((heading, paragraphs))

# Prepare lists for DataFrame columns
for heading, paragraphs in headings_and_paragraphs:
    headings.append(heading)
    # Join paragraphs into a single string for each heading
    paragraphs1.append(" ".join(paragraphs) if paragraphs else None)

# Create a DataFrame
df = pd.DataFrame({
    'Heading': headings,
    'Paragraph': paragraphs1
})



# Define the file path where you want to save the CSV file
file_path = r'C:\Users\Gaurav\OneDrive\Desktop\Task 1\Content-Classifier\data\webtoons_data.csv'

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False, encoding='utf-8')

print(f"Data saved to {file_path}")
