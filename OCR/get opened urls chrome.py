import psutil
import os
import time

def get_chrome_tab_urls():
    # Get a list of all running processes
    procs = psutil.process_iter()
    for proc in procs:
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            #print(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        else:
            # Check if the process is Google Chrome
            if pinfo['name'] == 'chrome.exe':
                # Get the command line arguments of the process
                cmdline = proc.cmdline()
                print(cmdline)
                # Find the URLs of all open tabs
                for arg in cmdline[1:]:
                    if arg.startswith('--'):
                        continue
                    if arg.startswith('http'):
                        print(arg)

# Call the function to get the URLs of all open tabs
get_chrome_tab_urls()
