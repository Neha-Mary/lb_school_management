from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import *

class CustomLoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)


            if user.is_superuser or user.is_staff:
                role="Admin"
                redirect_url = "/admin_dashboard"
                response_data = {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "role": role,
                    "redirect_url": redirect_url,
                    "email": user.email,
                    "full_name": user.full_name,
                }
            elif user.is_officestaff:
                role = "office Staff"
                redirect_url = "/officestaff_dashboard"
                custom_id = user.office_staff.first().custom_id
                response_data = {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "role": role,
                    "redirect_url": redirect_url,
                    "email": user.email,
                    "full_name": user.full_name,
                    "custom_id": custom_id,
                }
            elif user.is_librarian:
                role = "Librarian"
                redirect_url = "/librarian_dashboard"
                custom_id = user.librarian.first().custom_id

                response_data = {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "role": role,
                    "redirect_url": redirect_url,
                    "email": user.email,
                    "full_name": user.full_name,
                    "custom_id": custom_id,
                }
            else:
                return Response({"error":"User role not defined"},status = status.HTTp_400_BAD_REQUEST)
            
            return Response(response_data,status=status.HTTP_200_OK)
        
        return Response({"error":"Invalid email or password"},status=status.HTTP_401_UNAUTHORIZED)