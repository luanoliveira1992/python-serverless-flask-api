# metrics.py

class Metrics:
    def __init__(self, json_movie, list_recommendation):
        self.movie = json_movie['_source']
        self.recommendation = [movie['_source'] for movie in list_recommendation]
        self.m_genres = self.extract_genre(json_movie['_source'])
        self.r_genres = self.extract_genres([movie['_source'] for movie in list_recommendation])

    @staticmethod
    def extract_genre(json_movie):
        result = set()
        try:
            genres = json_movie["genres"]
            for genre in genres:
                title = genre["title"]
                if title != "Filmes":
                    result.add(genre["title"])
        except:
            pass
        return result

    def extract_genres(self, list_movies):
        result = []
        for json_movie in list_movies:
            result.append(self.extract_genre(json_movie))
        return result

    @staticmethod
    def equal_set_genres(m_genres, r_genres):
        result = []
        for genres in r_genres:
            result.append(m_genres == genres)
        return result

    @staticmethod
    def occurrence_set_genres(m_genres, r_genres):
        result = []
        for genres in r_genres:
            result.append(bool(m_genres.intersection(genres)))
        return result

    @staticmethod
    def intersection_genres(r_genres):
        result = set()
        for genre in r_genres:
            result.update(genre)
        return result

    @staticmethod
    def new_genres(u_genres, m_genres):
        return u_genres.difference(m_genres)

    def metric_equal_precision(self):
        len_r_genres = len(self.r_genres)
        equal = self.equal_set_genres(self.m_genres, self.r_genres)
        len_equal = len([value for value in equal if value])
        return len_equal / len_r_genres

    def metric_occurrence_precision(self):
        len_r_genres = len(self.r_genres)
        occ = self.occurrence_set_genres(self.m_genres, self.r_genres)
        len_equal = len([value for value in occ if value])
        return len_equal / len_r_genres

    def metric_diversity(self):
        u_genres = self.intersection_genres(self.r_genres)
        n_genres = self.new_genres(u_genres, self.m_genres)
        return len(n_genres) / len(u_genres)

    def metric_novelty(self):
        len_r_genres = len(self.r_genres)
        occ = self.occurrence_set_genres(self.m_genres, self.r_genres)
        len_novelty = len([value for value in occ if not value])
        return len_novelty / len_r_genres

    def get_json_metrics(self):
        response = {}

        equal_precision = self.metric_equal_precision()
        occurrence_precision = self.metric_occurrence_precision()
        novelty = self.metric_novelty()
        diversity = self.metric_diversity()

        response["size_recommendation"] = len(self.recommendation)
        response["films"] = self.recommendation
        response["metrics"] = {"precision": {"equal": ('%.2f' % equal_precision), "occurrence": ('%.2f' % occurrence_precision)},
                               "diversity": ('%.2f' % diversity), "novelty": ('%.2f' % novelty)}

        return response
