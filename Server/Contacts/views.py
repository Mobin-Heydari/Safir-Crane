from django.shortcuts import render, redirect
from django.views import View
from .models import Contact
from .forms import ContactsForm





class ContactView(View):
    """
    A view to handle the creation of a new contact entry using a contact form.
    """

    def get(self, request):
        """
        Handle GET requests by rendering a blank ContactsForm.
        """
        # Instantiate a blank form for the user to fill in
        form = ContactsForm()
        return render(request, 'Contacts/contact-us.html', {'form': form})

    def post(self, request):
        """
        Handle POST requests by processing the submitted ContactsForm.
        """
        # Instantiate the form with submitted data
        form = ContactsForm(request.POST)
        
        if form.is_valid():
            # Retrieve cleaned data from the form
            cd = form.cleaned_data
            
            # Create a new Contact object using the validated form data
            Contact.objects.create(
                f_name=cd['f_name'],
                l_name=cd['l_name'],
                title=cd['title'],
                phone=cd['phone'],
                email=cd['email'],
                content=cd['content']
            )
            # Redirect to the same contact page after successful submission
            return redirect('contacts:contact')
        
        # If the form is invalid, render the page with form errors displayed
        return render(request, 'Contacts/contact-us.html', {'form': form})
