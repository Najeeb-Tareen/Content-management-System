from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Person , Categories, Article
from .forms import PersonForm , Categories_Form, article_Form

# Create your views here.

def person_data(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            prsn = Person.objects.create(username=username, email=email, age=age)
            prsn.save()
            return HttpResponse('Data added succesfuly')
    form = PersonForm
    return render(request, 'app/person.html', {'form':form})

def Categories_data(request):
    if request.method == "POST":
        form = Categories_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            typi = form.cleaned_data['typi']

            catti = Categories.objects.create(name=name, typi=typi )
            catti.save()
            print(catti)
            return HttpResponse('Category is added successfuly')
        
    form = Categories_Form
    return render(request, 'app/Categories.html', {'form':form})


def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        publication_date = request.POST.get('publication_date')
        category = request.POST.get('category')
        
        categor_obj = Categories.objects.filter(name=name)

        catti = Article(title=title, content=content, publication_date=publication_date )
        catti.save()

        cat = []
        for x in categor_obj:
            cat.append(category.id)

        Article.cat.set(category)
        # print(cat)
        return HttpResponse(f'{Article} Article')
    else:
        request.method == 'GET'
        return render(request, 'app/Article.html' )


def article_data(request):
    if request.method == "POST":
        form = article_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            typi = form.cleaned_data['typi']

            catti = Article.objects.create(name=name, typi=typi )
            catti.save()
            return HttpResponse('Category is added successfuly')
        
    form = article_Form
    frm = {'form':form}
    return render(request, 'app/Categories.html', frm)



def article_data(request):
    if request.method == "POST":
        form = article_Form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publication_date = form.cleaned_data['publication_date']
            category = form.cleaned_data['category']

            arti = Article.objects.create(title=title, content=content,
                  publication_date=publication_date, category=category)
            arti.save()
            return HttpResponse('Article is added successfuly')
    form = article_Form
    context={'form':form}
    return render(request, 'app/Article.html', context)




def author(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')

        usr = Person(username=username, email=email, age=age )
        usr.save()

        return HttpResponse('Author registred successfully')
    return render(request, 'app/person.html')




def add_article(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        publication_date = request.POST.get('publication_date')
        author = request.POST.get('author')
        userr=Person.objects.get(username = author)
        category = [x.name for x in Categories.objects.all()]
        category_ids = []
        
        for x in category:
            category_ids.append(int(request.POST.get(x))) if request.POST.get(x) else print('shut_up')
        

        article = Article.objects.create(title=title, content=content, publication_date=publication_date, author=userr)

        for x in category_ids:
            article.category.add(Categories.objects.get(id=x))

            return HttpResponse('article added')
        return render(request, 'app/Article.html' ,{'category':article})
        
       
        
    else:
        print('powww')



def caty(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        type = request.POST.get('type')
        

        usrr = Categories(name=name, type=type)
        usrr.save()

        return HttpResponse('Catory registred successfully')
    return render(request, 'app/Categories.html')
    





        

