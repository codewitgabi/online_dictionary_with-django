from django.shortcuts import render
from PyDictionary import PyDictionary


def home(request):
    if request.method == "POST":
        word = request.POST.get('word')
        dictionary = PyDictionary()

        meanings = dictionary.meaning(word)
        synonyms = dictionary.synonym(word)
        antonyms = dictionary.antonym(word)

        context = {
            'word': word,
            'meanings': meanings,
            'synonyms': synonyms,
            'antonym': antonyms
        }
        return render(request, 'myapp/home.html', context)
    else:
        return render(request, 'myapp/home.html')
