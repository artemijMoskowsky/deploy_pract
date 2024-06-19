from project.settings import DATABASE

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.Text, nullable = False)

    def __repr__(self):
        return f"name: {self.name}"