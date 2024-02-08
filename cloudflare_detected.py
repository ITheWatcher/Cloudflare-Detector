import requests

class CloudflareCheck:
    def __init__(self, url='https://example.com', timeout=5):
        self.url = url
        self.timeout = timeout

    def check_website(self):
        try:
            response = requests.get(self.url, timeout=self.timeout)
            
            cloudflare_headers = [
                'Server',
                'CF-RAY',
                'CF-Cache-Status',
                'CF-Request-ID'
            ]

            for header in cloudflare_headers:
                if header in response.headers:
                    if 'cloudflare' in response.headers[header].lower():
                        return True
                
            return False

        except Exception as e:
            print("Error occurred:", e)
            return False
    
if __name__ == '__main__':
    while True:
        user_input = input("Enter The Website URL (e.g., https://example.com): ").strip()
        checker = CloudflareCheck(url=user_input)
        cloudflare_detected = checker.check_website()
        if cloudflare_detected:
            print("Cloudflare Is Used In This Website.")
        else:
            print("Cloudflare Is Not Used In This Website.")
        
        choice = input("Do You Want To Check Another Website? (Y/N): ").strip().lower()
        if choice != 'y':
            break
