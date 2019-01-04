import json
import sys
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile

class train_doc2vec():

    def train(self, hashtags, modelname):

        #load json object from the file
        hashlist = json.loads(open(hashtags).read())

        #creating document
        documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(hashlist['hashtags'])]

        #creating word2vec
        path = get_tmpfile(modelname)
        model = Doc2Vec(documents, size=100, window=5, min_count=5, workers=4)
        model.save(modelname)
        print('doc2vec model created')

if __name__ == '__main__':
    object = train_doc2vec()
    object.train(sys.argv[1], sys.argv[2])