-- Task: Create a table called first_table with specified columns if it doesn't exist
-- This script will create the table first_table

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
