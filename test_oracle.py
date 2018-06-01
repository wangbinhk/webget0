import cx_Oracle

conn = cx_Oracle.connect('data8l/oracle123@ladw_41')
c = conn.cursor()
c.close()
conn.close()