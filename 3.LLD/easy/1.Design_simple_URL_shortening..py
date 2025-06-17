import random
import string


class UrlShortener:
    CODE_LENGTH = 6

    def __init__(self):
        self.long_to_short = {}
        self.short_to_long = {}

    def _generate_code(self):
        return "".join(
            random.choices(string.ascii_letters + string.digits, k=self.CODE_LENGTH)
        )

    def shorten(self, long_url):
        short_code = self._generate_code()
        while short_code in self.short_to_long:
            short_code = self._generate_code()

        self.short_to_long[short_code] = long_url
        self.long_to_short[long_url] = short_code
        return short_code

    def redirect(self, short_code):
        return self.short_to_long.get(short_code, "Error: Short URL does not exist")


# ✅ Example usage:
shortener = UrlShortener()

code1 = shortener.shorten("https://www.vimleshverma.com")
print("Shortened:", code1)
print("Original:", shortener.redirect(code1))

code2 = shortener.shorten("https://www.pagalworld.com")
print("Shortened:", code2)
print("Original:", shortener.redirect(code2))

print("Invalid code redirect:", shortener.redirect("xyz999"))  # Error handling
