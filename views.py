from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,"cropCure/index.html",context)

import os
from django.shortcuts import render
from django.http import JsonResponse
  # Import your model if it's in models.py
from .disease_detection import detect_disease  # Import your model function

# def analyze_image(request):
#     if 'image' in request.FILES:
#             uploaded_image = request.FILES['image']
#             print("Image received")  # Debugging message

#             # Call your model's function to detect disease
#             disease_result = detect_disease(uploaded_image)
#     # if request.method == 'POST' and request.FILES['image']:
#     #     print("HIIIII")
#     #                 # Get the uploaded image
#     #     uploaded_image = request.FILES['image']
#     #         # Run the model to detect the disease
#     #     disease_result = detect_disease(uploaded_image)  # Call your model's function
#     #         # Return the result
#     #     print(disease_result)
#     #         # return render(request, 'results.html', {'disease': disease_result})
#     #     return JsonResponse({'disease_result': disease_result})
#     #     # else:
#     #     #     return "content is not safe and I can't generate an answer for your request"


# import os
# from django.conf import settings

# def analyze_image(request):
#     if 'image' in request.FILES:
#         uploaded_image = request.FILES['image']
#         print("Image received")  # Debugging message

#         # Get the image filename
#         image_filename = uploaded_image.name

#         # Create the directory if it doesn't exist
#         image_path = 'E:\dieasesDetector\cropCure\static\inputted_image'

#         # Save the image to the directory
#         with open(os.path.join(image_path, image_filename), 'wb') as f:
#             for chunk in uploaded_image.chunks():
#                 f.write(chunk)

#         # Call your model's function to detect disease
#         disease_result = detect_disease(image_filename)
#         return JsonResponse({'disease_result': disease_result})
#     else:
#         return JsonResponse({'error': 'No image uploaded'})
    
import os
from django.conf import settings

def analyze_image(request):
    if 'image' in request.FILES:
        uploaded_image = request.FILES['image']
        print("Image received")  # Debugging message

        # Get the image filename
        image_filename = uploaded_image.name

        # Create the directory if it doesn't exist
        image_path = os.path.join('C:/Users/rakhi/OneDrive/Desktop/dieasesDetector/cropCure/static/inputted_images')
        os.makedirs(image_path, exist_ok=True)

        # Save the image to the directory
        with open(os.path.join(image_path, image_filename), 'wb') as f:
            for chunk in uploaded_image.chunks():
                f.write(chunk)
        image_newpath = 'cropCure/static/inputted_images/'+image_filename

        # Call your model's function to detect disease
        disease_result = detect_disease(image_newpath)
        return JsonResponse({'disease_result': disease_result})
    else:
        return JsonResponse({'error': 'No image uploaded'})