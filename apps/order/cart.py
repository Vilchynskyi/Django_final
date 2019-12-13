from ..core.models import Book


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, book, quantity=1, update_quantity=False):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0, 'price': str(book.main_price)}
        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def clear(self):
        del self.session['cart']
        self.session.modified = True

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book

        for item in self.cart.values():
            item['price'] = item['price']
            item['total_price'] = float(item['price']) * float(item['quantity'])
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
