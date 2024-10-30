#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable

# Initialize Redis connection
redis_client = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """Decorator to cache the HTML content of a URL."""
    @wraps(method)
    def wrapper(url: str) -> str:
        redis_client.incr(f'count:{url}')

        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode('utf-8')

        content = method(url)
        redis_client.setex(url, 10, content)
        return content
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL."""
    # return requests.get(url).text
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text


if __name__ == '__main__':
    # Test the get_page function
    test_url = "http://slowwly.robertomurray.co.uk\
    /delay/5000/url/http://example.com"

    print("Fetching page...")
    page_content = get_page(test_url)
    print("Page fetched!")

    # Access the URL again to test caching
    print("Fetching page again...")
    cached_content = get_page(test_url)
    print("Page fetched from cache!")

    # Display access count
    access_count = redis_client.get(f'count:{test_url}')
    print(f"The URL {test_url} was accessed {int(access_count)} times.")
