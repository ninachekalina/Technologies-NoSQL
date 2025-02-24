

INSERT INTO employees (id, name, position, salary) 
VALUES (uuid(), 'Ivan Nedovarov', 'Software Engineer', 70000.00);

INSERT INTO employees (id, name, position, salary) 
VALUES (uuid(), 'Kati Smirnova', 'Data Analyst', 48000.00);

INSERT INTO employees (id, name, position, salary) 
VALUES (uuid(), 'Elena Polanskaja', 'Product Manager', 90000.00);


SELECT * FROM employees;


SELECT * FROM employees WHERE salary > 50000.00 ALLOW FILTERING;
