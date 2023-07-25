# Importing requests and urllib3 packages
import requests # python -m pip install requests
import urllib3
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Add json Content-Type Header variable
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Authentication credentials
username = 'Polycom' # username default:'admin', 'Polycom' or custom defined
password = '1234' # pin/passcode default: '456', '123', '789', '72227', or blank ''

def reboot():
    # Loop over subnets list
    for IPSubnet in ['10.30.2.', '10.30.4.']:
        try:
            for IPAddress in range(10, 254):
            #for IPAddress in ['.107', '.85', '.136', '.115']:
                try:

                    # Creating URL String with IPAddress
                    urlString = "https://{}{}/api/v1/mgmt/safeReboot".format(IPSubnet, IPAddress)

                    # New post request
                    #r = requests.post(urlString, headers=headers, verify=False, auth=(username, password))
                    s = requests.Session()

                    retries = Retry(total=0,
                                    backoff_factor=0,)
                    s.mount('https://', requests.adapters.HTTPAdapter(max_retries=retries))
                    s.post(urlString, headers=headers, verify=False, auth=(username, password), timeout=2)

                    # Do something with the response, depending on what it is
                    # print(r.text()) # Print Text response
                    print("Connected. Reboot phone IPAddress{}".format(IPAddress))

                    print(r.json()) # Print JSON response
                except Exception as err:
                    print("Error:{}{}".format(IPSubnet, IPAddress))
        except Exception as err:
            print("Error:{}{}".format(IPSubnet, IPAddress))

def main():
    subnet = input("Enter class C subnet Ex: 10.10.10.0: \n")
    print("You entered {}" .format(subnet))
    answer = input("Is that correct? Y or N\n")

    if (answer == 'Y' or answer == 'y'):
        print("Starting")
        reboot()
    else:
        return

if __name__ == "__main__":
    main()
