from django.shortcuts import render
from random import shuffle

def index(request):
    if request.method == 'POST':

        if request.POST.has_key('text'):
            text = request.POST['text']
        else:
            return render(request, 'index.html')

        text = text.split() 
        count = len(text)
        shuffle(text)
        shuffle(text)
        text = ' '.join(text)

        return render(request, 'shuffle.html', {'text': text, 'count': count})
    else:
        return render(request, 'index.html')

