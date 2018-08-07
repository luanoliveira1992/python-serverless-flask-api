from flask_restplus import Namespace, Resource

capitalize = Namespace('capitalize')


@capitalize.route('/<string:text>/')
class Capitalize(Resource):
    def get(self, text):
        return {'text' : text.capitalize()}