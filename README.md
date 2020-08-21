# Google Drive Download/Upload
 A collection of scripts to download or upload files from Google Drive

# How To Run
Make sure Pydrive is installed
```sh
    python install_dependencies.py
```
Run which ever function you need.
```sh
downloadFile(configPath,id,inputPath)
```
`configPath` is the folder that holds the credentials
`id` is the Shareble id of the file
`inputPath` is the path to where the file should be downloaded.
 
 ```sh
 uploadFile(configPath,pathToFile)
 ```
 `configPath` is the folder that holds the credentials
 `pathToFile` is the path to where the file exists.