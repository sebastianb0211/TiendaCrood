



class Category:

    category_id = None
    category_name = None

    def __init__(self, category_id, category_name):
        self._category_id = category_id
        self._category_name = category_name

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        self._category_name = category_name

    categories = {}

    def create_category(self):
        self._category_id = int(input("Id Categoria"))
        self._category_name = input("Nombre Categoria")
        self.categories[self._category_id] = {"Id": self._category_id, "Nombre": self._category_name}

    def listing_categories(self):
        for category in self.categories.items():
            print(category)



