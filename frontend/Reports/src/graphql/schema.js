const { gql } = require("apollo-server-express");

const typeDefs = gql`
 type Report {
 type: String
 content: String
 }

 type Query {
 getReports(type: String!): [Report]
 }
`;

module.exports = typeDefs;