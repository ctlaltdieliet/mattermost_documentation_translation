import os
import requests
import json
import re
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


mainfolder='C:/data/mm/' 
docsfolderEnglish='docs-master/source' #relative to mainfolder
translationfolder='C:/data/mm/translations/' #absolute path
languages=['nl','fr','de']
extensions=['rst','html']
folder=os.path.join(mainfolder,docsfolderEnglish)

 
        
 

def search_files(directory, extension='srt'):
    filelist= []
    counter=0
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                filedict={'name':name,'path':dirpath,'fullpath':os.path.join(dirpath, name)}
                filelist.append(filedict)
    return filelist


def translate(text,language):
    modelid='en-'+language
    authenticator = IAMAuthenticator('hidden')
    language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
    language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/hidden')
    translationibm = language_translator.translate(text=piece,model_id=modelid).get_result()
    return translationibm    

for extension in extensions:
    for language in languages:
        files=search_files(folder,extension)
        for englishfile in files:
            try:
                print(englishfile['fullpath'])
                f = open(englishfile['fullpath'], 'rb')
                origpath=englishfile['fullpath']
                relativepath=origpath.split(mainfolder)[1]
                pathtocreate=relativepath.replace(englishfile['name'],'')
                
                if not os.path.exists(translationfolder+'/'+language+'/'+pathtocreate):
                    os.makedirs(translationfolder+'/'+language+'/'+pathtocreate)
        
                newpath=os.path.join(translationfolder+'/'+language+'/'+relativepath)
                fulltranslation=''
                counter=1
                translatedfile=open(newpath,'w')
                piece = f.read(3024*counter)
                piece=piece.decode('utf-8').strip()
                while  piece:
                    translationibm=translate(piece,language)
                    for translatedtext in translationibm['translations']:
                        fulltranslation=fulltranslation+translatedtext['translation']+"\n"
                    counter=counter+1
                    piece = f.read(3024*counter)
                    piece=piece.decode('utf-8').strip()
            except:
                print("something went wrong with file:" +englishfile['fullpath'])
                
            translatedfile.write(fulltranslation)
            translatedfile.close()
            f.close()
