# source venv/bin/activate
# Import required modules
from lxml import html
import requests

# Request the page
# capacity_filter=true => otevrene kurzy
# pokud neni nic volneho vypise to: Žádný termín kurzu s danými parametry nebyl nenalezen.
page = requests.get('https://www.hardtask.cz/ajax_course_classes.php?filter_course_id=576&filter_country_part_id=&filter_instructors=undefined&user_filtered=1&capacity_filter=true&lang=cze&module_id=7')

# Parsing the page
# (We need to use page.content rather than
# page.text because html.fromstring implicitly
# expects bytes as input.)
#print(page.content)

if 'Žádný termín kurzu s danými parametry nebyl nenalezen.' in page.text:
    print("není volný kurz")
else:
    print("je volny")
#tree = html.fromstring(page.content)


# Get element using XPath
#buyers = tree.xpath('/html/body/main/div/div/div/div[1]/div/div[1]/div[4]/div[1]/h2/text()')
#print(buyers)
