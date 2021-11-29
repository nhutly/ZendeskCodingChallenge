1) I have built a ticket viewer with a browser-based UI. You can go to my heroku app (https://nhutticketviewer.herokuapp.com/request_ticket) to view all of my tickets I have on my accounts.
    .) Ticket viewer is connected to the Zendesk API
    .) Ticket viewer is able to request all the tickets for my account
    .) Ticket viewer is able to display all the tickets in a list
    .) The ticket viewer is not able to display individual ticket details yet
    .) The ticket viewer shows the tickets in sections, 25 of them each when more than 25 are returned

2) Problems I have encountered:
    i) Errors while trying to to import the test tickets. Main problem: the assignee ID field is read only and automatically assigned when create one, therefore I cannot manually edit each of the assignee ID for every tickets to match what assignee ID I currently have as it will cost a lot of time. Therefore I deleted the assignee ID field

    ii) I was not able to display individual ticket details and page through tickets due to time constraints

    iii) There was not unit tests available, and error handling since I have not finished the functioning requirements yet

** INSTRUCTION **

1) Download the zip file from github. To use the program, in the request_tickets.py, simply replace the <subdomain>, auth = <email address> <password> with your subdomain name, email address, and password.
2) Then go to your terminal (Mac) or cmd (Windows)
3) Navigate to project folder
4) Enter python3 request_tickets.py
5) Open a web browser, navigate to http://localhost:8080/request_ticket to see the output
6) Hit Ctrl-C in the terminal to stop the program
7) You then can go to https://github.com/chucknado/bottle_heroku_tutorial/blob/master/README.md for instruction how to deploy the app to the Heroku. then you can use the app on the browser.