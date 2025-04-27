from django.shortcuts import render

def app1(request):
    voter = [
        {'name':"Vinamra kumar", 'age' :  21},
        {'name':"Pinkesh Rana", 'age' :  21},
        {'name':"Jaswant Yadav", 'age' :  17},
        {'name':"Amit Sinha", 'age' :  20},
    ]
    
    return render(request , "index.html",context = {'voter_info' : voter})
#voter info ka use hum index.html mein karenge voter ke jagah par 
def contact(request):
    return render(request , "contact.html")

def about(request):
    return render(request , "about.html")


