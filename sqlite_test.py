import sqlite3
#conn = sqlite3.connect('/tmp/example')
#c = conn.cursor()
#c.execute('''create table stocks
#    (data text, trans text, symbol text,
#    qty real, price real)''')
#c.execute("""insert into stocks
#        values ('2006-01-05','BUY','RHAT',100,35.14)""")
#for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#          ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#          ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#         ]:
#    c.execute("insert into stocks values(?,?,?,?,?)",t)
#c.execute("select * from stocks order by price")
#for row in c:
#    print row
#import md5
#
#def md5sum(t):
#    return md5.md5(t).hexdigest()
#
#con = sqlite3.connect(":memory:")
#con.create_function("md5",1,md5sum)
#cur = con.cursor()
#cur.execute("select md5(?)",("foo",))
#print cur.fetchone()
#print md5sum("foo")
class Point():
    def __init__(self,x,y):
        self.x,self.y = x,y
    def __conform__(self,protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%f;%f" % (self.x,self.y)
con = sqlite3.connect(":memory:")
cur = con.cursor()
p = Point(0.3,0.4)
cur.execute("select ?",(p,))
print cur.fetchone()[0]
