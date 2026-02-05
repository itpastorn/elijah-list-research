"""
Fetch a single Elijah List page by ID and return the raw HTML.

This module intentionally does only one thing.
Scaling, retries, and parsing will be added later.
"""

from typing import Optional
import requests

BASE_URL = "https://www.elijahlist.com/words/display_word.html"


def fetch_word_html(word_id: int, timeout: int = 20) -> Optional[str]:
    """
    Fetch the raw HTML for a single Elijah List word.

    Args:
        word_id: Numeric Elijah List ID
        timeout: Request timeout in seconds

    Returns:
        HTML as string if successful, otherwise None
    """
    params = {"ID": word_id}

    try:
        response = requests.get(BASE_URL, params=params, timeout=timeout)
    except requests.RequestException as exc:
        print(f"[ERROR] Network error for ID={word_id}: {exc}")
        return None

    if response.status_code != 200:
        print(f"[WARN] ID={word_id} returned status {response.status_code}")
        return None

    return response.text


if __name__ == "__main__":
    # Manual smoke test
    test_id = 16950
    html = fetch_word_html(test_id)

    if html:
        print(f"[OK] Fetched ID={test_id}, {len(html)} bytes")
    else:
        print(f"[FAIL] Could not fetch ID={test_id}")
