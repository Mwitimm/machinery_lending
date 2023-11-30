const sqlite3 = require("sqlite3").verbose();

// Connect to the SQLite database (or create it if it doesn't exist)
const db = new sqlite3.Database("./machinery_lending.db");

// Create the 'user' table
db.serialize(() => {
  db.run(`
    CREATE TABLE IF NOT EXISTS user (
      id INTEGER PRIMARY KEY,
      username TEXT NOT NULL,
      email TEXT NOT NULL,
      phone TEXT  NULL,
      password TEXT NOT NULL
    )
  `);

  // Display a message when the table creation is successful
  console.log('Table "user" created successfully.');

  // Close the database connection
  db.close((err) => {
    if (err) {
      return console.error(err.message);
    }
    console.log("Database connection closed.");
  });
});
