# About AgriEcon Predictor 
AgriEcon Predictor is a model designed to empower Indian policymakers enhance food security in the different Indian states. Our model utilizes machine learning, analyzing historical data and Consumer Price Index trends to provide accurate forecasts for food prices, aiding in strategic subsidy allocation and informed decision-making for a resilient and sustainable agriculture sector.

# Setting Up

## Install Git
Navigate to the following links to download Git on your OS:
- **Windows:** [Link to download for Windows](https://git-scm.com/download/win)
- **Mac OS:** [Link to download for Mac OS](https://git-scm.com/download/mac)

## Downloading the Repository
To clone our project directory from Github, change to your current working directory and download the repository. On your Terminal, type:

```shell
cd Downloads
git clone https://github.com/priyanshisaraogi/DDW_Bonus.git
```

## Go to the project folder
After downloading the repository, you can go to the folder named `BONUS`. It is the `root` folder of our application.

```shell
cd DDW_Bonus/BONUS
```
## Creating a Virtual Environment
**Open Anaconda Prompt to do the following steps.**

Install the `pipenv` package.
```shell
python -m pip install --user pipenv
```
If you are running the commands on `Vocareum` and you encounter warning messages, it basically means that you need to add the newly installed `pipenv` program into the `PATH`. You can do that by runnng the following command:
```shell
export PATH='/voc/work/.local/bin':$PATH
```
Install the packages in the root folder.
```shell
python -m pipenv install
```
To activate and enter the virtualenv, run
```shell
python -m pipenv shell
```
To exit the virtualenv at the end of this mini project, simply type:
```shell
exit
```
Run the program in the virtualenv shell and follow the abovementioned steps to enter and exit the shell each time.

# Running the Code
Make sure you have entered the virtual environment and the root folder is your current working directory. Once you have done that, run flask:
```shell
flask run
```

Some output will be generated on the terminal, one of the lines of which would be:
```shell
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Click on the link. On Vocareum, do `Ctrl+Click` (Windows) or `Cmd+Click` (Mac) on the link `http://127.0.0.1:5000/` and it should open the website in a new tab on your browser. 

Press `Ctrl+C` to stop the web app from running.

# Getting Output
