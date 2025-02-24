CREATE KEYSPACE IF NOT EXISTS company 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 2};

USE company;

CREATE TABLE IF NOT EXISTS employees (
    id UUID PRIMARY KEY,
    name TEXT,
    position TEXT,
    salary DECIMAL
);
