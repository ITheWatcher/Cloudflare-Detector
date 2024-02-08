# Cloudflare Detection Script

## Overview

This Python script is designed to check whether a given website is using Cloudflare for its web hosting or as a content delivery network (CDN). It examines the response headers from the website to determine if Cloudflare-related headers are present.

## Usage

1. **Installation**: Ensure you have Python installed on your system.

2. **Clone the Repository**: Clone or download the repository containing the script to your local machine.
    ```bash
    git clone https://github.com/ITheWatcher/Cloudflare-Detector.git
    cd Cloudflare-Detector
    ```
3. **Run the Script**: Execute the script by running the following command in your terminal:

    ```bash
    python cloudflare_detected.py
    ```

4. **Provide Website URL (Optional)**: If you want to check a specific website other than the default (`https://github.com`), you can modify the `url` variable in the script.

5. **View Output**: The script will output whether Cloudflare is detected for the provided website or not.

## Functionality

The script utilizes the `requests` library to fetch the website's URL and examines the response headers for typical Cloudflare indicators, such as "Server", "CF-RAY", "CF-Cache-Status", and "CF-Request-ID". If any of these headers are present, the script concludes that Cloudflare is being used.

## File Structure

- `cloudflare_detected.py`: The Python script for detecting Cloudflare usage.
- `README.md`: This README file providing an overview of the script and instructions for usage.

## Dependencies

- Python 3.x
- `requests` library (can be installed via pip)
- ```bash
    pip install requests
    ```

## Notes

- If the website is behind Cloudflare but doesn't expose Cloudflare-related headers, the script may not detect its usage accurately.
