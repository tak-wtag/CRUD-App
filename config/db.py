from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql+psycopg2://root:1234@localhost:5433/crud_db")
meta = MetaData()
conn = engine.connect()


