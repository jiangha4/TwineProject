from flask_restplus import Api

api = Api(version='1.0', title='Twine API',
                  description='Demo of data benchmarks')

@api.errorhandler
def default_error_handler(e):
        message = 'An unhandled exception occurred.'
        return {'message': message}, 500
