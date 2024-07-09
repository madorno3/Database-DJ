### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  an open-source object-relational database management system. It uses SQL. 
- What is the difference between SQL and PostgreSQL?
  SQL is a programming language and PostgreSQL uses SQL
- In `psql`, how do you connect to a database?
  \c 'database name'
- What is the difference between `HAVING` and `WHERE`?
  WHERE applies before any grouping occurs. HAVING applies after grouping data.
- What is the difference between an `INNER` and `OUTER` join?
  Inner join: returns only the rows where there is a match found in both tables based on a specified condition
  Outer join:there are different kinds of outer joins- left, right, full
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  Left - The rows from the left table combined with matching rows from the right.
  Right - The matching rows from left table, combined with all the rows from the right
- What is an ORM? What do they do?
  A programming technique that allows developers to interact with their databases
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

- What is CSRF? What is the purpose of the CSRF token?
  Cross-Site Request Forgery (CSRF).Tricks the authenticated user into giving away information

- What is the purpose of `form.hidden_tag()`?
  generates a hidden input field in the form that contains a CSRF token