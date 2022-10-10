from django.urls import path
from .views import Home_PageView, GetProfile, PostView

urlpatterns = [
    path('<str:pk>', Home_PageView.as_view(), name= "Profile"),
    path('profile/', GetProfile.as_view(), name= "ProfileIndividual"),
    path('createpost/', PostView.as_view())
]








# Phase 1:
# My profile and its pricing prompts.










#Dynamo db
# from dynamodb_json import json_util as dynamodb_json
# from .models import YourModel

# def get(request, partition_key):
#     table = boto3.resource(
#         'dynamodb',
#         aws_access_key_id=...,
#         aws_secret_access_key=...,
#         region_name=...,
#     ).Table(some_table_name)
#     try:
#         response = table.get_item(
#             Key={partition_key: partition_key})
#     except ClientError as e:
#         logger.warning(e.response['Error']['Message'])
#     else:
#         data_str = response['Item']
#         _data_dict = dynamodb_json.loads(data_str)

#         # Validation and modification of incoming data goes here.
#         data_dict = validation_and_modification(_data_dict)
#         # Then you can do whatever you need, for example:
#         obj, created = YourModel.objects.update_or_create(**data_dict)
#         ...
