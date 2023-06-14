import Levenshtein as lev

def search(query, db, n=10):
    sorted_db = sorted(db, key=lambda item: lev.distance(query, item))
    return sorted_db[:n]