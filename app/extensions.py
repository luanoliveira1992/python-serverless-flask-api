try:
  import unzip_requirements
except ImportError:
  pass

import os
from flask_cors import CORS
from flask_restplus import Api




'''
Extensões do Flask

'''
cors = CORS()
restplus = Api()




