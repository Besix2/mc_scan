<div align="center">
  <p align="center"><h1>mc_scan</h1></p>
</div>


<div align="center">
  <img src="https://img.shields.io/bitbucket/issues/Besix2/mc_scan" alt="Bitbucket open issues">
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
Start the container
```
docker-compose up
``` 

### usage

Once the container is started you can check his logs using  
```
docker logs scanner
``` 

To shutdown the container(you need to be in /mc_scan/container)
```
docker-compose down
``` 

The entrys to the database can be viewed using mongo compass.
```
mongodb://<your-ip>:27017/
```

### How it works
This script scans the web for minecraft server in the range from 0.0.0.0/16 to 0.0.0.0/8.
If a server is found information is pulled asynchrous, using celery and rabbitmq as broker, with [mc_status](https://github.com/py-mine/mcstatus)
This information than gets saved to a mongodb database.
This database can be accesed using a Discord Bot which is written with [hikari-lightbulb](https://github.com/tandemdude/hikari-lightbulb).

### To-do
Add explanation for Discord bot  
Fix typos
