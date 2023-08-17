import argparse 
import json
import requests
import io
from PIL import Image
import os

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": f"Bearer {os.env.get("HUGG_KEY"}"}

def get_predictions(word) -> io.BytesIO:
	response = requests.post(API_URL, headers=headers, json={"inputs": word})
	return io.BytesIO(response.content)


parser = argparse.ArgumentParser(
    prog="text2image"
)

parser.add_argument("-f", "--file", help="JSON file path", required=True, type=str)
parser.add_argument("-n", help="N images", required=False, default=1, type=int)
parser.add_argument("--no-save", help="save image on GDrive or not", default=True, required=False, action="store_true")
args = parser.parse_args()
file_path = args.file
n_images = args.n
no_save = args.no_save

with open(file_path) as file:
    words = json.load(file)


for prof_level in words.keys():
    for theme in words[prof_level]:
        for word_dict in words[prof_level][theme]:
            word = word_dict["word"]
            definition = word_dict["definitions"][0]
            for idx in range(n_images):
                image = Image.open(get_predictions(word + ' - ' + definition))

                img_path = f"images/{word}-{idx}.png"
                image.save(img_path)
                if not no_save:


                    from pydrive.auth import GoogleAuth
                    from pydrive.drive import GoogleDrive


                    gauth = GoogleAuth()        
                    gauth.LocalWebserverAuth()   
                    drive = GoogleDrive(gauth)  

                    gd_file = drive.CreateFile({'title': f"{word}.png"})
                    gd_file.SetContentFile(img_path)
                    gd_file.Upload()

                    gd_file = None
