from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def Auth(configPath):
    gauth = GoogleAuth()
    credentialPath = configPath + "credentials.json"
    clientSecretsPath = configPath + "client_secrets.json"
    if not os.path.exists(credentialPath):
        f = open(credentialPath,"w+")
        f.close()
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = clientSecretsPath
    gauth.LoadCredentialsFile(credentialPath)
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile(credentialPath)
    return gauth
def downloadFile(configPath,id,inputPath):
    mimetypes = {
        'application/vnd.google-apps.document': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.google-apps.presentation': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    }
    extension = {
        'application/vnd.google-apps.document': '.docx',
        'application/vnd.google-apps.spreadsheet': '.xlsx',
        'application/vnd.google-apps.presentation': '.pptx'
        }
    authToken = Auth(configPath)
    drive = GoogleDrive(authToken)
    file = drive.CreateFile({'id' : id})
    filename = file['title']
    download_mimetype = None
    if file['mimeType'] in mimetypes:
        download_mimetype = mimetypes[file['mimeType']]
        file.GetContentFile(inputPath + filename+extension[file['mimeType']], mimetype=download_mimetype)

def uploadFile(configPath,pathToFile):
    authToken = Auth(configPath)
    filename = os.path.basename(pathToFile)
    drive = GoogleDrive(authToken)
    file = drive.CreateFile({'title': filename})
    file.SetContentFile(pathToFile) 
    file.Upload()