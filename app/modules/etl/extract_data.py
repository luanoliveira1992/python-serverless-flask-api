# extract_data.py


class ExtractData:
    def __init__(self, json):
        self.json = json
        self.actor = 3
        self.actress = 2
        self.director = 1

    def collect_id(self, json, extract):
        if "_id" in json:
            extract["id"] = json["_id"]

    def collect_keywords(self, body, extract):
        if "keywords" in body:
            extract["keywords"] = body["keywords"]

    def collect_description(self, body, extract):
        if "description" in body:
            description = body['description']
            if description != None:
                extract['description'] = description
                return
        extract['description'] = ''

    def collect_genres(self, body, extract):
        if "genres" in body:
            genres = body['genres']
            if len(genres) > 1:
                g_titles = [self.collect_title(genre) for genre in genres]
                extract['genres'] = g_titles
  
    def collect_crew(self, body, extract):
        if 'cast' in body:
            for doc in body['cast']:
                if 'kind' in doc and 'person' in doc:
                    kind = doc['kind']
                    if kind == self.actor or kind == self.actress:
                        full_name = self.collect_name(doc['person'])
                        self.insert_name('cast', full_name, extract)
                    elif kind == self.director:
                        full_name = self.collect_name(doc['person'])
                        extract['director'] = full_name
                    else:
                        full_name = self.collect_name(doc['person'])
                        self.insert_name('crew', full_name, extract)

    def insert_name(self, key, name, extract):
        if key in extract:
            extract[key].append(name)
            return
        extract[key] = [name]

    def collect_title(self, genre):
        return genre['title']

    def collect_name(self, person):
        first_name = person['firstName'] 
        last_name = ""#person['lastName']
        full_name = '{} {}'.format(first_name, last_name)
        return full_name

    def collect_raw_data(self):
        extract_data = []
        extract_json = {}
        json_source = self.json
        #self.collect_id(json, extract_json)
        self.collect_keywords(json_source, extract_json)
        self.collect_genres(json_source, extract_json)
        self.collect_crew(json_source, extract_json)
        self.collect_description(json_source, extract_json)
        extract_data.append(extract_json)
        return extract_data
