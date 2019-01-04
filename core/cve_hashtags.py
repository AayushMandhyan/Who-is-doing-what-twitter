import json
import sys
from os import listdir

class cve_hashtags():

    def fetch_hashtags(self, dir, filename):

        #initialize variables
        tweet_hashtags_list = []
        h = set()

        # fetch list of file in the directory
        file_list = listdir(dir)
        file_list = [dir + file for file in file_list]
        print('file list: ' + str(file_list))

        # computing through each of the file in the dir
        for file in file_list:
            print('file name: ', file)
            data = open(file, 'r')

            # convert the data into json format
            tweets = data.readlines()

            # convert the tweets in json format
            tweets = [json.loads(tweet) for tweet in tweets]

            # get hashtags within tweets
            tweet_hashtags = [tweet['entities']['hashtags'] for tweet in tweets]
            for hashtag in tweet_hashtags:
                th = []
                for hashs in hashtag:
                    th.append(hashs['text'])
                    h.add(hashs['text'])
                tweet_hashtags_list.append(th)

        print(tweet_hashtags_list)

        #convert the tweet_hashtags_list to json
        tweet_hashtags_list_json = {'hashtags' : tweet_hashtags_list}

        #open json file and write the json output to it
        with open(filename, "w") as write_file:
            json.dump(tweet_hashtags_list_json, write_file)

        print('Tweet hashtags list json stored')
        print('\n')
        print(h)
        print(len(h))


if __name__ == '__main__':
    object = cve_hashtags()
    object.fetch_hashtags(sys.argv[1], sys.argv[2])