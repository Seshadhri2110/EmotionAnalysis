from Configuration.Configuration import downloadDataset,getFiles,readConfiguration,getCSVfiles
from Configuration.Configuration import get_training_data,get_data,getResponseAndStatusCode
#from Configuration.Configuration import getRequiredVFiles
import pandas as pd
import os
from flask import Flask, request,jsonify, render_template

# create a flask application
app = Flask(__name__)
# Read the configuration
config = readConfiguration()
url = config['IBMWatsonNLPURL']
header = {'grpc-metadata-mm-model-id': config['grpc-metadata-mm-model-id']}
print("configuration is",config)
kagglepath = config["kagglepath"]
filepath = downloadDataset(kagglepath)
allFiles = getFiles(filepath)
csvFiles = getCSVfiles(allFiles)
csvFileLength = len(csvFiles)
requiredFiles = config["requiredFiles"]
trainingData = get_training_data(allFiles, requiredFiles)
trainingData = get_data(allFiles, requiredFiles, "trainingData")
testingData = get_data(allFiles, requiredFiles, "testingData")
validationData = get_data(allFiles, requiredFiles, "validationData")
print("I am here")
# #Giving a text and verifying the emotions using Watson NLP
# EmotionText = config["EmotionText"]
# #response, status_code, emotions=getResponseAndStatusCode(EmotionText,header,url)
# response, status_code =getResponseAndStatusCode(EmotionText, header, url)
# #print(emotions)
# print("Status:", status_code)
# print("Response:", response.text)
# print("I am here2")
# #Flask route

# @app.route("/", methods = ["GET", "POST"])
# def emotion_detection():
#     emotion_result = None
#     status_cose = None
#     error_message = None

#     #When the user presses the button
#     if request.method == "POST":
#         # Get text entered in HTML
#         EmotionText = request.form.get("textToAnalyze")
#         print("\nTextReceived:")
#         print(EmotionText)

#     if not EmotionText:
#         error_message = "Please enter some text."
#     else:
#         try:
#             response, status_code =(getResponseAndStatusCode(EmotionText,header,url))
#             if status_code == 200:
#                 emotion_result = response.json()
#             else:
#                 error_message = ("Watson NLP returned" f'status code {status_code}')
#         except Exception as e:
#             error_message = str(e)

#     return render_template("index.html", emotion_result=emotion_result, status_code = status_code, error_message= error_message)

@app.route("/", methods=["GET", "POST"])
def emotion_detection():

    EmotionText = ""
    emotion_result = None
    status_code = None
    error_message = None

    if request.method == "POST":

        EmotionText = request.form.get(
            "textToAnalyze",
            ""
        )

        print("Text received:", EmotionText)

        if not EmotionText.strip():

            error_message = "Please enter some text."

        else:

            try:

                response, status_code = getResponseAndStatusCode(
                    EmotionText,
                    header,
                    url
                )

                if status_code == 200:

                    emotion_result = response.json()

                else:

                    error_message = (
                        f"Watson NLP returned "
                        f"status code {status_code}"
                    )

            except Exception as e:

                error_message = str(e)

    return render_template(
        "index.html",
        emotion_result=emotion_result,
        status_code=status_code,
        error_message=error_message
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )











