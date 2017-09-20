class RecordDataIntf(object):

    def get_high_score(self):
        raise NotImplementedError("Must Implement get_high_score")

    def post_score(self, score, word):
        raise NotImplementedError("Must Implement post_score")
