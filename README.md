# Emotion Detection

**Author:** Seshadhri Srinivasan

A Python-based Emotion Detection application that uses **Flask**, **KaggleHub**, **Pandas**, and **IBM Watson NLP** to analyse the emotions expressed in user-provided text.

The application provides a web interface where the user enters text and receives an emotion prediction from the Watson NLP service.

---

## 1. Project Overview

The project performs the following operations:

1. Reads application configuration from `Configuration.json`.
2. Downloads the required emotion classification dataset from Kaggle using `kagglehub`.
3. Searches the downloaded dataset for available files.
4. Identifies CSV files.
5. Loads the training, testing, and validation datasets using Pandas.
6. Provides a Flask-based web interface.
7. Accepts text entered by the user.
8. Sends the text to IBM Watson NLP.
9. Receives the emotion prediction.
10. Displays the result in the web browser.

---

## 2. Project Architecture

```text
                    ┌─────────────────────┐
                    │      Browser        │
                    │     index.html      │
                    └──────────┬──────────┘
                               │
                               │ HTTP POST
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Flask         │
                    │      main.py        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼─────────────────┐
              │                │                 │
              ▼                ▼                 ▼
       Configuration       KaggleHub        Watson NLP
       Configuration.py    Dataset          Emotion API
              │                │                 │
              ▼                ▼                 │
       Configuration.json   CSV Files            │
                               │                 │
                               ▼                 │
                         Pandas DataFrames       │
                                                 │
                               ◄─────────────────┘
                                  Emotion Result
                                       │
                                       ▼
                              Flask / HTML Response
```
----
##3. File structure
```text
EmotionDetection/
│
├── README.md
│
├── main.py
│
├── Configuration/
│   ├── __init__.py
│   ├── Configuration.py
│   └── Configuration.json
│
└── templates/
    └── index.html
```
##4. Description of files

| File | Purpose |
|---|---|
| `main.py` | Flask application and web interface logic |
| `Configuration/Configuration.py` | Configuration, Kaggle dataset, CSV and Watson NLP functions |
| `Configuration/Configuration.json` | Application configuration |
| `Configuration/__init__.py` | Makes the Configuration directory a Python package |
| `templates/index.html` | Web interface |
| `README.md` | Project documentation |

___

## 5.Tech used
The project uses the following technologies:

- Python 3
- Flask
- Pandas
- KaggleHub
- Requests
- IBM Watson NLP
- HTML
- CSS

---

## 6. Required packages
```bash
pip install flask
pip install kagglehub
pip install pandas
pip install requests
```

## 7. Configuration
```text
Configuration/Configuration.json
```
