import urllib.request
from myproject.myapp import views;
from myproject.myapp import templates;

def handle_button_click():
    url = "http://localhost:8000/signup/"  # Replace with the appropriate URL
    req = urllib.request.Request(url, method='POST')
     
handle_button_click()