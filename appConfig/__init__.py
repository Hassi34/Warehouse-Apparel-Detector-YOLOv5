import os 
from pathlib import Path

STATIC_DIR = Path(os.getcwd(),"static")

IMAGES_DIR = os.path.join(STATIC_DIR,"images")
os.makedirs(IMAGES_DIR, exist_ok=True)
INFERENCE_DIR = os.path.join(IMAGES_DIR,"inference")
os.makedirs(INFERENCE_DIR, exist_ok=True)

IMG_IN = os.path.join(INFERENCE_DIR, f"in.jpg")
IMG_OUT = os.path.join(INFERENCE_DIR, f"out.jpg")
COLOR_IMG_OUT = os.path.join(INFERENCE_DIR, f"color_img.jpg")

ARTIFACTS = Path("artifacts")
FINAL_MODEL = os.path.join(ARTIFACTS, "best.pt")

CONF_THRES = 0.50
IOU_THRES = 0.45
DEVICE = 'cpu'

PORT = 5000
HOST = '0.0.0.0'
DEBUG = False

