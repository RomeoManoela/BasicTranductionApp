from googletrans import Translator
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        text = request.POST['translate']
        language = request.POST['language']
        print(language)
        translator = Translator()
        result = translator.translate(text, dest=language)
        return render(request, 'translator.html', {'result': result.text})
    return render(request, 'translator.html')