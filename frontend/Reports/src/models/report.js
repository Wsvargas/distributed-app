const pool = require("../config/redshift");

class Report {
 static async getReports(type) {
 const query = `SELECT content FROM analytical_reports WHERE report_type = $1`;
 const result = await pool.query(query, [type]);
 return result.rows.map(row => ({ type, content: row.content }));
 }
}

module.exports = Report;