from django.shortcuts import render
from .models import Restaurant
def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "my_list":[
            {
                'name':'Subway',
                'food_type':'Sandwiches.',
            },
            {
                'name':'Steers',
                'food_type':'Burgers, Fries, and Pasta.',
            },
            {
                'name':'Backyard',
                'food_type':'Been there, done that...',
            },
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    res = Restaurant()
    res.name = "Al Baik"
    res.description = "Fast Food"
    res.opening_time = "11:00 AM"
    res.closing_time = "12:00 PM"
    res.save()

    '''
    rest2 = Restaurant.objects.create(name="AlSorror")
    rest2.name = "AlSorror"
    rest2.description = "mndy"
    rest2.opening_time="01:00 PM"
    rest2.closing_time="12:00 PM"
    rest2.save()
    Restaurant.objects.values_list('name', flat=True)
    '''

    res = 'Printing all Dreamreal entries in the DB : <br>'
    b = Restaurant.objects.all()
    attachment = {"my_object": {}}
    attachment['my_object'] = b[1]
    #attachment['my_object'] = b.description
    #attachment['my_object'] = b.opening_time
    #attachment['my_object'] = b.closing_time



    context = {
        "my_object":{
                        'name':'Subway',
                        'food_type':'Sandwiches.',
                    },
    }
    return render(request, 'detail.html', attachment)
