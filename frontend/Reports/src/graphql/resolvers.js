const Report = require("../models/report");

const resolvers = {
  Query: {
    getReports: async (_, { type }) => {
      return await Report.getReports(type);
    },
  },
};

module.exports = resolvers;
