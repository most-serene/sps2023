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
    cursor.execute('SELECT * from title_ratings ORDER BY "numVotes" DESC limit 20000')

    res = cursor.fetchall()
    pref_sum = [0]
    l = []
    for id, _, n in res:
        pref_sum.append(pref_sum[-1] + n)
        l.append(id)

    out = []
    for _ in range(10000):
        rand = random.randint(0, 1110145450)
        pos = binSearch(0, len(pref_sum), rand, pref_sum)
        out.append(l[pos])

    print(",".join(out))







except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)