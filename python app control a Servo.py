from Tkinter import *
import serial
import sys
import glob
import time

RightLeftCounter = 90
 
class App:
  def __init__(self, master, ser):
 
    self.ser  = ser
    self.button = Button(master, text="QUIT", fg="red",command=quit)
    self.button.grid(row=0, column=0, padx=0, pady=0,ipadx=25,ipady=25,sticky="nw")
 
    self.slogan = Button(master,text="Reset", command=self.write_reset)
    self.slogan.grid(row=0, column=4, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")
 
    self.Left = Button(master,text="Left",padx=10,command=self.write_Left)
    self.Left.grid(row=0, column=1, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")
 
    self.Right = Button(master,text="Right",padx=10,command=self.write_Right)
    self.Right.grid(row=0, column=6, padx=2, pady=0,ipadx=25,ipady=25, sticky="nw")

    self.sweep = Button(master,text="Sweep",command=self.write_sweep)
    self.sweep.grid(row=0, column=8, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")

    self.location = Button(master,text="location",command=self.write_location)
    self.location.grid(row=0, column=10, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")

    self.button1 = Button(master, text="30", fg="purple",command=self.write_30)
    self.button1.grid(row=1, column=0, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")

    self.button2 = Button(master, text="45", fg="purple",command=self.write_45)
    self.button2.grid(row=1, column=1, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")

    self.button3 = Button(master, text="60", fg="purple",command=self.write_60)
    self.button3.grid(row=1, column=4, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")

    self.button4 = Button(master, text="90", fg="purple",command=self.write_90)
    self.button4.grid(row=1, column=6, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")

    self.button5 = Button(master, text="135", fg="purple",command=self.write_135)
    self.button5.grid(row=1, column=8, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")

    self.button6 = Button(master, text="180", fg="purple",command=self.write_180)
    self.button6.grid(row=1, column=10, padx=0, pady=0,ipadx=25,ipady=25, sticky="nw")
 
 
  def write_Left(self):
    global RightLeftCounter
    if (RightLeftCounter>0):
      RightLeftCounter = RightLeftCounter +1
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())
 
  def write_Right(self):
    global RightLeftCounter
    if (RightLeftCounter<=180):
      RightLeftCounter = RightLeftCounter -1
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())
  def write_reset(self):
    global RightLeftCounter
    RightLeftCounter = 90
    print(RightLeftCounter)
    self.ser.write(chr(RightLeftCounter))
    print (self.ser.readline())
 
  def write_sweep(self):
    global RightLeftCounter
    for RightLeftCounter in range(0,180):
      print(RightLeftCounter)
      self.ser.write(chr(RightLeftCounter))
      print (self.ser.readline())
      time.sleep(0.01) 
    RightLeftCounter = 90
    self.ser.write(chr(RightLeftCounter))

  def write_location(self):
    global RightLeftCounter

    print (self.ser.readline())
 
  def write_30(self):
    global RightLeftCounter
    RightLeftCounter = 30
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())
    
  def write_45(self):
    global RightLeftCounter
    RightLeftCounter = 45
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())

  def write_60(self):
    global RightLeftCounter
    RightLeftCounter = 60
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())

  def write_90(self):
    global RightLeftCounter
    RightLeftCounter = 90
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())

  def write_135(self):
    global RightLeftCounter
    RightLeftCounter = 135
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())

  def write_180(self):
    global RightLeftCounter
    RightLeftCounter = 180
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())
    

  
 
def main():
  ser = serial.Serial()
  ser.port = 'COM4'
  ser.baudrate = 9600
  ser.timeout = 0
  if ser.isOpen() == False:
    ser.open()
  root = Tk()
  root.title("Servo_Controlled _By_Python_App")
  root.geometry("700x160+500+300")
  app = App(root,ser)
  root.mainloop()
 
if __name__ == '__main__':
  main()
