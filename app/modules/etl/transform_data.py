# transform_data.py


class TransformData:
    def __init__(self, jsons):
        self.jsons = jsons

    def filter_data(self, data):
        if 'keywords' in data:
            keywords = data['keywords']
            if 'Futebol' not in keywords and 'Esportes' not in keywords:
                self.filter_genres(data)
                self.filter_keywords(data)
                self.filter_crew(data)
                self.filter_director(data)
                return data

    def filter_director(self, data, rep=3):
        if 'director' in data:
            director = data['director'].lower().replace(' ', '')
            filter_director = [director] * rep
            data['director'] = ' '.join(filter_director)

    def filter_crew(self, data, limit=3):
        if "cast" in data:
            crew = data['cast']
            filter_crew = [person.lower().replace(' ', '') for person in crew]
            if len(filter_crew) > limit:
                data['cast'] = filter_crew[:limit]
                return
            data['cast'] = filter_crew

    def filter_keywords(self, data):
        if 'keywords' in data:
            keywords = data['keywords']
            filter_keywords = [key.lower().replace(' ', '') for key in keywords if key.lower() != "filmes"]
            data['keywords'] = filter_keywords

    def filter_genres(self, data):
        if 'genres' in data:
            filter_genres = []
            genres = data['genres']
            for genre in genres:
                if genre.lower() != 'filmes' and genre.lower() != 'pago por evento':
                    filter_genres.append(genre)
            filter_genres = [genre.lower().replace(' ', '') for genre in filter_genres]
            data['genres'] = filter_genres

    def collect_t_data(self):
        extract_data = []
        for json in self.jsons:
            if self.filter_data(json):
                extract_data.append(json)
        return extract_data
