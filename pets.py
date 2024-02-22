#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 18:44:53 2023

@author: koushalsmodi
"""
# creating classes 
# self will be as a parameter in all methods
# accessor: get_name, get_birthdate, get_breed, get_color, __str__
# mutator: set_name, set_birthdate, set_breed, set_color
# in mutator 2 parameters: self and data attribute
# str method to get all values all at once when called

class Dogs:
    # initalizing data attributes: name, birthdate, breed, color
    def __init__(self, name, birthdate, breed, color):
        self.__name = name
        self.__birthdate = birthdate
        self.__breed = breed
        self.__color = color
    
    def set_name(self, name):
        self.__name = name
    
    def set_birthdate(self,birthdate):
        self.__birthdate = birthdate
    
    def set_breed(self, breed):
        self.__breed = breed
    
    def set_color(self, color):
        self.__color = color
    
    def get_name(self):
        return self.__name
    
    def get_birthdate(self):
        return self.__birthdate
    
    def get_breed(self):
        return self.__breed
    
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f'Name: {self.get_name()}\tBirthdate: {self.get_birthdate()}\tBreed: {self.get_breed()}\tColor: {self.get_color()}'

class Cats:
    def __init__(self, name, birthdate, breed, color):
        self.__name = name
        self.__birthdate = birthdate
        self.__breed = breed
        self.__color = color
    
    def set_name(self, name):
        self.__name = name
    
    def set_birthdate(self,birthdate):
        self.__birthdate = birthdate
    
    def set_breed(self, breed):
        self.__breed = breed
    
    def set_color(self, color):
        self.__color = color
    
    def get_name(self):
        return self.__name
    
    def get_birthdate(self):
        return self.__birthdate
    
    def get_breed(self):
        return self.__breed
    
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f'Name: {self.get_name()}\tBirthdate: {self.get_birthdate()}\tBreed: {self.get_breed()}\tColor: {self.get_color()}'

class Fish:
    def __init__(self, name, birthdate, breed, color):
        self.__name = name
        self.__birthdate = birthdate
        self.__breed = breed
        self.__color = color
    
    def set_name(self, name):
        self.__name = name
    
    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate
    
    def set_breed(self, breed):
        self.__breed = breed
    
    def set_color(self, color):
        self.__color = color
    
    def get_name(self):
        return self.__name
    
    def get_birthdate(self):
        return self.__birthdate
    
    def get_breed(self):
        return self.__breed
    
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f'Name: {self.get_name()}\tBirthdate: {self.get_birthdate()}\tBreed: {self.get_breed()}\tColor: {self.get_color()}'

class Bird:
    def __init__(self, name, birthdate, breed, color):
        self.__name = name
        self.__birthdate = birthdate
        self.__breed = breed
        self.__color = color
    
    def set_name(self, name):
        self.__name = name
    
    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate
    
    def set_breed(self, breed):
        self.__breed = breed
    
    def set_color(self, color):
        self.__color = color
    
    def get_name(self):
        return self.__name
    
    def get_birthdate(self):
        return self.__birthdate
    
    def get_breed(self):
        return self.__breed
    
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f'Name: {self.get_name()}\tBirthdate: {self.get_birthdate()}\tBreed: {self.get_breed()}\tColor: {self.get_color()}'

class Cow:
    def __init__(self, name, birthdate, breed, color):
        self.__name = name
        self.__birthdate = birthdate
        self.__breed = breed
        self.__color = color
    
    def set_name(self, name):
        self.__name = name
    
    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate
    
    def set_breed(self, breed):
        self.__breed = breed
    
    def set_color(self, color):
        self.__color = color
    
    def get_name(self):
        return self.__name
    
    def get_birthdate(self):
        return self.__birthdate
    
    def get_breed(self):
        return self.__breed
    
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f'Name: {self.get_name()}\tBirthdate: {self.get_birthdate()}\tBreed: {self.get_breed()}\tColor: {self.get_color()}'

class Tortoise:
    def __init__(self, name, birthdate, breed, color):
        self.__name = name
        self.__birthdate = birthdate
        self.__breed = breed
        self.__color = color
    
    def set_name(self, name):
        self.__name = name
    
    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate
    
    def set_breed(self, breed):
        self.__breed = breed
    
    def set_color(self, color):
        self.__color = color
    
    def get_name(self):
        return self.__name
    
    def get_birthdate(self):
        return self.__birthdate
    
    def get_breed(self):
        return self.__breed
    
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f'Name: {self.get_name()}\tBirthdate: {self.get_birthdate()}\tBreed: {self.get_breed()}\tColor: {self.get_color()}'





