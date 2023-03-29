import mysql.connector as mysql
import plantsconfig
import sys

#Connection to the plant database with error handling.
#Uses a config file with the .connect() method for security.
try:
    db = mysql.connect(**plantsconfig.config)
except mysql.ProgrammingError as err:
    if err.errno == 1049:
        print("ERROR: Database not found.")
        print("Terminating program.")
        sys.exit(0)
    else:
        print("An unknown error occurred.")
        print("Terminating program.")
        sys.exit(0)


#Create a cursor for accessing database.
db_cursor = db.cursor()


#The query that will be used to generate plants for the planter.
planter_query = "SELECT plant_name, series_and_color FROM annuals WHERE planter_use = %s AND sun = %s ORDER BY RAND() LIMIT 1;"


#Initialize the variable for how much sun the planter will get.
#This makes a difference for which plants are chosen for the planter.
#Only  plants with all the same light requirements will be chosen.
#If a plant is considered a "sun" plant, it wants sunlight after 12pm. 
#A "shade" plant wants the morning sunlight before 12pm.
sun = ''



#Takes the light requirement as a parameter.
#Thrillers are taller plants that act as a centerpiece, fillers are medium height plants, 
#and spillers are low height and often spill over the sides of the planter.
def generate_planter(sun):
    '''#The method that uses the query to generate a planter. '''
    db_cursor.execute(planter_query, ("thriller", sun))
    thriller = db_cursor.fetchall()
    
    db_cursor.execute(planter_query, ("filler", sun))
    filler = db_cursor.fetchall()
    
    db_cursor.execute(planter_query, ("spiller", sun))
    spiller= db_cursor.fetchall()
    
    print(f"Try making a planter with: \n \t{thriller[0][1]} {thriller[0][0]}, \n \t{filler[0][1]} {filler[0][0]}, \n \t{spiller[0][1]} {spiller[0][0]}\n")


print("Welcome to the planter generator!\n")


#A loop to handle user input and the main logic of the running program.
while True:
    sun = input("Will your planter be getting afternoon sun? \nAnswer Y or N to generate a planter, or press Q to quit: ").lower()
    if sun in ('y', 'n'):
        generate_planter(sun)
    elif sun.lower() == 'q':
        sys.exit(0)
    else:
        print("please enter y or n: ")


db.close()