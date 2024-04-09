from blog_app.models import Catagory
from blog_app.models import Article

def categores(request):
    
    categore=Catagory.objects.all()
    
    return {'categore': categore}


def recent_articles(request):
    
    recent_article=Article.objects.order_by('-created')
    
    return {'recent_article':  recent_article}
