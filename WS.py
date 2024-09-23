import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict

def check_status(url : str) -> None:
    try:
        response: Response = requests.get(url)
        #Information
        status_code : int = response.status_code
        headers : CaseInsensitiveDict[str] = response.headers
        content_type : str = response.headers.get('Content-Type', 'Unknown')
        severs : str = response.headers.get('Server', 'Unknown')
        response_time : float = response.elapsed.total_seconds()

        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {severs}')
        print(f'Response Time: {response_time:.2f} Seconds')
    except RequestException as e:
        print(f'Error: {e}')

def main() -> None:
        url_to_check: str = input('Enter websites URL: ')
        check_status(url= url_to_check)

if __name__ == '__main__':
        main()
