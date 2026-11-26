# Project 9 – Tuple-Based Product Catalogue Audit

## Description
The Tuple-Based Product Catalogue Audit is a Python program designed to maintain and analyse product information using tuples. Each product contains a product ID, price, and available stock quantity.

The program calculates the total inventory value, identifies products that require replenishment, and detects duplicate product IDs.

## Objectives
- To understand and use tuples in Python.
- To store product details using tuples.
- To calculate the total inventory value.
- To identify products with low stock.
- To detect duplicate product IDs.
- To apply loops and conditional statements.

## Concepts Used
- Tuples
- Lists
- Tuple unpacking
- For loops
- Conditional statements (`if`, `elif`, `else`)
- Arithmetic operators
- Duplicate detection

## Assumptions
- Each product contains a product ID, price, and quantity.
- Product price must be greater than zero.
- Product quantity cannot be negative.
- Products with a quantity below 5 require replenishment.
- Inventory value is calculated by multiplying price by quantity.
- Duplicate product IDs are reported during the audit.

## Sample Output 1 – Product Catalogue Audit

```text
----- PRODUCT CATALOGUE AUDIT -----

P101 - Product Value: 1000.0
P102 - Product Value: 600.0
Replenishment Required
P103 - Product Value: 0.0
Replenishment Required
P104 - Invalid record

Total Inventory Value: 1600.0

----- DUPLICATE PRODUCT IDs -----

No duplicate product IDs
```

## Sample Output 2 – Duplicate Product ID

```text
----- DUPLICATE PRODUCT IDs -----

Duplicate Product ID: P101
```

## How to Run
1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Open the Python source file `main.py`.
4. Run the program using Python.
5. Enter the number of products.
6. Enter each product's ID, price, and stock quantity.
7. View the product catalogue audit report.

## Output Screenshots
The output screenshots demonstrate product details, inventory value, low-stock identification, and duplicate product ID detection.

- `Product-Catalogue-Output-1.png`
- `Product-Catalogue-Output-2.png`

## Conclusion
The Tuple-Based Product Catalogue Audit program successfully stores product information using tuples and performs basic inventory analysis. It calculates the total inventory value, identifies products requiring replenishment, and detects duplicate product IDs.

This project demonstrates the practical use of tuples, lists, loops, conditional statements, and arithmetic operations in Python programming.
