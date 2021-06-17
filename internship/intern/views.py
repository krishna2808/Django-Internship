from django.shortcuts import render
from .models import Post, Registration
from django.shortcuts import redirect
# Create your views here.

def calculator(request):
    sum = ''
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        sum = num1 + num2
    return render(request, 'intern/calculator.html', {'sum': sum})


def portfolio(request):
    return render(request, 'intern/portfolio.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username != '' and email != '' and password != '':
            User = Registration(username=username, email=email, password= password)
            User.save()
            return redirect('dashboard')
    return render(request, 'intern/registration.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        object = Registration.objects.filter(username=username)
        if object:
            for singleAttribute in object:
                password1 = singleAttribute.password
            if password1 == password:
                request.session['username'] = username
                # return render(request,'intern/posts.html')
                return redirect('posts')
            return render(request, 'intern/login.html', {'invalid':"Password invalid"})
        return render(request, 'intern/login.html', {'invalid':"Username isn't found"})

    return render(request, 'intern/login.html')

def profile(request):
    if 'username' in request.session.keys():
        User = Registration.objects.get(username= request.session['username'])
        successfully = ''
        if request.method == 'POST':
            username = request.POST['username']
            fullname = request.POST['fullname']
            email = request.POST['email']
            password = request.POST['password']
            address = request.POST['address']
            image = request.FILES.get('image')

            User.username = username
            User.fullname = fullname
            User.email = email
            User.password = password
            User.address = address
            if image != None:
                User.image = image
            User.save()
            successfully = 'your Details has been updated'

        return render(request, 'intern/profile.html', {'User': User, 'successfully': successfully})
    return redirect('login')

def dashboard(request):
    return render(request, 'intern/dashboard.html')

def insertUpdateDelete(request):
    return render(request, 'intern/insertUpdateDelete.html')

userName = ''
def update(request):
    global userName
    invalid = ''
    if request.method =='POST':
        username = request.POST['username']
        userObject = Registration.objects.filter(username=username)
        print(userObject)
        if userObject:
            print('**************************************')

            for single in userObject:
                userName = single.username
            return redirect('updateDetails')
        invalid = "User isn't found"

    return render(request, 'intern/update.html', {'invalid': invalid})

def updateDetails(request):
    global userName
    User = Registration.objects.get(username=userName)
    successfully = ''
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        image = request.FILES.get('image')

        User.username = username
        User.fullname = fullname
        User.email = email
        User.password = password
        User.address = address
        if image != None:
            User.image = image
        User.save()
        successfully = 'your Details has been updated'

    return render(request, 'intern/updateDetails.html',{'User': User, 'successfully': successfully})

def insert(request):
    successfully = ''
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        image = request.FILES.get('image')

        if username != '' and email != '' and password != '' and fullname != ''  and address != '' and image != '':
            User = Registration(username=username, email=email, password=password, fullname=fullname, address=address, image=image)
            User.save()
            successfully = 'your Details has been inserted'
    return render(request, 'intern/insert.html', {'successfully': successfully})

def delete(request):
    temp  = ''
    if request.method == 'POST':
        username = request.POST['username']
        userObject = Registration.objects.filter(username=username)
        if userObject:
            for singleAttribute in userObject:
                userName = singleAttribute.username
            User = Registration.objects.get(username=userName)
            User.delete()
            return render(request, 'intern/delete.html', {'temp': "Account has been deleted successfully "})

        temp = "User isn't found "

    return render(request, 'intern/delete.html', {'temp':temp})

def postUpload(request):
    if 'username' in request.session.keys():
        successfully = ''
        if request.method == 'POST':
            username = request.session['username']
            title = request.POST['title']
            instance = Registration.objects.get(username=username)
            image = request.FILES.get('image')
            description = request.POST['description']
            if username != '' and title != '' and image != '' and description != '':
                post = Post(username=instance, title=title, image=image, description=description)
                post.save()
                successfully = 'Your Post  has been uploaded'


        return render(request, 'intern/postUpload.html', {'successfully': successfully})

    return redirect('login')


def posts(request):
    detailObjects = Post.objects.all()
    return render(request, 'intern/posts.html', {'detailObjects': detailObjects})

def userDetails(request):
    if 'username' in request.session.keys():

        return render(request, 'intern/userDetails.html', {'userDetails':userDetails})
def logout(request):
    if 'username' in request.session.keys():
        del request.session['username']
        return redirect('login')
    return redirect('login')

