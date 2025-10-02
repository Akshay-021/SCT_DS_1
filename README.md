# Population Distribution by Region (2020)

This project visualizes the distribution of the total population across world regions for the year 2020 using official World Bank datasets and Python.

## Project Overview

The project performs exploratory data analysis to show how population numbers differ among global regions. Using two official datasets—one for country population and another for country metadata (including region)—the code generates a bar chart illustrating total population per region in 2020.

## Data Sources

- **Population data**: `API_SP.POP.TOTL_DS2_en_csv_v2_1122588.csv`  
  Contains total population figures for each country.
- **Country metadata**: `Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_1122588.csv`  
  Provides country-to-region mappings and additional context.

> Both files are available from the World Bank Open Data repository.

## Features

- Reads and merges population and metadata files.
- Aggregates total population by region for 2020.
- Visualizes the result as a clear bar chart.
- Code is concise, reproducible, and focused on one key variable: region.

## Installation

1. Clone/download this repository and place both CSV files in the specified directory.
2. Ensure you have Python 3.x installed.
3. Install the required libraries:
   ```bash
   pip install pandas matplotlib
   ```
4. Update file paths in the script if your directory structure is different.

## Usage

Run the Python script to generate the visualization:
```bash
python your_script_name.py
```
You should see a bar chart display, showing total population by global region.

## Code Structure

- Loads and processes data with `pandas`.
- Merges datasets on country name.
- Sums population per region for 2020.
- Uses `matplotlib` to create and display a bar chart.

## Results

The output is a bar chart showing the total 2020 population for each world region, providing an at-a-glance comparison across regions.

## Dependencies

- `pandas`
- `matplotlib`

## Future Work

- Add filtering to focus on specific regions or countries.
- Analyze trends over time by adding earlier years.
- Introduce population normalization (e.g., per capita analysis).
- Include other categorical variables (income group, etc.).

## Acknowledgements

- Data sourced from the World Bank Open Data portal.

## License

This project is released for educational and analytical purposes. For any commercial or large-scale public use, please consult the terms of the World Bank data license.
