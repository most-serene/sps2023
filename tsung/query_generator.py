import psycopg2
import random

def binSearch(l, r, n, lis):
    if r-l == 1:
        return r
    m = (r+l)//2
    if n > lis[m]:
        return binSearch(m, r, n, lis)
    else:
        return binSearch(l, m, n, lis)

try:
    conn = psycopg2.connect(user='??',
            password='??',
            host='??',
            port='??',
            database='??')

    cursor = conn.cursor()
    cursor.execute('SELECT tr.tconst, tb."primaryTitle", tr."numVotes" FROM title_ratings AS tr NATURAL JOIN title_basics AS tb ORDER BY tr."numVotes" DESC limit 20000')


    res = cursor.fetchall()
    pref_sum = [0]
    l = []
    for id, title, n in res:
        pref_sum.append(pref_sum[-1] + n)
        l.append([title, id])


    out = []
    for _ in range(10000):
        rand = random.randint(0, 1110145450)
        pos = binSearch(0, len(pref_sum), rand, pref_sum)
        out.append(l[pos])

    csv_file = open("queryset.csv", "w")
    for i in out:
        name, id = i
        csv_file.write(f'"{name}","{id}"\n')
        print(",".join(i))





except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)