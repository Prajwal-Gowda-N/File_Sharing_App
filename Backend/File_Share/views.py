from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import UploadedFile
from .serializers import FileSerializer

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class FileDownloadView(APIView):
    def get(self, request, file_id):
        file = get_object_or_404(UploadedFile, id=file_id)
        return Response({'file_url': request.build_absolute_uri(file.file.url)})


from django.http import FileResponse, HttpResponseNotFound
from django.conf import settings
import os

def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)

    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    else:
        return HttpResponseNotFound("File not found")



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse
from .utils import convert_word_to_pdf, convert_pdf_to_word  # Make sure these functions exist in utils.py
import logging

logger = logging.getLogger(__name__)

class ConvertFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
 
        file = request.FILES.get('file')
        conversion_type = request.data.get('type')

       
        if not file or not conversion_type:
            return Response({"error": "No file or conversion type provided"}, status=400)

        try:
            
            if conversion_type == 'word_to_pdf':
             
                converted_file = convert_word_to_pdf(file)

             
                response = HttpResponse(converted_file, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename=converted.pdf'

            elif conversion_type == 'pdf_to_word':
      
                converted_file = convert_pdf_to_word(file)

              
                response = HttpResponse(converted_file, content_type='application/msword')
                response['Content-Disposition'] = 'attachment; filename=converted.docx'

            else:
              
                return Response({"error": "Invalid conversion type"}, status=400)

            return response

        except Exception as e:
         
            logger.error(f"Error during conversion: {e}")
            return Response({"error": str(e)}, status=500)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .utils import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt, summarize_text_huggingface

class SummarizeFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "No file provided"}, status=400)

        try:
      
            if file.name.endswith('.pdf'):
                text = extract_text_from_pdf(file)
            elif file.name.endswith('.docx'):
                text = extract_text_from_docx(file)
            elif file.name.endswith('.txt'):
                text = extract_text_from_txt(file)
            else:
                return Response({"error": "Unsupported file type"}, status=400)

  
            summary = summarize_text_huggingface(text)

            return Response({"summary": summary}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        file_url = request.data.get('file_url')

        if not email or not file_url:
            return Response({"error": "Email or file URL not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
          
            send_mail(
                'Your Uploaded File URL',
                f'Here is the URL to your uploaded file: {file_url}',
                'your-email@gmail.com',  
                [email],  
                fail_silently=False,
            )

            return Response({"message": "Email sent successfully!"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from django.contrib.auth.models import User
from rest_framework import serializers, views, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class SignUpView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SignInView(TokenObtainPairView):
   
    pass


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def logout(request):
    # Get the refresh token from the request
    refresh_token = request.data.get('refresh_token')

    if refresh_token:
        # Optionally blacklist the token or perform your token invalidation logic here
        # Example: blacklist refresh token or do nothing depending on your use case
        pass

    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

