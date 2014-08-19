from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')

def view_list(request, list_id):
    lst = List.objects.get(id=list_id)
    items = Item.objects.filter(list=lst)
    return render(request, 'list.html', {'items': items})

def new_list(request):
    lst = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=lst)
    return redirect('/lists/%d/' % (lst.id,))