const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const bcrypt = require("bcrypt");
const bodyParser = require("body-parser");
const helmet = require("helmet");
const cors = require("cors");

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());
app.use(helmet());
app.use(cors());

// Connect to the SQLite database (or create it if it doesn't exist)
const db = new sqlite3.Database("./machinery_lending.db");

// Endpoint to add a user
app.post("/add_user", async (req, res) => {
  const { username, email, phone, password } = req.body;

  try {
    // Hash the password before storing it
    const hashedPassword = await bcrypt.hash(password, 10);

    db.run(
      "INSERT INTO user (username, email, phone, password) VALUES (?, ?, ?, ?)",
      [username, email, phone, hashedPassword],
      (err) => {
        if (err) {
          console.error(err.message);
          return res
            .status(500)
            .json({ error: "Failed to add user to the database." });
        }

        console.log(`User ${username} added successfully.`);
        res.status(200).json({ message: "User added successfully." });
      }
    );
  } catch (error) {
    console.error("Error during user registration:", error);
    res.status(500).json({ error: "Internal server error." });
  }
});

// Endpoint for user login
app.post("/login", async (req, res) => {
  const { username, password } = req.body;

  try {
    db.get(
      "SELECT * FROM user WHERE username = ?",
      [username],
      async (err, row) => {
        if (err) {
          console.error(err.message);
          return res
            .status(500)
            .json({ error: "Error while fetching user from the database." });
        }

        if (!row) {
          return res
            .status(401)
            .json({ error: "Invalid username or password." });
        }

        // Compare the entered password with the stored hashed password
        const passwordMatch = await bcrypt.compare(password, row.password);

        if (passwordMatch) {
          return res.status(200).json({ message: "Login successful." });
        } else {
          return res
            .status(401)
            .json({ error: "Invalid username or password." });
        }
      }
    );
  } catch (error) {
    console.error("Error during user login:", error);
    res.status(500).json({ error: "Internal server error." });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
