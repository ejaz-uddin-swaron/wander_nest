import uuid
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from payments.models import Payment

class SSLCommerzPaymentView(APIView):
    permission_classes = [IsAuthenticated]  # Enforce login with token

    def post(self, request):
        user = request.user  # 🔐 Secure way to get the logged-in user
        data = request.data
        amount = data.get('amount')

        if not amount:
            return Response({"error": "amount is required"}, status=400)

        tran_id = str(uuid.uuid4())

        # Save payment
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
            "success_url": "http://localhost:3000/dashboard/",
            "fail_url": "http://localhost:3000/confirm-book/",
            "cancel_url": "http://localhost:3000/hotels-rooms/",
            "emi_option": 0,

            "cus_name": data.get("customer_name", "Test Customer"),
            "cus_email": data.get("customer_email", "test@email.com"),
            "cus_add1": "Dhaka",
            "cus_add2": "Mohakhali",
            "cus_city": "Dhaka",
            "cus_state": "Dhaka",
            "cus_postcode": "1212",
            "cus_country": "Bangladesh",
            "cus_phone": data.get("customer_phone", "01711111111"),
            "cus_fax": "N/A",

            "shipping_method": "NO",
            "ship_name": "Test Customer",
            "ship_add1": "Dhaka",
            "ship_add2": "Mohakhali",
            "ship_city": "Dhaka",
            "ship_state": "Dhaka",
            "ship_postcode": "1212",
            "ship_country": "Bangladesh",

            "product_name": data.get("service_name", "Wander Tour"),
            "product_category": "Tourism",
            "product_profile": "general"
        }

        response = requests.post("https://sandbox.sslcommerz.com/gwprocess/v4/api.php", data=ssl_payload)
        res_data = response.json()

        if res_data.get('status') == 'SUCCESS':
            return Response({"status": "SUCCESS", "GatewayPageURL": res_data["GatewayPageURL"]})

        return Response(res_data, status=400)
