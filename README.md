#### Getting Zip code zone from all brazilian states
This script scrapes all zip codes from all Brazilian states on the Correios website.    
    

##### Installing Webdrivers
###### Linux users:    
* Firefox:    
    - Geckodriver download
`https://github.com/mozilla/geckodriver/releases`
* Chrome:
    - Chromedriver download
`https://chromedriver.chromium.org/downloads`    
    
move the driver to /usr/bin or /usr/local/bin:    
`sudo mv NomeDoDriver /usr/bin`    

###### Windows users:    
It might be use `Chocolatey` following this tutorial in [Installing Chocolatey](https://chocolatey.org/install).    
Then you will be able to install all drivers using:  
`choco install selenium-all-drivers`.    

###### Installing PIPENV in Python
I am using Python 3.8 in this project.   
Now you need to install `pipenv` in Python using the terminal in order to install all
packages that I am using to run this project:
```code
python -m pip install pipenv
```
And now just run    
```code
pipenv update -d
```

- It will be install:    
    * pytest    
    * requests    
    * selenium    
   
##### Running the script in background    
```code
>>> url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
>>> options = ChromeOptions()
>>> options.add_argument("--headless")
>>> driver = Chrome(options=options)
>>> navegador = BuscaLocalidades(navegador, url)
>>> buscacep.acessar_site()  # access the website
>>> buscacep.salvar_localidades()  # saving the file
```    
##### Running tests
```code
pipenv run python -m pytest .
```
##### Reading jsonl file
```code
python ler_jsonl.py
```
###### ToDo: Try to use Threads to access the website and save the file