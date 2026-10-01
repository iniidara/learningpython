# Order Tracker — OOP Practice

*Modeled on MIT 6.100L Lecture 20 (Fitness Tracker OOP example). Same concepts, different domain — work through each section, do the "You Try It" exercises yourself before checking the answers at the bottom.*

---

## 1. Implementing vs. Using a Class (Recap)

| Implementing the class | Using the class |
|---|---|
| Define the class | Create instances |
| Define data attributes (WHAT IS the object) | Do operations with instances |
| Define methods (HOW TO use the object) | |

Class abstractly captures **common** properties and behaviors. Instances have **specific values** for attributes.

---

## 2. The Scenario: Order Tracker

Suppose you're building the order-tracking piece of a food/grocery delivery app (sound familiar?). Different kinds of orders share some properties but have their own specifics:

**Common properties (every order has these):**
- Order ID
- Customer name
- Timestamp placed
- Status (`placed`, `preparing`, `out for delivery`, `delivered`)
- Total price

**FoodOrder specific:**
- Restaurant name
- Estimated prep time (minutes)
- Number of items

**GroceryOrder specific:**
- Store name
- Total weight (kg)
- Delivery fee (calculated from weight)

This maps to a class hierarchy: `Order` (parent) → `FoodOrder`, `GroceryOrder` (children).

---

## 3. Define a Simple Class

```python
class Order(object):
    def __init__(self, order_id, customer, total):
        self.order_id = order_id
        self.customer = customer
        self.total = total
        self.status = 'placed'
        self.kind = 'Order'

my_order = Order(1001, 'Iniidara', 4500)
```

---

## 4. Getter and Setter Methods

```python
class Order(object):
    def __init__(self, order_id, customer, total):
        self.order_id = order_id
        self.customer = customer
        self.total = total
        self.status = 'placed'
        self.kind = 'Order'

    def get_total(self):
        return self.total

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def set_total(self, total):
        self.total = total
```

Access attributes via getters/setters, not directly — `my_order.get_total()` rather than `my_order.total`. This is "information hiding": it lets you change the internal implementation later without breaking code that uses the class.

---

## 5. Changing the Class Implementation (Class Variables)

Suppose the business adds a flat **service fee** applied to every order, unless a custom fee was set at creation.

```python
class Order:
    service_fee = 200  # class variable — shared by all instances

    def __init__(self, order_id, customer, subtotal, fee=None):
        self.order_id = order_id
        self.customer = customer
        self.subtotal = subtotal
        self.fee = fee  # may be None
        self.status = 'placed'
        self.kind = 'Order'

    def get_total(self):
        if self.fee is None:
            return self.subtotal + Order.service_fee
        else:
            return self.subtotal + self.fee
```

**Warning:** if you change a class variable through an instance's *class* (e.g. `Order.service_fee = 300`), it changes for **every** instance of `Order`, including ones already created.

### You Try It #1
Write lines of code to create two `Order` objects:
- `o_one`: order_id `2001`, customer `"Moses"`, subtotal `3000`, no custom fee. Print its total.
- `o_two`: order_id `2002`, customer `"Oge"`, subtotal `5000`, custom fee `100`. Print its total.

*(Answer at the bottom.)*

---

## 6. Class Hierarchies

```
                Order
               /      \
        FoodOrder    GroceryOrder
```

- **Parent class** (superclass): `Order`
- **Child class** (subclass): `FoodOrder`, `GroceryOrder`
  - Inherits all data and behaviors of the parent
  - Can add more info
  - Can add more behavior
  - Can override behavior

---

## 7. Inheritance: Subclass

```python
class FoodOrder(Order):
    def __init__(self, order_id, customer, subtotal, restaurant, prep_time=20, fee=None):
        super().__init__(order_id, customer, subtotal, fee)
        self.restaurant = restaurant
        self.prep_time = prep_time
        self.kind = 'FoodOrder'

    def get_prep_time(self):
        return self.prep_time

    def set_prep_time(self, minutes):
        self.prep_time = minutes
```

`super().__init__(...)` calls the parent's constructor so you don't have to re-write the logic for `order_id`, `customer`, `subtotal`, `fee`, and `status`. Then `FoodOrder` adds its own attributes (`restaurant`, `prep_time`) and its own methods.

---

## 8. Why Use Inheritance?

- **Clarity** — commonalities live in the parent, differences live in the subclass
- **Reuse** — write the shared logic once
- **Modularity** — a `FoodOrder` can be passed anywhere an `Order` is expected

---

## 9. Subclasses Reuse Parent Code

```python
class Order(object):
    ...
    def __str__(self):
        width = 24
        retstr = f"|{'-'*width}|\n"
        retstr += f"| Order #{self.order_id}{' '*(width-11-len(str(self.order_id)))}|\n"
        retstr += f"| {self.kind}{' '*(width-len(self.kind)-1)}|\n"
        retstr += f"| Status: {self.status}{' '*(width-9-len(self.status))}|\n"
        total_str = f"{self.get_total()}"
        retstr += f"| Total: {total_str} NGN{' '*(width-13-len(total_str))}|\n"
        retstr += f"|{'-'*width}|\n"
        return retstr
```

Every subclass (`FoodOrder`, `GroceryOrder`) can use this same `__str__` method without redefining it — it reads `self.kind`, `self.status`, and calls `self.get_total()`, which resolve correctly depending on the actual instance type.

---

## 10. Where Can I Use an Instance of a Class?

You can use a `FoodOrder` instance anywhere an `Order` is expected. The reverse isn't true.

```python
def total_revenue(orders):
    total = 0
    for o in orders:
        total += o.get_total()
    return total

def total_prep_time(food_orders):
    total = 0
    for f in food_orders:
        total += f.get_prep_time()
    return total
```

`total_revenue` works on a mixed list of `Order`, `FoodOrder`, and `GroceryOrder` objects. `total_prep_time` only works on `FoodOrder` objects, since `get_prep_time` doesn't exist on plain `Order`.

### You Try It #2
For each line below, what does `get_total()` return, and (where applicable) `get_prep_time()`?

```python
o1 = Order(3001, 'Onemen', 2000)
o2 = Order(3002, 'Onemen', 2000, fee=50)
f1 = FoodOrder(3003, 'Onemen', 2000, 'Mama Put', prep_time=15)
f2 = FoodOrder(3004, 'Onemen', 2000, 'Mama Put', prep_time=15, fee=80)
f3 = FoodOrder(3005, 'Onemen', 2000, 'Mama Put')
```

*(Answer at the bottom.)*

---

## 11. Overriding a Superclass Method

`GroceryOrder` calculates its total differently: a delivery fee based on weight instead of the flat service fee.

```python
class GroceryOrder(Order):
    fee_per_kg = 50

    def __init__(self, order_id, customer, subtotal, store, weight_kg):
        super().__init__(order_id, customer, subtotal)
        self.store = store
        self.weight_kg = weight_kg
        self.kind = 'GroceryOrder'

    def get_total(self):
        if self.weight_kg is not None:
            delivery_fee = self.weight_kg * GroceryOrder.fee_per_kg
            return self.subtotal + delivery_fee
        else:
            return super().get_total()
```

`get_total()` here **overrides** the parent's version. If `weight_kg` isn't set, it falls back to the parent's logic via `super().get_total()`.

---

## 12. Which Method Gets Called?

For an instance of a class, Python looks for the method name in the **current class definition** first. If not found, it looks **up the hierarchy** (parent, then grandparent, etc.) and uses the first one it finds.

So `grocery_order.get_total()` uses `GroceryOrder`'s version; `food_order.get_total()` (which doesn't define its own) falls back to `Order`'s version.

---

## 13. Testing Equality with Subclasses

```python
class Order(object):
    ...
    def __eq__(self, other):
        return type(self) == type(other) and \
               self.order_id == other.order_id and \
               self.customer == other.customer and \
               self.kind == other.kind and \
               self.get_total() == other.get_total()

class FoodOrder(Order):
    ...
    def __eq__(self, other):
        return super().__eq__(other) and self.restaurant == other.restaurant
```

`FoodOrder.__eq__` reuses `Order.__eq__` via `super()` and then checks its own extra attribute.

---

## 14. Object-Oriented Design: More Art Than Science

OOP is a powerful tool for modularizing code and grouping state with behavior — but it's possible to overdo it. Don't build an elaborate class hierarchy just because you can; ask whether the structure will actually make sense to whoever reads your code (including future you). You develop taste for this through practice, not rules.

---

## Your Turn: Build It Out

Before checking the answers below, try extending the hierarchy yourself:

1. Add a `DrinkOrder(Order)` subclass with a `container` attribute (`"bottle"` or `"cup"`) and a method `get_recycling_note()` that returns a message if `container == "bottle"`.
2. Give `FoodOrder` an override of `get_total()` that adds a small "hot food surcharge" (e.g. 100 NGN) on top of the parent's total.
3. Write a `total_by_kind(orders, kind)` function that sums `get_total()` only for orders whose `.kind` matches the given string.

---

## Answers

**You Try It #1**
```python
o_one = Order(2001, 'Moses', 3000)
print(o_one.get_total())  # 3000 + 200 (service_fee) = 3200

o_two = Order(2002, 'Oge', 5000, fee=100)
print(o_two.get_total())  # 5000 + 100 (custom fee) = 5100
```

**You Try It #2**

| Object | `get_total()` | `get_prep_time()` |
|---|---|---|
| `o1` | 2000 + 200 = 2200 | n/a (no such method on `Order`) |
| `o2` | 2000 + 50 = 2050 | n/a |
| `f1` | 2000 + 200 = 2200 | 15 |
| `f2` | 2000 + 80 = 2080 | 15 |
| `f3` | 2000 + 200 = 2200 | 20 (default) |
