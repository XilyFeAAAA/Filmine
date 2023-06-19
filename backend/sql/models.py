import time
from datetime import datetime
from typing import List, Optional

from sqlalchemy import String, BigInteger, Boolean, ForeignKey, Integer, FLOAT, desc, LargeBinary, Text
from sqlalchemy.orm import Mapped, DeclarativeBase
from sqlalchemy.orm import mapped_column, relationship


class Base(DeclarativeBase):
    pass


class MovieStats(Base):
    __tablename__ = "da_movie_stats"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    country: Mapped[str] = mapped_column(Text(), nullable=False)
    genre: Mapped[str] = mapped_column(Text(), nullable=False)
    year: Mapped[str] = mapped_column(Text(), nullable=False)
    rating: Mapped[str] = mapped_column(Text(), nullable=False)
    duration: Mapped[str] = mapped_column(Text(), nullable=False)
    lan: Mapped[str] = mapped_column(Text(), nullable=False)
    word: Mapped[str] = mapped_column(Text(), nullable=False)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)



class Douban(Base):
    __tablename__ = 'da_doubans'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    screenshot: Mapped[str] = mapped_column(String(100), nullable=False)
    douban_id:  Mapped[str] = mapped_column(String(100), nullable=False)
    wish:  Mapped[str] = mapped_column(Text(), nullable=False)
    do:  Mapped[str] = mapped_column(Text(), nullable=False)
    collect:  Mapped[str] = mapped_column(Text(), nullable=False)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)

class Store(Base):
    __tablename__ = 'da_stores'
    # ID of the store
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    source: Mapped[str] = mapped_column(String(100), nullable=False)
    notes: Mapped[str] = mapped_column(String(100), nullable=False)
    cookie: Mapped[str] = mapped_column(String(100),nullable=False)
    email: Mapped[str] = mapped_column(String(100),nullable=False)
    created_time: Mapped[int] = mapped_column(BigInteger, nullable=False)
    m_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('da_movie_stats.id'),autoincrement='no action', nullable=True) # 指向crawl表
    # relationship
    moviestats: Mapped[MovieStats] = relationship("MovieStats")
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)

class User(Base):
    __tablename__ = 'da_users'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)
    created_time: Mapped[int] = mapped_column(BigInteger, nullable=False)
    verified: Mapped[bool] = mapped_column(Boolean, default=False)
    # 外键
    store_record = relationship('StoreRecord',
                             back_populates='user',
                             primaryjoin='and_(User.id == StoreRecord.u_id, StoreRecord.deleted == False)')
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)



class Verify(Base):
    __tablename__ = 'da_verifies'
    # ID of the store
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    token: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[bool] = mapped_column(Boolean, default=False)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)



class Crawler(Base):
    __tablename__ = 'da_crawlers'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    qrcode_url: Mapped[str] = mapped_column(Text(), nullable=True)
    running: Mapped[int] = mapped_column(BigInteger, default=0)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)



class StoreRecord(Base):
    __tablename__ = 'da_storerecords'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    token: Mapped[str] = mapped_column(String(100), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_time: Mapped[int] = mapped_column(BigInteger, nullable=False)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    # 外键
    u_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('da_users.id'),autoincrement='no action', nullable=False) # 指向user表
    d_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('da_doubans.id'),autoincrement='no action', nullable=True) # 指向user表
    s_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('da_stores.id'),autoincrement='no action', nullable=True) # 指向store 表
    c_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('da_crawlers.id'),autoincrement='no action', nullable=True) # 指向crawl表
    # relationship
    user: Mapped[User] = relationship( back_populates='store_record')
    douban: Mapped[Douban] = relationship("Douban")
    store: Mapped[Store] = relationship("Store")
    crawl: Mapped[Crawler] = relationship("Crawler")


class Movie(Base):
    __tablename__ = 'da_movies'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    douban_id: Mapped[str] = mapped_column(String(100), nullable=True)
    imdb_id: Mapped[str] = mapped_column(String(100), nullable=True)
    title: Mapped[str] = mapped_column(String(100), nullable=True)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
    region: Mapped[str] = mapped_column(Text(), nullable=True)
    score: Mapped[str] = mapped_column(String(100), nullable=True)
    runtime: Mapped[str] = mapped_column(String(100), nullable=True)
    language: Mapped[str] = mapped_column(Text(), nullable=True)
    genre: Mapped[str] = mapped_column(Text(), nullable=True)
    time: Mapped[str] = mapped_column(String(100), nullable=True)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)

