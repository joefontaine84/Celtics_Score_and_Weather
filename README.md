<h1>Overview</h1>
<p>This is a program that is designed to (1) scrape the web for the latest Boston Celtics score, (2) scrape the web for the latest local weather information, and (3) send this information to a desired email address in a formatted way. 
  The libraries utilized for this project were <ol><li>smtplib;</li><li>requests;</li><li>bs4 (beatiful soup); and </li> <li>email.</li></ol>Refer to the detailed comments in the code
(the main.py file) for more information on the methodology on how this was done. </p>

<h2>Notes on Task Scheduler</h2>
<p>The primary challenge with this project was setting up the Windows operating system Task Scheduler. The Task Scheduler is the program which allows the user to manipulate when programs run.
For this project, the goal is to have the program run at 7:00 AM every day.</p>
<p>When you first open up the Task Scheduler, you can create a task. The "task" is a program, in this case. The first tab of creating a task is the "general" tab, as shown below:</p>
<img src="https://github.com/joefontaine84/Celtics_Score_and_Weather/blob/master/Images/General_Tab.png" alt="The general tab of a Task in the Task Scheduler GUI">
<p>Note the buttons that are selected above. The program should be able to run regardless of whether a user is logged in and should run with the highest privlidges.</p>
<p>The next tab in the Task Scheduler is the "triggers" tab, as shown below</p>
<img src=""https://github.com/joefontaine84/Celtics_Score_and_Weather/blob/master/Images/Triggers_Tab.png" alt="The triggers tab of a Task in the Task Scheduler GUI">
