import sqlite3
import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

# Adaptador personalizado para converter datetime para string
def adapt_datetime(dt):
    return dt.isoformat()

# Conversor personalizado para converter string de volta para datetime
def convert_datetime(s):
    return datetime.fromisoformat(s.decode('utf-8'))

# Registrar adaptadores e conversores personalizados
sqlite3.register_adapter(datetime, adapt_datetime)
sqlite3.register_converter('DATETIME', convert_datetime)

# Conectar ao banco de dados com detect_types=sqlite3.PARSE_DECLTYPES
db_connection_handler.connect()

def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trips_infos = {
        "id": str(uuid.uuid4()),
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Sapo",
        "owner_email": "sapo@gmail.com"
    }
    
    trips_repository.create_trip(trips_infos)

    

