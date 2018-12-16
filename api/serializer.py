from flask_restplus import fields
from . import restplus

# Data models

bucket = restplus.api.model('Peer Company Benchmarks', {
    'peer_group_attribute': fields.String(attribute='peer_group_attribute'),
    'peer_group_attribute_value': fields.String(attribute='peer_group_attribute_value'),
    'average_peer_group_value': fields.String(attribute='average_peer_group_value')
    })

response = restplus.api.model('Query Response', {
    'company': fields.String(attribute='company_name'),
    'metric': fields.String(attribute='query_metric'),
    'average_metric_value': fields.String(attribute='value'),
    'benchmarks' : fields.List(fields.Nested(bucket))
    })

