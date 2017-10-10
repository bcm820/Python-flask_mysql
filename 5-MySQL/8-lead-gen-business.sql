# Write a single query that retrieves total revenue collected from each client for each month of the year.
# Order it by client id.

SELECT
	CONCAT_WS(' ', clients.first_name, clients.last_name) AS client_name,
    SUM(billing.amount) AS total_revenue,
    MONTHNAME(billing.charged_datetime) AS month_charge,
    YEAR(billing.charged_datetime) AS year_charge
FROM clients
	JOIN billing ON billing.client_id = clients.client_id
GROUP BY DATE_FORMAT(billing.charged_datetime, '%M')
ORDER BY clients.client_id ASC, billing.charged_datetime