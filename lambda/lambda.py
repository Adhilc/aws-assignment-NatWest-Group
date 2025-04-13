import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("S3 Event: %s", json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Event logged!')
    }