const mongoose = require("mongoose");

const MONGO_URI = "mongodb://admin:secret123@ec2-34-193-168-237.compute-1.amazonaws.com:27017/flight_recommendations?authSource=admin";

mongoose.connect(MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  authSource: "admin",
});

const db = mongoose.connection;
db.on("error", console.error.bind(console, "❌ MongoDB connection error:"));
db.once("open", () => console.log("✅ Connected to MongoDB on EC2"));

module.exports = mongoose;
