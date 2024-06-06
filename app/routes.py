import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from .validation import *
from .mediapipe_handler import GestureRecognizer


api = Blueprint('api', __name__)
gesture_recognizer = GestureRecognizer()

@api.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image_file' not in request.files:
            raise BusinessValidationError(
                status_code=400, 
                error_message="Image file not found. Ensure that multipart/form-data contains key - 'image_file'"
            )
    
        image_file = request.files['image_file']

        if image_file.filename:
            filename = secure_filename(image_file.filename)
            temp_path = os.path.join('/temp', filename)
            image_file.save(temp_path)
            
            result = gesture_recognizer.process_image(image_file=temp_path)
            os.remove(temp_path)

            try:
                return jsonify({
                    'handedness' : result.handedness[0][0].category_name,
                    'gesture' : result.gestures[0][0].category_name
                })
            
            except:
                return jsonify({
                    'message' : 'No hand detected in the image.'
                })
            
        else:
            raise BusinessValidationError(status_code=400, error_message='Image file not found')


    except BusinessValidationError as error:
        return error.response
    
    except Exception as error:
        print(error)
        raise InternalServerError(error_message='Internal Server Error')
