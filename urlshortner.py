import hashlib

class URLShortener:
    def __init__(self):
        self.url_to_short = {}
        self.short_to_url = {}

    def shorten_url(self, original_url):
        if original_url in self.url_to_short:
            return self.url_to_short[original_url]

        # Hash the original URL to create a unique short key
        hash_object = hashlib.md5(original_url.encode())
        short_key = hash_object.hexdigest()[:6]

        # Store the mapping in both dictionaries
        self.url_to_short[original_url] = short_key
        self.short_to_url[short_key] = original_url

        return short_key

    def expand_url(self, short_key):
        if short_key in self.short_to_url:
            return self.short_to_url[short_key]
        else:
            return "Short URL not found."

# Example usage
shortener = URLShortener()

original_url = "https://www.example.com"
short_key = shortener.shorten_url(original_url)
print("Shortened URL:", short_key)

expanded_url = shortener.expand_url(short_key)
print("Expanded URL:", expanded_url)
