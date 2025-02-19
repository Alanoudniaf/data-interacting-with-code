# pylint: disable=missing-docstring, C0103


def directors_count(db):
    # return the number of directors contained in the database
    query ="""
            SELECT COUNT(*)
            FROM directors;
            """
    db.execute(query)
    return db.fetchone()[0]


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query ="""
            SELECT name
            FROM directors
            ORDER BY name;
            """
    db.execute(query)

    return [row[0] for row in db.fetchall()]


def river_movies(db):
    # return the list of all movies which contain the exact word "river"
    # in their title, sorted in alphabetical order
    query = """
            SELECT title
            FROM movies
            WHERE (lower(title) LIKE '% river %' OR
                   lower(title) LIKE 'river %' OR
                   lower(title) LIKE '% river' OR
                   lower(title) = 'river')
            ORDER BY title;
            """
    db.execute(query)
    return [row[0] for row in db.fetchall()]


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query ="""
            SELECT COUNT(*)
            FROM directors
            WHERE name LIKE ?;
            """
    db.execute(query,(f"%{name}%",))
    return db.fetchone()[0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query ="""
               SELECT title
               FROM movies
               WHERE minutes > ?
               ORDER BY title;
               """
    db.execute(query,(min_length,))
    return [row[0] for row in db.fetchall()]
