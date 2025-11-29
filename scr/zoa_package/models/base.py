"""ДЗ по теме SQLAlchemy."""
# ДЗ по теме SQLAlchemy, Подключение к СУБД, Таблицы, Описание
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, Float, Text, ForeignKey
from typing import Optional

class Base(DeclarativeBase):
    pass

# Определение таблицы users
class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(String(200), nullable=False, server_default='true')

#Core
'''users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(50), nullable=False, unique=True),
    Column('is_active', Boolean, nullable=False, server_default='true')
)'''

class Scarr(Base):
    __tablename__ = 'scarr'
    carrid: Mapped[int] = mapped_column(Integer, primary_key=True)
    carname: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

#Core
'''scarr_table = Table(
    'scarr',
    metadata,
    Column('carrid', Integer, primary_key=True),
    Column('carname', String(50), nullable=False, unique=True)
)'''

class Spfli(Base):
    __tablename__ = 'spfli'
    carrid: Mapped[int] = mapped_column(Integer, ForeignKey('scarr.carrid'), primary_key=True)
    connid: Mapped[int] = mapped_column(Integer, primary_key=True)
    countryfr: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    cityfr: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    airpfr: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    countryto: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    cityto: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    airpto: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    fltime: Mapped[int] = mapped_column(Integer, unique=False, nullable=False )

#Core
'''spfli_table = Table(
    'spfli',
    metadata,
    Column('carrid', Integer, ForeignKey('scarr.carrid'), primary_key=True),
    Column('connid', Integer, primary_key=True),
    Column('countryfr', String(50), nullable=True, unique=False),
    Column('cityfr', String(50), nullable=True, unique=False),
    Column('airpfr', String(50), nullable=True, unique=False),
    Column('countryto', String(50), nullable=True, unique=False),
    Column('cityto', String(50), nullable=True, unique=False),
    Column('airpto', String(50), nullable=True, unique=False),
    Column('fltime', Float, nullable=False, unique=False)
)'''

class Sflight(Base):
    __tablename__ = 'sflight'
    carrid: Mapped[int] = mapped_column(Integer, ForeignKey('scarr.carrid'), primary_key=True)
    connid: Mapped[int] = mapped_column(Integer, primary_key=True)
    fldate: Mapped[Date] = mapped_column(Date, primary_key=True)
    price: Mapped[Float] = mapped_column(Float(precision=2))
    currency: Mapped[str] = mapped_column(String(3), unique=False, nullable=False)
    seatmax: Mapped[int] = mapped_column(Integer, nullable=False, unique=False)
    seatocc: Mapped[int] = mapped_column(Integer, nullable=False, unique=False)
    carrid: Mapped[Spfli] = relationship('spfi', back_populates='sflight')
    connid: Mapped[Spfli] = relationship('spfi', back_populates='sflight')

#Core
'''sflight_table = Table(
    'sflight',
    metadata,
    #Column('carrid', Integer, ForeignKey('scarr.carrid'), ForeignKey('spfli.carrid'), primary_key=True),
    Column('carrid', Integer, ForeignKey('scarr.carrid'), primary_key=True),
    #Column('connid', Integer, ForeignKey('spfli.connid'), primary_key=True),
    Column('connid', Integer, primary_key=True),
    Column('fldate', Date, primary_key=True),
    Column('price', Float, nullable=False, unique=False),
    Column('currency', String(3), nullable=False, unique=False),
    Column('seatmax', Integer, nullable=False, unique=False),
    Column('seatocc', Integer, nullable=True, unique=False),
)'''

class Sbook(Base):
    __tablename__ = 'sbook'
    carrid: Mapped[int] = mapped_column(Integer, ForeignKey('scarr.carrid'), primary_key=True)
    connid: Mapped[int] = mapped_column(Integer, primary_key=True)
    fldate: Mapped[Date] = mapped_column(Date, primary_key=True)
    bookid: Mapped[int] = mapped_column(Integer, primary_key=True)
    userid: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    carrid: Mapped[Sflight] = relationship('sflight', back_populates='sbook')
    connid: Mapped[Sflight] = relationship('sflight', back_populates='sbook')
    fldate: Mapped[Sflight] = relationship('sflight', back_populates='sbook')

#Core
'''sbook_table = Table(
    'sbook',
    metadata,
    #Column('carrid', Integer, ForeignKey('scarr.carrid'), ForeignKey('sflight.carrid'), primary_key=True),
    Column('carrid', Integer, ForeignKey('scarr.carrid'), primary_key=True),
    #Column('connid', Integer, ForeignKey('sflight.connid'), primary_key=True),
    Column('connid', Integer, primary_key=True),
    #Column('fldate', Date,  ForeignKey('sflight.fldate'), primary_key=True),
    Column('fldate', Date,  primary_key=True),
    Column('bookid', Integer, primary_key=True),
    Column('userid', Integer, ForeignKey('users.id'))
)'''

