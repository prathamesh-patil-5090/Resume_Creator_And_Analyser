# views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import os
import io
import base64
import pdf2image
import google.generativeai as genai
from django.core.files.storage import FileSystemStorage

# Configure Gemini AI
genai.configure(api_key='AIzaSyD0knw8oD1QJFryNDF3tmkwuNrWH2mDQ7Q')

def analyze_resume(request):
    return render(request, 'analysis.html')


def get_gemini_response(input_prompt, pdf_content, job_description):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input_prompt, pdf_content[0], job_description])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        #images = pdf2image.convert_from_bytes(uploaded_file.read())
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=r'C:/Program Files/poppler-24.08.0/Library/bin')
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

@csrf_exempt
def resume_analyzer(request):
    if request.method == 'POST':
        job_description = request.POST.get('job_description', '')
        if 'resume' in request.FILES:
            resume = request.FILES['resume']
            
            if not resume.name.endswith('.pdf'):
                return JsonResponse({'error': 'Please upload a PDF file'})
            
            try:
                pdf_content = input_pdf_setup(resume)
                
                # Determine which analysis to perform based on button click
                if 'analyze_resume' in request.POST:
                    input_prompt = """
                    You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
                    Please share your professional evaluation on whether the candidate's profile aligns with the role. 
                    Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
                    """
                elif 'improve_skills' in request.POST:
                    input_prompt = """
                    You are an experienced programming mentor with deep knowledge in modern coding practices, software development tools, and continuous skill improvement techniques.
                    Please look after my resume and skills I have and provide me with structured steps and resources, including recommended learning platforms, key topics or concepts to focus on, and practical exercises to enhance my skills.
                    Also, suggest ways to stay updated on the latest trends in programming and how I can effectively track my progress.
                    """
                elif 'match_percentage' in request.POST:
                    input_prompt = """
                    You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
                    your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
                    the job description. First the output should come as percentage and then keywords missing and last final thoughts.
                    """
                
                response = get_gemini_response(input_prompt, pdf_content, job_description)
                return JsonResponse({'response': response})
                
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'error': 'Please upload a resume'})
    
    return render(request, 'analysis.html')
