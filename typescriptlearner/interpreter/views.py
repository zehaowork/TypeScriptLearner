from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

#import dukpy for typescript interpreting
import dukpy

class InterpretForm(forms.Form):
    inputCode = forms.CharField(label='input', widget=forms.Textarea)
    
# Create your views here.

def index(request):
    #If incoming post request exists, render 
    if request.method == "POST":
        #Create a form instance and populate data

        #Figure out why this doesnt work?
        #form = InterpretForm(request.POST)
        #print(form)
        
        #if form.is_valid():
            #temporary placeholder for output
        #    output = form.inputCode
            #return to page with processed data
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
       #     return HttpResponseRedirect(reverse('polls:results', args=(output,)))


        #Second option
        print(request.POST['inputCode'])
        inputCode = request.POST['inputCode']
        
        #temporary placeholder for output
        output = inputCode
        return render(request, 'interpreter/index.html', { 'output': output })


    #else render normally
    else:
        return render(request,'interpreter/index.html')

