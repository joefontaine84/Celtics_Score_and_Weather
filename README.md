<h1>Overview</h1>
<p>This is a program that is designed to (1) scrape the web for the latest Boston Celtics score, (2) scrape the web for the latest local weather information, and (3) send this information to a desired email address in a formatted way. 
  The libraries utilized for this project were <ol><li>smtplib;</li><li>requests;</li><li>bs4 (beatiful soup); and </li> <li>email.</li></ol>Refer to the detailed comments in the code
(the main.py file) for more information on the methodology on how this was done. </p>

<h2>Notes on Task Scheduler</h2>
<p>The primary challenge with this project was setting up the Windows operating system Task Scheduler. The Task Scheduler is the program which allows the user to manipulate when programs run.
For this project, the goal is to have the program run at 7:00 AM every day.</p>
<p>When you first open up the Task Scheduler, you can create a task. The "task" is a program, in this case. The first tab of creating a task is the "general" tab, as shown below:</p>
<img src="https://github.com/joefontaine84/Celtics_Score_and_Weather/blob/master/Images/General_Tab.png" alt="The general tab of a Task in the Task Scheduler GUI">
<p>Note the buttons that are selected above. The program should be able to run regardless of whether a user is logged in and should run with the highest privileges.</p>
<p>The next tab in the Task Scheduler is the "triggers" tab, as shown below:</p>
<img src="https://github.com/joefontaine84/Celtics_Score_and_Weather/blob/master/Images/Triggers_Tab.png" alt="The triggers tab of a Task in the Task Scheduler GUI">
<p>The triggers tab is where you define the time and frequency in which you would like your task to run.</p>
<p>The next tab in the Task Scheduler is the "actions" tab, shown below:</p>
<img src="https://github.com/joefontaine84/Celtics_Score_and_Weather/blob/master/Images/Actions_Tab.png" alt="The triggers tab of a Task in the Task Scheduler GUI">
<p>The actions tab, in this case, tells the Task Scheduler to "start a program" (see drop down menu selection at the top). The actions tab also allows the user to input the following options for the program to run appropriately:
<ul><li>The location of the python interpreter that will be used to execute the program;</li>
<li>The "start in" option, which is essentially what directory the python interpreter should "start in" to locate the program of choice; and</li>
  <li>The arguments that should be passed into the python interpreter once the interpreter has been selected and the directory (start in location) has been selected.</li>
</ul></p>
<p>If non-standard python libraries are used for a project, such as bs4, I found that I had to use the python interpreter associated with the project created within the IDE used to code, since this will have access to all libraries used for the project.
Trying to use the built-in interpreter on my computer wasn't working because it did not have access to all the necessary python libraries (e.g., bs4). Perhaps a way to get around this, if you wanted to use the python interpreter on your computer rather than a project specific version (associated with your IDE), is to download all necessary libraries for the built-in intepreter to use and place them in a location where they can be accessed. Ultimately, for this project, the "program/script" is the file location of the python interpreter (python.exe file) assocatied with the IDE used to code the program. </p>
<p>The "start in" option is the folder location in which the program file (e.g., main.py) is held. The argument option is the name of the program file that should be run.</p>
<p>The "conditions" and "settings" tabs are self explanatory and relate to how the program, or task, should be handled while considering various conditions. Images of these tabs are shown below: </p>
<img src="https://github.com/joefontaine84/Celtics_Score_and_Weather/blob/master/Images/Conditions_Tab.png" alt="The conditions tab of a Task in the Task Scheduler GUI">
<img src="https://github.com/joefontaine84/Celtics_Score_and_Weather/blob/master/Images/Settings_Tab.png" alt="The settings tab of a Task in the Task Scheduler GUI">
