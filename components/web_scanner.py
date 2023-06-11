#------------[Imports]------------#
try:
    import requests
    from bs4 import BeautifulSoup
except ModuleNotFoundError as e:
    print(f"webscraper.py. {e}.\nExiting!")
    exit()


#------------[variables]------------#
link_list = []
download_list = []
deep_link_counter = 0
file_extensions = ['csv', 'doc', 'docx', 'pdf', 'xls', 'xlsx', 'csv','png','jpg', 'txt', 'zip' ,'rar']

#------------[scan website]------------#
def scan_website(url):
    print("starting webscan...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    found_link_list = soup.find_all('a', href=True)
    for link in found_link_list:
        if link['href'] not in link_list and url in link['href']:
            print(f"Link found: {link['href']}")
            link_list.append(link['href'])
        else:
            pass
    print(f"{len(link_list)} links have been found")
    pass

#------------[deep scan website]------------#
def deep_scan_website(url):
    print("\nstarting deep scan...")
    global deep_link_counter
    for link in link_list:
        if "javascript" in str(link):
            pass
        else:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            found_link_list = soup.find_all('a', href=True)
            
            for found_link in found_link_list:
                if found_link['href'] not in link_list and url in found_link['href']:
                    print(f"Deep link found: {found_link['href']}")
                    deep_link_counter += 1
                    link_list.append(found_link['href'])
                else:
                    pass
    print(f"{deep_link_counter} deep links have been found")
    pass

#------------[scan for download links]------------# 
def scan_download_links():
    print("\nstarting download link scan...")
    for link in link_list:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        found_link_list = soup.find_all('a', href=True, download=True)
        for found_link in found_link_list:
            if "javascript" in str(found_link):
                pass
            elif found_link['href'] not in download_list and any(found_link['href'].endswith(extension) for extension in file_extensions):
                print(f"download link found: {found_link['href']}")
                download_list.append(found_link['href'])
    print(f"{len(download_list)} links have been found")
    return download_list