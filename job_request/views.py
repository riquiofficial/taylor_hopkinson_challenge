from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework import status
from .models import *

# Create your views here.


@api_view(["GET", "POST"])
def new_job(request):
    if request.method == "POST":
        # Submit my details - Simplified Submission
        Model = JobApplication
        # if nothing posted, generate sample data

        application = {"job_id": 101,
                       "candidate_email": "example@example.com"}

        try:
            JobApplication.objects.get(
                job_id=application['job_id'], candidate_email=application['candidate_email'])
            return JsonResponse(application, status=status.HTTP_208_ALREADY_REPORTED)

        except JobApplication.DoesNotExist:
            # if does not exist try to create the application
            job = Job.objects.get(id=application['job_id'])
            Model.objects.create(
                job_id=job, candidate_email=application['candidate_email'])
            return JsonResponse(application, status=status.HTTP_201_CREATED)

    elif request.method == "GET":
        # Get job details - Example Simplified Response
        Model = Job
        job_request = Model.objects.get(id=101)
        job = {"id": job_request.id, "name": job_request.name,
               "role": job_request.role}

        return JsonResponse(job, status=status.HTTP_200_OK)
