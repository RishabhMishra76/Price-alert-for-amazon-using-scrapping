# Price-alert-for-amazon-using-scrapping
Alert for the low price of an amazon product using the beautifulsoup, requests and smtplib

## Beautifulsoup:
<p>Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.In our case we are parsing an HTML request so we used pre defied html.parser inside the beautifulsoup. </p>

## Request: 
<p>The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).</p>

## smtplib: 
<p>The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.</p>


## How to setup smtp session and send mail?

- Enable use of less secure apps from your google account https://myaccount.google.com/lesssecureapps
- Enable two step authentication in your google account https://www.google.com/landing/2step/
- Get the google password for the smtp session (google search google app password -> first link).
