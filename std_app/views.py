from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student

# Home Page
def HomePage(request):
    users = Student.objects.all()
    context = {'users': users}
    return render(request, "std_app/index.html", context)

# About Page
def AboutUS(request):
    return render(request, "std_app/about.html")

# Services Page
def Services(request):
    return render(request, "std_app/services.html")

# Add New Student
def Add_Std(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        aadhaar = request.POST.get("aadhaar")
        address = request.POST.get("address")
        purpose = request.POST.get("purpose")
        date = request.POST.get("date")
        
        if name and phone and aadhaar and address and purpose and date:
            user = Student(name=name, phone=phone, aadhaar=aadhaar, address=address, purpose=purpose, date=date)
            user.save()
            messages.success(request, "Customer Details added successfully! 🎉")
            return redirect("home")
        else:
            messages.error(request, "All fields are required! ❌")

    return render(request, "std_app/add_std.html")

# Edit Student Details
def EditStd(request, id):
    user = get_object_or_404(Student, id=id)

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.phone = request.POST.get("phone")
        user.aadhaar = request.POST.get("aadhaar")
        user.address = request.POST.get("address")
        user.purpose = request.POST.get("purpose")
        user.date = request.POST.get("date")
        user.save()
        messages.success(request, "Customer details updated successfully! ✅")
        return redirect("home")

    return render(request, "std_app/update.html", {"user": user})

# Delete Student
def DeleteStd(request, id):
    if request.method == "POST":
        user = get_object_or_404(Student, id=id)
        user.delete()
        messages.success(request, "Customer deleted successfully! 🗑️")
        return redirect('home')

    messages.error(request, "Something went wrong! ❌")
    return redirect('home')