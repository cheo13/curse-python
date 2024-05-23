import requests

def charge_dictionary(uri_dictionary):
    with open(uri_dictionary, 'r') as file:
        return [line.strip() for line in file]

def buzz(url, parameter, dictionary):
    for entry in dictionary:
        response = requests.get(url, params={parameter: entry})
        if response.status_code == 200:
            print(f"Response for '{entry}': {response.text}")
        else:
            print(f"Error fetching data for '{entry}': {response.status_code}")

def main():
    uri_dictionary = 'zip/john-the-ripper.txt'
    url = 'http://testphp.vulnweb.com/'
    parameter = 'word'

    dictionary = charge_dictionary(uri_dictionary)
    buzz(url, parameter, dictionary)

if __name__ == "__main__":
    main()
