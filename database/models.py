# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 19, 2024 05:47:51
# Database: sqlite:////tmp/tmp.r3GI8AJSCD/CarDealershipDatabase_iter_1_1/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Represents a customer of the dealership.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    unpaid_sales_count = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    ShowroomVisitList : Mapped[List["ShowroomVisit"]] = relationship(back_populates="customer")
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="customer")



class Dealer(SAFRSBaseX, Base):
    """
    description: Represents an individual or company that sells cars.
    """
    __tablename__ = 'dealers'
    _s_collection_name = 'Dealer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    contact_number = Column(String)
    inventory_limit = Column(Integer, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    CarList : Mapped[List["Car"]] = relationship(back_populates="dealer")



class Employee(SAFRSBaseX, Base):
    """
    description: Represents an employee working at the dealership.
    """
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class FinanceOption(SAFRSBaseX, Base):
    """
    description: Available finance options for purchasing cars.
    """
    __tablename__ = 'finance_options'
    _s_collection_name = 'FinanceOption'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    interest_rate = Column(Integer, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Insurance(SAFRSBaseX, Base):
    """
    description: Car insurance details related to dealership offerings.
    """
    __tablename__ = 'insurances'
    _s_collection_name = 'Insurance'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    policy_details = Column(String)
    monthly_premium = Column(Integer, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Car(SAFRSBaseX, Base):
    """
    description: Represents a car available in the dealership.
    """
    __tablename__ = 'cars'
    _s_collection_name = 'Car'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    description = Column(String)
    dealer_id = Column(ForeignKey('dealers.id'))

    # parent relationships (access parent)
    dealer : Mapped["Dealer"] = relationship(back_populates=("CarList"))

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="car")
    RepairList : Mapped[List["Repair"]] = relationship(back_populates="car")
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="car")
    ServiceAppointmentList : Mapped[List["ServiceAppointment"]] = relationship(back_populates="car")
    WarrantyList : Mapped[List["Warranty"]] = relationship(back_populates="car")



class ShowroomVisit(SAFRSBaseX, Base):
    """
    description: Tracks visits made by potential customers to the showroom.
    """
    __tablename__ = 'showroom_visits'
    _s_collection_name = 'ShowroomVisit'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'))
    visit_date = Column(DateTime, nullable=False)
    notes = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ShowroomVisitList"))

    # child relationships (access children)



class Inventory(SAFRSBaseX, Base):
    """
    description: Contains current stock details of cars in dealership inventory.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    stock_amount = Column(Integer, nullable=False)
    location = Column(String)
    total_stock = Column(Integer)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Repair(SAFRSBaseX, Base):
    """
    description: Details repair work done on vehicles.
    """
    __tablename__ = 'repairs'
    _s_collection_name = 'Repair'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    repair_date = Column(DateTime, nullable=False)
    cost = Column(Integer, nullable=False)
    repair_shop = Column(String)
    description = Column(String)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("RepairList"))

    # child relationships (access children)



class Sale(SAFRSBaseX, Base):
    """
    description: Represents a sale transaction of a car to a customer.
    """
    __tablename__ = 'sales'
    _s_collection_name = 'Sale'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    customer_id = Column(ForeignKey('customers.id'))
    sale_date = Column(DateTime)
    amount = Column(Integer, nullable=False)
    paid = Column(Boolean)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("SaleList"))
    customer : Mapped["Customer"] = relationship(back_populates=("SaleList"))

    # child relationships (access children)



class ServiceAppointment(SAFRSBaseX, Base):
    """
    description: Holds details of service appointments for cars.
    """
    __tablename__ = 'service_appointments'
    _s_collection_name = 'ServiceAppointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    appointment_date = Column(DateTime, nullable=False)
    serviced_by = Column(String)
    notes = Column(String)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("ServiceAppointmentList"))

    # child relationships (access children)



class Warranty(SAFRSBaseX, Base):
    """
    description: Details warranty information of cars sold.
    """
    __tablename__ = 'warranties'
    _s_collection_name = 'Warranty'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('cars.id'))
    coverage_details = Column(String)
    valid_until = Column(DateTime)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("WarrantyList"))

    # child relationships (access children)
