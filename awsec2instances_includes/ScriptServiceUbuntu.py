from awsec2instances_includes.UserDataProcess import UserDataProcess
from awsec2instances_includes.ScriptServiceInterface import ScriptServiceInterface
import os

class ScriptServiceUbuntu(ScriptServiceInterface):

    def __init__(self):
        self.home_directory = "/home/ubuntu"
        self.http_user = "www-data"

    def setUserScript(self, userStript):
        self.userScript = userStript
        return self

    def firstUpdate(self):
        self.userScript.add_scripts("apt update -y")
        self.userScript.add_scripts("apt upgrade -y")
        return self

    def install_httpd(self):
        self.userScript.add_scripts("apt install apache2 -y")
        return self

    def install_https(self):
        self.userScript.add_scripts("a2enmod ssl")
        self.userScript.add_scripts("a2ensite default-ssl.conf")
        self.userScript.add_scripts("systemctl restart apache2")
        return self

    def install_php(self):
        self.userScript.add_scripts("apt install php7.4 php7.4-mysql -y")
        self.userScript.add_scripts("service apache2 restart")
        return self

    def install_php_mbstring(self):
        self.userScript.add_scripts("apt install php-mbstring -y")
        return self

    def install_php_dom(self):
        self.userScript.add_scripts("apt install php-dom -y")
        return self

    def install_php_gd(self):
        self.userScript.add_scripts("apt install php-gd -y")
        return self

    def enable_httpd(self):
        self.userScript.add_scripts("chkconfig httpd on")
        self.userScript.add_scripts("service httpd start")
        return self
    

    def database(self):
        self.userScript.add_scripts("apt install mariadb-server mariadb-client -y")
        self.userScript.add_scripts("systemctl enable --now mariadb")
        return self

    def assingWwwPermissionToLocalUser(self):
        self.userScript.add_scripts("chmod 775 /var/www/html")
        self.userScript.add_scripts("chgrp ubuntu /var/www/html")
        return self

    def checkpointType(self, message: str):
        self.userScript.add_scripts("echo $(date \"+%Y%m%d %Hh%Mm%Ss\") " + message + " >> " + self.home_directory + "/bootstrap.log")
        return self

    def get_http_user(self):
        return self.http_user

    def httpd_restart(self):
        self.userScript.add_scripts("service apache2 restart")
        return self
