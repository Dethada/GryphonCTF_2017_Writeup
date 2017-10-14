#!/usr/bin/python
	
class Language():
    def __init__(self, English, Alphabetrium, Gazorpazorpian, 
                Numberconian, Martian, Unition, Blitzion, Chipzion, Morphian):
        self.English=English
        self.Alphabetrium=Alphabetrium
        self.Gazorpazorpian=Gazorpazorpian
        self.Numberconian=Numberconian
        self.Martian=Martian
        self.Unition=Unition
        self.Blitzion=Blitzion
        self.Chipzion=Chipzion
        self.Morphian=Morphian
    
    def translate(self, lang):
        if lang == "English":
            return self.English
        elif lang == "Alphabetrium":
            return self.Alphabetrium
        elif lang == "Gazorpazorpian":
            return self.Gazorpazorpian
        elif lang == "Numberconian":
            return self.Numberconian
        elif lang == "Martian":
            return self.Martian
        elif lang == "Unition":
            return self.Unition
        elif lang == "Blitzion":
            return self.Blitzion
        elif lang == "Chipzion":
            return self.Chipzion
        else:
            return self.Morphian
