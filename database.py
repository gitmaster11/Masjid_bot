from sqlite3 import connect
import sqlite3
import datetime 



def table_user():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    Create Table If Not Exists users (
    id Integer Primary Key Unique,
    telegram_id Integer,
    first_name Varchar(150)
    )   
    """)
    conn.commit()
table_user()

def insert_table_user(telegram_id,first_name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into users (telegram_id,first_name)
    Values({telegram_id},"{first_name}")
    """)
    conn.commit()


def get_user_id(telegram_id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Select * from users
    where telegram_id = {telegram_id}
    """)
    data = cursor.fetchone()
    if data:
        return True
    else:
        return False



def table_namaztime_uzbekistan():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    Create Table If Not Exists image1 (
    id Integer Primary Key Unique,
    sana Varchar(150)
    )   
    """)
    conn.commit()

table_namaztime_uzbekistan()

def table_namaztime_poshshopirim():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    Create Table If Not Exists image2 (
    id Integer Primary Key Unique,
    sana Varchar(150)
    )  
    """)
    conn.commit()

table_namaztime_poshshopirim()



def select_namaztime_uzb():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    select * from image1
    """)
    data = cursor.fetchone()
    return data



def select_namaztime_posh():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    select * from image2
    """)
    data = cursor.fetchone()
    return data

def delete_uzb(num):
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    Delete  from image1
    where id = {num}
    """)
    conn.commit()


def delete_posh(num):
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    Delete  from image2
    where id = {num}
    """)
    conn.commit()

    


def add_image_time_posh(sana):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into image2 (sana)
    values ("{sana}")
    """)
    conn.commit()
    
def add_image_time_uzb(sana):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into image1 (sana)
    values ("{sana}")
    """)
    conn.commit()




def table_juma_maruza():
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    Create Table If Not Exists juma_maruza (
    id Integer Primary Key Unique,
    name Varchar(150)
    )   
    """)
    conn.commit()

table_juma_maruza()


def get_juma_maruza(id):
    conn  = sqlite3.connect("main.db")
    cursor  = conn.cursor()
    cursor.execute(f"""
    Select * from juma_maruza 
    where id = "{id}"
    
    """)
    data = cursor.fetchone()
    return data
    

def delete_juma_maruza(id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Delete from juma_maruza
    Where id ={id}
    """)
    conn.commit()


def add_juma_maruza_name(name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    Insert Into juma_maruza (name)
    values ("{name}")
    """)
    conn.commit()



def count_users():
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    cursor.execute(f"""
    select * from users
    """)
    data = cursor.fetchall()
    return data

