import requests
from bs4 import BeautifulSoup

URL = 'https://www.linkedin.com/jobs/view/software-engineer-remote-at-groupgreeting-2412543282/'
page = requests.get(URL)

# Get the 'Copy Link' from LinkedIn job posting in /Jobs

# Retrieve the first href from the page.content to get link to job posting

# Job Title : unify-apply-page__job-title
# Company Name : unify-apply-page__company-name-location
print(page.content)

