
import tweepy as tw

api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''

#Bloques necesarios para empezar la app
auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth, wait_on_rate_limit=True)

#FUNCIONALIDADES
#Comentadas para que no de errores

#Buscar usuario (puede ser por id o screen_name, o por id de tweet)
#user = api.get_user(id=)
#print=(user.name)
#print(user.description)

#Seguir usuario
api.create_friendship(screen_name='generic_name')    

#Twitear
api.update_status("Generic tweet")


#Likear 10 tweets de la timeline
#tweets_home= api.home_timeline(count=10)
#for tweet in tweets_home:
#    if tweet.author.name.lower() != 'generic_name':
#        if not tweet.favorited:
#            print(f"Liking this tweet from ({tweet.author.name})")
#            api.create_favorite(tweet.id)
            

#Buscar usuario y likear ultimos tweets
#user= api.get_user(screen_name='generic_name')
#user_tweets=api.user_timeline(user_id=user.id)
#for tweet in user_tweets:
#    if not tweet.favorited:
#       api.create_favorite(tweet.id)  


#Busca e imprime por contenido de tweet
#tweets=api.search_tweets( q='generic_search', count=10)
#for tweet in tweets:
#    print(tweet.text)    
            
            
            
