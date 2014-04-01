clickpirc
=========

Click Button Control for Raspberrypi RC-Car

Project by www.rasplay.org - Multi-Control-RCCar

This is HTML5 and Python Source Code for Webiopi, and RC Car with Raspberry-pi.

Dependency
HW 
 1. RC Car with DC Motor
 2. Raspberry-pi, it is ultra-low-cost ($35) credit-card sized computer, can run Linux.
 3. Multi-Pi, it is Raspberry-pi extension Board, easy to connect DC Motor and it is like breadboard. Some sample in www.rasplay.org

SW
 1. Webiopi, it is Raspberry IO Web Software using Python, HTML5, JS.

$ cd /usr/share/webiopi/htdocs/app

$ sudo git clone https://github.com/rasplay/clickpirc.git

I'm using in webiopi macro function.

$ sudo vi /etc/webiopi/config

myscript = /usr/share/webiopi/htdocs/app/clickpirc/script.py

$ sudo /etc/init.d/webiopi restart

Run Web Brower, supported HTML5 (like Chrome browser)

"http://[raspberrypi-IP]/app/clickpirc"

Enjoy!!  
