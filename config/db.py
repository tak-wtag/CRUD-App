from sqlalchemy import create_engine, MetaData
import psycopg2

#engine = create_engine("postgresql+psycopg2://root:1234@localhost:5433/crud_db")
meta = MetaData()
conn = psycopg2.connect(host = "localhost", database = "crud_db" , user = "root", password = "1234" , port = "5433")

