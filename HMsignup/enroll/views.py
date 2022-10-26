from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create Sign up views here.

def Sign_up(request):
    form = UserCreationForm()
    context = {'form': form}
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirmpassword']
        return render(request, 'enroll/result.html',{'value': username})
        

    return render(request, 'enroll/Signup.html',{})
    




# Create Login Views here

def Log_in(request):
    form = UserCreationForm()
    context = {'form' : form}
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        return render ( request, 'enroll/Login.html',{'value': username})

    return render ( request, 'enroll/Login.html',{})
    





    
            


        


   