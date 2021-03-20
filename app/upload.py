from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from flask import Blueprint
from flask_jwt_extended import jwt_required

bp = Blueprint("upload", __name__)
azure_endpoint = "https://store-med.cognitiveservices.azure.com/"

@bp.route("/file")
@jwt_required()
def upload_file():
    pass
