import tweepy

def main():

    twitter_auth_keys = { 

        "consumer_key"        : "nNoojM2RPCZ4jSBMfXmqJczOA",

        "consumer_secret"     : "agVOB8PHhIP56aw0JSGLgtCc8KNw10TZ9tAiX7ta36SeJSA0Yv",

        "access_token"        : "1269884561946587137-LnkRKoTOiZUgczwBObIuaEsuHwE5EE",

        "access_token_secret" : "p8mQjWf4jcxx9LkmGgZNzalagc4e9pxY8OYRjSphMw6Hb"

    }

 

    auth = tweepy.OAuthHandler(

            twitter_auth_keys['consumer_key'],

            twitter_auth_keys['consumer_secret']

            )

    auth.set_access_token(

            twitter_auth_keys['access_token'],

            twitter_auth_keys['access_token_secret']

            )

    api = tweepy.API(auth)

 

    tweet = "bottest#6969 #fuckthejannies"

    status = api.update_status(status=tweet) 

 

if __name__ == "__main__":

    main()