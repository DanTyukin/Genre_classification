# Music-genre-recognizer

Клиент-серверное приложение с использованием искусственного интеллекта для распознавания жанра музыки.

## Как запустить

### Клиент-сервер

Клиент - это интерактивный клиент с командной строкой.

### Запуск сервера

Сначала запустите сервер:

```
cd server
pip install -r requirements.txt
python app.py
```

### Запуск клиента
Затем запустите клиента:

```
cd ../client
pip install -r requirements.txt
python client.py
```

### Описание проекта
Этот проект включает серверную часть, реализованную на Flask, и клиентскую часть, реализованную на Python. Сервер принимает аудиофайлы, извлекает из них признаки, используя заранее обученные модели, и предсказывает жанр музыки. Клиентская часть предоставляет интерфейс для отправки аудиофайлов на сервер и получения результатов.

### Структура проекта
     our_server/

       ├── client/
           │   ├── client.py
           │   └── requirements.txt
       ├── server/
           │   ├── app.py
           │   ├── requirements.txt
           │   ├── model/
               │   │   ├── min_max_scaler.pkl
               │   │   └── xgb_mgen.pkl
           │   ├── templates/
               │   │   ├── index.html
               │   │   └── result.html
           │   ├── uploads/
               │   │   └── (загруженные файлы будут здесь)
           │   └── utils/
               │       └── feature_extraction.py│  
               

### Файлы и папки
```
client/: Содержит клиентскую часть приложения.
       client.py: Основной файл клиента.
       requirements.txt: Зависимости для клиента.

server/: Содержит серверную часть приложения.
       app.py: Основной файл сервера Flask.
       requirements.txt: Зависимости для сервера.
       model/: Папка с моделями для предсказаний.
             min_max_scaler.pkl: Модель нормализации.
             xgb_mgen.pkl: Модель XGBoost.
       templates/: Папка с HTML-шаблонами.
             index.html: Шаблон для загрузки аудиофайла.
             result.html: Шаблон для отображения предсказанного жанра и рекомендаций.
       uploads/: Папка для загруженных файлов.
       utils/: Папка с утилитами.
             feature_extraction.py: Модуль для извлечения признаков из аудиофайлов.
```

### Требования
-Python 3.6 или выше

-Flask

### Установка
Установите зависимости для сервера:

```
cd server
pip install -r requirements.txt
```

Установите зависимости для клиента:

```
cd ../client
pip install -r requirements.txt
```

### Использование
Запустите сервер:
```
cd server
python app.py
```

Запустите клиента:
```
cd client
python client.py
```

Теперь вы можете загружать аудиофайлы через клиент и получать предсказания жанра музыки от сервера.
