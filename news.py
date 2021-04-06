from selenium import webdriver # importing web driver for opening web browser
from selenium.webdriver.common.keys import Keys # The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
import datetime, time, os # importing all necessary environment like like date, time and operating system
import smtplib # Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon
from email.message import EmailMessage # Import the email modules we'll need to send file over internet by email

td = datetime.date.today()

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome(r'D:\Selenium\chromedriver.exe',options=CO) # providing location of chromiumdriver sftware installed in computer

print ("Connecting to Authentic News source, Please wait .....\n")
news_site = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en" # site from where data should be scraped

print (" ------------------------------------------------------------------------------------------- ")
print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  TODAY's TOP NEWS HEADLINES  <<<<<<<<<<<<<<<<<<<<<<<<<<<<< ")
print ("Date:",td.strftime("%b-%d-%Y"))
print (" -------------------------- ")

wd.get(news_site)
wd.implicitly_wait(wait_imp)

elems = wd.find_elements_by_tag_name('h3')

file_loc = r'D:\Selenium\newsfile.txt'
file_to_write = open(file_loc, 'w+')
ind = 1
for elem in elems:
    file_to_write.write(str(ind)+ '>> ')
    file_to_write.write(elem.text+'\n')
    print (str(ind) + ") " + elem.text)
    ind += 1
file_to_write.close()
print('\n')

# Get credentials from the system
USER_EMAIL = os.environ['']
MY_PASS = os.environ['']
MY_EMAIL = os.environ['']
  
# Compose message
msg = EmailMessage()
msg['From'] = MY_EMAIL
msg['To']   = USER_EMAIL
msg['Subject'] = " Hello ! Today's TOP news HEADLINES >>"

with open(file_loc,'rb') as f:
    N_file = f.read()

# Body of email  
msg.set_content("Find the attached document for detailed NEWS .. ")
msg.add_attachment(N_file, maintype = 'document',subtype = 'txt', filename = f.name )

# Configure server
server = smtplib.SMTP('smtp.gmail.com', 587) #tls , ssl
server.ehlo()
server.starttls()
server.ehlo()
server.login(MY_EMAIL,MY_PASS)
server.send_message(msg)

print ("A copy of this NEWS HEADLINES has been sent to your E-mail Successfully !!")
print ("Have a Nice Day !!")
server.quit()
