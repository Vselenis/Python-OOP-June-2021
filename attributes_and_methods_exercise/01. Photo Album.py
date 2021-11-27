import math


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE))

    def add_photo(self, label):
        for idx, page in enumerate(self.photos):
            if len(page) == self.MAX_PHOTOS_PER_PAGE:
                continue
            page.append(label)
            return f"{label} photo added successfully on page {idx+1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        pages = [('[] ' * len(page)).rstrip(" ") + '\n' for page in self.photos]
        delim = '-' * 11 + '\n'

        return delim + (delim).join(pages) + delim

