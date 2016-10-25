Sikuli tests for GPII
=====================

Quick setup
-----------
 
 1. Clone this git repository
 2. vagrant up
 3. vagrant winrm -c "do.ps1 -c 'java -jar c:\vagrant\tests\sikulix.jar -r c:\vagrant\tests\test_001.sikuli'"



This repository contains an example of how some integration tests can be
performed usin SikuliX(http://sikulix.com/).

SikuliX automates anything you see on the screen of your desktop computer
running Windows, Mac or some Linux/Unix. It uses image recognition powered by
OpenCV to identify and control GUI components.

In this repository you will find a test(tests/test_001.sikuli) that performs an
installation and some checks, then it removes the application using the 
installer.

In the [directory test](tests/test_001.sikuli), you will find the images that 
SikuliX uses to recognize the elements where apply the events and a [Jython 
script](tests/test_001.sikuli/test_001.py) where the tests steps are defined.
