import requests
import os
from bottle import redirect, route, template, request, static_file, run, response

@route('/')
def handle_root_url():
    redirect('/request_ticket')

@route('/home')
def handle_root_url():
    redirect('/request_ticket')

@route('/request_ticket')
def handle_root_url():
    # Set the request parameters
    url = 'https://<yoursubdomain>.zendesk.com/api/v2/tickets.json?page[size]=25'
    auth = '<eamil_address>', '<password>'

    stringsList = list()
    curticket = '\nStatus  ID    Subject\n' 
    count = 0
     
    
    while url:
         # Do the HTTP get request
        response = requests.get(url, auth=auth)

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        
        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        ticket_list = data['tickets']
        max = len(ticket_list)
        for ticket in ticket_list:
            strg =" "+ticket['status']+"    "+str(ticket['id'])+"   "+ticket['subject'] 
            curticket +="\n"+ strg+"\n"
                
        if data['meta']['has_more']:
            url = data['links']['next']
            stringsList.append(curticket+"\n")      
            curticket = '\nStatus  ID    Subject\n'  
            count = count + 1
            yield template('ticket_form',feedback = stringsList[count-1])
        else:
            url = None
            yield template('ticket_form',feedback = curticket)
        print(count)
        
    
    

@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)