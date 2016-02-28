# embedded-project-rcs

Project Rapid Confidential Smoke

Project Description

Week 1: 14-02-16

Connected a push button to beaglebone, created a local python client to poll for button presses, then sent the press and timestamp when pressed to a local python udp server, which in turn sent an http post request to a flask server

Week 2: 21-02-16

Connected the DFR0066 Temperature and Humidity Sensor to arudino, then connected arduino to beaglebone via serial usb

Week 3: 28-02-16

Set up a test DB for recording results with flask and sqlite3, made a random data generator that sends data every second through udp to local server, and then on to remote, to be recorded on database

Coming Up:

Create a typescript client to view live data
Hook up to a remote db server (MySQL)
Connect temperature sensor to replace fake data
Show live graphs on ts app
