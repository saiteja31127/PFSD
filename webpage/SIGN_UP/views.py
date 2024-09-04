from django.shortcuts import render
import mysql.connector as sql

fn = ''
ln = ''
s = ''
em = ''
pwd = ''


# Create your views here.
def signaction(request):
    global fn, ln, s, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Saiteja@548", database='astrology')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "insert into users Values('{}','{}','{}','{}','{}')".format(fn, ln, s, em, pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'sign_up.html')

def about(request):
    return render(request, 'about.html')
def aries(request):
    return render(request, 'aries.html')
def taurus(request):
    return render(request, 'taurus.html')
def gemini(request):
    return render(request, 'gemini.html')
def cancer(request):
    return render(request, 'cancer.html')
def leo(request):
    return render(request, 'leo.html')
def virgo(request):
    return render(request, 'virgo.html')
def libra(request):
    return render(request, 'libra.html')
def scorpio(request):
    return render(request, 'scorpio.html')
def sagittarius(request):
    return render(request, 'sagittarius.html')
def capricorn(request):
    return render(request, 'capricorn.html')
def aquarius(request):
    return render(request, 'aquarius.html')
def pisces(request):
    return render(request, 'pisces.html')
def astrologers(request):
    return render(request, 'astrologers.html')
def zodiac(request):
    return render(request, 'zodiac.html')