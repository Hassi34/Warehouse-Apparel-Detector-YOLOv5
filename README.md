<p align="center">
    <b>
        <h1 align="center">🧑🏻‍🏭 Warehouse Apparel Detector 👨🏻‍🔧</h1>
    </b>
</p>
<!-- <p align="center">
    <em>A Vision AI based object detection web app to detect the warehouse apparel present in the image</em>
</p> -->
<p align="center">
<a href="https://github.com/Hassi34/Warehouse-Apparel-Detector-YOLOv5">
    <img src="https://readme-typing-svg.demolab.com?font=Georgia&c=g&size=18&duration=3000&pause=6000&multiline=True&center=true&width=800&height=40&lines=A+Vision+AI+based+object+detection+web+app+to+detect+the+warehouse+apparel+present+in+the+image;" alt="Typing SVG" />
</a>
<a href="https://github.com/Hassi34/Warehouse-Apparel-Detector-YOLOv5">
    <img src="https://readme-typing-svg.demolab.com?font=Georgia&size=18&duration=2000&pause=1000&multiline=False&color=10D736FF&center=true&width=400&height=40&lines=AI+%7C+Computer+Vision+%7C+Web+App%7C+REST+API;Python+%7C+3.7+%7C+3.8+%7C+3.9+%7C+3.10;YOLOv5+%7C+Flask" alt="Typing SVG" />
</a>
</p>

<p align="center">
    <a href="https://github.com/Hassi34/Warehouse-Apparel-Detector-YOLOv5/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/hassi34/Warehouse-Apparel-Detector-YOLOv5?color=g">
    </a>
    <a href="https://github.com/Hassi34/Warehouse-Apparel-Detector-YOLOv5">
        <img alt="Last Commit" src="https://img.shields.io/github/last-commit/hassi34/Warehouse-Apparel-Detector-YOLOv5/main?color=g">
    </a>
    <a href="https://github.com/Hassi34/Warehouse-Apparel-Detector-YOLOv5">
        <img alt="Code Size" src="https://img.shields.io/github/languages/code-size/hassi34/Warehouse-Apparel-Detector-YOLOv5?color=g">
    </a>
    <a href="https://github.com/Hassi34/Warehouse-Apparel-Detector-YOLOv5">
        <img alt="Repo Size" src="https://img.shields.io/github/repo-size/hassi34/Warehouse-Apparel-Detector-YOLOv5?color=g">
    </a>
</p>
<p align="center">
    <img width="450" height="300" src="static/web.gif" alt="About Web-App">
    <img width="450" height="300" src="static/inferences.gif" alt="Iferences">
</p>

## Overview
This is a web app empowered by Vision AI to detect the warehouse apparel in the image.The model is trained using YOLOv5.After successful deployment of the application, the REST API for the service will be exposed to the web so users can use the web interface or the REST API.<br>
Following are the major contents to follow, you can jump to any section:

>   1. [Run Locally](#run-local)
>   2. [Model Training](https://github.com/Hassi34/Warehouse-Apparel-Detector-YOLOv5/blob/main/Yolov5_custom_training.ipynb)
>   3. [REST API](#rest-api)

## Run Locally<a id='run-local'></a>

Clone the project

```bash
  git clone https://github.com/Hassi34/Warehouse-Apparel-Detector-YOLOv5.git
```

Go to the project directory

```bash
  cd Warehouse-Apparel-Detector-YOLOv5
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```
## REST API<a id='rest-api'></a>
```python
import requests
import base64

IN_IMG_PATH = "./in.jpg"
OUT_IMG_PATH = "./out.jpg"
ENDPOINT = "http://127.0.0.1:5000/predict"

def decodeImage(imgstring, OUT_IMG_PATH):
    imgdata = base64.b64decode(imgstring)
    with open(OUT_IMG_PATH, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(IN_IMG_PATH):
    with open(IN_IMG_PATH, "rb") as f:
        return base64.b64encode(f.read())

if __name__ == '__main__':

    BASE64_STR = encodeImageIntoBase64(IN_IMG_PATH).decode("utf-8")
    res = requests.post(ENDPOINT, json={"image":BASE64_STR})

    if res.status_code == 200:
        res = res.json()
        decodeImage(res["image"], OUT_IMG_PATH)
    else :
        print(res)
```
#### **Thank you for visiting 🙏 I hope you found this project useful**<br><br>

**Copyright &copy; 2022 Hasanain** <br>
Let's connect on **[``LinkedIn``](https://www.linkedin.com/in/hasanain-mehmood)** <br>