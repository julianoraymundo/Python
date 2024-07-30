#"""
#You will be supplied with two data files in CSV format .
#The first file contains statistics about various dinosaurs.
#The second file contains additional data.
#Given the following formula, 
#speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#Where g = 9.8 m/s^2 (gravitational constant)

#Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
#Do not print any other information.

#$ cat dataset1.csv
#NAME,LEG_LENGTH,DIET
#Hadrosaurus,1.4,herbivore
#Struthiomimus,0.72,omnivore
#Velociraptor,1.8,carnivore
#Triceratops,0.47,herbivore
#Euoplocephalus,2.6,herbivore
#Stegosaurus,1.50,herbivore
#Tyrannosaurus Rex,6.5,carnivore

#$ cat dataset2.csv 
#NAME,STRIDE_LENGTH,STANCE
#Euoplocephalus,1.97,quadrupedal
#Stegosaurus,1.70,quadrupedal
#Tyrannosaurus Rex,4.76,bipedal
#Hadrosaurus,1.3,bipedal
#Deinonychus,1.11,bipedal
#Struthiomimus,1.24,bipedal
#Velociraptor,2.62,bipedal
#"""
import csv
from math import sqrt

# Gravitational constant
g = 9.8

def calculate_speed(stride_length, leg_length):
    return ((stride_length / leg_length) - 1) * sqrt(leg_length * g)

def read_dinosaur_data(file_path):
    data = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row['NAME']] = {
                'leg_length': float(row['LEG_LENGTH']),
                'stride_length': float(row['STRIDE_LENGTH']),
                'stance': row['STANCE']
            }
    return data

def main():
    dataset1 = read_dinosaur_data('D:\\OneDrive - Lock IT\\Juliano Raymundo dos Santos\\4. Scripts\\Python\\dataset1.csv')
    dataset2 = read_dinosaur_data('D:\\OneDrive - Lock IT\\Juliano Raymundo dos Santos\\4. Scripts\\Python\\dataset2.csv')

    bipedal_dinosaurs = []
    for dino_name in dataset1.keys():
        # testar com switch case, validar se o dino é bipede e calcular dentro do switch, salvar em uma lista e ordenar no final 
        if dino_name in dataset1 and dataset2[dino_name]['stance'] == 'bipedal':
            leg_length = dataset1[dino_name]['leg_length']
            stride_length = dataset2[dino_name]['stride_length']
            speed = calculate_speed(stride_length, leg_length)
            bipedal_dinosaurs.append((dino_name, speed))

    bipedal_dinosaurs.sort(key=lambda x: x[1], reverse=True)

    for dino, speed in bipedal_dinosaurs:
        print(dino)

if __name__ == "__main__":
    main()