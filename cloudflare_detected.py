import requests

class CloudflareCheck:
    def __init__(self, url = 'https://github.com', timeout = 5):
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

            for headers in cloudflare_headers:
                if headers in response.headers:
                    return True
                
                return False

        except Exception as e:
            print("Error occurred:", e)
            return True
    
checker = CloudflareCheck()
cloudflare_detected = checker.check_website()

if cloudflare_detected:
    print("Cloudflare Is Used In This Website .")
else:
    print("Cloudflare Is Not Used In This Website ..")
