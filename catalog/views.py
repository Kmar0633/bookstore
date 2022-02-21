from django.shortcuts import render,redirect
from django.views import generic
from locallibrary.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY , AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3


# Create your views here.
from .models import Book, CustomUser



def book_list_view(request):
    """displays the user book list pages for kid customer, adult customer and admin"""

    # Creates a list of all the books from the django database
    
    book_list = Book.objects.all()

    # Filters the list of books to only include books that are under eighteen

    children_book_list=Book.objects.filter(age_group='e')

    # stores book list into context

    context = {
            
            'book_list':book_list
      
            }
   

    # checks if the user is authenticated and in the database

    if request.user.is_authenticated:

        # checks if the user is an admin
        if request.user.position=='b':
            
             # renders the admin page 
            return render(request, 'admin.html', context=context)

        # checks if the user is a kid customer

        if request.user.position=='e':

            # Redclares the book_list variable with books only suited for children

            book_list=children_book_list
            context = {
            'book_list':children_book_list
            }

            # renders the customer user page 
            return render(request, 'customer.html', context=context)

        
        # renders the customer user page 

        return render(request, 'customer.html', context=context)
        
    # if the user tries to access the page without logging in, the function will render an error pahe
    else:
         return render(request, 'error_page.html')





def delete_book(request,book_id =None):
    """deletes a specific book from the database using book  id """

    #gets a book object from the book id
    book = Book.objects.get(pk=book_id)
    #deletes the book
    book.delete()
    #redirects user to book list view page
    return redirect('/')

def add_profilepicture(request,user_id =None):
    """adds a profile picture to a specific user from the user id """

    #checks if the request method is a psot
    if request.method == 'POST':

        #checks if the request contains a ket named filetoUpload
        if request.FILES.get('fileToUpload', True):

            #declares a variable called user containing the user object based on their specific id
            user = CustomUser.objects.get(pk=user_id)

            #declares the users profile image with the file uploaded in fileToUpload
            user.profile_image=request.FILES.get('fileToUpload')
           
            #saves the user
            user.save()
            return redirect('/')

def add_book(request):
     #checks if the request method is a psot
	 if request.method == 'POST':

            #checks if the post request contained values for the title, author, fileToUpload and age_group attributes from the form in admin.html
            # that allows you to add books
            if request.FILES.get('fileToUpload', True) and request.POST.get('title')  and request.POST.get('author')  and request.POST.get('age_group'):

            # creates a new book class and declares the attributes within the book model class to have the attributes filled in the form in admin.html and uploaded
           
            

                post=Book()
                
              
                post.title=request.POST.get('title')
                post.author=request.POST.get('author')
                post.age_group=request.POST.get('age_group')
                post.book_cover_image= request.FILES['fileToUpload']
                
                post.save()

                return redirect('/') 

           
            else:

                #if the form is not filled and the user selects upload, he or she will be redirected to the admin.htmk page with an error message stored in the context

                book_list = Book.objects.all()
    
                context = {
                'book_list':book_list,
                'ERROR':'Error message: Input field is empty'
                }

                return render(request, 'admin.html', context)


