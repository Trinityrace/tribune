from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
import datetime as dt
from .models import Article

# Create your views here.
def welcome(request):
    #return HttpResponse('Welcome to the Moringa Tribune')
    return render(request, 'news/welcome.html')

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date, "news":news})

# def news_of_day(request):
#     date = dt.date.today()

#     # #Function to convert date object to find exact day
#     # day = convert_dates(date)
#     # html = f'''
#     #     <html>
#     #         <body>
#     #             <h1>News For {day} {date.day}-{date.month}-{date.year}</h1>
#     #         </body>
#     #     </html>
#     #         '''
#     # return HttpResponse(html)
#     return render(request, 'all-news/today-news.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_news(request,past_date):
    # error handling 
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
        
    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)

    return render(request, 'all-news/past-news.html', {"date": date, "news":news})
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #         '''
    # return HttpResponse(html)

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = (f"{search_term}")

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term,search again!"
        return render(request, 'all-news/search.html',{"message":message})