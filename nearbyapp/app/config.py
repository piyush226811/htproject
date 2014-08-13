# config.py

from authomatic.providers import oauth2

CONFIG = {
    
    'fb': {
           
        'class_': oauth2.Facebook,
        
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '278440232342735',
        'consumer_secret': '371c9524d2b8d0ace350d6c75157a30f',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream','user_friends'],
    },
}
