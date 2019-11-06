
import pymysql

class DB():
	def __init__(self,host,user,passwd,port,db):
		self.conn=pymysql(host=host,user=user,password=passwd,port=port,database=db,charset="utf8")
		self.cursor=self.conn.cursor
	def select_sql(self,sql):
		try:
			self.cursor.execute(sql)
		except:
			pass
		data=self.cursor.fetchall()
		return data

	def execute_sql(self,sql):
		try:
			self.cursor.execute(sql)
			self.conn.commit()
		except:
			self.conn.rollback()
		














