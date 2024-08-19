This is webstack debugging project
I had to run a container and fix an Issue that was preventing to
load a webpages using curl 0:8080.
I run the container and with in bash, I tried to look for the cause
I found that web server Apache was not running, I tried to start it
using systemctl and service but I found that they were not available in the
container.
I had to look for alternative way to start the program and used
sudo /etc/init.d/apache2 start
and it worked perfectly, from then I could load the webpages normally.

This project is for learning perpuse only.
Author: D-Murenzi.
