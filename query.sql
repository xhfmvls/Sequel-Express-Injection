-- Create the items table
CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

-- Insert initial data into the items table
INSERT INTO items (id, name, description) VALUES
(1, 'Item 1', 'Description for Item 1'),
(2, 'Item 2', 'Description for Item 2'),
(3, 'Item 3', 'Description for Item 3'),
(4, 'Item 4', 'Description for Item 4'),
(5, 'Item 5', 'Description for Item 5'),
(6, 'Item 6%', 'A versatile and innovative product with a touch of mystery, perfect for the modern adventurer'),
(7, 'Korea Item', 'Item from South Korea');