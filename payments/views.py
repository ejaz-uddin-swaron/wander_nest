import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid

class SSLCommerzPaymentView(APIView):
    def post(self, request):
        data = request.data
        amount = data.get('amount', 10)  # Default to 10 Taka

        tran_id = str(uuid.uuid4())  # Generate unique transaction ID

        payment_data = {
            "store_id": "byteb67e6e2713890c",
            "store_passwd": "byteb67e6e2713890c@ssl",
            "total_amount": amount,
            "currency": "BDT",
            "tran_id": tran_id,
            "success_url": "https://example.com/payment-success",  # Replace later
            "fail_url": "https://example.com/payment-fail",
            "cancel_url": "https://example.com/payment-cancel",
            "emi_option": 0,

            # Customer Info (required)
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

            # Shipping Info (optional but recommended)
            "shipping_method": "NO",
            "ship_name": "Test Customer",
            "ship_add1": "Dhaka",
            "ship_add2": "Mohakhali",
            "ship_city": "Dhaka",
            "ship_state": "Dhaka",
            "ship_postcode": "1212",
            "ship_country": "Bangladesh",

            # Product info
            "product_name": "Wander Tour",
            "product_category": "Tourism",
            "product_profile": "general"
        }

        url = "https://sandbox.sslcommerz.com/gwprocess/v4/api.php"

        try:
            response = requests.post(url, data=payment_data)
            res_data = response.json()

            if res_data.get('status') == 'SUCCESS':
                return Response({"GatewayPageURL": res_data['GatewayPageURL']})
            else:
                return Response(res_data, status=status.HTTP_400_BAD_REQUEST)

        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
