-- 1. Create the 'departments' table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- 2. Insert some sample data into the 'departments' table
INSERT INTO departments (department_name, location) VALUES
('Human Resources', 'New York'),
('Finance', 'Chicago'),
('IT', 'San Francisco'),
('Marketing', 'Los Angeles');

-- 3. Create the 'employees' table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- 4. Update the 'departments' table by modifying the 'location' column type (e.g., increasing the size)
ALTER TABLE departments
MODIFY COLUMN location VARCHAR(150);

-- 5. Delete a specific row from the 'departments' table by department_id
-- Let's delete the department with department_id = 2 (Finance)
DELETE FROM departments WHERE department_id = 2;
