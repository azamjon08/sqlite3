import sqlite3

boglanish = sqlite3.connect('mydatabase.db')
int = input("Malumotni kiriting: ")
name = boglanish.cursor()
# BIRINCHISI
name.execute("""
CREATE TABLE IF NOT EXISTS shopping(
    name TEXT,
    last_name TEXT
)            
                
                
""")

name.execute("""
INSERT INTO shopping VALUES   
('Azamjon', 'Ziyobiddinov'),            
('Azamjon', 'Ziyobiddinov'), 
('Azamjon', 'Ziyobiddinov') 
                
""")

name.execute("SELECT * FROM shopping")
# IKKINCHISI
meva = boglanish.cursor()
meva.execute("""
CREATE TABLE IF NOT EXISTS meva(
    name TEXT,
    last_name TEXT
)            
                
                
""")

meva.execute("""
INSERT INTO meva VALUES   
('NOK', '12000'),            
('OLMA', '10000'), 
('SHAFTOLI', '35000') 
                
""")

meva.execute("SELECT * FROM meva")



if int == 'car':
    print(car.fetchall())
elif int == 'name':
    print(name.fetchall())
elif int == 'meva':    
    print(meva.fetchall())
  
else:
    print("Bu malumot mavjut emas! ")       

