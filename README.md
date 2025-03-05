# Text-To-Speech-API (Flask & FastAPI)

This repository provides a tutorial for building a simple **Text-to-Speech (TTS) API** using **Flask** and **FastAPI**. The API converts text input into speech using **Google Text-to-Speech (gTTS)** and returns an MP3 file.

## Features

- **Text-to-Speech Conversion**: Converts plain text into speech using `gTTS`.
- **RESTful API**: Send text data and receive an audio file.
- **Customizable**: Supports multiple languages and different voice configurations.
- **Lightweight**: Both Flask and FastAPI versions are optimized for performance.

## Requirements

Ensure you have **Python 3.7+** installed. It's recommended to use a virtual environment.

### Install Dependencies

```bash
pip install flask fastapi gtts uvicorn
```


## **Flask Implementation**

* Flask is a lightweight web framework, making it ideal for simple APIs.
* The **Flask API** is implemented in **app_flask.py**.
* It accepts **POST** requests with JSON data containing the text to be converted.
* Returns an **MP3 file** as a response.

### **How to Run Flask API**

```
python app_flask.py
```

### Test Flask API

```
curl -X POST "http://127.0.0.1:5000/speak" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello from Flask"}' \
     --output output.mp3
```

## **FastAPI Implementation**

* FastAPI is a modern, high-performance framework for building APIs.
* The **FastAPI version** is in **app_fastapi.py**.
* Uses **Pydantic models** for request validation.
* Provides **automatic documentation** via Swagger UI.

### **How to Run FastAPI**

```
uvicorn app_fastapi:app --host 0.0.0.0 --port 8000
```

### **Test FastAPI API**

```
curl -X POST "http://127.0.0.1:8000/speak" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello from FastAPI"}' \
     --output output.mp3
```

### **Comparison: Flask vs FastAPI**

| Feature       | Flask       | FastAPI                      |
| ------------- | ----------- | ---------------------------- |
| Performance   | Slower      | Faster (async support)       |
| Ease of Use   | Easy        | Easy but requires type hints |
| Auto Docs     | No          | Yes (Swagger & ReDoc)        |
| Async Support | No          | Yes                          |
| Best For      | Simple APIs | High-performance APIs        |

### License

This project is open-source and available under the **MIT License**.
