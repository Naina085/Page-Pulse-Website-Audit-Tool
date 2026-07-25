import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def analyze_website(url):

    # Add https:// automatically
    if not url.startswith(("http://", "https://")):
        url = "https://" + url


    # -----------------------------
    # URL Validation
    # -----------------------------
    parsed = urlparse(url)

    if (
        not parsed.scheme
        or not parsed.netloc
        or "." not in parsed.netloc
    ):
        return {
            "status": "Invalid URL",
            "response_time": "--",
            "title": "--",
            "meta": "--",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0,
            "page_size": "--",
            "seo_score": 0
        }


    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/138 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }


    try:

        # -----------------------------
        # Website Request
        # -----------------------------

        start_time = time.time()

        response = requests.get(
            url,
            headers=headers,
            timeout=10,
            allow_redirects=True
        )

        response_time = round(
            (time.time() - start_time) * 1000
        )


        page_size = round(
            len(response.content) / 1024,
            2
        )


        content_type = response.headers.get(
            "Content-Type",
            ""
        )


        # -----------------------------
        # Non HTML Check
        # -----------------------------

        if "text/html" not in content_type:

            return {
                "status": response.status_code,
                "response_time": f"{response_time} ms",
                "title": "Non HTML Page",
                "meta": "Not Available",
                "h1_count": 0,
                "missing_alt": 0,
                "word_count": 0,
                "page_size": f"{page_size} KB",
                "seo_score": 0
            }



        # -----------------------------
        # BeautifulSoup Parsing
        # -----------------------------

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        # Title
        title = (
            soup.title.get_text(strip=True)
            if soup.title
            else "No Title"
        )


        # Meta Description

        meta_tag = soup.find(
            "meta",
            attrs={
                "name": "description"
            }
        )


        meta_description = (
            meta_tag.get("content").strip()
            if meta_tag and meta_tag.get("content")
            else "Not Found"
        )



        # H1 Count

        h1_count = len(
            soup.find_all("h1")
        )



        # Images without ALT

        images = soup.find_all("img")


        missing_alt = sum(
            1
            for img in images
            if not img.get("alt")
            or img.get("alt").strip() == ""
        )



        # Word Count

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        word_count = len(
            text.split()
        )



        # -----------------------------
        # SEO Score Calculation
        # -----------------------------

        seo_score = 0


        # Website accessible
        if response.status_code == 200:
            seo_score += 20


        # Title check
        if title != "No Title":
            seo_score += 20


        # Meta check
        if meta_description != "Not Found":
            seo_score += 20


        # H1 check
        if h1_count > 0:
            seo_score += 20


        # Image ALT check
        if len(images) == 0:
            seo_score += 20

        elif missing_alt == 0:
            seo_score += 20

        elif missing_alt <= len(images) * 0.2:
            seo_score += 10



        return {

            "status": response.status_code,

            "response_time":
                f"{response_time} ms",

            "title":
                title,

            "meta":
                meta_description,

            "h1_count":
                h1_count,

            "missing_alt":
                missing_alt,

            "word_count":
                word_count,

            "page_size":
                f"{page_size} KB",

            "seo_score":
                seo_score
        }



    # -----------------------------
    # Exception Handling
    # -----------------------------

    except requests.exceptions.Timeout:

        return {
            "status": "Timeout",
            "response_time": "--",
            "title": "--",
            "meta": "--",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0,
            "page_size": "--",
            "seo_score": 0
        }



    except requests.exceptions.SSLError:

        return {
            "status": "SSL Error",
            "response_time": "--",
            "title": "--",
            "meta": "--",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0,
            "page_size": "--",
            "seo_score": 0
        }



    except requests.exceptions.ConnectionError:

        return {
            "status": "Network Error",
            "response_time": "--",
            "title": "--",
            "meta": "--",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0,
            "page_size": "--",
            "seo_score": 0
        }



    except requests.exceptions.RequestException:

        return {
            "status": "Request Failed",
            "response_time": "--",
            "title": "--",
            "meta": "--",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0,
            "page_size": "--",
            "seo_score": 0
        }