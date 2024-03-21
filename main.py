""" This program is designed to automatically fetch data pertaining to the most recent Boston Celtics game
and data pertaining to the most recent weather forcast. The data is then sent to a desired email address.
Manipulation of the computer's task scheduler can automatically run this program at a specific time per day. """

import smtplib  # Simple mail transfer protocol library, used to send and/or receive an email.
import requests  # Library used for webscraping.
import bs4  # Beautiful soup used for extracting particular CSS elements within the desired web page.
from email.message import EmailMessage  # Email package used to construct an email.


# The send function is used to 'send' and email. The email is how the Celtics & weather data will be transmitted.
def send(text):

    # Email address to send message to
    toEmail = 'enter email address'

    # A tuple that contains authorization information that will be passed into an SMTP object. The first element
    # in the tuple is the email address, and the second is an app password. The app password is a feature gmail offers
    # allows apps to sign in to accounts; it is an alternative to entering a personal password. For more on this,
    # refer to https://support.google.com/mail/answer/185833?hl=en. You can set the app password as an environment
    # variable so that it is not placed directly into the code.
    auth = (toEmail, '16-letter app password')

    # An SMTP object which defines the host (first parameter) and the port number in which the mail will be transferred.
    server = smtplib.SMTP("smtp.gmail.com", 587)

    # Refer to documentation on this method. TLS represents "transfer layer security" and acts to encrypt elements of
    # the SMTP message.
    server.starttls()

    # Login to server with authorization information
    server.login(auth[0], auth[1])

    # Construct email message
    msg = EmailMessage()
    msg['Subject'] = "Celtics Score & Weather"
    msg['From'] = server
    msg['To'] = toEmail
    msg.set_content(text)

    # Send the email
    server.send_message(msg)

    # Close the server
    server.quit()

# Try sending an email message
try:
    # Create message. This represents the body of the email that will be sent.
    message = ""

    # Get data from last Celtics game.
    bballWebsite = requests.get('https://www.basketball-reference.com/teams/BOS/2024.html')

    # The beautifulsoup constructor takes the desired website (converted into text) and the type of HTML parser.
    # For this project, the HTML parser is Python's built in 'html.parser'.
    # bs4 docs can be found here: https://beautiful-soup-4.readthedocs.io/en/latest/
    bballSoup = bs4.BeautifulSoup(bballWebsite.text, 'html.parser')

    # The fScoreRaw variable uses the 'select' method available to the newly created BeautifulSoup object.
    # This method is used to parse through the HTML tags of the desired website.
    # In this case, the project aims to extract the final score of the latest Celtics game.
    # The fScoreRaw variable represents the first location in which the final score of the last Celtics game
    # is extracted from the HTML text. However, extracting only the score will take additional cleaning.
    fScoreRaw = bballSoup.select('#info p')[3].select('a')
    fScoreRaw = str(fScoreRaw)

    # The firstIndex & lastIndex are used as variables to help extract the final score of the Celtics game.
    # The firstIndex represents the starting point of where the final score begins, and the lastIndex variable
    # represents the ending point of the final score.
    # This required analysis of the text comprising the fScoreRaw variable to determine what to use as a
    # parameter within the index function shown below.
    firstIndex = fScoreRaw.index('>') + 1
    lastIndex = fScoreRaw.index('</')

    # The scoreOppCombo variable represents a cleaned version of the final score. Note that, at this point,
    # the final score stored in the scoreOppCombo variable contains both (1) the final score and (2) the
    # name of the opponent (represented as a three letter code, e.g. - BOS = Boston Celtics).
    # The score variable extracts only the score from the scoreOppCombo variable.
    # The opponent variable extracts only the opponent info from the scoreOppCombo variable.
    scoreOppCombo = fScoreRaw[firstIndex:lastIndex].strip()
    score = scoreOppCombo[0:9]
    opponent = scoreOppCombo[-3:]

    # The website used in this program also provides information on the date of the next Celtics game and
    # who the opponent will be. This information should be included in the email that we want to send.
    # The nextOpp variable (a BeautifulSoup object) represents this information. The replace methods are used to
    # simplify the text a bit, so that blank spaces and new lines are removed.
    # An example of what the nextOpp variable would look like is "NextGame:Thursday,Mar.14vs.PHO"
    nextOpp = bballSoup.select('#info p')[4].text.replace(" ", "").replace("\n", "")

    # Note in the comments abbove that an example of what a nextOpp variable may look like is
    # "NextGame:Thursday,Mar.14vs.PHO". For home games, "vs." is used and for away games, "at" is used.
    # To handle this, a try-except block is used to determine which word is being used. The index of the "vs." or
    # "at" word will be stored in the atVsIndex variable.
    try:
        atVsIndex = nextOpp.index("at")
    except ValueError:
        atVsIndex = nextOpp.index("vs.")

    # The nextOppReformat variable is a reformatted version of the nextOpp variable
    nextOppReformat = nextOpp[0:4] + " Celtics " + nextOpp[4:9] + " " + \
                             nextOpp[9:nextOpp.index(",") + 1] + " " + \
                             nextOpp[nextOpp.index(",") + 1:atVsIndex] + " " + \
                             nextOpp[atVsIndex:atVsIndex + 2] + " " + \
                             nextOpp[-3:]

    # The message variable, which will be used to represent the main body of the email, is started by including the
    # Celtics info.
    message = "Last Celtics Game: " + score + " " + opponent + "\n" + nextOppReformat + "\n" + "\n" + \
              "Weather Info: " + "\n" + "\n"

    # Get Data for Weather ____________________________________________________________________________________________

    # Similar web scraping methods discussed above are used to extract weather data. One element of the code
    # below not discussed yet is the "find_all" method, which identifies specific html tags of the beautifulsoup
    # object and can narrow your search down further by passing in specific attribute information associated with
    # those html tags (see second parameter).
    weatherWebsite = requests.get(
        'https://forecast.weather.gov/MapClick.php?lat=42.1013&lon=-72.5893')
    weatherSoup = bs4.BeautifulSoup(weatherWebsite.text, 'html.parser')
    forecastLabel = list(weatherSoup.find_all("div", {"class": "col-sm-2 forecast-label"}))
    forecastText = list(weatherSoup.find_all("div", {"class": "col-sm-10 forecast-text"}))

    # Adding the weather information to the message variable
    for i in range(len(forecastText)):
        message = message + forecastLabel[i].text + ": " + forecastText[i].text + "\n" + "\n"

    # Send Message ____________________________________________________________________________________________________

    # Send the message!
    send(message)

# If an error is thrown trying to send an email message about the Celtics and local weather, an email will be sent
# containing details on the error that was thrown.
except Exception as e:
    message = str(e)
    send(message)
