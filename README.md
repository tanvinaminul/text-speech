# text-speech
## Convert text input into audio
## Requirements
* Azure Speech Service
* Python Speech SDK for Azure
## Set up the environment
### Create python Virtual Environment
```
python -m venv Speech
```
### Activate the Virtual Environment
```
Scripts\Activate
```
### Install Speech SDK
```
pip install azure-cognitiveservices-speech
```
## Run File
Replace YOUR_SPEECH_SERVICE_KEY, REGION_OF_SERVICE, YOUR_PREFERRED_VOICE, YOUR_DESIRED_FILE_NAME as your service credentials. Then run this command
```
python speech.py
```
You will get the output file is same directory
