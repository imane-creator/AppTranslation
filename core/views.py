from django.shortcuts import render
from translate import Translator

def translator(request):
    if request.method == 'POST':
            from_lang = request.POST.get('from_lang') # Get with default
            to_lang = request.POST['to_lang']    # Get with default
            text = request.POST.get('text', '')           # Get with default

            translator = Translator(
                to_lang=to_lang,
                from_lang=from_lang
            )
            translated_text = translator.translate(text=text)

            return render(request, 'translator.html', {'translated_text': translated_text})
    return render(request,'translator.html')