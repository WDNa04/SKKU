### Exercise

A snack store sells a limited quantity of snacks, and each snack type has a specific stock and price, as shown below.

| Type | Stock | Price |
| :---: | :---: | :---: |
| A | 3 | 1000 |
| B | 5 | 2500 |
| C | 10 | 3300 |

You are given the type and quantity of snacks that a customer wants to purchase. The snack type is always one of A, B, or C, and the quantity is a positive integer.

Write a code that outputs the price the customer needs to pay if <ins> the snack is available in stock</ins>. However, if <ins>the requested quantity exceeds the available stock</ins>, the code should output "Sorry".

For example, if a customer wants to buy 2 units of snack B, the code should output "5000". But if a customer wants to buy 15 units of snack C, the code should ouput "Sorry". 

### Example

input
<pre>
snack_type: B
quantity: 2
</pre>
output
<pre>
5000
</pre>