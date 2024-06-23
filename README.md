
# Todo Flask ORM API

## Index
<a href="#run-this-repo">Run this repo</a><br />
<a href="#start-fresh-project">Start Fresh Project</a><br />
<a href="#upload-your-project-in-github">Upload your project in github</a><br />
<a href="#clone-the-repo">Clone the repo from github</a><br />

## Run

## <div id="run-this-repo">&rarr; Run this repo,</div>

 Clone this repo and follw the <a href="#start-fresh-project">`Start Fresh`</a> steps. but you can skip `step 3` because, you have project files and folder no need to create again.

---

## <div id="start-fresh-project">&rarr; Start fresh Project,</div> 

`Step: 1` Create a `venv` and activate
    
    // create
    python -m venv venv

    // activate
    venv/Scripts/active (Powershell)
    source venv/Scripts/active (Bash)
    
NOTE: If Powershell Shows `ERROR` run this command. If it not work simply googe it, you can find the solution.
    
    Get-ExecutionPolicy
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

`Step: 2` Choose correct `Python interpreter` Vscode

    Ctrl + Shift + P and Python: Select interpreter    
    (or)
    Select the version from bottom right corner in py file after creating basic folder structure.

`Step: 3` You need to a folder structure for the project.

    flask_todo/
    │
    ├── src/
    │   ├── __init__.py
    │   ├── models/
    │   |    └── todo_model.py  
    │   ├── routes/
    │   |    └── todo_route.py  
    │   ├── controllers/
    │   |    └── todo_controller.py  
    │   └── config.py
    │
    ├── migrations/
    │   └── (auto-generated files by Flask-Migrate)
    │
    ├── venv/ 
    │   └── Packages and etc..
    │
    ├── app.py
    ├── requirements.txt
    └── README.md

NOTE: 
    In here 

    1) You do not need to create venv folder manually. It will be created automatically when the venv is initialized.

    2) There is no need to manually create a migrations folder. It will be generated automatically when a migration is created.

`Step: 4` Install Needed packages from PIP

    pip install Flask
    pip install Flask-SQLAlchemy
    pip install PyMySQL
    pip install Flask-Migrate

`Step: 5` Create a DB in MySql (PhpMyAdmin)

`Step: 6` Run this Command in terminal for migration,
        
        flask db init
        flask db migrate -m "Migration Meassage"
        flask db upgrade

---

## <div id="upload-your-project-in-github">&rarr; Upload your project in `github`,</div>

- Make sure you replace your credentials with some placeholder in `config.py`.

- Generate or upload `requirements.txt`

        pip freeze > requirements.txt

- You must add your migrations folder to git.

- Export your DB in PhpMyAdmin, send it your friend any otherways like mail, whatsapp, ...


---

## <div id="clone-the-repo">&rarr; clone the repo from `github,</div>

`Step: 1` Clone the repo.

    git clone https://github.com/dmmuralitharan/todo-flask-orm-api.git

`Step: 2` Map the repo's root folder using `cd` command

NOTE: Make you have the `migrations` folder.

`Step: 3` Create a `venv` and activate
    
    // create
    python -m venv venv

    // activate
    venv/Scripts/active (Powershell)
    source venv/Scripts/active (Bash)
    
NOTE: If Powershell Shows `ERROR` run this command. If it not work simply googe it, you can find the solution.
    
    Get-ExecutionPolicy
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

`Step: 4` Choose correct `Python interpreter` Vscode

    Ctrl + Shift + P and Python: Select interpreter    
    (or)
    Select the version from bottom right corner in py file.

`Step: 5` Install the Package from PIP, Using `requirements.txt`.

    pip install -r requirements.txt
   
`Step: 6` Create a DB and Import your .sql DB file received from your friend in PhpMyAdmin.

---



