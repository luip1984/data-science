import pandas as pd
import sqlalchemy as sqla

# postgresql://user@host/dbname
engine = sqla.create_engine("postgresql://awz@localhost/thinkful")

listings = pd.read_csv('cph_listings.csv.gz', parse_dates=['last_scraped'])

listings.to_sql('cph_listings', engine, schema='public', if_exists='replace')
