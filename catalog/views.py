from django.shortcuts import render,redirect
from django.views import generic
from locallibrary.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY , AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3


# Create your views here.
from .models import Book, CustomUser

session = boto3.Session(
    aws_access_key_id=  'AKIAUQV4RBORGRQYYSVX',
    aws_secret_access_key = '9cqXxDBAjwwy3plgyAwB/K9FNY/fHId19kCe8Xfy'
   
)

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()
    children_book_list=Book.objects.filter(age_group='e')
    context = {
            'num_books': num_books,
            'book_list':book_list,
      
            }
    # The 'all()' is implied by default.
    if request.user.is_authenticated:
        if request.user.position=='b':
            
    
            
            return render(request, 'admin.html', context=context)
        if request.user.position=='e':
            book_list=children_book_list
            context = {
            'num_books': num_books,
            'book_list':children_book_list,
      
            }
            
            return render(request, 'index.html', context=context)

        

        return render(request, 'index.html', context=context)
        

    else:
         return render(request, 'error_page.html')

def error(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()
    children_book_list=Book.objects.filter(age_group='e')
    context = {
            'num_books': num_books,
            'book_list':book_list,
      
            }
    # The 'all()' is implied by default.
    if request.user.is_authenticated:
        if request.user.position=='e':
            book_list=children_book_list

def admin(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()
    
    
    context = {
        'num_books': num_books,
        'book_list':book_list,
      
    }
    if request.user.is_authenticated:
        if request.user.position=='b':
            
    
            
            
            return render(request, 'admin.html', context=context)
        
    
    return render(request, 'error_page.html')
    # Render the HTML template index.html with the data in the context variable
    


#class BookListView(generic.ListView):
    
  #  context_object_name = 'my_book_list'   # your own name for the list as a template variable
 #   queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
  #  template_name = 'templates/profile.html'  # Specify your own template name/location



def delete_book(request,book_id =None):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('/')

def add_profilepicture(request,user_id =None):
    if request.method == 'POST':
        if request.FILES.get('fileToUpload', True):
            print(CustomUser.objects.get(pk=user_id))
            print(CustomUser.objects.get(pk=user_id).profile_image)
            user = CustomUser.objects.get(pk=user_id)
            user.profile_image=request.FILES.get('fileToUpload')
           
            user.save()
            return redirect('/')

def add_book(request):
	 if request.method == 'POST':
            if request.FILES.get('fileToUpload', True) and request.POST.get('title')  and request.POST.get('author')  and request.POST.get('age_group'):
                post=Book()
                
              
                post.title=request.POST.get('title')
                post.author=request.POST.get('author')
                post.age_group=request.POST.get('age_group')
                post.book_cover_image= request.FILES['fileToUpload']

                #upload(request)


                post.save()

               
      
                
                return redirect('/') 
            else:
                book_list = Book.objects.all()
    
    
                context = {
                'book_list':book_list,
                'ERROR':'Input field is empty'
                }

                return render(request, 'admin.html', context)

def upload(request):
    
    fileToUpload = request.FILES.get('fileToUpload')
    cloudFilename = 'images/' + fileToUpload.name 
    session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3 = session.resource('s3')
    s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key=cloudFilename, Body=fileToUpload)

    return redirect('/')