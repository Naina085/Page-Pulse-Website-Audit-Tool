import time
import requests
from bs4 import BeautifulSoup


def analyze_website(url):

    # Add https:// automatically
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:

        start_time = time.time()

        response = requests.get(
            url,
            headers=headers,
            timeout=10,
            allow_redirects=True
        )

        response_time = round((time.time() - start_time) * 1000)

        content_type = response.headers.get("Content-Type", "")

        # Handle non-HTML pages
        if "text/html" not in content_type:
            return {
                "status": response.status_code,
                "response_time": f"{response_time} ms",
                "title": "Non-HTML Response",
                "meta": "Not Available",
                "h1_count": 0,
                "missing_alt": 0,
                "word_count": 0
            }

        soup = BeautifulSoup(response.text, "html.parser")

        # Title
        title = soup.title.get_text(strip=True) if soup.title else "No Title"

        # Meta Description
        meta_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta_tag.get("content").strip()
            if meta_tag and meta_tag.get("content")
            else "Not Found"
        )

        # H1 Count
        h1_count = len(soup.find_all("h1"))

        # Images Missing ALT
        images = soup.find_all("img")
        missing_alt = sum(
            1 for img in images
            if not img.get("alt") or img.get("alt").strip() == ""
        )

        # Word Count
        text = soup.get_text(separator=" ", strip=True)
        word_count = len(text.split())

        return {
            "status": response.status_code,
            "response_time": f"{response_time} ms",
            "title": title,
            "meta": meta_description,
            "h1_count": h1_count,
            "missing_alt": missing_alt,
            "word_count": word_count
        }

    except requests.exceptions.Timeout:
        return {
            "status": "Timeout",
            "response_time": "--",
            "title": "Request Timed Out",
            "meta": "--",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0
        }

    except requests.exceptions.InvalidURL:
        return {
            "status": "Invalid URL",
            "response_time": "--",
            "title": "--",
            "meta": "--",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "Error",
            "response_time": "--",
            "title": "Unable to Analyze",
            "meta": "--",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0,
            "error": str(e)
        }