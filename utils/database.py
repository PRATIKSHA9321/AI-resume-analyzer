# utils/database.py
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Resume(Base):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True)
    filename = Column(String(200))
    score = Column(Integer)
    skills = Column(Text)
    missing_skills = Column(Text)
    suggestions = Column(Text)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

# Database connection
engine = create_engine('sqlite:///resume_analyzer.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()