from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.objects.all().order_by('-created_at')
    form = StudentForm()
    return render(request, 'index.html', {'students': students, 'form': form})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return redirect('index')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {'form': form, 'student': student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'confirm_delete.html', {'student': student})
# Create your views here.
