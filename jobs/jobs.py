from concurrent.futures import ThreadPoolExecutor

from django.template.defaultfilters import slugify

from blog.models import Category, Post


class API_SCHEDULAR:
    def __init__(self):
        self.categories = Category.objects.filter(is_active=True)

    def get_posts_details(self, category):
        """
        Take link of rss feed as argument
        """
        print("At " + category.name)
        
        if category.rss is not None:
            # import the library only when url for feed is passed
            import feedparser 
            
            # parsing blog feed
            # blog_feed = blog_feed = feedparser.parse(rss)
            blog_feed = feedparser.parse(category.rss)
            
            # getting lists of blog entries via .entries
            posts = blog_feed.entries
            
            # dictionary for holding posts details
            posts_details = {
                "Blog title": blog_feed.feed.title,
                "Blog link": blog_feed.feed.link,
            }
            
            # iterating over individual posts
            for post in posts:
                print()
                # if any post doesn't have information then throw error.
                try:
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
                except:
                    print("Unable to save")
                    print()

            print(posts_details)  # returning the details which is dictionary
        else:
            return None

    def run(self):
        print("At run")
        # with ThreadPoolExecutor() as executor:
        #     executor.map(self.get_posts_details, self.categories)
        for category in self.categories:
            self.get_posts_details(category)


class Newsletter:
  
  def __init__(self, request):
      self.current_site = get_current_site(request)
      self.subject = "Market Insider"
      self.subcribers = Newsletter.objects.filter(is_active=True)
    #   self.categories = Category.objects.prefetch_related("posts").filter(is_active=True)
  
  def send_newsletter(self, subscriber):
      message = render_to_string("newsletter/email/index.html", {
        "subscriber": subscriber,
        "domain": self.current_site.domain,
        "uuid": subscriber.uuid,
        "posts": Post.objects.prefetch_related("category").all(),
      })
        # "categories": self.categories,
      subscriber.email_user(self.subject, message)