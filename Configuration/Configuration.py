import kagglehub
import os
import json
import pandas as pd
from fastapi import FastAPI
import requests
import os
import pandas as pd

# Read configuration.json and return config
def readConfiguration():
    configFile = os.path.join(os.path.dirname(__file__),"Configuration.json")
    with open(configFile, "r") as configFile:
        config = json.load(configFile)
    return config

# Read the kaggle path
def downloadDataset(kagglepath):
    # Read datafile path from kaggle
    filepath = kagglehub.dataset_download(kagglepath)
    return(filepath)

# Get the files
def getFiles(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            full_path = os.path.join(root,file)
            all_files.append(full_path)
    return all_files


# get CSV files
def getCSVfiles(allFiles):
    csvFiles = []
    for file in allFiles:
        if file.lower().endswith(".csv"):
            csvFiles.append(file)
    return(csvFiles)

def getRequiredVFiles(allFiles,requiredFiles):
    foundFiles = {}
    for file in allFiles:
        fileName = os.path.basename(file)
        if fileName in requiredFiles:
            foundFiles[fileName] = file
        # Check for missing files
    missingFiles = set(requiredFiles.values()) - set(foundFiles.keys())
    if missingFiles:
        raise FileNotFoundError(
            f"Missing required CSV file(s): {sorted(missingFiles)}"
        )
    # Check for extra CSV files
    csvFilesFound = {
        os.path.basename(file)
        for file in allFiles
        if file.lower().endswith(".csv")
    }
    extraFiles = csvFilesFound - requiredFiles

    if extraFiles:
        raise ValueError(
            f"Unexpected CSV file(s) found: {sorted(extraFiles)}"
        )
    return [
        foundFiles["train.csv"],
        foundFiles["test.csv"],
        foundFiles["validation.csv"]
    ]




def get_training_data(allFiles, requiredFiles):
    foundFiles = {}

    for file in allFiles:
        fileName = os.path.basename(file)
        print("Seshadhri", fileName)

        if fileName in requiredFiles.values():
            index = list(requiredFiles.values()).index(fileName)
            foundFiles[fileName] = index

    print("FOUND FILES:")
    print(foundFiles)

    trainIndex = next(
        index for fileName, index in foundFiles.items()
        if "train" in fileName.lower()
    )

    print("Training file index:", trainIndex)

    trainingData = pd.read_csv(allFiles[trainIndex])

    print(trainingData.head())

    return trainingData
    
def get_data(allFiles, requiredFiles, dataType):

    requiredFileName = requiredFiles[dataType]

    for file in allFiles:
        fileName = os.path.basename(file)

        if fileName == requiredFileName:
            return pd.read_csv(file)

    raise FileNotFoundError(f"{requiredFileName} not found")


def getResponseAndStatusCode(text_to_analyse, header, url):

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    print("Calling Watson...")
    print("URL:", url)
    print("Input:", input_json)

    response = requests.post(
        url,
        json=input_json,
        headers=header,
        timeout=30
    )

    print("Response received")

    status_code = response.status_code

    return response, status_code

# def getResponseAndStatusCode(text_to_analyse,header,url):
#     input_json = { "raw_document": { "text": text_to_analyse } }
#     response = requests.post(url, json=input_json, headers=header, timeout=30)
#     status_code = response.status_code
#     emotions = {}
#     if status_code == 200:
#         formatted_response = json.loads(response.text)
#         emotions = formatted_response['emotionPredictions'][0]['emotion']
#         dominant_emotion = max(emotions.items(), key=lambda x: x[1])
#         emotions['dominant_emotion'] = dominant_emotion[0]
#     elif status_code == 400:
#         emotions['anger'] = None
#         emotions['disgust'] = None
#         emotions['fear'] = None
#         emotions['joy'] = None
#         emotions['sadness'] = None
#         emotions['dominant_emotion'] = None  
#     return response, status_code,emotions


