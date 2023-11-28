from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
    newsapi = NewsApiClient(api_key='7d28cc5d8b874e1584c4ee8801ac738f')

    # Check if a search query is present in the request
    search_query = request.GET.get('q', '')
    
    selected_sources = request.GET.getlist('source')

    sources = ["NPR", "Reuters", "CNN", "Fox Business", "The Washington Post", "Google News", "Time", "Daily FX", "Business Insider"]

    if not selected_sources:
        selected_sources = sources
    
    if search_query:
        # If there is a search query, use /v2/everything endpoint
        search_results = newsapi.get_everything(q=search_query, sources=','.join(selected_sources))
        articles = search_results['articles']
    else:
        # If no search query, fetch top headlines
        top_headlines = newsapi.get_top_headlines(sources=','.join(selected_sources))
        articles = top_headlines['articles']

    news_titles = []
    descriptions = []
    images = []
    publishedAt = []
    source = []
    url = []

    for article in articles:
        news_titles.append(article['title'])
        descriptions.append(article['description'])
        images.append(article['urlToImage'])
        publishedAt.append(article['publishedAt'])
        source.append(article['source']['name'])
        url.append(article['url'])


    news_list = zip(news_titles, descriptions, images, publishedAt, source, url)

    
    return render(request, 'news.html', context={"mylist": news_list, "search_query": search_query, "sources": sources})

