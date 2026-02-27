from django.shortcuts import render, get_object_or_404,redirect
from .models import Job
from .forms import JobForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import logout

from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.auth import logout



@login_required
# def home(request):
#     jobs = Job.objects.all().order_by('-posted_at')
#     return render(request, 'jobs/home.html', {'jobs': jobs})




def home(request):
    job_list = Job.objects.all().order_by('-posted_at')

    paginator = Paginator(job_list, 5)  # 5 jobs per page
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    return render(request, 'jobs/home.html', {'jobs': jobs})


@login_required
def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'jobs/job_detail.html', {'job': job})


# @login_required
# def create_job(request):
#     if request.method == "POST":
#         form = JobForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = JobForm()

#     return render(request, 'jobs/create_job.html', {'form': form})


# Ab job create karne wale user ko owner assign ho raha hai.

@login_required
def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user
            job.save()
            return redirect('home')
    else:
        form = JobForm()

    return render(request, 'jobs/create_job.html', {'form': form})





@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)

    if job.owner != request.user:
        messages.error(request, "You are not allowed to delete this job.")
        return redirect('home')

    job.delete()
    messages.success(request, "Job deleted successfully!")
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'jobs/register.html', {'form': form})    



def logout_view(request):
    logout(request)
    return redirect('login')