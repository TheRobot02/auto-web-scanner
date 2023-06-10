#python 3.11


#------------[Imports]------------#
try:
    
    from components import scan_website, deep_scan_website, scan_download_links, download_files
except ModuleNotFoundError as e:
    print(f"main.py. {e}.\nExiting!")
    exit()
    

#------------[fariables]------------#
download_start_dir = "downloads"


#------------[main]------------#
if __name__ == "__main__":
    try:
        url = "https://filesamples.com" 
        url_list = scan_website(url)
        while True:
            menu = input("\nMake a deeper scan? (y/n): ")
            if menu == "y":
                deep_scan_website(url_list, url)
                break
            elif menu == "n":
                break
            else:
                print(f"{menu} is a invalid input.")
        download_list = scan_download_links(url_list)
        download_files(download_list, download_start_dir, url)


    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.\nExiting")
        exit()
