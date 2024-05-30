import requests

def classify_genre(file_path):
    url = 'http://192.168.1.90:5000/predict'  # Убедитесь, что этот URL правильный
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    if response.status_code == 200:
        try:
            return response.json().get('genre', 'Error: Genre not found in response')
        except ValueError as e:
            print("Error parsing JSON:", e)
            return 'Error: Invalid JSON response'
    else:
        return 'Error: Unable to classify genre'

# Пример использования
file_path = 'Rammstein_-_Ich_will_57658983 (mp3cut.net).mp3'  # Загрузите файл в проект
genre = classify_genre(file_path)
print(f'The predicted genre is: {genre}')
