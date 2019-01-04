import json
import sys
from datetime import datetime

class clusterd_tweet_day_count():

    def count(self, tweet_cluster_path, cluster_timeseries_path):

        #initialize variables
        tweet_frequency = {}

        # time format
        tweet_date_format = '%a %b %d %X %z %Y'

        #read tweet cluster
        tweet_cluster = json.loads(open(tweet_cluster_path).read())

        for key, values in tweet_cluster.items():
            for tweet in values:
                tweet_date_unformated = tweet['created_at']
                parsed_retweet_creation_date = datetime.strptime(tweet_date_unformated, tweet_date_format)
                tweet_date = str(parsed_retweet_creation_date.year) + '-' + str(parsed_retweet_creation_date.month) + '-' + str(parsed_retweet_creation_date.day)
                try:
                    tweet_frequency[key][tweet_date] += 1
                except:
                    tweet_frequency[key][tweet_date] = 1

        # open json file and write the json output to it
        with open(cluster_timeseries_path, "w") as write_file:
            json.dump(tweet_frequency, write_file)

if __name__ == '__main__':
    object = clusterd_tweet_day_count()
    object.count(sys.argv[1], sys.argv[2])
