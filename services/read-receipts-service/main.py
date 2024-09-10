import grpc
import json

from dapr.clients import DaprClient
from fastapi import FastAPI, HTTPException
import logging
import os


read_receipts_db = os.getenv('READ_RECEIPTS_TABLE', 'read-receipts-service-table')
group_subscription_topic = os.getenv('GROUP_SUBSCRIPTION_TOPIC', 'group-subscription-topic')

from models.read_receipt_model  import ReadReceiptModel
app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
def health_check():
    return {"Health is Ok"}

@app.post('/read-receipts/group/messages')
def add_read_receipts(message: ReadReceiptModel ):
    return