import psycopg2

conn = psycopg2.connect(database='d15du25cqi1ai', user='kxacqnvdigfpcg', password='ed3463995fdce46daef26f789f90627fa45993b3bee0cb55e95fb2293c015a02', host='ec2-52-72-99-110.compute-1.amazonaws.com', port=5432)

cursor = conn.cursor()
cursor.execute("INSERT INTO publishers(publisher_id,name) values (1,'O Reilly Media'); ")

conn.commit()
conn.close()