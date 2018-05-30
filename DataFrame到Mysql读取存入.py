#encoding=utf-8
import pandas as pd
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.types import String,BLOB
mysql_cn = create_engine('mysql+mysqldb://root:bmg123@localhost:3306/bbs_pro?charset=utf8')
#mysql_cn=MySQLdb.connect(host="localhost",port=3306,user='root',passwd='bmg123',db='bbs_pro',charset='utf8')
df=pd.read_sql("select * from app01_bbs",con=mysql_cn)
#mysql_cn.close()
#mysql_cn=MySQLdb.connect(host="localhost",port=3306,user='root',passwd='bmg123',db='bbs_pro',charset='utf8')
pd.io.sql.to_sql(df,'app01_bbs_1',con=mysql_cn,if_exists='append',index=False)

