import grpc
import json

from dapr.clients import DaprClient
from fastapi import FastAPI, HTTPException
import logging
import os


read_receipts_db = os.getenv('DAPR_READ_RECEIPTS_TABLE', '')
pubsub_name = os.getenv('DAPR_PUB_SUB', '')
send_message_topic = os.getenv('DAPR_SEND_MESSAGE_TOPIC', '')

from models.read_receipt_model  import ReadReceiptModel
app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post('/v1.0/subscribe/group/messages')
def add_read_receipts(message: ReadReceiptModel ):
    return