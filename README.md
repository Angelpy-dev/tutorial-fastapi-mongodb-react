# tutorial-fastapi-mongodb-react

#so... i will write every single step i do below.

- i install extension for python
- git command works on the files in current folder

1. create folders backend, inside create venv using 'python -m venv venv'
2. activate venv 'source venv/bin/activate {still in backend folder btw}
3. create database.py, main.py and requirements.txt **create .gitignore in root folder, add files and folder as needed**
4. install fastapi, uvicorn, pymongo (pengganti motor driver for mongodb), python-dotenv
(if theres clashing issue where failed to import even after install, do ctrl+shift+p then choose interpreter through path make sure its './venv/bin/python)
5. open mongodb cloud atlas, login, copy connection string from cluster dashboard
6. create codespace secrets for MONGO_URL and DB_NAME
7. write connection to mongodb code in database.py
8. write fastapi-mongodb connection in main.py just the /root 
9. run server with uvicorn main:app --reload
9. navigate to /frontend then in terminal: npm create vite@latest frontend, select react and javascript.
10. inside /frontend, there will be another folder name /frontend which contains react stuffs, so navigate to that /frontend and in terminal "npm install" to install packages
11. inside this /frontend, youll find folder /src which contains files that actually you gonna works on
11. in vite.config.json we add server:{port: 5173}
12. in App.jsx we connect fastapi server unicorn which in port 8000 to react server which run in port 5173.
13. in codespace cors will be block if both port backend and frontedn are private, make it public it fix it, do it in ctrl+j tab ports. if port address changing, change the url in codes too.
14. never forget to add exception and error handling.
15. dont focus energy to AI debugging.
16. sanity check env variabels (codespace secrets) IN TERMINAL echo $MONGO_URL 
17. run farm stack: 
        1st terminal: cd /backend, activate venv "source venv/bin/activate" , run server "uvicorn main:app --reload" 
        2nd terminal: cd /backend, activate venv "source venv/bin/activate" , cd .. , cd /frontend, cd/ frontend, run server "npm run dev"
        if failed to connect frontend and backedn, maybe url are different (codespace changes them)

18. push to github guide:
        make sure your requirements.txt and gitignore are done
        frontend dependencies are on package.json so only backedn dependencies are on requirements.txt
        a. remove all sensitives information: including public URL ports 
        b. /backend: git add main.py, database.py, requirements.py
        c. /frontend: git add index.html, package.json, package-lock.json, vite.config.js
        d. /frontend: src/ git add main.jsx, App.jsx
        e. /root: git add README.md , .gitignore
        f. commit
        g. push

this is how the ready to commit git status looks like:
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        modified:   README.md
        new file:   backend/database.py
        new file:   backend/main.py
        new file:   backend/requirements.txt
        new file:   frontend/frontend/index.html
        new file:   frontend/frontend/package-lock.json
        new file:   frontend/frontend/package.json
        new file:   frontend/frontend/src/App.jsx
        new file:   frontend/frontend/src/main.jsx
        new file:   frontend/frontend/vite.config.js