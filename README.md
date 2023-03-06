<div align="center">
  <p align="center"><h1>mc_scan</h1></p>
</div>


<div align="center">
  <img src="https://img.shields.io/github/issues/Besix2/mc_scan" alt="GitHub open issues">
  <img src="https://img.shields.io/github/last-commit/Besix2/mc_scan" alt="GitHub last commit">
  <img src="https://img.shields.io/github/commit-activity/m/Besix2/mc_scan" alt="GitHub commit activity">
  <img src="https://img.shields.io/github/stars/Besix2/mc_scan" alt="GitHub Repo stars">
</div>


### Installation

Clone the Repository
``` 
https://github.com/Besix2/mc_scan.git
```
Enter the mc_scan directoy
```
cd /mc_scan/container
```
Enter you discord token (explaination below)
```
nano config.txt
``` 
Start the container
```
docker-compose up
``` 
### discord bot 
To use the discord bot you have to create a application on discord.
To do this go to the [discord developer portal](https://discord.com/developers/applications). If you cant acces this you need to turn on developer mode in discord.

1. create the application
![Screenshot 2023-03-06 162437](https://user-images.githubusercontent.com/92743858/223155994-6d201d41-440b-402a-bfe9-580700755f63.png)

2. activate intents and copy the token
![Screenshot 2023-03-06 162753](https://user-images.githubusercontent.com/92743858/223156203-49067427-5301-4132-b377-f51f17c35663.png)

3. give the bot permissions and invite it
![Screenshot 2023-03-06 163106](https://user-images.githubusercontent.com/92743858/223156449-51e6d79f-548c-44fd-a2b7-045d547bb425.png)


### config
In the config.txt are 3 lines.  
The first one is the rate for masscan.  
The second is the wait time for masscan.  
The third one is your discord token.

Tweaking the values for masscan can lead to performance increase but it can also crash your internet. I suggest you check out [masscan](https://github.com/robertdavidgraham/masscan) github for more info.



### usage

Once the container is started you can check his logs using  
```
docker logs scanner
``` 

To shutdown the container(you need to be in /mc_scan/container)
```
docker-compose down
``` 

The entrys to the database can be manually viewed using mongo compass.
```
mongodb://<your-ip>:27017/
```

### How it works
This script scans the web for minecraft server in the range from 0.0.0.0/16 to 0.0.0.0/8.
If a server is found information is pulled asynchrous, using celery and rabbitmq as broker, with [mc_status](https://github.com/py-mine/mcstatus)
This information than gets saved to a mongodb database.
This database can be accesed using a Discord Bot which is written with [hikari-lightbulb](https://github.com/tandemdude/hikari-lightbulb).

### note

This is my first project of this size so if you have any suggestions just open a issue.
