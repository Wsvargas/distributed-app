const mongoose = require("mongoose");

const RecommendationSchema = new mongoose.Schema({
  userId: mongoose.Schema.Types.ObjectId,
  preferences: [String],
  history: [String],
});

const Recommendation = mongoose.model("Recommendation", RecommendationSchema);

module.exports = Recommendation;
