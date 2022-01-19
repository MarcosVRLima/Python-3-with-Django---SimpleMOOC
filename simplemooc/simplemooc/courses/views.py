from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Course, Enrollment
from .forms import ContactCourse

# Create your views here.

def coursePageView(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {'courses': courses,}
    return render(request, template_name, context)

def detailsPageView(request, slug):
    course = get_object_or_404(Course, slug=slug)  #Course.objects.get(pk=pk)
    context = {}

    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_email(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    
    context['form'] = form
    context['course'] = course
    
    template_name = 'courses/details.html'
    return render(request, template_name, context)

@login_required
def enrollmentPageView(request, slug):
    course = get_object_or_404(Course, slug=slug)  #Course.objects.get(pk=pk)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course = course)
    context = {}

    if created:
        enrollment.active()
        context['color'] = 'success'
        context['message'] = 'Incrição realizada com sucesso no curso "' + course.name + '" !'
        
    else:
        context['color'] ='red'
        context['message'] = 'Incrição já realizada neste curso!'

    return render(request, 'accounts/dashboard.html', context)
    

