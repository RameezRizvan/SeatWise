from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Create your views here.
def index(request):
    a = cardmodel.objects.all()
    id1 = []
    img = []
    for i in a:
        id3=i.id
        id1.append(id3)
        im=str(i.image).split('/')[-1]
        img.append(im)
    pair = zip(img,id1)
    return render(request, 'index.html', {'list': pair})
    # return render(request,'index.html')


def signup(request):
    if request.method=='POST':
        a=signupform(request.POST)
        if a.is_valid():
            firstname=a.cleaned_data['firstname']
            lastname=a.cleaned_data['lastname']
            email=a.cleaned_data['email']
            phone=a.cleaned_data['phone']
            password=a.cleaned_data['password']
            confirmpass=a.cleaned_data['confirmpass']
            if password==confirmpass:
                b=signupmodel(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password)
                b.save()
                subject = "your account has been created Successfully"
                message = "registered successfully"
                email_from = "rameez04rizvan@gmail.com"
                email_to = email
                send_mail(subject, message, email_from, [email_to])
                return redirect('login')
            else:
                return HttpResponse('password does not match')
        else:
            return HttpResponse('registration failed')
    return render(request,'registration.html')


def login(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=signupmodel.objects.all()
            for i in b:
                if i.email==em and i.password==ps:
                  return redirect(index)
            else:
                return HttpResponse('incorrect email/password')
        else:
            return HttpResponse('Failed')
    return render(request,'login.html')



def moviecard(request):
    return render(request,'movie_cards.html')





def cardupload ( request ):
    if request.method == 'POST':
        a=cardform(request.POST,request.FILES)
        if a.is_valid():
            image=a.cleaned_data['image']
            name=a.cleaned_data['cardname']
            gen=a.cleaned_data['genres']
            cat=a.cleaned_data['category']
            youtu=a.cleaned_data['youtube']
            lang=a.cleaned_data['language']
            dur=a.cleaned_data['duration']
            abt=a.cleaned_data['about']
            b=cardmodel(image=image,cardname=name,genres=gen,category=cat,youtube=youtu,language=lang,duration=dur,about=abt)
            b.save()
            return redirect(cardupload)
        else:
            print(a.errors)
            return HttpResponse('failed')
    return render(request,'cards_upload.html')



def carddisplay(request):
    a=cardmodel.objects.all()
    id1=[]
    img=[]
    fname=[]
    gen=[]
    for i in a:
        id3=i.id
        id1.append(id3)
        im=str(i.image).split('/')[-1]
        img.append(im)
        fn=i.cardname
        fname.append(fn)
        ge=i.genres
        gen.append(ge)
    pair=zip(img,fname,gen,id1)
    return render(request,'movie_cards.html',{'list':pair})




def movie(request,id):
    a=cardmodel.objects.get(id=id)
    img=str(a.image).split('/')[-1]
    return render(request,'movie.html',{'a':a,'img':img,})







# def seat(request,id):
#     c=cardmodel.objects.get(id=id)
#     ticket_cost=int(150)
#     total_cost = 0
#     if request.method == 'POST':
#         a = seatselecform(request.POST)
#         if a.is_valid():
#             selected_seats = a.cleaned_data['selectedseats']
#             date=a.cleaned_data['date']
#             time=a.cleaned_data['time']
#             request.session['seat_name']=selected_seats
#             request.session['date']=date
#             request.session['time']=time
#             selected_seat_list = selected_seats.split(',')
#             total_cost=ticket_cost*len(selected_seat_list)
#             print('tc=',total_cost)
#             request.session['total_cost'] = total_cost
#             booked_seats = seatselection1.objects.values_list('selectedseats', flat=True)
#             for seat in selected_seat_list:
#                 if seat in booked_seats:
#                     return HttpResponse(movie,'Seats already booked')
#
#             for i in range(1, len(selected_seat_list) + 1):
#                 for j in range(len(selected_seat_list) - i + 1):
#                     group = selected_seat_list[j:j+i]
#                     if ','.join(group) in booked_seats:
#                         return HttpResponse('Group seats already booked')
#             b = seatselection1(movie=c,selectedseats=selected_seats,date=date,time=time)
#             b.save()
#             return redirect(f'http://127.0.0.1:8000/seatwiseapp/ticket/{c.id}')
#         else:
#             print(a.errors)
#             return HttpResponse('Failed')
#     booked_seats = seatselection1.objects.values_list('selectedseats', flat=True)
#     return render(request, 'seat_selection.html',{'booked_seats': booked_seats,'c':c})
def seat(request, id):
    c = cardmodel.objects.get(id=id)
    ticket_cost = int(150)
    total_cost = 0

    if request.method == 'POST':
        a = seatselecform(request.POST)

        if a.is_valid():
            selected_seats = a.cleaned_data['selectedseats']
            date = a.cleaned_data['date']
            time = a.cleaned_data['time']

            # Assign the selected movie to the seat reservation
            request.session['seat_name'] = selected_seats
            request.session['date'] = date
            request.session['time'] = time
            request.session['selected_movie'] = c.id  # Store the movie ID

            selected_seat_list = selected_seats.split(',')
            total_cost = ticket_cost * len(selected_seat_list)
            request.session['total_cost'] = total_cost

            # Check if the selected seats are already booked for the same movie
            booked_seats = seatselection1.objects.filter(movie=c, selectedseats__in=selected_seat_list)
            if booked_seats:
                return HttpResponse(f'Seats already booked for movie {c.title}')

            # Check if any group of seats is already booked for the same movie
            for i in range(1, len(selected_seat_list) + 1):
                for j in range(len(selected_seat_list) - i + 1):
                    group = selected_seat_list[j:j + i]
                    group_seats = ','.join(group)
                    if seatselection1.objects.filter(movie=c, selectedseats=group_seats).exists():
                        return HttpResponse(f'Group seats already booked for movie {c.title}')

            # Save the seat reservation with the associated movie
            b = seatselection1(movie=c, selectedseats=selected_seats, date=date, time=time)
            b.save()

            return redirect(f'http://127.0.0.1:8000/seatwiseapp/ticket/{c.id}')
        else:
            print(a.errors)
            return HttpResponse('Failed')

    # Retrieve booked seats for the same movie
    booked_seats = seatselection1.objects.filter(movie=c).values_list('selectedseats', flat=True)
    return render(request, 'seat_selection.html', {'booked_seats': booked_seats, 'c': c})


def ticket(request, id):
    c = get_object_or_404(cardmodel, id=id)  # Retrieve the cardmodel instance by its id
    a = request.session['seat_name'] # Filter seatselection records by movieid
    b= request.session['date']
    d=request.session['time']
    e = request.session.get('total_cost',)
    return render(request, 'ticket.html', {'c': c, 'a': a, 'b': b, 'd' : d,'e':e})


def payment(request):
    if request.method=='POST':
        return redirect(index)
    return render(request,'payment.html')

def test(request):
    a = seatselection1.objects.all()
    movie2=[]
    id1 = []
    date = []
    time = []
    seats = []
    for i in a:
        id3 = i.id
        id1.append(id3)
        date1=i.date
        date.append(date1)
        time1=i.time
        time.append(time1)
        seats1=i.selectedseats
        seats.append(seats1)
        movie1 = i.movie
        movie2.append(movie1)
    pair = zip(movie2, date, time, seats, id1)
    return render(request,'test.html',{'list':pair})



def cancel(request,id):
    a=seatselection1.objects.get(id=id)
    a.delete()
    return redirect(test)