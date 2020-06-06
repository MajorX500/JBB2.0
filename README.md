# JBB.py
Discord bot programmed in Python

## Getting Started
### Setting up
### Credentials
* Get a discord bot Token and place it into a text file named `auth`
* Get a access key to wolfram alpha and place the key in a file named `WA_KEY`
* Get acess to google via `client_secret.json`

#### Automatic
```bash
sh run.sh
```
* follow the instructions on screen to activate the access to google calendar

#### Manual
* Create a virtual env
```bash
virtualenv .env
```

* Activate the virtual env
```bash
source .env/bin/activate
```

* Install all dependencies
```bash
pip install -r requirements.txt --upgrade
```

<details><summary>Update dependencies</summary>
<p>

```bash
pip3 freeze > requirements.txt
```
</p>
</details>

* Run the Bot
```
python bot.py
```
* follow the instructions on screen to activate the access to google calendar

## Built With
* [discord.py](https://github.com/Rapptz/discord.py) - API for discord
* [baseconvert](https://github.com/squdle/baseconvert) - Convert numbers
* [rapidfuzz](https://github.com/maxbachmann/rapidfuzz) - Search quotes
* [wolframalpha](https://github.com/jaraco/wolframalpha) - Python 3 wrapper for Wolfram|Alpha v2.0 API.
* [ftfy](https://github.com/LuminosoInsight/python-ftfy) - Fixes glitches in Unicode text.
* [deckofcards](https://deckofcardsapi.com/)

## Contribuitors
* [João Teixeira](https://github.com/jtexeira) - [say](Extensions/manage.py)
* [Pedro Mendes](https://github.com/mendess2526) - [media](bot.py)
* [Rodrigo Pimentel](https://github.com/RodrigoProjects/) - [EGPP](Extensions/programming.py)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
