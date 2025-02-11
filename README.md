# Assignment for Developer Role

## List of Assigments:

### Task 1
#### Write a python program to find the unique words in the given sentence
##### Solution given in the folder "coding_questions" as "unique_words.py"

---

### Task 2
#### Rewrite the function to reduce time complexity.
##### Solution given in the folder "coding_questions" as "duplicates.py"

---

### Task 3
#### Build a Simple API Using Flask (or Django, if preferred)
##### Requirements:
Use Flask (or Django/FastAPI) to create an API with the following endpoints:
1. POST /tasks → Add a new task 
2. GET /tasks → Get all tasks
3. PUT /tasks/<task_id> → Update a task
4. DELETE /tasks/<task_id> → Delete a task
5. Store tasks in a list (or a database if comfortable).
6. Ensure error handling (e.g., task not found, invalid input).

--- 

### In the todoapp_django folder the django project has been built 

#### There are two project
1. taskapp : The main project comprises listed above endpoints
2. todolist : In this app i have creating api based on user sessions. There we have api like GET, POST, DELETE

--- 

# 1. TASKAPP

## The taskapp has the requested assignments 

## Steps to run the project

### To navigate to the project:

#### In the terminal
`cd todoapp_django`

`python manage.py runserver` to run the server


### The API Endpoints as follows for the taskapp

#### 1. GET /tasks → Get all tasks
```

In the browser, add /api that will re-route to the home page

http://127.0.0.1:8000/api/

```

#### 2. POST /tasks → Add a new task 

In the browser, add /api/tasks/create that will re-route to the create page where you can add new task


```

http://127.0.0.1:8000/api/tasks/create/

```
#### 3. PUT /tasks/<task_id> → Update a task

In the browser, add /api/tasks/update/int:<id>/  that will re-route to the update page where you can toggle the task to its completion

```

http://127.0.0.1:8000/api/tasks/update/int:<id>/

```


#### 4. DELETE /tasks/<task_id> → Delete a task
In the browser, add /api/tasks/delete/int:<id>/  that will re-route to the delete page where we get a page asking for confirmation to delete the task
```
http://127.0.0.1:8000/api/tasks/delete/int:<id>/

```


#### 5. Store tasks in a list (or a database if comfortable).

##### The data is stored in the PostgreSQL

![Image.Png](./images/image.png)

##### Database Config()

```

{ 
  'ENGINE': 'django.db.backends.postgresql',
  'NAME': 'loginregister', 
}

```

6. Ensure error handling (e.g., task not found, invalid input).
Implemented try and Except for the functions used in veiws.py 

``` py

def update_task(request, id):
    try: 
        task = get_object_or_404(Task, id=id)

        if request.method == 'POST':
            task.completed = True
            task.save()
            return redirect('home')
    except Exception as e:
        print(f'Updated faild: Due to Error {e}')
    
    return render(request, 'content/update_task.html', {'task': task})

```



# 2. TASKAPP