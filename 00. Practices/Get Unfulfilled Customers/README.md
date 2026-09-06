# Amazon OA Practice — Unfulfilled Customers by Inventory Priority

## Problem

During a flash sale, customers submit requests for a limited quantity of a product.

Each request is represented as:

```text
[customerId, quantity, bidAmount, timestamp]
```

where:

- `customerId` is the unique identifier of the customer.
- `quantity` is the number of items requested.
- `bidAmount` is the amount the customer bids per item.
- `timestamp` represents when the request was submitted.

You are also given an integer:

```text
totalInventory
```

representing the total number of items available.

---

## Allocation Rules

Inventory is allocated according to the following rules.

### 1. Higher bids have higher priority

Customers with a higher `bidAmount` are processed before customers with a lower bid.

### 2. Equal bids use round-robin allocation

If multiple customers have the same bid amount:

- Customers are ordered by their `timestamp`.
- Earlier timestamps have priority within each round.
- Each customer receives exactly **one item per round**.
- A customer that has already received their entire requested quantity is skipped.
- Rounds continue until:
  - every request in the bid group has been fulfilled, or
  - the inventory becomes empty.

### 3. Lower bid groups are processed afterward

Only after the current bid group has finished can inventory be allocated to the next lower bid group.

---

## Task

Return the IDs of all customers who receive **zero items**.

---

## Example 1

### Input

```python
requests = [
    [1, 5, 5, 0],
    [2, 7, 8, 1],
    [3, 7, 5, 1],
    [4, 10, 3, 3]
]

totalInventory = 18
```

### Output

```python
[4]
```

### Explanation

Customer `2` has the highest bid:

```text
customer 2 → bid 8 → requests 7 items
```

After fulfilling customer `2`:

```text
18 - 7 = 11
```

items remain.

Customers `1` and `3` both have bid `5`, so their allocation is performed using round robin.

```text
customer 1 → requests 5
customer 3 → requests 7
```

The remaining 11 items are distributed between them.

Both customers receive at least one item.

There is no inventory remaining when customer `4`, whose bid is `3`, is reached.

Therefore:

```python
[4]
```

---

## Example 2

### Input

```python
requests = [
    [1, 2, 10, 0],
    [2, 2, 10, 1],
    [3, 2, 10, 2]
]

totalInventory = 2
```

### Allocation

All customers have the same bid.

Round 1:

```text
customer 1 → gets 1
customer 2 → gets 1
```

Inventory becomes empty before customer `3` receives anything.

### Output

```python
[3]
```

---

## Example 3

### Input

```python
requests = [
    [1, 3, 20, 0],
    [2, 5, 10, 1],
    [3, 2, 5, 2]
]

totalInventory = 8
```

### Output

```python
[3]
```

---

## Function Signature

Implement:

```python
def get_unfulfilled_customers(
    requests: list[list[int]],
    total_inventory: int
) -> list[int]:
```

---

## Constraints

Assume:

```text
1 <= len(requests)
1 <= quantity
1 <= bidAmount
0 <= timestamp
0 <= totalInventory
```

Each `customerId` is unique.

---

## Goal

Try to design an efficient solution.

Avoid simulating the allocation one item at a time when the requested quantities can be very large.

Consider:

- How should requests be ordered?
- How should customers with equal bids be grouped?
- Can round-robin allocation be calculated without allocating every individual item?
- How can you determine whether a customer received at least one item?