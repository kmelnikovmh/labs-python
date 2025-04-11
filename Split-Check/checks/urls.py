from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'checks'

urlpatterns = [
    path("my_receipts/", login_required(views.my_receipts), name="my_receipts"),
    path("create_receipt/", login_required(views.create_receipt), name="create_receipt"),
    path("receipt/<int:receipt_id>/", login_required(views.receipt_detail), name="receipt_detail"),
    path("receipt/<int:receipt_id>/delete/", login_required(views.delete_receipt), name="delete_receipt"),
]
