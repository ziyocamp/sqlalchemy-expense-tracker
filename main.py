from app.database import engine, metadata_obj
import app.models

metadata_obj.create_all(engine)
