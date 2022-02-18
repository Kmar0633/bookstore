from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Book
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
  
    # The 'all()' is implied by default.
  

    context = {
        'num_books': num_books,
        
      
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'templates/profile.html'  # Specify your own template name/location