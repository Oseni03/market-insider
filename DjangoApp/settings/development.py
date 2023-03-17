from .core import *

# debug_toolbar settings
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
    # Database
    
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = "smtp.zoho.com"
    EMAIL_HOST_USER = "marketinsider@zohomail.com"
    EMAIL_HOST_PASSWORD = "bRUNbdf8NNmh"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True 
    
    # SUPABASE DATABASE CONFIGURATION
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'b99yW7DZOOoWKeLL',
            'HOST': "db.mppmrfilfloqpzxlajuc.supabase.co",
            'POST': "5432"
        }
    }
    
    # RAILWAY DATABASE CONFIGURATION 
    
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'railway',
    #         'USER': 'postgres',
    #         'PASSWORD': '67MDGlPTtCinbrbYVdb2',
    #         'HOST': "containers-us-west-57.railway.app",
    #         'POST': "5809"
    #     }
    # }