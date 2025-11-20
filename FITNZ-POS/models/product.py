# File: FITNZ/models/product.py

class Product:
    """Represents a single product in the store's inventory."""
    def _init_(self, product_id: str, name: str, price: float, stock: int, description: str = ""):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description # <-- NEW

    def update_stock(self, quantity: int):
        """Updates the stock level. Can be positive (adding stock) or negative (selling)."""
        if self.stock + quantity >= 0:
            self.stock += quantity
        else:
            print(f"Error: Not enough stock for {self.name}.")

    def _str_(self):
        """String representation for easy display."""
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"

