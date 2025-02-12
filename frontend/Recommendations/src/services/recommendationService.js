const AWS = require("aws-sdk");

AWS.config.update({ region: "us-east-1" });

const sns = new AWS.SNS();
const TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:NewRecommendations";

async function notifyNewRecommendation(userId) {
  await sns.publish({
    Message: `New recommendation added for user ${userId}`,
    TopicArn: TOPIC_ARN,
  }).promise();
}

module.exports = { notifyNewRecommendation };
