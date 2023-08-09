import json


def get_clone_urls(raw):
    parsed = json.loads(raw)
    urls = []
    for i in parsed:
        urls.append(i['url'] + '.git')
    return urls