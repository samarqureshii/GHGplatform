// Sample CSV data
const csvData = `Annual Electricity_Quantity (MWh),Annual NaturalGas_Quantity (m3),Annual GHG Emissions (kgCO2e)
11173,598473,2702323`;

// Parse CSV data
const parseCsvData = (csv) => {
  const rows = csv.split('\n');
  const headers = rows.shift().split(',');

  return rows.map(row => {
    const rowData = row.split(',');
    return headers.reduce((obj, header, index) => {
      obj[header] = rowData[index];
      return obj;
    }, {});
  });
}
