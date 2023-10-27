from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.lb = Library("Test")

    def test_init(self):
        self.assertEqual("Test", self.lb.name)
        self.assertEqual({}, self.lb.books_by_authors)
        self.assertEqual({}, self.lb.readers)

    def test_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            Library('')
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_new_author(self):
        author = "Lucas"
        title = "Star wars"
        self.lb.books_by_authors = {}
        self.lb.add_book(author, title)
        self.assertEqual(1, len(self.lb.books_by_authors))


    def test_add_book_with_new_title(self):
        author = "Lucas"
        title = "Star wars one"
        self.lb.books_by_authors = {}
        self.lb.add_book(author, title)
        new_title = "Star wars two"
        self.lb.add_book(author, new_title)
        self.assertEqual(["Star wars one", "Star wars two"], self.lb.books_by_authors[author])

    def test_rent_book_new_name(self):
        name = "Grogu"
        self.lb.readers = {}
        self.lb.add_reader(name)
        self.assertEqual(1, len(self.lb.readers))

    def test_rent_book_already_reg(self):
        name = "Grogu"
        self.lb.readers = {}
        self.lb.add_reader(name)
        self.assertEqual(1, len(self.lb.readers))
        self.assertEqual("Grogu is already registered in the Test library.", self.lb.add_reader(name))

    def test_rent_book_no_reg_reader(self):
        reader_name = "Grogu"
        book_author = "Lucas"
        book_title = "Star wars"
        self.assertEqual(f"Grogu is not registered in the Test Library.",
                         self.lb.rent_book(reader_name, book_author, book_title))

    def test_rent_book_no_book_author(self):
        reader_name = "Grogu"
        book_author = "Lucas"
        book_title = "Star wars"
        self.lb.readers = {"Grogu": []}
        self.assertEqual(f"Test Library does not have any Lucas's books.",
                         self.lb.rent_book(reader_name, book_author, book_title))

    def test_rent_book_no_book_title(self):
        reader_name = "Grogu"
        book_author = "Lucas"
        book_title = "Star wars two"
        self.lb.readers = {"Grogu": []}
        self.lb.books_by_authors = {"Lucas": ["Star wars one"]}
        self.assertEqual(f"""Test Library does not have Lucas's "Star wars two".""",
                         self.lb.rent_book(reader_name, book_author, book_title))


    def test_rent_book_add_dict(self):
        reader_name = "Grogu"
        book_author = "Lucas"
        book_title = "Star wars one"
        self.lb.readers = {"Grogu": []}
        self.lb.books_by_authors = {"Lucas": ["Star wars one"]}
        self.lb.rent_book(reader_name, book_author, book_title)
        self.assertEqual({"Grogu": [{"Lucas": "Star wars one"}]}, self.lb.readers)
        self.assertEqual({'Lucas': []}, self.lb.books_by_authors)


    def test_rent_book_delete_book(self):
        reader_name = "Grogu"
        book_author = "Lucas"
        book_title = "Star wars one"
        self.lb.readers = {"Grogu": []}
        self.lb.books_by_authors = {"Lucas": ["Star wars one"]}
        self.lb.rent_book(reader_name, book_author, book_title)
        self.assertEqual({'Lucas': []}, self.lb.books_by_authors)


if __name__ == "__main__":
    main()
