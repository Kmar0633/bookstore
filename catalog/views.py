from django.shortcuts import render,redirect
from django.views import generic


# Create your views here.
from .models import Book
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
    return redirect('admin')

def add_book(request):
	 if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('image') and request.POST.get('author') and request.POST.get('age_group'):
                post=Book()
                post.title= request.POST.get('title')
                post.book_cover_image= request.POST.get('image')
                post.author= request.POST.get('author')
                post.age_group= request.POST.get('age_group')
                post.save()

               
      
                
                return redirect('admin') 

            else:
                return redirect('admin')
