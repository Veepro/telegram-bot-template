# telegram-bot-template
## What is it
You can use this project as a template for your bots. An important feature of this template is convenient local testing. That was the responsibility the variable **“MODE”**. On your computer set “MODE=0”, but in server set “MODE=1”. Also use different values for **“TG_API_TOKEN”** (on local: token of test bot; on serve: token of real bot).

## Instruction
Firstly **fork** this repository, and **clone** your forked repository. [View more about fork and clone](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
### Virtual environment setup
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```
Requirements for base project (Flask and pyTelegramBotAPI) has already in *requirements.txt*. You can import this libs with command:
```
pip install -r requirements.txt
```

After installing other use command for **update** *requirements.txt*:
```
pip freeze > requirements.txt
```
### Deploy to Heroku
Heroku is a cloud platform as a service. For work your Python web app must have the following base structure:
- **Procfile** wich indicates Heroku what and how run 
- **main.py** is entry point for web app
- **requirements.txt** with all the right libraries

For deploy your app use following command:
```
git push heroku main
```

[Read more about deploying with Git](https://devcenter.heroku.com/articles/git)

## Conclusion
Note: lear more about [
pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) and read [Telegram API Documentation](https://core.telegram.org/)
