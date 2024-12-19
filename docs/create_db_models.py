# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Car(Base):
    """description: Represents a car available in the dealership."""
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    description = Column(String)
    dealer_id = Column(Integer, ForeignKey('dealers.id'))


class Dealer(Base):
    """description: Represents an individual or company that sells cars."""
    __tablename__ = 'dealers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String)
    contact_number = Column(String)
    inventory_limit = Column(Integer, nullable=False)


class Customer(Base):
    """description: Represents a customer of the dealership."""
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    unpaid_sales_count = Column(Integer, default=0)


class Sale(Base):
    """description: Represents a sale transaction of a car to a customer."""
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    sale_date = Column(DateTime, default=datetime.utcnow)
    amount = Column(Integer, nullable=False)
    paid = Column(Boolean, default=False)


class ServiceAppointment(Base):
    """description: Holds details of service appointments for cars."""
    __tablename__ = 'service_appointments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    appointment_date = Column(DateTime, nullable=False)
    serviced_by = Column(String)
    notes = Column(String)


class Employee(Base):
    """description: Represents an employee working at the dealership."""
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String)
    email = Column(String)


class Inventory(Base):
    """description: Contains current stock details of cars in dealership inventory."""
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    stock_amount = Column(Integer, nullable=False)
    location = Column(String)
    total_stock = Column(Integer, default=0)


class Warranty(Base):
    """description: Details warranty information of cars sold."""
    __tablename__ = 'warranties'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    coverage_details = Column(String)
    valid_until = Column(DateTime)


class FinanceOption(Base):
    """description: Available finance options for purchasing cars."""
    __tablename__ = 'finance_options'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    interest_rate = Column(Integer, nullable=False)


class Insurance(Base):
    """description: Car insurance details related to dealership offerings."""
    __tablename__ = 'insurances'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    policy_details = Column(String)
    monthly_premium = Column(Integer, nullable=False)


class Repairs(Base):
    """description: Details repair work done on vehicles."""
    __tablename__ = 'repairs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    repair_date = Column(DateTime, nullable=False)
    cost = Column(Integer, nullable=False)
    repair_shop = Column(String)
    description = Column(String)


class ShowroomVisit(Base):
    """description: Tracks visits made by potential customers to the showroom."""
    __tablename__ = 'showroom_visits'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    visit_date = Column(DateTime, nullable=False)
    notes = Column(String)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    car1 = Car(make="Toyota", model="Camry", year=2020, description="Camry SE", dealer_id=1)
    car2 = Car(make="Honda", model="Civic", year=2019, description="Civic Sport", dealer_id=2)
    car3 = Car(make="Ford", model="Mustang", year=2021, description="Mustang GT", dealer_id=3)
    car4 = Car(make="Chevrolet", model="Cruze", year=2018, description="Cruze LT", dealer_id=4)
    dealer1 = Dealer(name="City Auto", address="123 Main St.", contact_number="555-1234", inventory_limit=50)
    dealer2 = Dealer(name="Town Motors", address="789 Elm St.", contact_number="555-6789", inventory_limit=60)
    dealer3 = Dealer(name="Auto Plaza", address="456 Oak St.", contact_number="555-4567", inventory_limit=70)
    dealer4 = Dealer(name="Village Cars", address="321 Pine St.", contact_number="555-9876", inventory_limit=40)
    customer1 = Customer(name="John Doe", email="jdoe@example.com", phone="555-1212", unpaid_sales_count=1)
    customer2 = Customer(name="Jane Smith", email="jsmith@example.com", phone="555-3434", unpaid_sales_count=0)
    customer3 = Customer(name="Alice Brown", email="abrown@example.com", phone="555-5656", unpaid_sales_count=1)
    customer4 = Customer(name="Bob Green", email="bgreen@example.com", phone="555-7878", unpaid_sales_count=2)
    sale1 = Sale(car_id=1, customer_id=1, sale_date=date(2021, 6, 15), amount=25000, paid=False)
    sale2 = Sale(car_id=2, customer_id=2, sale_date=date(2021, 7, 18), amount=22000, paid=True)
    sale3 = Sale(car_id=3, customer_id=3, sale_date=date(2021, 8, 21), amount=35000, paid=False)
    sale4 = Sale(car_id=4, customer_id=4, sale_date=date(2021, 9, 25), amount=20000, paid=False)
    service_appointment1 = ServiceAppointment(car_id=1, appointment_date=date(2021, 10, 1), serviced_by="Mike's Garage", notes="Oil change completed")
    service_appointment2 = ServiceAppointment(car_id=2, appointment_date=date(2021, 10, 2), serviced_by="City Servicing", notes="Brake pads replaced")
    service_appointment3 = ServiceAppointment(car_id=3, appointment_date=date(2021, 10, 3), serviced_by="Auto Shop", notes="Tire rotation done")
    service_appointment4 = ServiceAppointment(car_id=4, appointment_date=date(2021, 10, 4), serviced_by="Mike's Garage", notes="Battery replaced")
    employee1 = Employee(first_name="Michael", last_name="Scott", position="Manager", email="michael@dealership.com")
    employee2 = Employee(first_name="Dwight", last_name="Schrute", position="Salesman", email="dwight@dealership.com")
    employee3 = Employee(first_name="Pam", last_name="Beesly", position="Receptionist", email="pam@dealership.com")
    employee4 = Employee(first_name="Jim", last_name="Halpert", position="Salesman", email="jim@dealership.com")
    inventory1 = Inventory(car_id=1, stock_amount=5, location="Showroom A", total_stock=5)
    inventory2 = Inventory(car_id=2, stock_amount=3, location="Showroom B", total_stock=3)
    inventory3 = Inventory(car_id=3, stock_amount=2, location="Warehouse", total_stock=2)
    inventory4 = Inventory(car_id=4, stock_amount=4, location="Showroom A", total_stock=4)
    warranty1 = Warranty(car_id=1, coverage_details="3 years/36,000 miles", valid_until=date(2024, 6, 15))
    warranty2 = Warranty(car_id=2, coverage_details="5 years/60,000 miles", valid_until=date(2025, 7, 18))
    warranty3 = Warranty(car_id=3, coverage_details="4 years/48,000 miles", valid_until=date(2025, 8, 21))
    warranty4 = Warranty(car_id=4, coverage_details="2 years/24,000 miles", valid_until=date(2023, 9, 25))
    finance_option1 = FinanceOption(name="Standard Plan", description="2.5% interest for 60 months", interest_rate=2.5)
    finance_option2 = FinanceOption(name="Premium Plan", description="1.8% interest for 48 months", interest_rate=1.8)
    finance_option3 = FinanceOption(name="Economic Plan", description="3.0% interest for 72 months", interest_rate=3.0)
    finance_option4 = FinanceOption(name="Short-term Plan", description="1.5% interest for 24 months", interest_rate=1.5)
    insurance1 = Insurance(name="Full Coverage", policy_details="Comprehensive coverage", monthly_premium=120)
    insurance2 = Insurance(name="Basic Coverage", policy_details="Collision only", monthly_premium=80)
    insurance3 = Insurance(name="Liability Only", policy_details="Liability only", monthly_premium=50)
    insurance4 = Insurance(name="Ultimate Coverage", policy_details="Roadside assistance included", monthly_premium=150)
    repair1 = Repairs(car_id=1, repair_date=date(2021, 11, 5), cost=150, repair_shop="Joe's Auto Repair", description="Replaced alternator")
    repair2 = Repairs(car_id=2, repair_date=date(2021, 11, 8), cost=250, repair_shop="City Auto Fix", description="Fixed transmission leak")
    repair3 = Repairs(car_id=3, repair_date=date(2021, 11, 10), cost=300, repair_shop="Auto Repair Co.", description="Paint touch-up")
    repair4 = Repairs(car_id=4, repair_date=date(2021, 11, 12), cost=200, repair_shop="Quick Fix Autos", description="Brakes repair")
    showroom_visit1 = ShowroomVisit(customer_id=1, visit_date=date(2021, 12, 1), notes="Interested in SUVs")
    showroom_visit2 = ShowroomVisit(customer_id=2, visit_date=date(2021, 12, 2), notes="Looking for a compact car")
    showroom_visit3 = ShowroomVisit(customer_id=3, visit_date=date(2021, 12, 3), notes="Considering a sedan")
    showroom_visit4 = ShowroomVisit(customer_id=4, visit_date=date(2021, 12, 4), notes="Checking out electric vehicles")
    
    
    
    session.add_all([car1, car2, car3, car4, dealer1, dealer2, dealer3, dealer4, customer1, customer2, customer3, customer4, sale1, sale2, sale3, sale4, service_appointment1, service_appointment2, service_appointment3, service_appointment4, employee1, employee2, employee3, employee4, inventory1, inventory2, inventory3, inventory4, warranty1, warranty2, warranty3, warranty4, finance_option1, finance_option2, finance_option3, finance_option4, insurance1, insurance2, insurance3, insurance4, repair1, repair2, repair3, repair4, showroom_visit1, showroom_visit2, showroom_visit3, showroom_visit4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
