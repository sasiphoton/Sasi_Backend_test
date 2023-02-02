from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .serializers import TFUserSerializer
from .models import TFUser
from rest_framework.decorators import api_view

import json


@api_view(['POST'])
def user_authentication(request):
    """
    This API is used to authenticate the user with the given user email.
    return:
     1. Success: user information
     2. Error code and status message
    """
    response = {}
    status = 200

    try:
        body = request.body.decode()
        content = json.loads(body)
        email = content['email']
        tf_obj = TFUser.objects.get(email=email)
        response['name'] = tf_obj.name
        response['email'] = tf_obj.email
        response['role'] = tf_obj.role

        # Checking for Admin
        if tf_obj.role == "Admin":
            # if Admin, check for other admins in the active_role column
            try:
                TFUser.objects.get(active_role='Admin')
            except ObjectDoesNotExist as exc_obj:
                tf_obj.active_role = "Admin"
                tf_obj.save()

        response['active_role'] = tf_obj.active_role

    except ObjectDoesNotExist:
        status = 404
        response['error_code'] = 'TF1000'
        response['err_msg'] = 'User not found in the TruFit Application'

    except Exception as err_obj:
        status = 500
        response["error_code"] = "TF1005"
        response["error_msg"] = f"Error With --> {err_obj}"

    return JsonResponse(response, status=status)


@api_view(['GET'])
def user_logout(request):
    response = {}
    status = 200

    try:
        body = request.body.decode()
        data = json.loads(body)

        user = TFUser.objects.get(email=data["email"])
        # check the user is admin or not
        if user.role == "Admin":
            user.active_role = "SalesEngineer"
            user.save()
        response["status_msg"] = "User Logged out successfully"

    except ObjectDoesNotExist as err_obj:
        status = 404
        response["error_code"] = "TF1003"
        response["error_msg"] = "User not exists"

    except Exception as err_obj:
        status = 500
        response["error_code"] = "TF1005"
        response["error_msg"] = f"Error With --> {err_obj}"

    return JsonResponse(response, status=status)


@api_view(['POST'])
def add_new_user(request):
    response = {}
    status = 201

    try:
        body = request.body.decode()
        data = json.loads(body)

        user_list = TFUser.objects.filter(email=data['email'])
        if user_list:
            status = 200
            response['error_code'] = "TF1001"
            response['error_msg'] = "User already exists"
        else:
            tf_obj = TFUser.objects.create(
                name=data['username'],
                email=data['email'],
                role=data['role'],
                active_role='SalesEngineer'
            )
            tf_obj.save()

            response['Status_msg'] = 'User created successfully'

    except Exception as err_obj:
        status = 500
        response["error_code"] = "TF5000"
        response["error_msg"] = f"Error With --> {err_obj}"

    return JsonResponse(response, status=status)


@api_view(['POST'])
def modify_user_information(request):
    response = {}
    status = 204

    try:
        body = request.body.decode()
        data = json.loads(body)
        user_obj = TFUser.objects.get(email=data['email'])

        user_obj.name = data['username']
        user_obj.email = data['email']
        user_obj.role = data['role']
        user_obj.save()

        response['Status_msg'] = 'User modified successfully'

    except ObjectDoesNotExist:
        status = 404
        response['error_code'] = "TF1003"
        response['error_msg'] = "User not exists"

    except Exception as err_obj:
        status = 500
        response["error_code"] = "TF1005"
        response["error_msg"] = f"Error With --> {err_obj}"

    return JsonResponse(response, status=status)


@api_view(['GET'])
def list_users(request):
    user_records = []
    response = {}
    status = 200

    try:
        records = TFUser.objects.all().values()

        for record in records:
            user_records.append(record)
        response['user_info'] = user_records

    except Exception as err_obj:
        status = 500
        response["error_code"] = "TF1005"
        response["error_msg"] = f"Error With --> {err_obj}"

    return JsonResponse(response, status=status)


@api_view(['GET'])
def delete_user(request):
    response = {}
    status = 405

    try:
        body = request.body.decode()
        data = json.loads(body)

        tf_obj = TFUser.objects.get(email=data["email"])
        tf_obj.delete()

        response["status_msg"] = "User deleted successfully"

    except ObjectDoesNotExist:
        status = 404
        response["error_code"] = "TF1003"
        response["error_msg"] = "User not exists"

    except Exception as err_obj:
        status = 500
        response["error_code"] = "TF1005"
        response["error_msg"] = f"Error With --> {err_obj}"

    return JsonResponse(response, status=status)


@api_view(['GET'])
def get_user_emails(request):
    response = {}
    email_list = []
    status = 200

    try:
        # To get user emails from DB
        emails = TFUser.objects.values_list('email')
        for email in emails:
            email_list.append(email[0])

        response['useremail'] = email_list

    except ObjectDoesNotExist:
        response["error_code"] = "TF1003"
        response["error_msg"] = "User not exists"
        status = 404

    except Exception as err_obj:
        status = 500
        response["error_code"] = "TF1005"
        response["error_msg"] = f"Error With --> {err_obj}"

    return JsonResponse(response, status=status)


@api_view(['GET'])
def get_user_information(request):
    response = {}
    status = 200

    try:
        body = request.body.decode()
        data = json.loads(body)

        # To get user emails from DB
        user = TFUser.objects.get(email=data['email'])

        response['username'] = user.name
        response['email'] = user.email
        response['role'] = user.role

    except ObjectDoesNotExist:
        status = 404
        response["error_code"] = "TF1003"
        response["error_msg"] = "User not exists"

    except Exception as err_obj:
        status = 500
        response["error_code"] = "TF1005"
        response["error_msg"] = f"Error With --> {err_obj}"

    return JsonResponse(response, status=status)
