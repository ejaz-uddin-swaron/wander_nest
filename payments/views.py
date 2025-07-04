import uuid
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from payments.models import Payment

User = get_user_model()

class SSLCommerzPaymentView(APIView):
    def post(self, request):
        data = request.data
        amount = data.get('amount')
        user_id = data.get('user_id')

        if not amount or not user_id:
            return Response({"error": "user_id and amount are required"}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        tran_id = str(uuid.uuid4())

        # ✅ Save to your local DB (Supabase handled by Django DB engine)
        Payment.objects.create(
            user=user,
            amount=amount,
            tran_id=tran_id,
            status="Pending"
        )

        ssl_payload = {
            "store_id": "byteb67e6e2713890c",
            "store_passwd": "byteb67e6e2713890c@ssl",
            "total_amount": amount,
            "currency": "BDT",
            "tran_id": tran_id,
            "success_url": "https://example.com/payment-success",
            "fail_url": "https://example.com/payment-fail",
            "cancel_url": "https://example.com/payment-cancel",
            "emi_option": 0,

            "cus_name": "Test Customer",
            "cus_email": "test@email.com",
            "cus_add1": "Dhaka",
            "cus_add2": "Mohakhali",
            "cus_city": "Dhaka",
            "cus_state": "Dhaka",
            "cus_postcode": "1212",
            "cus_country": "Bangladesh",
            "cus_phone": "01711111111",
            "cus_fax": "N/A",

            "shipping_method": "NO",
            "ship_name": "Test Customer",
            "ship_add1": "Dhaka",
            "ship_add2": "Mohakhali",
            "ship_city": "Dhaka",
            "ship_state": "Dhaka",
            "ship_postcode": "1212",
            "ship_country": "Bangladesh",

            "product_name": "Wander Tour",
            "product_category": "Tourism",
            "product_profile": "general"
        }

        response = requests.post("https://sandbox.sslcommerz.com/gwprocess/v4/api.php", data=ssl_payload)
        res_data = response.json()

        if res_data.get('status') == 'SUCCESS':
            return Response({"GatewayPageURL": res_data["GatewayPageURL"]})

        return Response(res_data, status=400)
