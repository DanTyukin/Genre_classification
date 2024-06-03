import argparse
import requests
from bs4 import BeautifulSoup


def classify_genre(url, file_path):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        try:
            return response.json().get('genre', 'Error: Genre not found in response')
        except ValueError:
            soup = BeautifulSoup(response.text, 'html.parser')
            genre_tag = soup.find('p')
            if genre_tag:
                return genre_tag.text
            else:
                return 'Error: Genre not found in HTML response'
    else:
        return 'Error: Unable to classify genre'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Classify music genre.')
    parser.add_argument('url', type=str, help='URL of the prediction endpoint')
    parser.add_argument('file_path', type=str, help='Path to the input file')
    args = parser.parse_args()

    genre = classify_genre(args.url, args.file_path)
    print(f'The predicted genre is: {genre}')




