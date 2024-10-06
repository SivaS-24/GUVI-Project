import requests

url = "https://api.github.com/repos/pandas-dev/pandas/issues"

details = requests.get(url)

if details.status_code == 200:
    issues = details.json() 
    html_urls = [issue['html_url'] for issue in issues if 'html_url' in issue]

    for url in html_urls:
        print(url)
else:
    print(f"Error: {details.status_code}")
