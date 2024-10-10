from typing import List


class OrderStatus:
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order:
    def __init__(self, order_id: int, items: List[str], total_price: float):
        self.order_id = order_id
        self.items = items
        self.total_price = total_price
        self.status = OrderStatus.PENDING

    def add_item(self, item: str, price: float):
        self.items.append(item)
        self.total_price += price

    def remove_item(self, item: str, price: float):
        if item in self.items:
            self.items.remove(item)
            self.total_price -= price

    def mark_as_shipped(self):
        if self.status != OrderStatus.PENDING:
            raise ValueError("Order cannot be shipped unless it's in pending status")
        self.status = OrderStatus.SHIPPED

    def cancel(self):
        if self.status == OrderStatus.DELIVERED:
            raise ValueError("Delivered orders cannot be canceled")
        self.status = OrderStatus.CANCELLED
