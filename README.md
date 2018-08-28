## Create & activate virtual environment


virtualenv venv 

source venv/bin/activate



## Remove database stuff: 


rm -rf django_rest/migrations && rm -rf django_rest/blog

## Create new database: 


./manage.py makemigrations blog 


./manage.py migrate blog 


## Create user so you can post to db 
./manage.py createsuperuser 



## Run 
./manage.py runserver 




#### Main page where all blog posts are: 
http://127.0.0.1:8000/



#### View a specific blog post by pk: 
http://127.0.0.1:8000/post/1/



#### Make new blog post (but must be signed in as admin): 
http://127.0.0.1:8000/post/new/



#### View all of API: 
http://127.0.0.1:8000/api/



#### View API by PK: 
http://127.0.0.1:8000/api/1 

