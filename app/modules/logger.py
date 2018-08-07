# logger.py

import sys
import json
import logging

from datetime import datetime

from app.modules.singleton import Singleton


@Singleton
class Logger:

    def __init__(self):
        self.process_id = ''
        self.process_owner = ''
        self.partner_queue = ''
        self.sub_process_id = ''
        self.is_ftp = ''
        self.recall_step_function = ''

    def log(self, message, severity=logging.INFO):

        if(isinstance(message, str) and isinstance(message, dict)):
            message = json.dumps(message.__dict__, ensure_ascii=False)

        message = self.configure_message(message)
        message = json.dumps(message, ensure_ascii=False)

        self.fire_log(severity, message)

    def fire_log(self, severity, message):
        logger = logging.getLogger()
        logger.setLevel(severity)
        logger.log(severity,message)

    def log_error(self, message, error):

        if(isinstance(error, str)):
            error = json.dumps(error, ensure_ascii=False)

        if(isinstance(message, str)):
            message = json.dumps(message, ensure_ascii=False)

        message = self.configure_message(message)
        if(error != None):
            message['error'] = error
        message = json.dumps(message, ensure_ascii=False)

        self.fire_log(logging.ERROR, message)

    def configure_message(self, message):

        message = {
            'processId': self.process_id,
            'message': message,
            'date':  str(datetime.now())
        }

        if(self.process_owner != None):
            message['processOwner'] = self.process_owner

        if(self.partner_queue != None):
            message['partnerQueue'] = self.partner_queue

        if(self.sub_process_id != None):
            message['subProcessId'] = self.sub_process_id

        return message

    def http_log(self, status_code, query_parameter, event, start, res_body):

        try:
            res_length = 0
            user_agent = ""
            consume_key = ""
            consumer_ip = ""

            if(res_body != None and type(res_body) != 'str'):
                try:
                    json.dumps(res_body, ensure_ascii=False)
                except:
                    res_body = ''
                res_length = sys.getsizeof(res_body)

            if(res_body == None or status_code == 200):
                res_body = {}

            if(event != None):
                if(type(event) != "dict"):
                    event = event.__dict__

                method = event['httpMethod'] if event['httpMethod'] != None else ''

                if(event['headers'] != None):
                    user_agent = event['User-Agent'] if event['User-Agent'] != None else ''
                    consume_key = event['X-API-KEY'] if event['X-API-KEY'] != None else ''

                if(event['requestContext'] != None
                        and event['requestContext']['identity'] != None
                        and event['requestContext']['identity']['sourceIp'] != None):
                    consumer_ip = event['requestContext']['identity']['sourceIp']

                object_log = {
                    'httpLog': True,
                    'date': start,
                    'duration': datetime.now() - start,
                    'method': method,
                    'statusCode': status_code,
                    'path': event['path'] if event['path'] != None else '',
                    'body': event['path'] if event['path'] != None else '',
                    'resBody': res_body,
                    'resLength': res_length,
                    'query': query_parameter if query_parameter != None else {},
                    'userAgent': user_agent,
                    'consumerKey': consume_key,
                    'consumerIp': consumer_ip
                }

                if(event['dataOrigin'] != None and event['cached'] != None):
                    object_log['dataOrigin'] = event['dataOrigin']
                    object_log['cached'] = event['cached']

                if(event['warmup'] != None):
                    object_log['warmup'] = event['warmup']

                if(event['coldStart'] != None):
                    object_log['coldStart'] = event['coldStart']

                self.log(object_log)

        except:
            exception = sys.exc_info()[0]
            self.log_error('HTTP-ERROR: error on generate log ', exception)
