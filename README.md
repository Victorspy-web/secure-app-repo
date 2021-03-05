Getting Started


First clone the repository from Github and switch to the new directory:

$ git clone git@github.com/USERNAME/{{ project_name }}.git
$ cd {{ project_name }}


Install pipenv for your project.

$ sudo apt install pipenv


Install Django, activate and migrate project

$ pipenv install django==3.1.4
$ pipenv shell
$ python manage.py migrate


You can now run the development server:

$ python manage.py runserver

