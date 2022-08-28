# Study Micro-Blog
# Introduction
StudyBuddy discussion room project is a Python based application developed in Django Framework. This project has features to create multiple discussion rooms and other users can follow discussion rooms and comment their opinions.  
Different python packages were used to develop this project such as crispy-form, celery, redis, pillow, and so on, which are all mentioned in requirements.txt file.

# Tech Stack
  1. [Python 3.9](https://www.python.org/)
  2. [Django 4.0.4](https://www.djangoproject.com/)
  3. [PostgreSQL](https://www.postgresql.org/)
  4. [jQuery 3.6.0](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/)
  5. [Bootstrap5](https://getbootstrap.com/)
  6. [Docker](https://www.docker.com/)

# Installation
**GIT clone from GitHub**

###### First step is to make a directory.
```
$ mkdir student_blog
$ cd student_blog
```

###### Then clone the [student-microblog App Repo](https://github.com/Shuvam77/student-microblog) from the GitHub.
```
student_blog $ git clone https://github.com/Shuvam77/student-microblog.git .
```

**Docker**
###### Docker Compose
Build Images and Run Docker Containers
```
student_blog $ docker build .
student_blog $ docker-compose up
```

###### Migrations
Propogate your models into database schema
```
student_blog $ docker-compose exec web python manage.py makemigrations
student_blog $ docker-compose exec web python manage.py showmigrations
student_blog $ docker-compose exec web python manage.py migrate 
```

###### Create Django Superuser
For super access in application
```
student_blog $ docker-compose exec web python manage.py createsuperuser

Username: admin
Email address: admin@email.com
Password: sudo@123

URL: http://YOUR_LOCALHOST_URL/admin/
```

###### Run docker containers
```
student_blog $ docker-compose up
or
student_blog $ docker-compose up -d (run in background)
```

###### Stop docker container
```
student_blog $ docker-compose down
```

###### Run and build container
```
student_blog $ docker-compose up --build
```
