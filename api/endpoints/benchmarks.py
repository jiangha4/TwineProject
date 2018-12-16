from .. import restplus
from .. import parser
from .. import metrics
from .. import serializer
from flask_restplus import Resource

ns = restplus.api.namespace('benchmarks', description='Operations for employee benchmarks')

@ns.route('/')
class BenchmarkCollection(Resource):
    @restplus.api.expect(parser.args, validate=True)
    @restplus.api.marshal_with(serializer.response)
    def get(self):
        """
            Get benchmark metrics
        """
        args = parser.args.parse_args()
        company = args['company']
        metric = args['metric']

        return metrics.response_object(company, metric)
