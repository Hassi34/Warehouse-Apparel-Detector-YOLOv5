import sys 
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = ROOT.relative_to(Path.cwd())  # relative
import os
IMG_PATH = Path(os.path.join(ROOT, "unitTests", "test_img.jpg")).resolve()
from app import app
import unittest
from common import encodeImageIntoBase64
import json

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.base64_str = encodeImageIntoBase64(IMG_PATH).decode("utf-8")
        self.inference = self.app.post('/predict',
                            data=json.dumps(dict(image=self.base64_str)),
                            content_type='application/json')
    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        print(response)
        self.assertEqual(response.status_code, 200)
    
    def test_prediction(self):
        self.assertEqual(self.inference.status_code, 200)

    def test_content_type(self):
        self.assertEqual(self.inference.content_type, "application/json")

    def test_data(self):
        self.assertTrue(b'image' in self.inference.data)




if __name__ == '__main__':
    unittest.main()