# LIS Data Entry Web App

This is a simple data entry web application using Python and Django.
###  Prequisites

This program requires Python 3 and Django in order to run.

To install ```Python 3```, visit [python.org/downloads](python.org/downloads) and follow instructions for your 
operating system.

To install ```Django```:

```commandline
pip install Django
```

If Python and/or Django are already installed, check if either are up-to-date.

```commandline
python --version
```

```commandline
 python -m django --version
```

If Python/Django are installed and neither command works, try replacing 
```python``` with ```python3```.

### Recommended

It's recommended to create a ```virtual environment```.  To create a virtual environment: 
```
python -m venv <env_name>
```
To activate virtual environment:

Windows: 
```
.\<env_name>\Scripts\activate
```
macOS/Linux: 
```
source <env_name>/bin/activate
```

### Run Program

In the commandline, navigate to the directory holding the lisform repo. You can verify
you are in the corrected directory using the ```ls``` command in your current directory. 
The output should read 
```
README.md       db.sqlite3      form            lisform         manage.py
```

To run the program:

```
python3 manage.py runserver <port: optional>
```

In a web browser, navigate to ```localhost:<port>```. If a port was specified,
use the port number in place of ```<port>```. Otherwise, the default address is ```localhost:8000```.

To quit the server, on your commandline, press ```Ctrl + C``` or ```^C```.
