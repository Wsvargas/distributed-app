const { Pool } = require("pg");

const pool = new Pool({
  user: "admin",
  host: "reports",
  database: "reports",
  password: "secret123",
  port: 5439,
  ssl: { rejectUnauthorized: false },
});

pool.on("connect", () => {
  console.log("✅ Connected to Amazon Redshift");
});

module.exports = pool;
