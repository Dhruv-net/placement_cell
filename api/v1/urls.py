from django.urls import path
from django.urls import include
from applicants.views import ApplicantProfile as ApplicantProfile
from applicants.views import ApplicantView as Applicant
from applicants.views import ApplicationView as Application
from attachments.views import Attachment

urlpatterns = [
    path("applicant/create/", Applicant.as_view(), name="create-applicant"),
    path("applicantprofile/create/", ApplicantProfile.as_view(), name="create-applicant-profile"),
    path("application/create/", Application.as_view(), name= "create-app"),
    path("attachment/create/", Attachment.as_view(), name="create-attachment"),
    path("org/create/", Org.as_view(), name="create-organisation"),
    path("job/", Job.as_view(), name="create-job"),
]
