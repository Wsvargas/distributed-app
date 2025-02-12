require("dotenv").config();
const express = require("express");
const { ApolloServer } = require("apollo-server-express");
const cors = require("cors");
const typeDefs = require("./graphql/schema");
const resolvers = require("./graphql/resolvers");
require("./config/redshift");

async function startServer() {
  const app = express();
  app.use(cors());

  const server = new ApolloServer({ typeDefs, resolvers });
  await server.start();
  server.applyMiddleware({ app });

  const PORT = 4001;
  app.listen(PORT, () => {
    console.log(`🚀 GraphQL Server for Reports running at http://localhost:${PORT}/graphql`);
  });
}

startServer();
