from django.shortcuts import render,redirect
from .models import *
from .models import UserProfile
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Tsoc.settings import *
from datetime import datetime
from time import time
from dotenv import load_dotenv
load_dotenv()

from Tsoc import settings
# from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
# import razorpay
# client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

# from django.views.decorators.cache import cache_control

def home(request):
    courses = Course.objects.all()
    context = {"courses":courses}
    return render(request,'tango/home.html',context)

def About(request):
    context = {}
    return render(request,'tango/about.html',context)

@login_required(login_url='/login')
def Courses(request,slug):
    course = Course.objects.get(slug=slug)
    print(course.name)
    chapters = Chapter.objects.all().order_by("serial_number")
    # print(chapters)
    certificate = False


    if request.user.is_authenticated is False:
        return redirect("login")
        
    context = {
        "course" : course,
        'chapters':chapters,
        'certificate':certificate
    }
    return render(request,'tango/playlist.html',context)


def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()

        send_notification(name, email, phone, message)

        # Send confirmation email to the user
        send_confirmation_email(name, email)

        return redirect('contact')
    
    return render(request,'tango/contact.html')

def send_notification(name, email, phone, message):
    subject_owner = 'New Contact Form Submission'
    message_owner = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
    send_mail(subject_owner, message_owner, settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])

def send_notification_to_support(name, email, message):
    subject_owner = 'Support and Help From Tsoc'
    message_owner = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    send_mail(subject_owner, message_owner, settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])


def send_confirmation_email(name, email):
    
    subject = 'Thank you for contacting us. We will conect to you soon.'
    message = f'Dear {name},\n\nThank you for contacting us. We will get back to you soon!'

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,[email])

@login_required(login_url='/login')
def Articles(request):
    context = {}
    return render(request,'newsletter.html',context)

@login_required(login_url='/login')
def Help(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
            
        send_notification_to_support(name, email, message)
        send_confirmation_email(name, email)
        return redirect('profile')
    
    return render(request,'tango/help.html')
       
    
@login_required(login_url='/login')
def Profile(request):
    user = request.user.userprofile
    form = ProfileForm(instance=user)
    context = {'form':user.profileid}
    return render(request,'tango/profile.html',context)

@login_required(login_url='/login')
def UpdateProfile(request,pk):
    user = UserProfile.objects.get(id=pk)
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            print('ok')
            form.save()
            return redirect('profile')
        
    context = {'form':form}
    return render(request,'tango/updateprofile.html',context)

@login_required(login_url='/login')
def PaymentPage(request,slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('action')
    couponcode = request.GET.get('couponcode')
    couponcode_message = ''
    coupon = None
    order = None
    payment = None
    error = None
    try:
        user_course = UserCourse.objects.get(user = user  , course = course)
        error = "You are Already Enrolled in this Course"
    except:
        pass
    amount=None
    if error is None : 
        amount =  int((course.price - course.discount) * 100)
   # if ammount is zero dont create paymenty , only save emrollment obbect 
    
    if couponcode:
        try:
            coupon = CouponCode.objects.get(course=course,code=couponcode)
            amount = course.price - coupon.discount
            amount = int(amount) * 100
            print(amount)
        except:
            couponcode_message = 'Invalid Coupon Code!'
            print('Code is Invalid!')

    if amount==0:
        userCourse = UserCourse(user = user , course = course)
        userCourse.save()
        return redirect('my-courses')   
                # enroll direct
    
    if action == 'create_payment':

            currency = "INR"
            notes = {
                "email" : user.email, 
                "name" : f'{user.first_name} {user.last_name}'
            }
            reciept = f"codewithvirendra-{int(time())}"
            # order = client.order.create(
                # {'receipt' :reciept , 
                # 'notes' : notes , 
                # 'amount' : amount ,
                # 'currency' : currency
                # }
            # )

            payment = Payment()
            payment.user  = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()

    context = {
            "course" : course , 
            "order" : order, 
            "payment" : payment, 
            "user" : user , 
            "error" : error,
            "coupon":coupon,
            "couponcode_message":couponcode_message,
    }
    return render(request,'tango/payment.html',context)

def LoginPage(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=name,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')

        else:
            return render(request,'loginpage.html')
        
    return render(request,'tango/loginpage.html')

def Register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 == pass2:
            if form.is_valid():
                form.save()
                return redirect('loginpage')

        else:
            return render(request,'register.html')
        
    return render(request,'tango/register.html',{'form':form})

def LogoutPage(request):
    logout(request)
    return redirect('home')
    
@login_required(login_url='/login')
@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        print(data)
        try:
            # client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id  = razorpay_payment_id
            payment.status =  True
            
            userCourse = UserCourse(user = payment.user , course = payment.course)
            userCourse.save()

            print("UserCourse" ,  userCourse.id)

            payment.user_course = userCourse
            payment.save()

            return redirect('my-courses')   

        except:
            return HttpResponse("Invalid Payment Details")
        
@login_required(login_url='/login')
def adminPage(request):
    data = User.objects.all()
    context = {'data':data}
    return render(request,'tango/admin.html',context)

@login_required(login_url='/login')
def News(request):
    context = {'data':0}
    return render(request,'tango/news.html',context)

def TermsCondition(request):
    context = {'data':0}
    return render(request,'tango/term_and_condition.html',context)

def ReturnPolicy(request):
    context = {'data':0}
    return render(request,'tango/return_policy.html',context)

def PrivacyPolicy(request):
    context = {'data':0}
    return render(request,'tango/privacy_policy.html',context)

def TestimonialPolicy(request):
    context = {'data':0}
    return render(request,'tango/testimonial_policy.html',context)


# def playlist(request,slug):
#     course = Course.objects.get(slug=slug)
#     serial_number = request.GET.get('lecture')
#     videos = course.video_set.all().order_by("serial_number")
   
#     if serial_number is None:
#         serial_number = 1 

#     video = Video.objects.get(serial_number = serial_number , course = course)
    
        
#     context = {
#         "course" : course , 
#         "video" : video , 
#         'videos':videos,
#     }
#     return render(request,'course.html',context)

@login_required(login_url='/login')
def watch(request,slug,pk):
    chapter = Chapter.objects.get(slug=slug)
    chapter = Chapter.objects.get(serial_number=pk)
    course = Course.objects.all()
    serial_number = request.GET.get('lecture')
    videos = chapter.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1 

    video = Video.objects.get(serial_number = serial_number)
        
    context = {
        "course" : course , 
        "video" : video , 
        'videos':videos
    }
    return render(request,'tango/watch-video.html',context)