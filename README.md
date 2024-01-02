<div id = "top"></div>

# Discord Bot

A Simple Discord Bot made with python which has the following features:
- Give inspirational quotes.
- Give random Chuck Norris Jokes.
- Give a photo based on the keywords provided.
- Give answers to query done
- Translate any given language to english.
- Greeting the users or Saying "Good Bye" to them when they join or leave the server respectively.

## Installation and Usage
### List of things you need before the next step:
- A Discord Bot token (*Can be obtained by making a bot in the [Discord Developer](https://discord.com/developers/applications) section*)
- API key for Unsplash (*Can be obtained by making a developer account in [Unsplash](https://unsplash.com/developers)*)

### Cloning the repository

You can clone the repository using the following command:

```bash
https://github.com/SleepyMiner/Discord_Bot.git
```
### Creating a Virtual Environment
First install the **virutalenv** module:
```bash
pip install virtualenv
```
Secondly, create a virtual environment using:
```bash
python -m venv env
```
***or***
```bash
venv env
```
Lastly, activating the virtual environment:
```bash
 env/Scripts/activate.bat //In CMD
 env/Scripts/Activate.ps1 //In Powershel
```
### Installing dependencies
After cloning the repository, navigate to the project directory and install the dependencies by running the following command:
```bash
pip install -r requirements.txt
```
>Make sure you are in the directory while executing this command.
### Running the project
Make a **".env"** file in the directory and keep it in the following format with the exact variable names:
```bash
TOKEN = '<YOUR DISCORD BOT TOKEN HERE>'
API_KEY = '<YOUR UNSPLASH API KEY HERE>'
SECRET_KEY = '<YOUR UNSPLASH SECRET KEY HERER>'
```
To run the project:
- Run the main.py file.
- Make the following channels in your discord server:
- - **get_inspired:** For the inspire function to work.
- - **jokes:** For jokes function to work.

After all the above have been done the following commands can be run:
- **$joke**: To get a random Chuck Norris joke. (Make sure to run this command on the "jokes" channel)
- **$inspire**: To get a inspirational quote. (Make sure to run this command on the "get_inspired" channel)
- **$photo [keyword]**: The key word can be anything you want the picture of. Ex - Dog.
- **$search [keyword]**: The key word can be anything you want to search. Ex - Capital of India.
- **$t [words]**: The words can be in any language you want to translate to English. 
- **$invite**: To create a invite link to the server when it is used.

> Except for the "joke" and "inspire" command the rest of the commands can be used in any channels.


## Contributing


Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## License

[MIT](https://choosealicense.com/licenses/mit/)
