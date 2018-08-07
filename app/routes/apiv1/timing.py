from flask_restplus import Namespace, Resource

timing = Namespace('timing')


@timing.route('/')
class CurrentTimeTest(Resource):
    def get(self):
        import datetime
        _date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return [{'date' : _date}]

