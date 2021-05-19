import requests
from bs4 import BeautifulSoup

# > Get the 'Copy Link' from LinkedIn job posting in /Jobs
# > Retrieve the first href from the page.content to get link to job posting

URL = 'https://www.linkedin.com/jobs/view/2507865886/'  # Link to linkedin job posting
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
