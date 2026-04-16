from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .serializers import ContactSerializer


@api_view(['POST'])
def contact_create(request):
    """
    API endpoint to handle contact form submissions.
    POST /api/contact/
    Expected JSON:
    {
        "name": "string",
        "email": "string",
        "message": "string"
    }
    """
    try:
        serializer = ContactSerializer(data=request.data)
        
        if serializer.is_valid():
            contact = serializer.save()
            
            # Send email to admin
            try:
                send_mail(
                    subject=f"New Contact Message from {contact.name}",
                    message=f"""You have received a new message from your portfolio contact form.

Name: {contact.name}
Email: {contact.email}

Message:
{contact.message}

---
This is an automated message from your portfolio website.
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['manueshanchekkali@gmail.com'],
                    fail_silently=False,  # Show errors for debugging
                )
                print(f"[SUCCESS] Email sent for contact from {contact.name}")
            except Exception as e:
                print(f"[EMAIL ERROR] Failed to send email: {str(e)}")
            
            return Response(
                {
                    "success": True,
                    "message": "Message received successfully. We'll get back to you soon!",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        # Validation errors
        print(f"[VALIDATION ERROR] {serializer.errors}")
        return Response(
            {
                "success": False,
                "detail": "Invalid data provided. Please check all fields.",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    except Exception as e:
        print(f"[SERVER ERROR] {str(e)}")
        return Response(
            {
                "success": False,
                "detail": f"Server error: {str(e)}"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
