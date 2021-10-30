from sqlalchemy import UniqueConstraint, PrimaryKeyConstraint, Column, Integer, DateTime, func, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint

_DECL_BASE = declarative_base()


class OrderEntity(_DECL_BASE):
    __tablename__ = 'ORDERS'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    registration_datetime = Column(DateTime, default=func.now())
    type = Column(String)
    symbol = Column(String)
    quantity = Column(Float)
    side = Column(String)
    position_side = Column(String)
    status = Column(String)
    price = Column(Float)
    stop_price = Column(Float)
    timeInForce = Column(String)
    activation_price = Column(Float)
    callback_rate = Column(Float)
    close_position = Column(Boolean)


class DailyBalanceEntity(_DECL_BASE):
    __tablename__ = 'DAILY_BALANCE'
    id = Column(Integer, primary_key=True)
    registration_datetime = Column(DateTime, default=func.now())
    day = Column(DateTime)
    totalWalletBalance = Column(Float)


class BalanceEntity(_DECL_BASE):
    __tablename__ = 'BALANCE'
    id = Column(Integer, primary_key=True)
    registration_datetime = Column(DateTime, default=func.now())
    totalWalletBalance = Column(Float)
    totalUnrealizedProfit = Column(Float)
    assets = relationship("AssetBalanceEntity",
                          back_populates="balance", cascade="all, delete")


class AssetBalanceEntity(_DECL_BASE):
    __tablename__ = 'ASSET_BALANCE'
    id = Column(Integer, primary_key=True)
    registration_datetime = Column(DateTime, default=func.now())
    asset = Column(String)
    walletBalance = Column(Float)
    unrealizedProfit = Column(Float)
    balance_id = Column(Integer, ForeignKey('BALANCE.id'))
    balance = relationship("BalanceEntity", back_populates="assets")


class PositionEntity(_DECL_BASE):
    __tablename__ = 'POSITION'
    id = Column(Integer, primary_key=True)
    registration_datetime = Column(DateTime, default=func.now())
    symbol = Column(String)
    side = Column(String)
    unrealizedProfit = Column(Float)
    entryPrice = Column(Float)
    quantity = Column(Float)


class CurrentPriceEntity(_DECL_BASE):
    __tablename__ = 'PRICE'
    id = Column(Integer, primary_key=True)
    registration_datetime = Column(DateTime, default=func.now())
    symbol = Column(String)
    price = Column(Float)


class IncomeEntity(_DECL_BASE):
    __tablename__ = 'INCOME'
    id = Column(Integer, primary_key=True)
    registration_datetime = Column(DateTime, default=func.now())
    transaction_id = Column(Integer, nullable=False,
                            unique=True, sqlite_on_conflict_unique='IGNORE')
    symbol = Column(String)
    incomeType = Column(String)
    income = Column(Float)
    asset = Column(String)
    time = Column(DateTime)
    timestamp = Column(Integer)

    __table_args__ = (
        #PrimaryKeyConstraint(transaction_id, sqlite_on_conflict='IGNORE'),
        (UniqueConstraint('transaction_id', sqlite_on_conflict='IGNORE')),

    )
