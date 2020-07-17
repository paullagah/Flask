# Gymnast Web Application 
###### by Paul Lagah
## Project Description
This project has been to build an application with **Create**, **Read**, **Update** and **Delete** functionality. 
The project is to make an application for the Gymnastics clubs to Monitor and manage Gymnast details.

_Requirements of the project are:_
* A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.
* A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
* Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board
* Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
* A functioning front-end website and integrated API's, using Flask.
Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine. 

## Functionality


This app will allow the users to:
* Add a Gymnast & Skill
* See all Gymnast & Skills on the home page, with option to search by ID
* Update a Gymnasts entry
* Delete a Gymnast from the database

## Technologies
Here is a list of technologies used :

| Required  | Used    |
|-----------|---------|
| Kanban Board |  Trello |
| Database |MYSQL|
| Programming |Python  |
| Front End | Flask/HTML |
| Version Control | Git |
| CI Server | Jenkins |
| Cloud Server | Google Cloud Platform (GCP) |

Python Modules used in the project were:
* Flask
* Jinja2
* Flask-SQLAlchemy
* SQLAlchemy
* pymysql
* WTForms
* Flask-WTF
* Flask-Bcrypt
* email_validator
* flask-login

## CI Pipeline
Below is my CI Pipeline Diagram with the technologies explained above:

![CI Pipeline](https://github.com/paullagah/DevOps/blob/master/CI_Pipeline.jpg)


## Data
The design of the data will be as follows in the Entity Relationship Diagram:

![ERD](https://github.com/paullagah/DevOps/blob/master/Entity%20Relationship%20Diagram.jpg)

This ERD is the final draft that was completed after consideration about how to 
design the database in the first instance.

The initial design was as seen below:

![OLD ERD](https://github.com/paullagah/DevOps/blob/master/ERD.jpg)

Changes were made to the design as the project went on, 
for security purposes only Coaches/Gymnastic Staff should be able to make changes to the gymnast entries.

This required a stand-alone table to be set for the Coaches as the implemented "Users" table that you can see above.

## Front-End Design
As the project went on the Front end design improved in comparison to my initial Wireframe design.

#### Wireframe Initial Design
![Initial Homepage](https://github.com/paullagah/DevOps/blob/master/WireframeHome.JPG)
![Initial Add](https://github.com/paullagah/DevOps/blob/master/WireframeAdd.JPG)
![Initial Update](https://github.com/paullagah/DevOps/blob/master/WireframeUpdate.JPG)
![Initial Search](https://github.com/paullagah/DevOps/blob/master/WireframeCheck.JPG)
![Initial Delete](https://github.com/paullagah/DevOps/blob/master/WireframeDelete.JPG)


#### Completed Design
![Final Homepage](https://github.com/paullagah/DevOps/blob/master/HomeLoggedOut.JPG)
![Final Registration Page](https://github.com/paullagah/DevOps/blob/master/registration.JPG)
![Final Login Page](https://github.com/paullagah/DevOps/blob/master/Login.JPG)
![Final Add Gymnast](https://github.com/paullagah/DevOps/blob/master/AddGymnast.JPG)
![Final Add Skill](https://github.com/paullagah/DevOps/blob/master/AddSkill.JPG)
![Final Update Gymnast](https://github.com/paullagah/DevOps/blob/master/UpdateGymnast.JPG)
![Final Update Skill](https://github.com/paullagah/DevOps/blob/master/UpdateSkill.JPG)
![Final Search Gymnast](https://github.com/paullagah/DevOps/blob/master/SearchGymnast.JPG)
![Final Search Skill](https://github.com/paullagah/DevOps/blob/master/SkillSearch.JPG)
![Final Delete Prompt](https://github.com/paullagah/DevOps/blob/master/DeletePrompt.JPG)
![Final About Page](https://github.com/paullagah/DevOps/blob/master/About.JPG)
