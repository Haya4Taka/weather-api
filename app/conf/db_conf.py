import os
DB_CONFIG = {
  'user': os.environ['DB_USERNAME'],
  'password': os.environ['DB_PASSWORD'],
  'host': os.environ['DB_URL'],
  'database': os.environ['DB_NAME']
}