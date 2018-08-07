from flask import Blueprint
from flask_restplus import Api

from .capitalize import capitalize
from .timing import timing


api_v1 = Api(
          title='Flask Serverless Api',
          version='1.0',
          description='The basic code for serverless with python',
          )


api_v1.add_namespace(capitalize)
api_v1.add_namespace(timing)
