
# Education platform for Pythoneers
[![Build Status](https://api.travis-ci.com/kacperstyslo/education-platform-for-pythoneers.svg?branch=master)](https://app.travis-ci.com/github/kacperstyslo/education-platform-for-pythoneers)

# Application link
http://educationplatformforpythoneers-env.eba-qm3mmjhw.us-east-1.elasticbeanstalk.com/

# Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Application view](#application-view)

## General info

<details>
    <summary>Click here to see general information about application!</summary>
        <br>
        With this application, a Python programmer can test his skills by performing increasingly difficult tasks. This application has been developed in django framework.
</details>

## Technologies

<details>
    <summary>Click here to see the technologies used!</summary>
        <ul>
            <li>Python 3.8.5</li>
            <li>Django 3.2.5</li>
            <li>Postgres 2.9.1</li>
            <li>Pytest 6.2.4</li>
            <li>Selenium==3.141.0</li>
            <li>Docker 20.10.7</li>
            <li>Docker-compose 1.29.2</li>
        </ul>
</details>

## Setup

<details>
    <summary>Click here to see how to run app!</summary>
    
    To run app localy (after running this command app will be available on: https:\\127.0.0.1:8000):
    docker-compose up --build -d; docker-compose ps --filter "status=running"
   
    To run tests:
    docker exec -it education-platform-for-pythoneers-app bash -c "python manage.py test"

</details>

## Application view

### Features in VERSION 1.4
https://user-images.githubusercontent.com/57534862/127873801-0ff454b1-30ba-497c-98db-70fcde75f1ed.mp4

### Ranking table view
![ranking_page](https://user-images.githubusercontent.com/57534862/127873815-9a0b868f-42a3-4c55-946d-3f0e6f50a70f.PNG)





