from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify



# class ArticleManager(models.Manager):
#     def counter(self):
#         return len(self.all())
#     def   puplished(self):
#         return self.filter(puplished=True)

class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())
 
class Catagory(models.Model):
    title=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

class Article(models.Model):
    choices1=(
        ('a', 'پایتون'),
        ('b', 'جنگو'),
    )
    auther=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  #SET_NULL: یعنی زمانی  کاربر حذف می شود مقالات زیر مجموعه حذف نمی شود و فقط نام نویسنده خالی می شود د 
    # auther=models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='1')    #set_default:  وقتی نویسنده یا یوزیر حذف می شود یک مقدار دیفالت از داخل یوزرهای موجود انتخاب می کند و به جای یوزیر حذف شده قرار می دهد وآیدی یکی از یوزرها را بصورت پیش فرض قرار می دهیم
    # auther=models.ForeignKey(User, on_delete=models.PROTECT)     #  ایعنی محافظت شده به راحتی اجازه حذف کاربر را نمی دهد ینی اگر این کاربر مقالاتی زیر مجموعه خود داشته باشد حذف نمی شود اما اگر کاربر زیر مجموعی نداشته باشد به راحتی یوزیر حذف می شود
    # auther=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)   # CASCADE: اگر یوزر را حذف کنیم تمام مقالات یر مجموعه آن یوزیر 
    category=models.ManyToManyField(Catagory)
    title=models.CharField(max_length=40)
    # title=models.CharField(max_length=40,  help_text="inter your Title", choices=choices1, default='a')
    #  unique_for_date='pub_data'  # یعنی در اون تاریخ تو نمی تونی یک تای تل با نام یکسان ایجاد کنی
    
  
    body=models.TextField()
    image=models.ImageField(upload_to="images/articles")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)   # فیلد به روزرسانی
    pub_data=models.DateField(default=timezone.now())  #زمان انتشارکردن
  
    # data=models.DurationField(timezone.timedelta(days=23, hours=12, minutes=30, seconds=45))
    # information=models.BigIntegerField(default=0)
    url=models.URLField(null=True, blank=True)
    # myfile=models.FileField(upload_to='assets', null=True)      #این نوع فایل برای ذخیره فیلم و پی دی اف و حتی تصاویر هم میشه
    puplished=models.BooleanField(default=True)
    objects=ArticleManager()  
    slug=models.SlugField(blank=True, unique=True)
    
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.slug = slugify(self.title)
    #     super(Article, self).save()
   
    # models.Manager
    
    # class Meta:
    #     ordering= ('-created',)   #یعنی براساس اخرین آیتم مرتب کن
    #     verbose_name="مقاله"
    #     verbose_name_plural="مقاله ها"
  
  
    
    def get_absolute_url(self):
        return reverse('blog_app:article_detail', args=[self.id])
    
    def __str__(self):
         return self.title
    class Meta:
        ordering = ("-created" ,)
    
    



# class Comment(models.Model):
    
#     article= models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
#     user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    
#     parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='replies')
    
#     body = models.TextField()
    
#     created_at=models.DateTimeField(auto_now_add=True)    #تاریخ ثبت نظر 
    
    
    
#     def __str__(self):
        
#         return self.body[:35]
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments')
    
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replaies', null=True, blank=True)
    
    body = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.body[:50]
    
    
class Messagee(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    
    
    data = models.DateTimeField(default=timezone.now())
    
   
    
 
    
    def __str__(self):
        return self.title
    
    
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    






class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=500)
    phone_number=models.CharField(max_length=13, default='0')
    Gender=models.BooleanField()
  
    
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title
    
    
   
        
    
    
