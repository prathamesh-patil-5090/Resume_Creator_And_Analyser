from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')

def analysis(request):
    return render(request, 'core/resume_analyzer/templates/analysis.html')

def gen_resume(request):
    if request.method == 'POST':
        # Personal Information
        name = request.POST.get('name', '')
        location = request.POST.get('location', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        linkedin = request.POST.get('linkedin', '')
        x = request.POST.get('x', '')

        # Skills
        skills = request.POST.get('skills', '')

        # Education
        degree1 = request.POST.get('degree1', '')
        college1 = request.POST.get('college1', '')
        year1 = request.POST.get('year1', '')

        degree2 = request.POST.get('degree2', '')
        college2 = request.POST.get('college2', '')
        year2 = request.POST.get('year2', '')

        degree3 = request.POST.get('degree3', '')
        college3 = request.POST.get('college3', '')
        year3 = request.POST.get('year3', '')

        # Projects
        project1_title = request.POST.get('project1_title', '')
        pduration1 = request.POST.get('pduration1', '')
        pdescription1 = request.POST.get('pdescription1', '')
        project1_languages = request.POST.get('project1_languages', '')
        project1_github = request.POST.get('project1_github', '')

        project2_title = request.POST.get('project2_title', '')
        pduration2 = request.POST.get('pduration2', '')
        pdescription2 = request.POST.get('pdescription2', '')
        project2_languages = request.POST.get('project2_languages', '')
        project2_github = request.POST.get('project2_github', '')

        project3_title = request.POST.get('project3_title', '')
        pduration3 = request.POST.get('pduration3', '')
        pdescription3 = request.POST.get('pdescription3', '')
        project3_languages = request.POST.get('project3_languages', '')
        project3_github = request.POST.get('project3_github', '')

        # Internships
        icompany1 = request.POST.get('icompany1', '')
        ipost1 = request.POST.get('ipost1', '')
        iduration1 = request.POST.get('iduration1', '')
        internship1_description = request.POST.get('internship1_description', '')

        icompany2 = request.POST.get('icompany2', '')
        ipost2 = request.POST.get('ipost2', '')
        iduration2 = request.POST.get('iduration2', '')
        internship2_description = request.POST.get('internship2_description', '')
        
        icompany3 = request.POST.get('icompany3', '')
        ipost3 = request.POST.get('ipost3', '')
        iduration3 = request.POST.get('iduration3', '')
        internship3_description = request.POST.get('internship3_description', '')

        # Work Experience
        company1 = request.POST.get('company1', '')
        post1 = request.POST.get('post1', '')
        duration1 = request.POST.get('duration1', '')
        work_description1 = request.POST.get('work_description1', '')


        company2 = request.POST.get('company2', '')
        post2 = request.POST.get('post2', '')
        duration2 = request.POST.get('duration2', '')
        work_description2 = request.POST.get('work_description2', '')

        company3 = request.POST.get('company3', '')
        post3 = request.POST.get('post3', '')
        duration3 = request.POST.get('duration3', '')
        work_description3 = request.POST.get('work_description3', '')

        # Achievements
        achievement1 = request.POST.get('achievement1', '')
        achievement2 = request.POST.get('achievement2', '')
        achievement3 = request.POST.get('achievement3', '')

        # Certifications
        cert1 = request.POST.get('cert1', '')
        cert2 = request.POST.get('cert2', '')
        cert3 = request.POST.get('cert3', '')
        cert4 = request.POST.get('cert4', '')
        cert5 = request.POST.get('cert5', '')

        # Profile Links
        prof1 = request.POST.get('prof1', '')
        prof2 = request.POST.get('prof2', '')
        prof3 = request.POST.get('prof3', '')

        proflink1 = request.POST.get('proflink1', '')
        proflink2 = request.POST.get('proflink2', '')
        proflink3 = request.POST.get('proflink3', '')
        

        data = {
            'name': name,
            'location': location, 
            'email': email,
            'phone': phone,
            'linkedin': linkedin,
            'x':x,
            'skills': skills,
            'degree1': degree1, 'college1': college1, 'year1': year1,
            'degree2': degree2, 'college2': college2, 'year2': year2,
            'degree3': degree3, 'college3': college3, 'year3': year3,
            'project1_title': project1_title, 'pduration1': pduration1, 'pdescription1': pdescription1, 'project1_github': project1_github, 'project1_languages':project1_languages,
            'project2_title': project2_title, 'pduration2': pduration2, 'pdescription2': pdescription2, 'project2_github': project2_github, 'project2_languages':project2_languages,
            'project3_title': project3_title, 'pduration3': pduration3, 'pdescription3': pdescription3, 'project3_github': project3_github, 'project3_languages':project3_languages,
            'icompany1': icompany1, 'ipost1': ipost1, 'iduration1': iduration1, 'internship1_description': internship1_description,
            'icompany2': icompany2, 'ipost2': ipost2, 'iduration2': iduration2, 'internship2_description': internship2_description,
            'icompany3': icompany3, 'ipost3': ipost3, 'iduration3': iduration3, 'internship3_description': internship3_description,
            'company1': company1, 'post1': post1, 'duration1': duration1, 'work_description1': work_description1,
            'company2': company2, 'post2': post2, 'duration2': duration2, 'work_description2': work_description2,
            'company3': company3, 'post3': post3, 'duration3': duration3, 'work_description3': work_description3,
            'achievement1':achievement1,'achievement2':achievement2,'achievement3':achievement3,
            'cert5': cert5, 'cert4': cert4, 'cert3': cert3, 'cert2': cert2, 'cert1': cert1,
            'prof1': prof1, 'prof2': prof2, 'prof3': prof3,
            'proflink1':proflink1, 'proflink2':proflink2, 'proflink3':proflink3,
        }
        return render(request, 'resume.html', data)

    return render(request, 'index.html')
