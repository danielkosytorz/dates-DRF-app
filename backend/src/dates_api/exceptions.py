from rest_framework import status
from rest_framework.exceptions import APIException


class NumbersAPIErrorException(APIException):
    default_code = "error"
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Numbers API error."
