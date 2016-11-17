#This file is update bootstrap.sh

#!/usr/bin/env bash

#apt-get update
#apt-get install -y apache2
#if ! [ -L /var/www ]; then
#  rm -rf /var/www
#  ln -fs /vagrant /var/www
#fi
import os
from subprocess import call
s = "#!/usr/bin/env bash"
s+="""
echo "Install packages ..."
sudo add-apt-repository -y ppa:git-core/ppa > /dev/null 2>&1
sudo apt-get update > /dev/null 2>&1
sudo apt-get install -y git
sudo apt-get install -y default-jre
sudo apt-get install -y apache2 apache2-mpm-prefork apache2-utils libexpat1 ssl-cert
sudo apt-get install -y libapache2-mod-wsgi
sudo apt-get install -y python-dev python-pip
sudo apt-get install -y  mongodb
git config --global user.name "OnToologyUser"
git config --global user.email ontoology@delicias.dia.fi.upm.es



echo "Old Home is: "
echo $HOME
export HOME=/home/vagrant
echo "New Home is: "
echo $HOME
# setup widoco
echo "Widoco setup ..."
cd $HOME;mkdir widoco;cd widoco; wget --progress=bar:force https://github.com/dgarijo/Widoco/releases/download/v1.2.3/widoco-1.2.3-jar-with-dependencies.jar ; mv widoco-* widoco-0.0.1-jar-with-dependencies.jar ; chmod 777 widoco-*

# setup ar2dtool
echo "ar2dtool ..."
cd $HOME;git clone https://github.com/idafensp/ar2dtool.git; chmod 777 ar2dtool/bin/ar2dtool.jar

# vocablite
echo "vocabLite ..."
cd $HOME;mkdir vocabLite;cd vocabLite; mkdir jar; cd jar; wget --progress=bar:force https://github.com/dgarijo/vocabLite/releases/download/v1.0.1/vocabLite-1.0.1-jar-with-dependencies.jar ; mv vocabLite-*  vocabLite-1.0-jar-with-dependencies.jar; chmod 777 vocabLite-*


echo "owl2jsonld"
cd $HOME;mkdir owl2jsonld; cd owl2jsonld; wget --progress=bar:force https://github.com/stain/owl2jsonld/releases/download/0.2.1/owl2jsonld-0.2.1-standalone.jar


echo "mk dirs ..."

# publish dir
cd ~
mkdir publish
mkdir temp
mkdir config
mkdir wget_dir
mkdir repos
chmod 777 *
chmod 777 -R /var/log/apache2

sudo pip install virtualenv
virtualenv -p /usr/bin/python2.7 venv

echo "Install OnToology requirements.txt"
sudo pip install -r /vagrant/requirements.txt

echo "Install OnToology requirements.txt for virtual environment"
source /home/vagrant/venv/bin/activate; pip install -r /vagrant/requirements.txt

"""

s+="""
cat <<EOT >> /etc/apache2/envvars
export github_username=OnToologyUser
export github_password=%s
export github_repos_dir=/home/vagrant/repos/
export ar2dtool_dir=/home/vagrant/ar2dtool/bin/
export ar2dtool_config=/home/vagrant/config/
export widoco_dir=/home/vagrant/widoco/
export SECRET_KEY=%s
export tools_config_dir=%s
export user_github_username=%s
export user_github_password=%s
export test_repo=%s
export test_folder=/home/vagrant/test
export tests_ssh_key=/home/vagrant/.ssh/id_rsa
export test_github_username=%s
export test_github_password=%s
export client_id_login=e2ea731b481438fd1675
export client_id_public=878434ff1065b7fa5b92
export client_id_private=dd002c8587d08edfaf5f
export client_secret_login=%s
export client_secret_public=%s
export client_secret_private=%s
export previsual_dir=/home/vagrant/vocabLite/jar
export publish_dir=/home/vagrant/publish
export wget_dir=%s
export OnToology_home=true
EOT
    """ % (os.environ['github_password'], os.environ['SECRET_KEY'], os.environ['tools_config_dir'], os.environ['user_github_username'], os.environ['user_github_password'], os.environ['test_repo'], os.environ['test_github_username'], os.environ['test_github_password'], os.environ['client_secret_login'], os.environ['client_secret_public'], os.environ['client_secret_private'], os.environ['wget_dir'])


s+="""
cat <<EOT >> /home/vagrant/venv/bin/activate
export github_username=OnToologyUser
export github_password=%s
export github_repos_dir=/home/vagrant/repos/
export ar2dtool_dir=/home/vagrant/ar2dtool/bin/
export ar2dtool_config=/home/vagrant/config/
export widoco_dir=/home/vagrant/widoco/
export SECRET_KEY=%s
export tools_config_dir=%s
export user_github_username=%s
export user_github_password=%s
export test_repo=%s
export test_folder=/home/vagrant/test
export tests_ssh_key=/home/vagrant/.ssh/id_rsa
export test_github_username=%s
export test_github_password=%s
export client_id_login=e2ea731b481438fd1675
export client_id_public=878434ff1065b7fa5b92
export client_id_private=dd002c8587d08edfaf5f
export client_secret_login=%s
export client_secret_public=%s
export client_secret_private=%s
export previsual_dir=/home/vagrant/vocabLite/jar
export publish_dir=/home/vagrant/publish
export wget_dir=%s
export OnToology_home=true
EOT
""" % (os.environ['github_password'], os.environ['SECRET_KEY'], os.environ['tools_config_dir'], os.environ['user_github_username'], os.environ['user_github_password'], os.environ['test_repo'], os.environ['test_github_username'], os.environ['test_github_password'], os.environ['client_secret_login'], os.environ['client_secret_public'], os.environ['client_secret_private'], os.environ['wget_dir'])


s+="""
echo "Writing to apache"
#source: http://unix.stackexchange.com/questions/77277/how-to-append-multiple-lines-to-a-file-with-bash
cat <<EOT > /etc/apache2/sites-available/000-default.conf
#WSGIPythonPath /vagrant
<VirtualHost *:80>
SetEnv github_username %s
SetEnv github_password %s
SetEnv github_repos_dir %s
SetEnv ar2dtool_dir %s
SetEnv ar2dtool_config %s
SetEnv widoco_dir %s
SetEnv owl2jsonld_dir %s
SetEnv SECRET_KEY %s
SetEnv tools_config_dir %s
SetEnv previsual_dir %s
SetEnv wget_dir %s
SetEnv client_id_login %s
SetEnv client_secret_login %s
SetEnv client_id_public %s
SetEnv client_secret_public %s
SetEnv client_id_private %s
SetEnv client_secret_private %s
SetEnv user_github_username %s
SetEnv user_github_password %s
SetEnv OnToology_home true
ServerAdmin ontoology@delicias.dia.fi.upm.es
Alias /publish/ %s/
<Directory %s>
Options Indexes FollowSymLinks MultiViews
AllowOverride All
Order allow,deny
allow from all
Require all granted
</Directory>
WSGIDaemonProcess www-data python-path=/vagrant:/home/vagrant/venv/lib/python2.7/site-packages
WSGIScriptAlias / /vagrant/OnToology/wsgi.py process-group=www-data
#WSGIScriptAlias / /vagrant/OnToology/wsgi.py
<Directory /vagrant/OnToology>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
DocumentRoot /vagrant
ErrorLog \\${APACHE_LOG_DIR}/error.log
CustomLog \\${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOT
""" % (os.environ['github_username'] ,os.environ['github_password'], os.environ['github_repos_dir'], os.environ['ar2dtool_dir'], os.environ['ar2dtool_config'], os.environ['widoco_dir'], os.environ['owl2jsonld_dir'], os.environ['SECRET_KEY'], os.environ['tools_config_dir'], os.environ['previsual_dir'], os.environ['wget_dir'],
       os.environ['client_id_login'],
       os.environ['client_secret_login'],
       os.environ['client_id_public'],
       os.environ['client_secret_public'],
       os.environ['client_id_private'],
       os.environ['client_secret_private'],
       os.environ['user_github_username'],
       os.environ['user_github_password'],
       os.environ['publish_dir'],
       os.environ['publish_dir'])

s+="""
cat <<EOT > /home/vagrant/config/ar2dtool-class.conf
pathToDot=/usr/bin/dot;
pathToTempDir=/home/vagrant/temp;

imageSize=1501;
rankdir=LR;

########
#shapes#
########

#classShape=diamond;
#individualShape=diamond;
#literalShape=box;
#arrowhead=normal;
#arrowtail=normal;
#arrowdir=forward;

########
#colors#
########

classColor=orange;
#individualColor=orange;
#literalColor=blue;
#arrowColor=blue;

#############
#RDF options#
#############

nodeNameMode=prefix;
ignoreLiterals=true;
ignoreRdfType=true;
synthesizeObjectProperties=true;

#######
#lists#
#######

#ignoreElementsList=[];

ignoreElementList=[<http://www.w3.org/2000/01/rdf-schema#subClassOf,http://www.w3.org/2000/01/rdf-schema#isDefinedBy,http://www.w3.org/2002/07/owl#inverseOf>];
EOT

cat <<EOT > /home/vagrant/config/ar2dtool-taxonomy.conf
pathToDot=/usr/bin/dot;
pathToTempDir=/home/vagrant/temp;

imageSize=1000;
rankdir=LR;

########
#shapes#
########

#classShape=diamond;
#individualShape=diamond;
#literalShape=box;
#arrowhead=normal;
#arrowtail=normal;
#arrowdir=forward;

########
#colors#
########

#classColor=orange;
#individualColor=orange;
#literalColor=blue;
#arrowColor=blue;

#######
#files#
#######

generateGvFile=true;
generateGraphMLFile=false;

#############
#RDF options#
#############

nodeNameMode=prefix;
ignoreLiterals=true;
ignoreRdfType=false;
synthesizeObjectProperties=false;

#######
#lists#
#######

includeOnlyElementList=[
<
http://www.w3.org/2000/01/rdf-schema#subClassOf
>
];
EOT

"""

#source: https://github.com/Anomen/vagrant-selenium/blob/master/script.sh
s+="""

#=========================================================
echo "Install Selenium prerequisits packages..."
#=========================================================
sudo apt-get -y install fluxbox xorg unzip vim default-jre rungetty firefox

#=========================================================
echo "Set autologin for the Vagrant user..."
#=========================================================
sudo sed -i '$ d' /etc/init/tty1.conf
sudo echo "exec /sbin/rungetty --autologin vagrant tty1" >> /etc/init/tty1.conf

#=========================================================
echo -n "Start X on login..."
#=========================================================
PROFILE_STRING=$(cat <<EOF
if [ ! -e "/tmp/.X0-lock" ] ; then
startx
fi
EOF
)
echo "${PROFILE_STRING}" >> .profile
echo "ok"

#=========================================================
echo "Download latest selenium server..."
#=========================================================
SELENIUM_VERSION=$(curl "https://selenium-release.storage.googleapis.com/" | perl -n -e'/.*<Key>([^>]+selenium-server-standalone[^<]+)/ && print $1')
wget --progress=bar:force "https://selenium-release.storage.googleapis.com/${SELENIUM_VERSION}" -O selenium-server-standalone.jar
chown vagrant:vagrant selenium-server-standalone.jar


#=========================================================
echo -n "Install tmux scripts..."
#=========================================================
TMUX_SCRIPT=$(cat <<EOF
#!/bin/sh
tmux start-server
tmux new-session -d -s selenium
tmux send-keys -t selenium:0 './chromedriver' C-m
tmux new-session -d -s chrome-driver
tmux send-keys -t chrome-driver:0 'java -jar selenium-server-standalone.jar' C-m
EOF
)
echo "${TMUX_SCRIPT}"
echo "${TMUX_SCRIPT}" > tmux.sh
chmod +x tmux.sh
chown vagrant:vagrant tmux.sh
echo "ok"

#=========================================================
echo -n "Install startup scripts..."
#=========================================================
STARTUP_SCRIPT=$(cat <<EOF
#!/bin/sh
~/tmux.sh &
xterm &
EOF
)
echo "${STARTUP_SCRIPT}" > /etc/X11/Xsession.d/9999-common_start
chmod +x /etc/X11/Xsession.d/9999-common_start
echo "ok"

"""

s+="""
sudo service apache2 restart
"""

f = open("bootstrap.sh", "w")
f.write(s)
f.close()
call("vagrant up", shell=True)


