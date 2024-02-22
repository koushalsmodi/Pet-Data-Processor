#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:46:14 2023

@author: koushalsmodi
"""

import pets # importing pets for classes

def fReadData():
    # creating empty lists and opening csv file
    lstPets = []
    with open('pets.csv', 'r') as file:
        for line in file:
            # iterating and using indexing to store data as required: type, name, birthdate, breed and color
            pet_data = line.strip().split(',')
            pet_type = pet_data[0].strip()
            pet_name = pet_data[1].strip()
            pet_birthdate = pet_data[2].strip()
            pet_breed = pet_data[3].strip()
            pet_color = pet_data[4].strip()
            
            # depending on the pet type, save it from classes imported as pet
            if pet_type == 'Dog':
                pet = pets.Dogs(pet_name, pet_birthdate, pet_breed, pet_color)
            elif pet_type == 'Cat':
                pet = pets.Cats(pet_name, pet_birthdate, pet_breed, pet_color)
            elif pet_type == 'Fish':
                pet = pets.Fish(pet_name, pet_birthdate, pet_breed, pet_color)
            elif pet_type == 'Bird':
                pet = pets.Bird(pet_name, pet_birthdate, pet_breed, pet_color)
            elif pet_type == 'Cow':
                pet = pets.Cow(pet_name, pet_birthdate, pet_breed, pet_color)
            elif pet_type == 'Tortoise':
                pet = pets.Tortoise(pet_name, pet_birthdate, pet_breed, pet_color)
            else:
                print(f'Unknown: {pet_type}')
                continue # learnt to use continue to prevent unknown type being appended to the lstPets

            lstPets.append(pet) 

    return lstPets # returning whatever is appended

def main():
    lstPets = fReadData() # calling function and storing in list
    fShowMenu(lstPets) # passing list as an argument to the menu function

def fShowMenu(lstPets):
    # constants, to prevent phantom values
    
    NAMES = 1
    SEARCH = 2
    LIST = 3
    CERTAIN = 4
    SORT = 5
    EXIT = 6
    
    #print details as required in output
    print('----------Pet Menu Finder----------')
    print('1. Show Pet Names')
    print('2. Search for Pet')
    print('3. Show List')
    print('4. Shows Pets of Certain Type')
    print('5. Sort all of the pets Alphabetically')
    print('6. Exit the program')
    print('-' * 25)
    print()
    
    choice = int(input('Please enter one of the above options: ')) # getting choice as integer
    
    # depending on choice number entered call the function with list as argument to be entered
    if choice == NAMES:
        show_names(lstPets)
    
    elif choice == SEARCH:
        search(lstPets)
    
    elif choice == LIST:
        show(lstPets)
    
    elif choice == CERTAIN:
        certain(lstPets)
    
    elif choice == SORT:
        sort_names(lstPets)
    
    elif choice == EXIT:
        exit()
    else:
        print('Invalid choice')
        
    while choice < NAMES or choice > EXIT: # if out of range
        choice = int(input('Please enter one of the above options: '))

def show_names(lstPets):
    print('---------Show Pet Names---------')
    for pet in lstPets:
        print(pet.get_name()) # for each pet object in loop, call get name

def search(lstPets):
    print('-------Search Pet---------')
    name = input('What is the name of the pet you want to find?: ')
    
    findPets = [] # empty list
    
    for pet in lstPets:
        if pet.get_name() == name: # validating if name is present in the list
            findPets.append(pet) # add everything about that pet into the list
            
    if findPets:
        for pet in findPets: # loop over it and get all details
            print(f'Name: {pet.get_name()}\tBirthdate: {pet.get_birthdate()}\tBreed: {pet.get_breed()}\tColor: {pet.get_color()}')
            print('Index: ', lstPets.index(pet)) # getting index
    
    else:
        print(f'Sorry, {name} is not in the list')  
    

def show(lstPets):
    print('---------Show Pets---------')
    for pet in lstPets:
        print(pet.__str__()) # using str function to get details of all pets

def certain(lstPets):
    print('----- Show Pet Type -------')
    # getting integer value as input
    kind = int(input('What kind of pet would you like to find? Please enter a number between 1-6. 1 = Dog, 2 = Cat, 3 = Fish, 4 = Bird, 5 = Cow, 6 = Tortoise: ' ))
    # validating 
    if kind == 1:
        pet_type = 'Dog'
    elif kind == 2:
        pet_type = 'Cat'
    elif kind == 3:
        pet_type = 'Fish'
    elif kind == 4:
        pet_type = 'Bird'
    elif kind == 5:
        pet_type = 'Cow'
    elif kind == 6:
        pet_type = 'Tortoise'
    else:
        print('Invalid choice')
        return

    found_pets = [] # empty list
    for pet in lstPets:
        # checking whether pet object is an instance of the class and whether their type is equal to that kind
        if isinstance(pet, pets.Dogs) and pet_type == 'Dog':
            found_pets.append(pet)
        elif isinstance(pet, pets.Cats) and pet_type == 'Cat':
            found_pets.append(pet)
        elif isinstance(pet, pets.Fish) and pet_type == 'Fish':
            found_pets.append(pet)
        elif isinstance(pet, pets.Bird) and pet_type == 'Bird':
            found_pets.append(pet)
        elif isinstance(pet, pets.Cow) and pet_type == 'Cow':
            found_pets.append(pet)
        elif isinstance(pet, pets.Tortoise) and pet_type == 'Tortoise':
            found_pets.append(pet) # appending in empty list
    
    # validating
    if found_pets:
        print(f'--- {pet_type}s ---')
        for pet in found_pets:
            print(pet.__str__()) # get details using str that is stored in classes
    else:
        print(f'Sorry, {pet_type}s is not in the list.')


def sort_names(lstPets):
    print('---Show Sorted Pet Names-------')
    pets_sorted = sorted(lstPets, key=lambda pet: pet.get_name()) # using sorted function as was mentioned in the docs
    for pet in pets_sorted:
        print(pet.get_name()) # getting name as stored in classes
main()        
        
        
