from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models1 import CustomUser,AdminTables,UserTokenTable,AdminStatusTable,AdminTokenTable,OTPVerification_TABLE,profile_image_table
from rest_framework.decorators import api_view
from .serializers1 import UserSerializer,AdminSerializer,UserTokenSerializer,AdminStatusChangeSerializer,AdminTokenSerializer,ImageSerializer
from rest_framework.permissions import IsAuthenticated
import jwt,datetime
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_protect 
import json
from rest_framework.exceptions import AuthenticationFailed


class UserSignIN(APIView):
    def post(self,request):
        token = request.headers.get('Authorization')
        print('token',token)

        if not token:
            
            serializer=UserSerializer(data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'User has been created successfully ','data':serializer.data,'status':status.HTTP_200_OK},status.HTTP_200_OK)

        # The token obtained from the header might be prefixed with "Bearer "
        # Remove the "Bearer " prefix if present
        token = token.replace('Bearer ', '')
        

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

        userId = payload['id']
        users=CustomUser.objects.filter(id=userId).first()
        if not users:
            return Response({'error':'User Not found'},status.HTTP_404_NOT_FOUND)
            

        try:
            serializer=UserSerializer(data=request.data)
            
            if serializer.is_valid():
                user=serializer.save()
                x=user.ammounts
                user.ammounts=user.ammounts+users.ammounts/2
                user.save()
                users.ammounts=users.ammounts+x
                users.save()
                
                return Response({'message':'User has been created successfully','ref_user_ammt':users.ammounts,'data':serializer.data,'status':status.HTTP_200_OK},status.HTTP_200_OK)
            
            else:
                return Response({'error':serializer.errors},status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'error':str(e)},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class UserLogIn(APIView):
    def post(self,request):
        try:
            email=request.data.get('email')
            password=request.data.get('password')
            
            if not email:
                return Response({'error':'Invalid Email','status':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
            
            user=CustomUser.objects.filter(email=email).first()
            user.ammounts+=50
            user.save()

            
            if not user:
                return Response({'error':'User not found','status':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
            
            if not check_password(password,user.password):
                return Response({"error": "Password entered is wrong, please check and try again",'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            serializer=UserSerializer(user)
            if serializer:
               
            
            
                if check_password(password,user.password):
                    payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=9),
                    'iat': datetime.datetime.utcnow()
                    }

                    token = jwt.encode(payload=payload, key='secret', algorithm='HS256')
                
                
                    token_table_instance = UserTokenTable.objects.filter(user_id=user.id).first()

          # If an existing token entry exists, update the token, else create a new entry
                    if token_table_instance:
                        token_table_instance.token_store = token
                        token_table_instance.save()
                    else:
                        token_table_instance = UserTokenTable.objects.create(
                        user_id=user.id,
                        token_store=token,
                        email=user.email
                        )
                    return Response({'message':"User Login Successfully",'token':token,'data':serializer.data,'status':status.HTTP_200_OK},status.HTTP_200_OK)
                
        except Exception as e:
            return Response({'error':str(e),'status':status.HTTP_500_INTERNAL_SERVER_ERROR},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
class useReferal(APIView):
    def post(self, request):
        
        token = request.headers.get('Authorization')

        if not token:
            raise AuthenticationFailed('Token is required for this operation')

        # The token obtained from the header might be prefixed with "Bearer "
        # Remove the "Bearer " prefix if present
        token = token.replace('Bearer ', '')
        

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

        userId = payload['id']

        # Retrieve the token instance from the AdminTokenTable
        try:
            token_instance = UserTokenTable.objects.filter(user_id=userId).all()
            tokens=AdminTokenTable.objects.filter(user_id=userId).all()
            if token_instance is None and tokens is None:
                return Response({'error':"Token not found",'status':status.HTTP_404_NOT_FOUND},status.HTTP_404_NOT_FOUND)

            user=CustomUser.objects.filter(id=userId).first()
            user.ammounts=user.ammounts+30
            user.save()
            serializer=UserSerializer(user)
        
      
            if serializer:
             
                return Response({'message': 'Video Upload successfully', 'data': serializer.data,'status':status.HTTP_200_OK},status=200)
            else:
                return Response({'message': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':str(e)},status=500)
   
class UserLogOut(APIView):
    def post(self,request):
        try:
            email=request.data.get('email')
            
            if not email:
                return Response({'error':'Please Enter Valid Email','status':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
            
            
            user=CustomUser.objects.filter(email=email).first()
            
            if not user:
                return Response({'error':'Coach not found','status':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
            
            if user:
                return Response({'message':'Coach Logout Successfull','status':status.HTTP_200_OK},status.HTTP_200_OK)
            
        except Exception as e:
            return Response({'error':str(e),'status':status.HTTP_500_INTERNAL_SERVER_ERROR},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
class UserDetails(APIView):
    def get(self,request,id=None):
        try:
            if id is None:
                user=CustomUser.objects.all().order_by('-id')
                
                serializer=UserSerializer(user,many=True)
                
                
                return Response({'message':'All user details found successfully','data':serializer.data,'status':status.HTTP_200_OK},status.HTTP_200_OK)
                
                
            if id:
                user=CustomUser.objects.filter(id=id).first()
                serializer=UserSerializer(user)
                
            
                return Response({'message':'User details found successfully','data':serializer.data,'status':status.HTTP_200_OK},status.HTTP_200_OK)
                
        except Exception as e:
            return Response({'error':'ERROR','data':str(e),'status':status.HTTP_500_INTERNAL_SERVER_ERROR},status.HTTP_500_INTERNAL_SERVER_ERROR)
            


class User_profile_update(APIView):
   
    def put(self,request,id=None):
        try:
     
           if id is None:
               return Response({'error': 'User id not found', 'status': status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
           
    
           user = CustomUser.objects.get(id=id)
           
           
           if user is None:
               return Response({'error': 'User not found', 'status': status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)

           serializer = UserSerializer(user, data=request.data, partial=True)
           if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Profile updated successfully', 'data': serializer.data, 'status': status.HTTP_200_OK})
      
           
           else:
                return Response({'error': serializer.errors,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            
            return Response({'Message': 'Internal Server Error', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR},status.HTTP_500_INTERNAL_SERVER_ERROR)


           
        
        
#ADMIN code ---------------------------------------------------------------------------------------

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class AdminSignIN(APIView):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request):
        try:
            serializer = AdminSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User has been created successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
            
            else:
                return Response({'error': serializer.errors}, status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)

        
        
class AdminLogIn(APIView):
    def post(self,request):
        try:
            email=request.data.get('email')
            password=request.data.get('password')
            
            if not email:
                return Response({'error':'Invalid Email','status':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
            
            user=AdminTables.objects.filter(email=email).first()
            
            if not user:
                return Response({'error':'User not found','status':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
            
            if not check_password(password,user.password):
                return Response({"error": "Password entered is wrong, please check and try again",'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            
            if user:
                if check_password(password,user.password):
                    return Response({'message':"Admin Login Successfully",'status':status.HTTP_200_OK},status.HTTP_200_OK)
                
        except Exception as e:
            return Response({'error':str(e),'status':status.HTTP_500_INTERNAL_SERVER_ERROR},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class AdminLogOut(APIView):
    def post(self,request):
        try:
            email=request.data.get('email')
            
            if not email:
                return Response({'error':'Please Enter Valid Email','status':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
            
            
            user=AdminTables.objects.filter(email=email).first()
            
            if not user:
                return Response({'error':'Admin not found','status':status.HTTP_400_BAD_REQUEST},status.HTTP_400_BAD_REQUEST)
            
            if user:
                return Response({'message':'Admin Logout Successfull','status':status.HTTP_200_OK},status.HTTP_200_OK)
            
        except Exception as e:
            return Response({'error':str(e),'status':status.HTTP_500_INTERNAL_SERVER_ERROR},status.HTTP_500_INTERNAL_SERVER_ERROR)
            







# Media section using AWS cloud Storage

from rest_framework.parsers import MultiPartParser, FormParser
class Imageupload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        print(serializer)
      
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Image Upload successfully', 'data': serializer.data})
        
        # Handle case when serializer is not valid
        return Response({'message': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
# views.py

from django.http import JsonResponse
from .models1 import FormSubmission, GoogleForm

def submit_form(request):
    if request.method == 'POST':
        # Process form submission
        submission = FormSubmission.objects.first()
        if submission is None:
            # Create a default instance if it doesn't exist
            submission = FormSubmission.objects.create(submission_count=0)
        
        # Increment the submission count
        submission.submission_count += 1
        submission.save()
        
        # Get Google Form links
        google_form = GoogleForm.objects.first()
        pre_link = google_form.pre_link
        post_link = google_form.post_link
        mid_link = google_form.mid_link

        # Construct response JSON
        response_data = {
            'message': 'Form submitted successfully',
            'pre_link': pre_link,
            'post_link': post_link,
            'mid_link': mid_link
        }
        
        return JsonResponse(response_data)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
