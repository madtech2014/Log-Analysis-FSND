import psycopg2

DBNAME = "news"


def top_articles():
    """ Return: What are the most popular three articles of all time? """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT title, views FROM article_view LIMIT 3;")
    articles = c.fetchall()
    for i in articles:
        print (i[0] + ' <--->' + str(i[1]))
    db.close()

def top_authors():
    """ Return: Who are the most popular article authors of all time? """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT * FROM author_view;")
    authors = c.fetchall()
    db.close()
    for i in authors:
        print (i[0] + ' <---> ' + str(i[1]))

def request_errors():
    """ Return: On which days did more than 1% of requests lead to errors? """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT * FROM request_errors_view where \"Percent Error\" >1;")
    errors = c.fetchall()
    db.close()
    for i in errors:
        print (i[0])
        print (str(round((i[1]), 2)) + '% errors')


print ("=" * 60)
print ("The three all time most popular articles are:")
top_articles()
print ("=" * 47)
print ("The all time most popular article authors are:")
top_authors()
print ("=" * 47)
print ("These days had more than 1% of requests end in an error:")
request_errors()
print ("=" * 60)