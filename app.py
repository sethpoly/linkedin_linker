import requests
from bs4 import BeautifulSoup
import urllib.parse as urlparse
from urllib.parse import parse_qs


# > Get the 'Copy Link' from LinkedIn job posting in /Jobs
# > Retrieve the first href from the page.content to get link to job posting

# Returns corresponding job id from job URL
def get_job_id(url):
    parsed = urlparse.urlparse(url)
    return parse_qs(parsed.query)['currentJobId'][0]


URL = input('Paste a LinkedIn Job URL or type 'q' to exit: ')  # Link to linkedin job posting

# If user inputs non-direct link, check if it contains the jobID and build a valid URL
if 'currentJobId' in URL:
    print('Indirect URL found : parsing job id..')
    job_id = get_job_id(URL)
    URL = f'https://www.linkedin.com/jobs/view/{job_id}'
    print(f'New URL : {URL}')

# Make request to page
page = requests.get(URL)

# Set up beautiful soup object
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(id="main-content")
print(result.prettify())

# Get parent element containing comapny name and location
company_and_location = result.find('div', class_='sub-nav-cta__sub-text-container')

# Retrieve company name and location from parent element
company = company_and_location.find('a', class_='sub-nav-cta__optional-url')
location = company_and_location.select('span')[0].get_text(strip=True)

# Get parent element for job title
job_title_parent = result.find('h3', class_='sub-nav-cta__header')
job_title = job_title_parent.text

# Print parsed data
print(f'Job title: {job_title}')
print(f'Company : {company.text}')
print(f'Location : {location}')
