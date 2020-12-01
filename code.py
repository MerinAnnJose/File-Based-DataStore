'''
Freshworks-Backend Assignment
~A file-based key value data store that supports basic CRUD(Create, Read, Update, Delete) operations. 

Python version: 3.7.6
@author: Merin Ann Jose
@date: 01.12.2020
'''

def create():
	key=input("\nEnter key id: ")			
	if len(key)>32:			#checking key length 
		print("Key length exceeds limit!")
		return

	if my_file.exists(): #if file exits, add to same datastore file
		
		import os
		if os.stat(path).st_size > 1e+9:	#Ensuring file size below 1GB
			print("Data-Store File size exceeded 1GB!")
			return
		
		f=open(path,"r")
		d = json.load(f)
		if key in d:
			print("Already exixts!")	# error if entered key already exixts
			return
	
		'''get values inside nested dictionary for given key.
		Enter data as (example) Enter attribute 1 and value: Name MerinJose
		(i.e.) attribute <space> value  (Also, ensure no space inside value)'''
		n=int(input("Enter no of values: "))	
		temp={}	
		for i in range(1,n+1):																
			s=input("Enter attribute "+ str(i) +" and value: ").split(' ')
			temp[s[0]]=s[1]
		d[key]=temp
		json_object = json.dumps(d)		#converting into JSON object
		if sys.getsizeof(json_object)>16000:
			print("JSON Object value-size exceeded!")	#Ensuring JSON object size below 16KB
			return
		with open(path, "w") as outfile:
			outfile.write(json_object)

		ff=open(time_path,"r")
		dd = json.load(ff)
		t=input("Include TimeToLive? (y/n): ")
		if t=='y':
			sc=float(input("Enter TimeToLive in hours: "))
			seconds=sc*3600		#converting to seconds
		else:
			seconds=sys.maxsize*3600	#if TimeToLive not specified, take maxsize
		entered_time=time.time()
		dd[key]=[entered_time,seconds]		#storing the entered_time and TimeToLive(in seconds) (an array)
		json_time_object = json.dumps(dd)	#as value for given key
		with open(time_path, "w") as outfile:
			outfile.write(json_time_object)
		print("done")
		outfile.close()
	
	#file doesn't exist. (i.e.)Creating for the first time. Check same constraints
	else:
		data=dict()
		ttl=dict()
		n=int(input("Enter no of values: "))
		temp={}
		for i in range(1,n+1):
			s=input("Enter attribute "+ str(i) +" and value: ").split(' ')
			temp[s[0]]=s[1]
		data[key]=temp
		json_object = json.dumps(data)
		if sys.getsizeof(json_object)>16000:
			print("JSON Object value size exceeded!")
			return
		with open(path, "a+") as outfile:
			outfile.write(json_object)

		t=input("Include TimeToLive? (y/n): ")
		if t=='y':
			sc=float(input("Enter TimeToLive in hours: "))
			seconds=sc*3600
		else:
			seconds=sys.maxsize*3600
		entered_time=time.time()
		ttl[key]=[entered_time,seconds]
		json_time_object = json.dumps(ttl)
		with open(time_path, "a+") as outfile:
			outfile.write(json_time_object)

		print("done")
		outfile.close()



def read():
	if my_file.exists():	#read only if file exists
		f=open(path,"r")	
		data = json.load(f)		#load json data
		key=input("\nEnter id to retrieve: ")
		if key in data:
			t=open(time_path,"r")
			td=json.load(t)
			curr_time=time.time()
			if curr_time-td[key][0] > td[key][1]:	#if current_time - entered_time exceeds the time specified,then error)
				print("Cannot read! Exceeded TimeToLive")
				return
			print(data[key]) #Else print data
			print("done")
		else:
			print("Does not exist!")
		f.close()
	else:
		print("Empty data-store. Please enter values to read!")


def update():
	if my_file.exists():	#check if file exists
		f=open(path,"r")	
		data = json.load(f)		#load json data
		key=input("\nEnter id to update: ")
		if key in data:
			t=open(time_path,"r")
			td=json.load(t)
			curr_time=time.time()
			if curr_time-td[key][0] > td[key][1]:	#if current_time - entered_time exceeds the time specified,then error)
				print("Cannot read! Exceeded TimeToLive")
				return

			print("--Enter new data for key--")
			n=int(input("Enter no of values: "))	
			temp={}	
			for i in range(1,n+1):																
				s=input("Enter attribute "+ str(i) +" and value: ").split(' ')
				temp[s[0]]=s[1]
			
			data[key]=temp 			#update the key value
			json_object = json.dumps(data)		#converting into JSON object
			if sys.getsizeof(json_object)>16000:
				print("JSON Object value-size exceeded!")	#Ensuring JSON object size below 16KB
				return
			with open(path, "w") as outfile:
				outfile.write(json_object)		
			print("done")
			f.close()
	else:
		print("Empty data-store. Please enter values!")



def delete():
	if my_file.exists():	#check if file exists
		ff=open(path,"r")
		data = json.load(ff)
		key=input("\nEnter id to delete: ")
		if key in data:
			t=open(time_path,"r")
			td=json.load(t)
			curr_time=time.time()		
			if curr_time-td[key][0] > td[key][1]:	#if current time-entered time exceeds the time specified, then error)
				print("Cannot delete! Exceeded TimeToLive")
				return
			data.pop(key)
			json_object = json.dumps(data)
			with open(path, "w") as outfile:
				outfile.write(json_object)
			print("done")
		else:
			print("Does not exist!")
		ff.close()
	else:
		print("Empty data-store. Please enter values to delete!")


import json
import sys
import time
print("\n----DATA-STORE MANAGEMENT SYSTEM----\n")
choice=input("Specify data-store 'folder' path/Create new path?: (y/n) (note: default path: D:\\) : ")
if choice=='y':
	path=input("Enter path: ")
else:
	path="D:"

#appending filenames to paths 
time_path=path+"\\TimeToLive.txt"	#file to store TimeToLive
path+="\\datastore.txt"				#data-store file to store actual data
print("Your datastore path: "+path)

from pathlib import Path
my_file = Path(path)

while 1:
	op=int(input("\n\n\t---Operations:---\n1.Create\n2.Read\n3.Update\n4.Delete\n5.Exit\n\tEnter choice: "))
	if op==1:
		create()
	elif op==2:
		read()
	elif op==3:
		update()
	elif op==4:
		delete()
	else:
		exit()
		break

