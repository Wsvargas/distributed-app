const jwt = require("jsonwebtoken");
const Recommendation = require("../models/recomendacion"); 
const JWT_SECRET = "secret123"; 
const resolvers = {
  Query: {
    getRecommendations: async (_, args, { req }) => {
      const authHeader = req.headers.authorization;
      if (!authHeader) {
        throw new Error("Unauthorized: No token provided");
      }

      const token = authHeader.replace("Bearer ", ""); 
      
      try {
        const decoded = jwt.verify(token, JWT_SECRET);
        const recommendations = await Recommendation.findOne({ userId: decoded.id });

        if (!recommendations) {
          throw new Error("No recommendations found for this user");
        }

        return recommendations;
      } catch (error) {
        throw new Error("Invalid or expired token");
      }
    },
  },
};

module.exports = resolvers;
