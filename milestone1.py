from graphics import *
import numpy as np

#define more used figures to be functions

def drawline(x1,y1,x2,y2,width=3):
	pt1=Point(x1,y1)
	pt2=Point(x2,y2)
	ln=Line(pt1,pt2)
	ln.setOutline(color_rgb(255,255,255))
	ln.setWidth(width)
	return ln
def checkfield(mouse):
	#returns number depending on the field clicked (0 for beign not in anyfield)
	if  100.0 < mouse.x < 200.0 and 100.0 < mouse.y < 200.0:
		return 1
	elif 200.0 < mouse.x < 300.0 and 100.0 < mouse.y < 200.0:
		return 2
	elif 300.0 < mouse.x < 400.0 and 100.0 < mouse.y < 200.0:
		return 3
	elif 100.0 < mouse.x < 200.0 and 200.0 < mouse.y < 300.0:
		return 4
	elif 200.0 < mouse.x< 300.0 and 200.0 < mouse.y < 300.0:
		return 5
	elif 300.0 < mouse.x < 400.0 and 200.0 < mouse.y < 300.0:
		return 6
	elif 100.0 < mouse.x < 200.0 and 300.0 < mouse.y < 400.0:
		return 7
	elif 200.0 < mouse.x < 300.0 and 300.0 < mouse.y < 400.0:
		return 8
	elif 300.0 < mouse.x < 400.0 and 300.0 < mouse.y < 400.0:
		return 9
	else:
		return 0
def drawxo(num,i):
	if i == 'x':
		if num == 0:
			return
		if num == 1:
			ln1=drawline(120,180,180,120)
			ln2=drawline(120,120,180,180)
			return ln1,ln2
		if num == 2:
			ln1=drawline(220,180,280,120)
			ln2=drawline(220,120,280,180)
			return ln1,ln2
		if num == 3:
			ln1=drawline(320,180,380,120)
			ln2=drawline(320,120,380,180)
			return ln1,ln2
		if num == 4:
			ln1=drawline(120,280,180,220)
			ln2=drawline(120,220,180,280)
			return ln1,ln2
		if num == 5:
			ln1=drawline(220,280,280,220)
			ln2=drawline(220,220,280,280)
			return ln1,ln2
		if num == 6:
			ln1=drawline(320,280,380,220)
			ln2=drawline(320,220,380,280)
			return ln1,ln2
		if num == 7:
			ln1=drawline(120,380,180,320)
			ln2=drawline(120,320,180,380)
			return ln1,ln2
		if num == 8:
			ln1=drawline(220,380,280,320)
			ln2=drawline(220,320,280,380)
			return ln1,ln2
		if num == 9:
			ln1=drawline(320,380,380,320)
			ln2=drawline(320,320,380,380)
			return ln1,ln2
	if i == 'o':
		if num == 0:
			return
		if num == 1:
			pt=Point(150,150)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic
		if num == 2:
			pt=Point(250,150)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic
		if num == 3:
			pt=Point(350,150)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic
		if num == 4:
			pt=Point(150,250)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic
		if num == 5:
			pt=Point(250,250)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic
		if num == 6:
			pt=Point(350,250)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic
		if num == 7:
			pt=Point(150,350)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic
		if num == 8:
			pt=Point(250,350)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic
		if num == 9:
			pt=Point(350,350)
			cic=Circle(pt,30)
			cic.setOutline(color_rgb(255,255,255))
			cic.setWidth(3)
			return cic

def doarray(array,num,typ):
	

	if typ=='o':
		if num==1:
			array[0][0]='o'
		if num==2:
			array[0][1]='o'
		if num==3:
			array[0][2]='o'
		if num==4:
			array[1][0]='o'
		if num==5:
			array[1][1]='o'
		if num==6:
			array[1][2]='o'
		if num==7:
			array[2][0]='o'
		if num==8:
			array[2][1]='o'
		if num==9:
			array[2][2]='o'
	if typ=='x':
		if num==1:
			array[0][0]='x'
		if num==2:
			array[0][1]='x'
		if num==3:
			array[0][2]='x'
		if num==4:
			array[1][0]='x'
		if num==5:
			array[1][1]='x'
		if num==6:
			array[1][2]='x'
		if num==7:
			array[2][0]='x'
		if num==8:
			array[2][1]='x'
		if num==9:
			array[2][2]='x'

def arraycheck(array,typ):
	if typ=='x':
		if (np.array[0][0] == 'x' and np.array[0][1] == 'x' and np.array[0][2]=='x') or (np.array[1][0] == 'x' and np.array[1][1] == 'x' and np.array[1][2]=='x') or (np.array[2][0] == 'x' and np.array[2][1] =='x' and np.array[2][2]=='x'):
		   return True
		elif (np.array[0][0] == 'x' and np.array[1][0] == 'x' and np.array[2][0]=='x') or (np.array[0][1] == 'x' and np.array[1][1] == 'x' and np.array[2][1]=='x') or (np.array[0][2] == 'x' and np.array[1][2] == 'x' and np.array[2][2]=='x'):
			return True
		elif(np.array[0][0] == 'x' and np.array[1][1] == 'x' and np.array[2][2]=='x') or (np.array[2][0] == 'x' and np.array[1][1] == 'x' and np.array[0][2]=='x'):
			return True
		else:
			return False
	elif typ=='o':
		if (np.array[0][0] == 'o' and np.array[0][1] =='o' and np.array[0][2]=='o') or (np.array[1][0] == 'o' and np.array[1][1] == 'o' and np.array[1][2]=='o') or (np.array[2][0] =='o' and np.array[2][1] =='o' and np.array[2][2]=='o'):
		   return True
		elif (np.array[0][0] == 'o' and np.array[1][0] == 'o' and np.array[2][0]=='o') or (np.array[0][1] =='o' and np.array[1][1] =='o' and np.array[2][1]=='o') or (np.array[0][2] == 'o' and np.array[1][2] == 'o' and np.array[2][2]=='o'):
			return True
		elif(np.array[0][0] == 'o' and np.array[1][1] == 'o' and np.array[2][2]=='o') or (np.array[2][0] == 'o' and np.array[1][1] == 'o' and np.array[0][2]=='o'):
			return True
		else: 
			return False
	
	

def main():

	#set background for game
	win=GraphWin("Tic Tac Toe Game",500,500)
	win.setBackground('black')
	drawline(200,100,200,400).draw(win)
	drawline(300,100,300,400).draw(win)
	drawline(100,200,400,200).draw(win)
	drawline(100,300,400,300).draw(win)
	txt=Text(Point(250,50),'Kółko rozpoczyna grę!')
	txt.setTextColor(color_rgb(255,255,255))
	txt.setSize(30)
	txt.draw(win)
	#wait for the mouseclick
	#draws X
	#drawxo(num,'x')[0].draw(win)
	#drawxo(num,'x')[1].draw(win)
	#draws O
	#drawxo(num,'o').draw(win)
	check=False
	s=0
	x_count=0
	o_count=0
	np.array=([0,0,0],
			  [0,0,0],
			  [0,0,0])
	while check==False:
		for i in range(9):
			if i%2==0 and check==False:
				typ='o'
				#check the click
				num=checkfield(win.getMouse())
				#undraw last text
				txt.undraw()
				#draw the O
				drawxo(num,typ).draw(win)
				#make new text 
				txt=Text(Point(250,50),'Kolejny ruch: krzyżyk')
				txt.setTextColor(color_rgb(255,255,255))
				txt.setSize(30)
				txt.draw(win)
				#count
				s=s+1
				#array input and check if won = True
				doarray(np.array,num,typ)
				check=arraycheck(np.array,typ)
				if check==True:
					o_count=1
			elif i%2==1 and check==False:
				typ='x'
				#check the click
				num=checkfield(win.getMouse())
				#undraw last text
				txt.undraw()
				#draw the X
				drawxo(num,'x')[0].draw(win)
				drawxo(num,'x')[1].draw(win)
				#make new text
				txt=Text(Point(250,50),'Kolejny ruch: kółko')
				txt.setTextColor(color_rgb(255,255,255))
				txt.setSize(30)
				txt.draw(win)
				#count
				s=s+1
				#array input and check if won = True
				doarray(np.array,num,typ)
				check=arraycheck(np.array,typ)
				if check==True:
					x_count=1
			else: 
				break
		check=True

	if s <= 9 and check==True and x_count==1:
		txt.undraw()
		txt=Text(Point(250,50),'Krzyżyk wygrał!')
		txt.setTextColor(color_rgb(255,255,255))
		txt.setSize(30)
		txt.draw(win)
	elif s <= 9 and check==True and o_count==1:
		txt.undraw()
		txt=Text(Point(250,50),'Kółko wygrało!')
		txt.setTextColor(color_rgb(255,255,255))
		txt.setSize(30)
		txt.draw(win)	
	else:
		txt.undraw()
		txt=Text(Point(250,50),'Remis!')
		txt.setTextColor(color_rgb(255,255,255))
		txt.setSize(30)
		txt.draw(win)






	win.getMouse()
	win.close()
main()
