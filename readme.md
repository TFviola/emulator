# BUILD
```
pyinstaller --onefile --add-data "static;static" --add-data "templates;templates" --name "AIDOEmulator" main.py
```
**--onefile** means to create a single executable file
**--add-data "static;static"** means to add the static folder of source and copy to static
**--add-data "templates;templates"** means to copy templates folder to templates folder