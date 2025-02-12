const { gql } = require("apollo-server-express");

const typeDefs = gql`
  type Recommendation {
    id: ID!
    userId: ID!
    preferences: [String]
    history: [String]
  }

  type Query {
    getRecommendations(userId: ID!): Recommendation
  }

  type Mutation {
    addRecommendation(userId: ID!, preferences: [String], history: [String]): Recommendation
  }
`;

module.exports = typeDefs;
