#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
from ttk import Frame, Button, Style

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

def search():
	mentor = Query()
	d = 0
	while d != 1:

		print ('''
----------------------------------------------------
|What would you like to search by?                  |
|                                                   |
|If you would like to search by FIRST NAME, type 0  |
|                                                   |
|If you would like to search by LAST NAME, type 1   |
|                                                   |
|If you would like to search by AFFILIATION, type 2 |
|                                                   |
|If you would like to search by TOPIC, type 3       |
|                                                   |
|If you would like to search by STUDENT, type 4     |
---------------------------------------------------
''')
		selection = raw_input('\n Please Make Your Selection : ')
		if selection == '0':
			d = 1
			query = 'First_name'

		elif selection == '1':
			d = 1
			query = 'Last_name'

		elif selection == '2':
			d = 1
			query = 'Affiliation'

		elif selection == '3':
			d = 1
			query = 'topic'

		elif selection == '4':
			d = 1
			query = 'student'
		else:
			d = 0
			print "This is an invalid selection, please try again..."
	user_input = raw_input("\nPlease enter search text : ")
	print '''
-----------------------------------------------------------------------------------------------------------------------
|                                                                                                                      |
|                                                                                                                      |
|                                                          RESULTS                                                     |
|                                                                                                                      |
|                                                                                                                      |
-----------------------------------------------------------------------------------------------------------------------
	'''
	for x in db.all():
		try:
			if user_input.lower() in x[query].lower():
				print ( '''
---------------------------------------------
|Mentor name : %s                           
|
|Topic : %s
|
|Affiliation : %s
|
|Phone Number : %s
|
|Student : %s
---------------------------------------------
''' %(x['Name'], x['topic'], x['Affiliation'], x['Phone'], x['student']) )
		except TypeError:
			print 'TypeError'
		except AttributeError:
			print 'AttributeError'
	#print db.search(mentor.query.search('%s' %user_input))
	#info = db.get(mentor.query == '%s' %user_input)
	'''
	try:
		for i in info:
			print ("%s : %s") %(i, info[i])
		hi = raw_input("Press enter to continue: ")
	except TypeError:
		print ("There are no results to match that query...")
	'''
	Selection()

def add():
	a = 0
	while a != 1:
		print ("\nPlease enter the information as prompted")
		print ("\n NOTE: If information not available, press enter to skip... \n")
		print"----------------------------------------------------------------------------"
		prefix = raw_input("\nPrefix: ")
		first_name = raw_input("\nFirst Name: ")
		middle_initial = raw_input("\nMiddle Initial: ")
		last_name = raw_input("\nLast Name: ")
		affiliation = raw_input("\nAffiliation: ")
		phone  = raw_input("\nPhone Number: ")
		topic = raw_input("\nTopic: ")
		student = raw_input("\nStudent: ")
		print ("\n\nHere is what you inputted: \n\n    Scientist: %s %s %s %s \n\n    Affiliation: %s \n\n    Phone Number: %s \n\n    Topic: %s \n\n    Student: %s \n\n") %(prefix, first_name, middle_initial, last_name, affiliation, phone, topic, student)
		selection = raw_input('''
Is this information ok? 

-------------------------------------------------------------------------------
|If you would like to confirm this information and continue, type 0            |
|                                                                              |
|If you would like to input the information again, type 1                      |
|                                                                              |
|If you would like to exit, type 2                                             |
------------------------------------------------------------------------------


Please Make Your Selection : \n
''')
		b = 0
		while b != 1:
			if selection == '0':
				a = 1
				b = 1
				full_name = consolidate_name(prefix,first_name,middle_initial,last_name)
				db.insert({'Name': full_name,'Affiliation': affiliation, 'Phone': phone, 'topic': topic, 'student': student})

			elif selection == '1':
				a = 0
				b = 1
			elif selection == '2':
				a = 1
				b = 1

			else:
				a = 0
				b = 0
				print "This is an invalid selection, please try again..."
	Selection()

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()

    

        
    def initUI(self):

    	def create_search_window():
    		self.destroy
    		window = Toplevel(self)
    		label1 = Label(anchor = CENTER, text = "WELCOME TO THE EHS SCIENCE SCHOLARS MENTOR DATABASE")
        	label1.pack()
        	label2 = Label(anchor = CENTER, text = "DESIGNED BY FEDERICO REYES FOR THE E-TECH CLUB 2015")
        	label2.pack()
        	label3 = Label(anchor = CENTER, text = "THIS DATABASE CAN BE USED TO SEARCH FOR AND ADD MENTORS TO THE DATABASE")
        	label3.pack()
      
        	self.parent.title("Buttons")
        	self.style = Style()
        	self.style.theme_use("default")
        
        	#frame = Frame(self, relief=RAISED, borderwidth=1)
        	#frame.pack(fill=BOTH, expand=True)
       	
        	self.pack(fill=BOTH, expand=True)
        
        	closeButton = Button(self, text="CLOSE", command = self.quit)
        	closeButton.pack(side=RIGHT, padx=5, pady=5,fill=BOTH, expand=1)
        	searchButton = Button(self, text="SEARCH", command = create_search_window)
       		searchButton.pack(side=LEFT,fill=BOTH, expand=1)
        	addButton = Button(self, text="ADD", command = create_add_window)
        	addButton.pack(side=LEFT,fill=BOTH, expand=1)

    	def create_add_window():
    		window = Toplevel(self)



    	label1 = Label(anchor = CENTER, text = "WELCOME TO THE EHS SCIENCE SCHOLARS MENTOR DATABASE")
        label1.pack()
        label2 = Label(anchor = CENTER, text = "DESIGNED BY FEDERICO REYES FOR THE E-TECH CLUB 2015")
        label2.pack()
        label3 = Label(anchor = CENTER, text = "THIS DATABASE CAN BE USED TO SEARCH FOR AND ADD MENTORS TO THE DATABASE")
        label3.pack()
      
        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        
        #frame = Frame(self, relief=RAISED, borderwidth=1)
        #frame.pack(fill=BOTH, expand=True)
       
        self.pack(fill=BOTH, expand=True)
        
        closeButton = Button(self, text="CLOSE", command = self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5,fill=BOTH, expand=1)
        searchButton = Button(self, text="SEARCH", command = create_search_window)
        searchButton.pack(side=LEFT,fill=BOTH, expand=1)
        addButton = Button(self, text="ADD", command = create_add_window)
        addButton.pack(side=LEFT,fill=BOTH, expand=1)
        
              

def main():
  
    root = Tk()
    root.geometry("1400x1000+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  