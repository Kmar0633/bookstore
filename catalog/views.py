from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Book
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()
    children_book_list=Book.objects.filter(age_group='e')
   
    # The 'all()' is implied by default.
    if request.user.position=='e':
        book_list=children_book_list
    
    context = {
        'num_books': num_books,
        'book_list':book_list,
      
    }
    if request.user.position=='b':
        return render(request, 'admin.html', context=context)
    # Render the HTML template index.html with the data in the context variable
    else:
        
        return render(request, 'index.html', context=context)



#class BookListView(generic.ListView):
    
  #  context_object_name = 'my_book_list'   # your own name for the list as a template variable
 #   queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
  #  template_name = 'templates/profile.html'  # Specify your own template name/location