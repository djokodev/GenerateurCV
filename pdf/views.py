from django.http import HttpResponse
from django.shortcuts import render, redirect
import pdfkit
from django.template.loader import get_template
from pdf.models import Profile


def home(request):
    return render(request, "home.html")

def formulaire(request):
    if request.method == "POST":
        nom = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        competence = request.POST.get('competence')
        langue = request.POST.get('langue')
        interet = request.POST.get('interet')
        objectif = request.POST.get('objectif')
        experience = request.POST.get('experience')
        education = request.POST.get('education')
        projet = request.POST.get('projet')
        donnees = Profile(nom=nom, email=email, phone=phone, address=address, competence=competence, experience=experience, objectif=objectif, projet=projet, interet=interet, langue=langue, education=education)
        donnees.save()
        return redirect('verification')
    return render(request, "formulaire.html")

def verification(request):
    profiles = Profile.objects.all()[:1] #recupere jsute le premier element en bd
    for profile in profiles:
        nom = profile.nom
        phone = profile.phone
        email = profile.email
        address = profile.address
        com = profile.competence
        langue = profile.langue
        interet = profile.interet
        exp = profile.experience
        objectif = profile.objectif
        education = profile.education
        project = profile.projet
    return render(request, "verification.html",
                  {'address': address, 'name': nom, 'email': email, 'phone': phone, 'com': com, 'interet': interet,
                   'langue': langue, 'experience': exp, 'objectif': objectif, 'education': education,
                   'project': project})



def generer(request, id):
    profile = Profile.objects.get(pk=id)
    nom = profile.nom
    phone = profile.phone
    email = profile.email
    address = profile.address
    com = profile.competence
    langue = profile.langue
    interet = profile.interet
    exp = profile.experience
    objectif = profile.objectif
    education = profile.education
    project = profile.projet

    template = get_template('generator.html')
    context = {'address': address, 'name': nom, 'email': email, 'phone': phone, 'com': com, 'interet': interet,
                   'langue': langue, 'experience': exp, 'objectif': objectif, 'education': education,
                   'project': project}
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',

    }
    pdf = pdfkit.from_string(html, False, options)
    reponse = HttpResponse(pdf, content_type='application/pdf')
    reponse['Content-Disposition'] = 'attachement'
    return reponse

def download(request):
    profile = Profile.objects.all()[:1]
    return render(request, 'download.html', {'profile':profile})

def retour(request):
    return redirect('formulaire')