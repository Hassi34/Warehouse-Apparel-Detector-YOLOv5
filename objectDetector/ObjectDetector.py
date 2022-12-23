import sys
import os
sys.path.append(os.path.abspath("./"))

import cv2
import json
import torch
import numpy as np
from PIL import Image
from common import encodeImageIntoBase64
import appConfig as CONFIG
from objectDetector.detect import run


class Detector:
	def inference(self):
		run(weights=CONFIG.FINAL_MODEL, source= CONFIG.INFERENCE_DIR, conf_thres=CONFIG.CONF_THRES, 
			iou_thres=CONFIG.IOU_THRES, device=CONFIG.DEVICE, project='static/images', name = 'inference', exist_ok=True)
		#bgr_image = cv2.imread(CONFIG.IMG_OUT)
		#im_rgb = cv2.cvtColor(bgr_image, cv2.COLOR_RGB2BGR)
		#cv2.imwrite(CONFIG.COLOR_IMG_OUT, im_rgb)
		opencodedbase64 = encodeImageIntoBase64(CONFIG.IMG_OUT)
		result = {"image": opencodedbase64.decode('utf-8')}
		return result

	def clean_up(self):
		try:
			imgs = os.listdir(CONFIG.INFERENCE_DIR)
			[os.remove(os.path.join(CONFIG.INFERENCE_DIR, img)) for img in imgs]
		except:
			pass




