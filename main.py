#python 3.11


#------------[Imports]------------#
try:
    
    from components import scan_website, deep_scan_website, scan_download_links, download_files
except ModuleNotFoundError as e:
    print(f"main.py. {e}.\nExiting!")
    exit()
    

#------------[variables]------------#
download_start_dir = "downloads"
url = "https://filesamples.com" 

#------------[main]------------#
if __name__ == "__main__":
    try:       
        scan_website(url)
        while True:
            menu = input("\nPerform a deep scan? (y/n): ")
            if menu == "y":
                deep_scan_website(url)
                break
            elif menu == "n":
                break
            else:
                print(f"{menu} is a invalid input.")
        download_list = scan_download_links()
        download_files(download_list, download_start_dir, url)


    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.\nExiting")
        exit()
