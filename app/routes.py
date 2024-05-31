from flask import Blueprint, request, jsonify


api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def index():
    return('Hello World')