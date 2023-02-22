from concurrent.futures import ThreadPoolExecutor

from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site
from django.template.loader import render_to_string

from blog.models import Category, Post
from newsletter.models import Newsletter 


def get_posts_details(category):
    """
    Take link of rss feed as argument
    """
    print("At " + category.name)
    
    if category.rss is not None:
        import feedparser 
        
        blog_feed = feedparser.parse(category.rss)
        posts = blog_feed.entries
        
        if posts:
            for post in posts:
                title = post.title
                link = post.link
                author = post.author
                time_published = post.published
                authors = [author.name for author in post.authors]
                try:
                    summary = post.summary
                except:
                    summary = ""
                art = Post.objects.filter(slug=slugify(title))
                if not art.exists():
                    Post.objects.create(
                        title=title,
                        url=link,
                        author=author,
                        published_at=time_published,
                        description=summary,
                        category=category,
                    )

    else:
        return

def feedsCronJob():
    print("Running feeds CronJob")
    categories = Category.objects.filter(is_active=True)
    with ThreadPoolExecutor() as executor:
        executor.map(get_posts_details, categories)
    # for category in categories:
    #     get_posts_details(category)


current_site = Site.objects.get_current()
subject = "Market Insider"

def send_newsletter(subscriber):
  print("About to send newsletter")
  message = render_to_string(
      "newsletter/email/newsletter-email.html", {
        "subscriber": subscriber,
        "domain": current_site.domain,
        "uuid": subscriber.uuid,
        "posts": Post.objects.prefetch_related("category").all()[:4],
      })
  subscriber.email_user(subject, message)
    
def newsletterCronJob():
  subscribers = Newsletter.objects.filter(is_active=True)
  
  print("Running newsletter CronJob")
  with ThreadPoolExecutor() as executor:
      executor.map(send_newsletter, subscribers)
#   for subscriber in subscribers:
#       send_newsletter(subscriber)