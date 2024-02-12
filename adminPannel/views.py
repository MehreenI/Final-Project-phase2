from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.http import JsonResponse
from django.db.models import Avg
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.conf  import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import FAQ,Slider,Product,Category,Contact,Review,User

# HOME PAGE
def index(request):
  try:
    slider = Slider.objects.all()
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_featured=True)
    new_arrival = Product.objects.all().order_by('-created_at')[:4]
    sale = Product.objects.filter(for_sale=True)[:4]
    testimonials = Review.objects.all().order_by('-createdAt')[:3]

# FETCH RATING FOR FEATURED PRODUCTS, NEW PRODUCTS, AND DISCOUNTED PRODUCTS
    for product in featured_products:
      reviews = Review.objects.filter(product=product)
      rating = round(float((reviews.aggregate(Avg('rating'))['rating__avg']))) if reviews else None
      
      product.reviews = reviews
      product.avg_ratings = rating

    for new_products in new_arrival:
      reviews = Review.objects.filter(product=new_products)
      rating = round(float((reviews.aggregate(Avg('rating'))['rating__avg']))) if reviews else None
      
      new_products.reviews = reviews
      new_products.avg_ratings = rating

    for discounted_products in sale:
      reviews = Review.objects.filter(product=discounted_products)
      rating = round(float((reviews.aggregate(Avg('rating'))['rating__avg']))) if reviews else None
      
      discounted_products.reviews = reviews
      discounted_products.avg_ratings = rating
      
    data = {
      'slider':slider,
      'categories':categories,
      'featured_products':featured_products,
      'new_arrival':new_arrival,
      'sale':sale,
      'testimonials':testimonials
    }
    return render(request,"index.html",data)
  except:
    return render(request,"index.html")

# ABOUT PAGE
def about(request):
  return render(request, "about_us.html")

# PRODUCT PAGE
def products(request):
  try:
    products = Product.objects.all()
    for product in products:
      reviews = Review.objects.filter(product=product)
      rating = round(float((reviews.aggregate(Avg('rating'))['rating__avg']))) if reviews else None

      product.reviews = reviews
      product.avg_ratings = rating
    return render(request, "products.html", {'products' : products})
  except:
    return render(request, "products.html")
  

# display Single Products
def productDetail(request,id=None):
  try:
    # Fetching Single Product Details
    product = Product.objects.get(id=id)
    products = Product.objects.filter(category=product.category)
    reviews = Review.objects.filter(product=product)
    rating = round(float((reviews.aggregate(Avg('rating'))['rating__avg']))) if reviews else None

    data = {'product':product, 
    'related_products':products,
    'reviews':reviews,
    'rating':rating}
    
    return render(request, "product_detail.html", data)
  except:
    return render(request, "product_detail.html")
  

# Frequently Asked Questions
def faq(request):
  try:
    faq = FAQ.objects.all()
    return render(request, "faq.html", {'faqs' : faq})
  except:
    return render(request, "faq.html")


# CONTACT FORM SUBBMISSION
def contact(request):
  try:
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      message = request.POST.get('message')
      if name == "" or email == "" or message == "":
        return render(request, 'contact.html',{'error' : True})
      else:
        contact=Contact()
          
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        send_mail(
              'New Contact Form Submission',
              f'A new contact form submission has been received from {name} ({email}). Message: {message}',
              'hina.zailai97@gmail.com',['mehreenm.imran27@gmail.com', 'hina.zailai97@gmail.com'], fail_silently=False)
        return render(request, 'contact.html',{'success' : True})
    else:
        return render(request, 'contact.html')
  except:
    return render(request, "contact.html")


# display Products Accoording to Category
def category_product_list_view(request,id):

  try:
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)

    data={
      "categories":category,
      "products":products
    }

    return render (request,"products.html",data)

  except Exception as e:  
    return render(request, "products.html")
    
  
# Use To Submit Reviews
def submit_review(request,id):
  
  if request.user.is_authenticated:
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

      product = Product.objects.get(id=id)
      user = request.user
      name = request.POST.get('name')
      email = request.POST.get('email')
      review_text = request.POST.get('review')
      product_rating = request.POST.get('rate')
        
      review = Review.objects.create(
        product=product,
        user=user,
        name=name,
        email=email,
        comment=review_text,
        rating=product_rating
      )

      # Return a JSON response indicating success
      return JsonResponse({'message': 'Review submitted successfully. id'})
    else:
      # Return an error response if the request is not valid
      return redirect("login")
  else:
    return redirect("login")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("YOu Have Been logged In!"))
            return redirect('index')
        else:
            messages.success(request, ("There was an error, Please try again"))
    else:
        return render(request, 'login.html', {})
    

def logout_user(request):
        logout(request)
        messages.success(request , ("You have been logged out..."))
        return redirect('index')

def registration(request):
    return render(request,'registration.html')

def register_user(request):
  try:
    if request.method == "POST":
      username = request.POST['firstName']
      password = request.POST['password']
      email = request.POST['email']
      firstName = request.POST['firstName']
      lastName = request.POST['lastName']

      user = User.objects.create_user(username=username, password=password, email=email, first_name=firstName, last_name=lastName)
      user.save()
      return redirect("/")
    else:
      return render(request,'registration.html')
  except Exception as e :
    return render(request,'registration.html')

  