import random
a=[[0,0,0],
   [0,0,0],
   [0,0,0]]

m=0
n=0
def board():
	for row in a:
		print(row)


def inu(x,y):
	global m
	global n
	if(x==1):
		m=n=0
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y
	elif(x==2):
		m=0
		n=1
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y
	elif(x==3):
		m=0
		n=2
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y
	elif(x==4):
		m=1
		n=0
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y
	elif(x==5):
		m=1
		n=1
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y
	elif(x==6):
		m=1
		n=2
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y
	elif(x==7):
		m=2
		n=0
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y
	elif(x==8):
		m=2
		n=1
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y
	else:
		m=2
		n=2
		if(a[m][n]==1 or a[m][n]==2):
			print("Invalid Place!!!!")
		else:
			a[m][n]=y


def toggle(a):
	if(a==1):
		return 2
	else:
		return 1

def logic():
	print("Welcome!!!!!!\n")
	board()
	t=2
	x=0
	count=0
	Game_over=False
	while (Game_over!=True):
		t=toggle(t)
		if count==5:
			print "\nGame Draw!!!"
			Game_over=True
		elif(t==1):
			x=input("\nIt's Your turn:\nPlease Enter place do you want play:\n")
			if x==0:
				Game_over=True
			elif(x>9 or x<1):
				x=input("Please Enter Valid Place!!!")
			else:
				inu(x,t)
				board()
				w=win()
				if w==1:
					print "\nCongrates You Are Winner!!!!"
					Game_over=True
				count+=1
		else:
			AI(count,t)
			board()
			w=win()
			if w==2:
				print "\nAI Is winner!!!!!"
				Game_over=True

def AI(count,t):
	print("\nAI Thinkng.....\n")
	if(count==1):
		if(m==0 and n==0 or m==0 and n==2 or m==2 and n==0 or m==2 and n==2):
			inu(5,t)
		elif(m==0 and n==1 or m==1 and n==0):
			inu(random.choice([1,3]),t)
		elif(m==1 and n==2 or m==2 and n==1):
			inu(random.choice([9,7]),t)
		elif(m==1 and n==1):
			inu(random.choice([1,3,7,9]),t)
	if(count==2):
		if(a[0][0]==2 and a[0][1]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[0][0]==2 and a[0][1]==0 and a[0][2]==2):
			inu(2,t)
		elif(a[0][0]==0 and a[0][1]==2 and a[0][2]==2):
			inu(1,t)
		elif(a[0][0]==2 and a[1][0]==2 and a[2][0]==0):
			inu(7,t)
		elif(a[0][0]==2 and a[1][0]==0 and a[2][0]==2):
			inu(4,t)
		elif(a[0][0]==0 and a[1][0]==2 and a[2][0]==2):
			inu(1,t)
		elif(a[0][0]==2 and a[1][1]==2 and a[2][2]==0):
			inu(9,t)
		elif(a[0][0]==2 and a[1][1]==0 and a[2][2]==2):
			inu(5,t)
		elif(a[0][0]==0 and a[1][1]==2 and a[2][2]==2):
			inu(1,t)
		elif(a[2][2]==2 and a[1][2]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[2][2]==2 and a[1][2]==0 and a[0][2]==2):
			inu(6,t)
		elif(a[2][2]==0 and a[1][2]==2 and a[0][2]==2):
			inu(9,t)
		elif(a[2][2]==2 and a[2][1]==2 and a[2][0]==0):
			inu(7,t)
		elif(a[2][2]==2 and a[2][1]==0 and a[2][0]==2):
			inu(8,t)
		elif(a[2][2]==0 and a[2][1]==2 and a[2][0]==2):
			inu(9,t)
		elif(a[2][2]==2 and a[1][1]==2 and a[0][0]==0):
			inu(1,t)
		elif(a[2][2]==2 and a[1][1]==0 and a[0][0]==2):
			inu(5,t)
		elif(a[2][2]==0 and a[1][1]==2 and a[0][0]==2):
			inu(1,t)
		elif(a[2][0]==2 and a[1][1]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[2][0]==2 and a[1][1]==0 and a[0][2]==2):
			inu(5,t)
		elif(a[2][0]==0 and a[1][1]==2 and a[0][2]==2):
			inu(7,t)
		elif(a[0][1]==2 and a[1][1]==2 and a[2][1]==0):
			inu(8,t)
		elif(a[0][1]==2 and a[1][1]==0 and a[2][1]==2):
			inu(5,t)
		elif(a[0][1]==0 and a[1][1]==2 and a[2][1]==2):
			inu(2,t)
		elif(a[1][0]==2 and a[1][1]==2 and a[1][2]==0):
			inu(6,t)
		elif(a[1][0]==2 and a[1][1]==0 and a[1][2]==2):
			inu(5,t)
		elif(a[0][0]==1 and a[0][1]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[0][0]==1 and a[0][1]==0 and a[0][2]==1):
			inu(2,t)
		elif(a[0][0]==0 and a[0][1]==1 and a[0][2]==1):
			inu(1,t)
		elif(a[0][0]==1 and a[1][0]==1 and a[2][0]==0):
			inu(7,t)
		elif(a[0][0]==1 and a[1][0]==0 and a[2][0]==1):
			inu(4,t)
		elif(a[0][0]==0 and a[1][0]==1 and a[2][0]==1):
			inu(1,t)
		elif(a[0][0]==1 and a[1][1]==1 and a[2][2]==0):
			inu(9,t)
		elif(a[0][0]==1 and a[1][1]==0 and a[2][2]==1):
			inu(5,t)
		elif(a[0][0]==0 and a[1][1]==1 and a[2][2]==1):
			inu(1,t)
		elif(a[2][2]==1 and a[1][2]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[2][2]==1 and a[1][2]==0 and a[0][2]==1):
			inu(6,t)
		elif(a[2][2]==0 and a[1][2]==1 and a[0][2]==1):
			inu(9,t)
		elif(a[2][2]==1 and a[2][1]==1 and a[2][0]==0):
			inu(7,t)
		elif(a[2][2]==1 and a[2][1]==0 and a[2][0]==1):
			inu(8,t)
		elif(a[2][2]==0 and a[2][1]==1 and a[2][0]==1):
			inu(9,t)
		elif(a[2][2]==1 and a[1][1]==1 and a[0][0]==0):
			inu(1,t)
		elif(a[2][2]==1 and a[1][1]==0 and a[0][0]==1):
			inu(5,t)
		elif(a[2][2]==0 and a[1][1]==1 and a[0][0]==1):
			inu(1,t)
		elif(a[2][0]==1 and a[1][1]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[2][0]==1 and a[1][1]==0 and a[0][2]==1):
			inu(5,t)
		elif(a[2][0]==0 and a[1][1]==1 and a[0][2]==1):
			inu(7,t)
		elif(a[0][1]==1 and a[1][1]==1 and a[2][1]==0):
			inu(8,t)
		elif(a[0][1]==1 and a[1][1]==0 and a[2][1]==1):
			inu(5,t)
		elif(a[0][1]==0 and a[1][1]==1 and a[2][1]==1):
			inu(2,t)
		elif(a[1][0]==1 and a[1][1]==1 and a[1][2]==0):
			inu(6,t)
		elif(a[1][0]==1 and a[1][1]==0 and a[1][2]==1):
			inu(5,t)
		elif(a[1][0]==0 and a[1][1]==1 and a[1][2]==1):
			inu(4,t)
		elif(a[0][0]==2 and a[0][1]==1 and a[1][0]==1):
			inu(5,t)
		elif(a[0][2]==2 and a[0][1]==1 and a[1][2]==1):
			inu(5,t)
		elif(a[2][2]==2 and a[1][2]==1 and a[2][1]==1):
			inu(5,t)
		elif(a[2][0]==2 and a[2][1]==1 and a[1][0]==1):
			inu(5,t)
		else:
			for (q,i) in enumerate(a):
				for (p,j) in enumerate(i):
					if j==0:
						a[q][p]=2
						break
				else:
					continue
				break
		
	if(count==3):
		if(a[0][0]==2 and a[0][1]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[0][0]==2 and a[0][1]==0 and a[0][2]==2):
			inu(2,t)
		elif(a[0][0]==0 and a[0][1]==2 and a[0][2]==2):
			inu(1,t)
		elif(a[0][0]==2 and a[1][0]==2 and a[2][0]==0):
			inu(7,t)
		elif(a[0][0]==2 and a[1][0]==0 and a[2][0]==2):
			inu(4,t)
		elif(a[0][0]==0 and a[1][0]==2 and a[2][0]==2):
			inu(1,t)
		elif(a[0][0]==2 and a[1][1]==2 and a[2][2]==0):
			inu(9,t)
		elif(a[0][0]==2 and a[1][1]==0 and a[2][2]==2):
			inu(5,t)
		elif(a[0][0]==0 and a[1][1]==2 and a[2][2]==2):
			inu(1,t)
		elif(a[2][2]==2 and a[1][2]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[2][2]==2 and a[1][2]==0 and a[0][2]==2):
			inu(6,t)
		elif(a[2][2]==0 and a[1][2]==2 and a[0][2]==2):
			inu(9,t)
		elif(a[2][2]==2 and a[2][1]==2 and a[2][0]==0):
			inu(7,t)
		elif(a[2][2]==2 and a[2][1]==0 and a[2][0]==2):
			inu(8,t)
		elif(a[2][2]==0 and a[2][1]==2 and a[2][0]==2):
			inu(9,t)
		elif(a[2][2]==2 and a[1][1]==2 and a[0][0]==0):
			inu(1,t)
		elif(a[2][2]==2 and a[1][1]==0 and a[0][0]==2):
			inu(5,t)
		elif(a[2][2]==0 and a[1][1]==2 and a[0][0]==2):
			inu(1,t)
		elif(a[2][0]==2 and a[1][1]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[2][0]==2 and a[1][1]==0 and a[0][2]==2):
			inu(5,t)
		elif(a[2][0]==0 and a[1][1]==2 and a[0][2]==2):
			inu(7,t)
		elif(a[0][1]==2 and a[1][1]==2 and a[2][1]==0):
			inu(8,t)
		elif(a[0][1]==2 and a[1][1]==0 and a[2][1]==2):
			inu(5,t)
		elif(a[0][1]==0 and a[1][1]==2 and a[2][1]==2):
			inu(2,t)
		elif(a[1][0]==2 and a[1][1]==2 and a[1][2]==0):
			inu(6,t)
		elif(a[1][0]==2 and a[1][1]==0 and a[1][2]==2):
			inu(5,t)
		elif(a[1][0]==0 and a[1][1]==2 and a[1][2]==2):
			inu(4,t)
		elif(a[0][0]==1 and a[0][1]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[0][0]==1 and a[0][1]==0 and a[0][2]==1):
			inu(2,t)
		elif(a[0][0]==0 and a[0][1]==1 and a[0][2]==1):
			inu(1,t)
		elif(a[0][0]==1 and a[1][0]==1 and a[2][0]==0):
			inu(7,t)
		elif(a[0][0]==1 and a[1][0]==0 and a[2][0]==1):
			inu(4,t)
		elif(a[0][0]==0 and a[1][0]==1 and a[2][0]==1):
			inu(1,t)
		elif(a[0][0]==1 and a[1][1]==1 and a[2][2]==0):
			inu(9,t)
		elif(a[0][0]==1 and a[1][1]==0 and a[2][2]==1):
			inu(5,t)
		elif(a[0][0]==0 and a[1][1]==1 and a[2][2]==1):
			inu(1,t)
		elif(a[2][2]==1 and a[1][2]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[2][2]==1 and a[1][2]==0 and a[0][2]==1):
			inu(6,t)
		elif(a[2][2]==0 and a[1][2]==1 and a[0][2]==1):
			inu(9,t)
		elif(a[2][2]==1 and a[2][1]==1 and a[2][0]==0):
			inu(7,t)
		elif(a[2][2]==1 and a[2][1]==0 and a[2][0]==1):
			inu(8,t)
		elif(a[2][2]==0 and a[2][1]==1 and a[2][0]==1):
			inu(9,t)
		elif(a[2][2]==1 and a[1][1]==1 and a[0][0]==0):
			inu(1,t)
		elif(a[2][2]==1 and a[1][1]==0 and a[0][0]==1):
			inu(5,t)
		elif(a[2][2]==0 and a[1][1]==1 and a[0][0]==1):
			inu(1,t)
		elif(a[2][0]==1 and a[1][1]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[2][0]==1 and a[1][1]==0 and a[0][2]==1):
			inu(5,t)
		elif(a[2][0]==0 and a[1][1]==1 and a[0][2]==1):
			inu(7,t)
		elif(a[0][1]==1 and a[1][1]==1 and a[2][1]==0):
			inu(8,t)
		elif(a[0][1]==1 and a[1][1]==0 and a[2][1]==1):
			inu(5,t)
		elif(a[0][1]==0 and a[1][1]==1 and a[2][1]==1):
			inu(2,t)
		elif(a[1][0]==1 and a[1][1]==1 and a[1][2]==0):
			inu(6,t)
		elif(a[1][0]==1 and a[1][1]==0 and a[1][2]==1):
			inu(5,t)
		elif(a[1][0]==0 and a[1][1]==1 and a[1][2]==1):
			inu(4,t)
		else:
			for (q,i) in enumerate(a):
				for (p,j) in enumerate(i):
					if j==0:
						a[q][p]=2
						break
				else:
					continue
				break
		
	if count==4:
		if(a[0][0]==2 and a[0][1]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[0][0]==2 and a[0][1]==0 and a[0][2]==2):
			inu(2,t)
		elif(a[0][0]==0 and a[0][1]==2 and a[0][2]==2):
			inu(1,t)
		elif(a[0][0]==2 and a[1][0]==2 and a[2][0]==0):
			inu(7,t)
		elif(a[0][0]==2 and a[1][0]==0 and a[2][0]==2):
			inu(4,t)
		elif(a[0][0]==0 and a[1][0]==2 and a[2][0]==2):
			inu(1,t)
		elif(a[0][0]==2 and a[1][1]==2 and a[2][2]==0):
			inu(9,t)
		elif(a[0][0]==2 and a[1][1]==0 and a[2][2]==2):
			inu(5,t)
		elif(a[0][0]==0 and a[1][1]==2 and a[2][2]==2):
			inu(1,t)
		elif(a[2][2]==2 and a[1][2]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[2][2]==2 and a[1][2]==0 and a[0][2]==2):
			inu(6,t)
		elif(a[2][2]==0 and a[1][2]==2 and a[0][2]==2):
			inu(9,t)
		elif(a[2][2]==2 and a[2][1]==2 and a[2][0]==0):
			inu(7,t)
		elif(a[2][2]==2 and a[2][1]==0 and a[2][0]==2):
			inu(8,t)
		elif(a[2][2]==0 and a[2][1]==2 and a[2][0]==2):
			inu(9,t)
		elif(a[2][2]==2 and a[1][1]==2 and a[0][0]==0):
			inu(1,t)
		elif(a[2][2]==2 and a[1][1]==0 and a[0][0]==2):
			inu(5,t)
		elif(a[2][2]==0 and a[1][1]==2 and a[0][0]==2):
			inu(1,t)
		elif(a[2][0]==2 and a[1][1]==2 and a[0][2]==0):
			inu(3,t)
		elif(a[2][0]==2 and a[1][1]==0 and a[0][2]==2):
			inu(5,t)
		elif(a[2][0]==0 and a[1][1]==2 and a[0][2]==2):
			inu(7,t)
		elif(a[0][1]==2 and a[1][1]==2 and a[2][1]==0):
			inu(8,t)
		elif(a[0][1]==2 and a[1][1]==0 and a[2][1]==2):
			inu(5,t)
		elif(a[0][1]==0 and a[1][1]==2 and a[2][1]==2):
			inu(2,t)
		elif(a[1][0]==2 and a[1][1]==2 and a[1][2]==0):
			inu(6,t)
		elif(a[1][0]==2 and a[1][1]==0 and a[1][2]==2):
			inu(5,t)
		elif(a[1][0]==0 and a[1][1]==2 and a[1][2]==2):
			inu(4,t)
		elif(a[0][0]==1 and a[0][1]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[0][0]==1 and a[0][1]==0 and a[0][2]==1):
			inu(2,t)
		elif(a[0][0]==0 and a[0][1]==1 and a[0][2]==1):
			inu(1,t)
		elif(a[0][0]==1 and a[1][0]==1 and a[2][0]==0):
			inu(7,t)
		elif(a[0][0]==1 and a[1][0]==0 and a[2][0]==1):
			inu(4,t)
		elif(a[0][0]==0 and a[1][0]==1 and a[2][0]==1):
			inu(1,t)
		elif(a[0][0]==1 and a[1][1]==1 and a[2][2]==0):
			inu(9,t)
		elif(a[0][0]==1 and a[1][1]==0 and a[2][2]==1):
			inu(5,t)
		elif(a[0][0]==0 and a[1][1]==1 and a[2][2]==1):
			inu(1,t)
		elif(a[2][2]==1 and a[1][2]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[2][2]==1 and a[1][2]==0 and a[0][2]==1):
			inu(6,t)
		elif(a[2][2]==0 and a[1][2]==1 and a[0][2]==1):
			inu(9,t)
		elif(a[2][2]==1 and a[2][1]==1 and a[2][0]==0):
			inu(7,t)
		elif(a[2][2]==1 and a[2][1]==0 and a[2][0]==1):
			inu(8,t)
		elif(a[2][2]==0 and a[2][1]==1 and a[2][0]==1):
			inu(9,t)
		elif(a[2][2]==1 and a[1][1]==1 and a[0][0]==0):
			inu(1,t)
		elif(a[2][2]==1 and a[1][1]==0 and a[0][0]==1):
			inu(5,t)
		elif(a[2][2]==0 and a[1][1]==1 and a[0][0]==1):
			inu(1,t)
		elif(a[2][0]==1 and a[1][1]==1 and a[0][2]==0):
			inu(3,t)
		elif(a[2][0]==1 and a[1][1]==0 and a[0][2]==1):
			inu(5,t)
		elif(a[2][0]==0 and a[1][1]==1 and a[0][2]==1):
			inu(7,t)
		elif(a[0][1]==1 and a[1][1]==1 and a[2][1]==0):
			inu(8,t)
		elif(a[0][1]==1 and a[1][1]==0 and a[2][1]==1):
			inu(5,t)
		elif(a[0][1]==0 and a[1][1]==1 and a[2][1]==1):
			inu(2,t)
		elif(a[1][0]==1 and a[1][1]==1 and a[1][2]==0):
			inu(6,t)
		elif(a[1][0]==1 and a[1][1]==0 and a[1][2]==1):
			inu(5,t)
		elif(a[1][0]==0 and a[1][1]==1 and a[1][2]==1):
			inu(4,t)
		else:
			for (q,i) in enumerate(a):
				for (p,j) in enumerate(i):
					if j==0:
						a[q][p]=2
						break
				else:
					continue
				break

def win():
		if(a[0][0]==2 and a[0][1]==2 and a[0][2]==2):
			return 2
		
		if(a[0][0]==2 and a[1][0]==2 and a[2][0]==2):
			return 2
		
		if(a[0][0]==2 and a[1][1]==2 and a[2][2]==2):
			return 2
		
		if(a[2][2]==2 and a[1][2]==2 and a[0][2]==2):
			return 2
		
		if(a[2][2]==2 and a[2][1]==2 and a[2][0]==2):
			return 2
		
		if(a[2][2]==2 and a[1][1]==2 and a[0][0]==2):
			return 2
		
		if(a[2][0]==2 and a[1][1]==2 and a[0][2]==2):
			return 2
		
		if(a[0][1]==2 and a[1][1]==2 and a[2][1]==2):
			return 2
		
		if(a[1][0]==2 and a[1][1]==2 and a[1][2]==2):
			return 2

		if(a[0][0]==1 and a[0][1]==1 and a[0][2]==1):
			return 2
		
		if(a[0][0]==1 and a[1][0]==1 and a[2][0]==1):
			return 2
		
		if(a[0][0]==1 and a[1][1]==1 and a[2][2]==1):
			return 1
		
		if(a[2][2]==1 and a[1][2]==1 and a[0][2]==1):
			return 1
		
		if(a[2][2]==1 and a[2][1]==1 and a[2][0]==1):
			return 1
		
		if(a[2][2]==1 and a[1][1]==1 and a[0][0]==1):
			return 1
		
		if(a[2][0]==1 and a[1][1]==1 and a[0][2]==1):
			return 1
		
		if(a[0][1]==1 and a[1][1]==1 and a[2][1]==1):
			return 1
		
		if(a[1][0]==1 and a[1][1]==1 and a[1][2]==1):
			return 1
		
logic()