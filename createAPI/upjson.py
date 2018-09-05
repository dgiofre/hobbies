import os
import json
import time
import numpy as np

xy = dict()
databuf  = dict()
circles = list()

def bufferJsonFile():
    jsonFile = open("static/points-definition.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file
    return data

    ## Working with buffered content
def updateJsonFile(data):  
    ## Save our changes to JSON file
    jsonFile = open("static/points.json", "w+")
    jsonFile.write(json.dumps(data, indent=2))
    jsonFile.close()

def main(): 
 #range in x&y axes
    databuf=bufferJsonFile()
    xy=databuf["range"]
    
    # PARAMETERS
    L, Ly,  h, y0, t = (xy["max_x"]-xy["min_x"]), (xy["max_y"]-xy["min_y"]), 25., 100., time.time()

    ### Fist Sphere
    T=13.
    x =  L*t/T 
    x = x -  L*(int(round(x/L))) + L/2
    y = y0+h*np.sin(2*np.pi*x/y0)
    y = y -  Ly*(int(round(y/Ly))) + Ly/2
    circle={'x' : x , 'y' : y, 'id' : 0 }
    databuf["circles"][0]=circle
    #circles.append(circle)
    ### Second Sphere
    T=14.
    x =  30.*np.cos(2*np.pi*t/T) + 50.
    x = x -  L*(int(round(x/L))) + L/2
    y = 65.*np.sin(2*np.pi*t/T) + 185.
    y = y -  Ly*(int(round(y/Ly))) + Ly/2
    circle={'x' : x , 'y' : y, 'id' : 1 }
    databuf["circles"][1]=circle
    #circles.append(circle)
    ### Third Sphere
    T=11.
    x = L*t/T
    x = x -  L*(int(round(x/L))) + L/2
    y = L*t/T
    y = y -  Ly*(int(round(y/Ly))) + Ly/2
    circle={'x' : x , 'y' : y, 'id' : 2 }
    databuf["circles"][2]=circle
    

    updateJsonFile(databuf)





