# The Oppenheimer Project 
As part of the policy to increase taxation relief to its working class hero affected by the Novel Coronavirus Infection, the governer of the City of Carson has called for an immediate a cut to all IT services budget. This includes terminating **all** applications hosted on cloud providers, include the one which you were tasked to work on.

Fear not... The development team has provided you with the Dev environment in the form of a `jar` file to assist you on your task.

## To proceed further:

##### 1. Download and clone this repository to your desktop. You may also choose to download the jar `OppenheimerProjectDev.jar`  
##### 2. To run the application, issue the following to your terminal. Replace `{path-to-this-jar}` with your actual path to the folder containing the jar 
```
java -jar {path-to-this-jar}/OppenheimerProjectDev.jar
```

##### 3. Give it a min or two to boot up and you should be able to visit the app and API interface here:
```
http://localhost:8080/
http://localhost:8080/swagger-ui.html
```

##### 4. Good luck and have fun

_Note that should you encounter any problems or have any questions, please do not hesitate to contact us for assistance =)_ 


Prerequisites
Git must be installed on the system where the Robot Framework scripts will be executed.
Robot Framework must be installed on the system where the Robot Framework scripts will be executed.
Steps
Clone the Git repository containing the Robot Framework scripts to a local directory on the system where the scripts will be executed.

git clone <repository-url>

Navigate to the directory where the Robot Framework scripts are located.

cd <repository-directory>

Execute the Robot Framework scripts using the following command:

robot <test-suite-file>

Replace <test-suite-file> with the name of the Robot Framework test suite file to be executed. This file must have a .robot extension.
Optionally, you can specify additional arguments to the robot command. For example, to run the tests in verbose mode, use the --verbose argument: robot --verbose <test-suite-file>
After the execution of the Robot Framework tests, a report file and a log file will be generated. These files will be located in the same directory where the test suite file is located.

The report file will have a .html extension and can be opened in a web browser to view the test results.
The log file will have a .log extension and can be used to debug any issues that occurred during the test execution.
  
### What is Robot Framework? ###

Robot framework is a python based, open source test automation framework with great extensibility. Robot framework is cross platform and will run on Mac, Linux and Windows. 

See [here ](https://robotframework.org/)for Robot Framework home page


### What exactly is this? ###

A basic Robot Framework API test suite with the following tests:

* 001_Post_Insert_Single_Record
* 002_Post_Insert_Multiple_Record
* 003_Upload_CSV_File
* 004_AC1_AC2_GET_TaxReliefCalculation
* 004_AC3_AC4_AC5_AC6_TaxReliefCalculation
* 005_dispense_tax_relief

The following supporting librarys are used in this suite alongside some of the built in librarys...

[BrowserLibrary](https://github.com/MarketSquare/robotframework-browser)

[RequestsLibrary](https://github.com/bulkan/robotframework-requests)
  
[DataDriver](https://github.com/Snooz82/robotframework-datadriver)



### How do I get set up? ###

* Install [Python 3](https://python.org/)
* Clone or download this repository
* Using the command line navigate in to the project folder and execute the command ```pip install -r requirements.txt``` this will install robot framework and the required supporting library's and their dependencies

Once everything has been installed you can run the test suite from the command line in the projects folder with the command```robot testscripts
``` 



### Who do I talk to? ###

* Yogesh Pawar - [LinkedIn](https://www.linkedin.com/in/yogesh-pawar-73a99856/)
