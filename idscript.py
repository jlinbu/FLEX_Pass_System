#!/usr/bin/env python
import csv
import os
import cups
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


data = []
known_badges = []
def main():
    with open('badges.csv', 'r') as badges:
        reader = csv.reader(badges)
        for row in reader:
            print(row)
            data.append(row)
            known_badges.append(str(row[0]))
        badges.close()
        print (known_badges)

def scan(mode):
   scan = str(input("Please scan your ID now! "))
   if scan in known_badges:
        if mode == "br":
            br_print(scan)
        elif mode == "flex":
            flex_print(scan)
   else:
        register(scan, mode)
def br_print(scan):
         for entry in data:
            print (entry[0])
            if entry[0] == scan:
                print ("Welcome " + entry[1])
                file=open('print.txt','w')
                file.write("BATHROOM PASS \n******************\n" + entry[1] + "\n")
                date = time.strftime("%a, %d %b %Y",time.gmtime())
                timetoday = time.strftime("%X", time.gmtime())
                file.write("Time leaving class\n" + timetoday + "\n" + date)
                file.close()
                conn = cups.Connection()
                conn.printFile('ZJ-58','print.txt', 'printing', {})

def flex_print(scan):
         for entry in data:
            print (entry[0])
            if entry[0] == scan:
                print ("Welcome " + entry[1])
                file=open('print.txt','w')
                date = time.strftime("%a, %d %b %Y",time.gmtime())
                timetoday = time.strftime("%X", time.gmtime())
                file.write("FLEX PASS \n******************\n" + date)
                
                file.write("\nPlease allow\n" +entry[1] + "\nto attend flex in\nroom 109 today.\n\nX________________")
                file.close()
                conn = cups.Connection()
                conn.printFile('ZJ-58','print.txt', 'printing', {})    


def register(scan, mode):
    name = str(input("What is your full (first and last) name? "))
    print ("Registered! \n")
    data.append([scan,name])
    known_badges.append(scan)
    with open('badges.csv', 'w') as badges:
        writer = csv.writer(badges, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)
        badges.close()
        
        if mode == "br":
            print("br_print")
            br_print(scan)

class Handler:
    def onButtonPressed():
        print ("pressed")
    def bathroompressed(self, object):
        scan("br")
        print ("pressed")

        
class Gtkapp:
  def on_window1_destroy(self, object, data=None):
    print ("quit with cancel")
    gtk.main_quit()

  def on_gtk_quit_activate(self, menuitem, data=None):
    print ("quit from menu")
    gtk.main_quit()

    


  def __init__(self):
    self.gladefile = "idgui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    
    self.window = self.builder.get_object("window1")
    self.bathroom = self.builder.get_object("bathroom")
    self.builder.connect_signals(Handler())
    self.window.show_all()
    main()
   #main()

if __name__ == "__main__":
  main = Gtkapp()
  gtk.main()



