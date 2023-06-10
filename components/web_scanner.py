#------------[Imports]------------#
try:
    import requests
    from bs4 import BeautifulSoup
except ModuleNotFoundError as e:
    print(f"webscraper.py. {e}.\nExiting!")
    exit()


#------------[fariables]------------#
link_list = []
deep_link_list = []
dowload_list = []
file_extensions = ['csv', 'doc', 'docx', 'pdf', 'xls', 'xlsx', 'csv','png','jpg', 'txt', 'zip' ,'rar']

#------------[scan website]------------#
def scan_website(url):
    print("starting webscan...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links_list = soup.find_all('a', href=True)
    for link in links_list:
        if link['href'] not in link_list and url in link['href']:
            print(f"Link found: {link['href']}")
            link_list.append(link['href'])
    print(f"{len(link_list)} links have been found")
    return link_list

#------------[deep scan website]------------#
def deep_scan_website(url_list, origin_url):
    print("\nstarting deep webscan...")
    while True:
        for url in url_list:
            if "javascript" in str(url):
                pass
            else:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                links_list = soup.find_all('a', href=True)
                for link in links_list:
                    if link['href'] not in link_list and origin_url in link['href']:
                        print(f"Deep link found: {link['href']}")
                        deep_link_list.append(link['href'])
                        url_list.append(link['href'])
                    else:
                        pass
        print(f"{len(deep_link_list)} deep links have been found")
        return deep_link_list

#------------[scan for download links]------------# 
def scan_download_links(url_list):
    print("\nstarting download link scan...")
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links_list = soup.find_all('a', href=True, download=True)
        for link in links_list:
            if link['href'] not in dowload_list and any(link['href'].endswith(extension) for extension in file_extensions):
                print(f"download link found: {link['href']}")
                dowload_list.append(link['href'])
    print(f"{len(dowload_list)} links have been found")
    return dowload_list