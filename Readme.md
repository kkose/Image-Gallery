# Make-photo-gallery-from-image-directory-with-php

A simple php webpage creator that takes a folder of images and serves them on a website. 

## Credits:

Original Project is from 
Author: Yogesh singh
Author URL: http://makitweb.com/
Author Email: yssyogesh@makitweb.com
Tutorial Link: http://makitweb.com/make-photo-gallery-from-image-directory-with-php/

Edited by Kivanc Kose'2020



## Instructions

First install Php server to your computer. For a ubuntu system following steps can be used

#### ***Installing PHP 7.2 with Apache***

If you are using Apache as your web server to install PHP and Apache PHP module run the following command:

```shell
sudo apt install php libapache2-mod-php
```

Once the packages are installed restart the Apache service:

```shell
sudo systemctl restart apache2
```

After the php server is installed one can run it under any given folder by using the following command. 

```shell
php -S localhost:8000
```

replace "localhost" with the ip address of the computer to make the site accessible from another computer in the network. One can also change the port number. 

#### ***Running this Project***

The project takes a folder of images and their thumbnails, and serve them as a photo gallery. You need to run the php server initiation command in the project folder.

Step0: (In case the thumbnail images are not created before) 

Thumbnails of the images in a given folder can be prepared using thumbnailer.py python script under the project. 

```shell
python thumbnailer.py --direc XXX
```

This will create a subfolder called "thumbnails" under the target folder XXX. The current version of the script only looks for jpg files. But one can change that to a different file extension by updating Line 18.

###### **Step1**: 

After the creation of thumbnails, the gallery can be accessed via any internet browser by typing the address; 

localhost:8000 or ipAddr:8000 (replace ipAddr with the ip of the computer running the server.)



###### **Step2:**

Edit line 21 in index.php file to point to the images folder that you want to visualize. Due to apache restrictions, the folder of the images should be under the root folder of the project. You can copy the images folder inside the project and point the "$dir" variable to the respective location
$dir="images/YourImageFolder"
An alternative solution is to create a symbolic link to the location of your images. One can do this by

```shell
ln -s location_of_your_images ./images/
```


and then set $dir="images/YourImageFolder" to the symbolic link you just created.



==!!!HAPPY VIEWING!!!==









###### Other Notes

*******
To run PHP in MAC, one should start the built-in Apache Web server and also enable the PHP already installed.

This can be done with the following steps.

Go to /etc/apache2/httpd.conf and change the permission to sudo chmod 777 httpd.conf

Then open the above file to uncomment the line #LoadModule php5_module libexec/apache2/libphp5.so

To start the apache built-in server, use the command sudo apachectl start in the terminal.

Now .php files can be created and run from the terminal using php -f filename.php and it can also be run on a browser using http://localhost/filename.php

*******
