from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    good = relationship("Goods")
    def __repr__(self):
        return 'id: {}, root cause: {}'.format(self.id, self.name)

association_table= Table(
    "associoation",
    Base.metadata,
    Column("tags_id", ForeignKey("tags.id"), primary_key=True),
    Column("goods_id", ForeignKey("Goods.id"), primary_key=True)
)

class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer,primary_key=True)
    name = Column(String, unique=True)
    goods = relationship("Goods", secondary=association_table, back_populates="Goods")


class Goods(Base):
    __tablename__ = "Goods"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    category = Column(Integer, ForeignKey("Goods.id"))
    tags = relationship("Tags", secondary=association_table, back_populates="Tags")
    count = Column(Integer)