from src.useme.postgres_utility import PostgresUtil


class LogicHandler():
    def __init__(self):
        self.sql_obj = PostgresUtil()

    def get_list_of_mutual_funds(self):
        funds_query = "SELECT * FROM mutual_funds WHERE is_active=True ORDER BY fund_type, mf_name;"
        funds_data = self.sql_obj.fetch_data_from_postgres(query=funds_query)
        funds_data = [dict(row) for row in funds_data]
        template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mutual Fund Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }th {
            background-color: green;
	    color:#fff;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .positive {
            color: green;
        }
        .negative {
            color: red;
        }
        .neutral {
            color: black;
        }
    </style>
</head>
<body>

    <h1 style="display:flex;justify-content:center;color:green;border:2px solid;border-radius:10px;">Live Mutual Fund Tracker</h1>
    <h3 style="display:flex;justify-content:end;">Last Updated at: _lut_</h3>

    <table>
        <thead>
            <tr>
                <th>Mutual Fund</th>
		<th>Fund Type</th>
                <th>One-Time Available</th>
                <th>Expected Change %</th>
                <th>Stocks in Green</th>
                <th>Stocks in Red</th>
                <th>Avg Gain in Green %</th>
                <th>Avg Fall in Red %</th>
            </tr>
        </thead>
        <tbody>
            <!-- Data rows will be inserted here -->
        </tbody>
    </table>

    <script>
        // Example data
        const data = __data__;

        // Function to determine the CSS class based on the percentage value
        function getChangeClass(change) {
            const value = parseFloat(change.replace('%', ''));
            if (value > 0) {
                return 'positive';
            } else if (value < 0) {
                return 'negative';
            } else {
                return 'neutral';
            }
        }

        // Function to generate table rows dynamically
	function generateTableRows(data) {
            let rows = '';
            data.forEach(item => {
                rows += `
                    <tr>
                        <td>${item.mutualFund}</td>
                        <td>${item.fundType}</td>
                        <td>${item.oneTimeAvailable}</td>
                        <td class="${getChangeClass(item.expectedChange)}">${item.expectedChange}</td>
                        <td class="positive">${item.greenStocks}</td>
                        <td class="negative">${item.redStocks}</td>
                        <td class="${getChangeClass(item.greenAvg)}">${item.greenAvg}</td>
                        <td class="${getChangeClass(item.redAvg)}">${item.redAvg}</td>
                    </tr>
                `;
            });
            return rows;
        }

        // Insert rows into the table body
        document.querySelector('tbody').innerHTML = generateTableRows(data);
    </script>

</body>
</html>
"""
        r_temps = []
        if funds_data:
            last_updated = funds_data[0]["last_updated"]
        for each_data in funds_data:
            try:
                row_template = "{ mutualFund: 'val1', fundType: 'val2', oneTimeAvailable: 'val3', greenStocks: 'val4', " \
                               "redStocks: 'val5', greenAvg: 'val6', redAvg: 'val7', expectedChange: 'val8' }".\
                    replace("val1", each_data["mf_name"]).replace("val2", each_data["fund_type"]).\
                    replace("val3", str(each_data["onetime_available"])).replace("val4", "-" if each_data["green_stocks"] in ["", None] else str(each_data["green_stocks"])).replace("val5", "-" if each_data["red_stocks"] in ["", None] else str(each_data["red_stocks"])).replace("val6", "-" if each_data["green_avg"] in ["", None] else str(each_data["green_avg"])).replace("val7", "-" if each_data["red_avg"] in ["", None] else str(each_data["red_avg"])).replace("val8", "-" if each_data["expected_change"] in ["", None] else each_data["expected_change"])
                r_temps.append(row_template)
            except Exception as e:
                print(str(e))
                continue

        template = template.replace('__data__', "[" + ", ".join(r_temps) + "]").replace("_lut_", str(last_updated))
        return template
