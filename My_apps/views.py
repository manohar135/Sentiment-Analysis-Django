from django.shortcuts import render, HttpResponse
from joblib import load

def index(request):
    model = load('ML_models/Review.pkl')
    context = {'var': 'NULL'}
    if request.method == "POST":
        review = request.POST.get('comment')
        val = model.predict([review])[0]
        context['var'] = val
    return render(request, 'index.html', context)
