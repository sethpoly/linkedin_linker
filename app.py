import requests
from bs4 import BeautifulSoup

# > Get the 'Copy Link' from LinkedIn job posting in /Jobs
# > Retrieve the first href from the page.content to get link to job posting

URL = 'https://www.linkedin.com/jobs/view/2507865886/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find(id="main-content")
print(result.prettify())

# Find parent class for company name and location
company_and_location = result.find('p',
                                   class_='unify-apply-page__company-name-location')

# Retrieve the company name and location
company_name = company_and_location.select('p > span')[0].get_text(strip=True)
location = company_and_location.select('p > span')[1].get_text(strip=True)

print(f'Company: {company_name}')
print(f'Location: {location}')

# Job Title : unify-apply-page__job-title
# Company Name : unify-apply-page__company-name-location
