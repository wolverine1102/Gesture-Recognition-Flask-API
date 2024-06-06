import os
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class GestureRecognizer:
    def __init__(self):
        self.model_path = os.path.join(os.path.dirname(__file__), '../models/gesture_recognizer.task')
        self.base_options = python.BaseOptions(model_asset_path=self.model_path)
        self.running_mode = vision.RunningMode.IMAGE
        self.options = vision.GestureRecognizerOptions(
            base_options=self.base_options,
            running_mode=self.running_mode
        )
        self.recognizer = vision.GestureRecognizer.create_from_options(self.options)

    def process_image(self, image_file):
        image = mp.Image.create_from_file(image_file)
        recognition_result = self.recognizer.recognize(image)

        return recognition_result


