const express = require('express');
const mysql = require('mysql2');
require('dotenv').config();
const app = express();
const PORT = 8080;

const dbConfig = {
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    port: process.env.DB_PORT,
};

const pool = mysql.createPool(dbConfig).promise();

app.use(express.json());

app.get('/', async (req, res) => {
    res.status(200).json({ message: 'Hello World' });
});

app.post('/items', async (req, res) => {
    const item_name = req.body.item_name;
    if (!item_name) {
        return res.status(400).json({ error: 'Item name is required' });
    }
    try {
        const connection = await pool.getConnection();
        const query = 'SELECT id, name, description FROM items WHERE name = \'' + item_name + '\'';
        const [results] = await connection.execute(query);
        if (results.length === 0) {
            // return res.status(404).json({ error: 'No item found' });
            return res.status(404).json({ error: 'Item not found!' });
        }
        res.json({ items: results });
    } catch (error) {
        console.error('Error executing query: ', error);
        return res.status(500).json({ error: 'Database Error!' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
