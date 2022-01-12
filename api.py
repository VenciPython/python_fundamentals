from flask import Flask, request
from flask_restx import Resource, Api
from qr_code_generator import qr_code_generator_function

app = Flask(__name__)
api = Api(app)

qr_codes = []


@api.route('/mycode')
class TodoSimple(Resource):
    def get(self):
        qr_code_image = qr_code_generator_function(qr_codes[0])
        return qr_code_image

    def put(self, url):
        return qr_codes.append(url)
