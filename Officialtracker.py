import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import display

#  Dictionary containing GDP data for each country
gdp_data_by_country = {
    "USA": {"nominal_gdp": 22996100, "ppp_gdp": 22996100},
    "CHN": {"nominal_gdp": 17734063, "ppp_gdp": 27312548},
    "JPN": {"nominal_gdp": 4937422, "ppp_gdp": 5396819},
    "DEU": {"nominal_gdp": 4223116, "ppp_gdp": 4815479},
    "GBR": {"nominal_gdp": 3186860, "ppp_gdp": 3344468},
    "IND": {"nominal_gdp": 3173398, "ppp_gdp": 10218573},
    "FRA": {"nominal_gdp": 2937473, "ppp_gdp": 3424152},
    "ITA": {"nominal_gdp": 2099880, "ppp_gdp": 2713266},
    "CAN": {"nominal_gdp": 1990762, "ppp_gdp": 1990762},
    "KOR": {"nominal_gdp": 1798534, "ppp_gdp": 2427791},
    "RUS": {"nominal_gdp": 1775800, "ppp_gdp": 4785445},
    "BRA": {"nominal_gdp": 1608981, "ppp_gdp": 3435882},
    "AUS": {"nominal_gdp": 1542660, "ppp_gdp": 1542660},
    "ESP": {"nominal_gdp": 1425277, "ppp_gdp": 1425277},
    "MEX": {"nominal_gdp": 1293038, "ppp_gdp": 2609993},
}

# Function to extract the GDP data for a given metric and a list of countries
def extract_gdp_data(gdp_metric, countries):
 gdp_data_list = []
 for country in countries:
    gdp_data_list.append(gdp_data_by_country[country][gdp_metric])
    return gdp_data_list

# Create a dropdown widget for selecting the GDP metric to compare
gdp_metric_select = widgets.Dropdown(
  options=["nominal_gdp", "ppp_gdp"],
  value="nominal_gdp",
  description="GDP metric:",
  disabled=False,
)

# Create checkboxes for selecting the countries to compare
country_select = {}
for country in gdp_data_by_country.keys():
    country_select[country] = widgets.Checkbox(
        value=True, description=country, disabled=False
    )

# Function to update the bar chart with new data based on the selected GDP metric and countries
def update_plot(gdp_metric, countries):
    gdp_data = extract_gdp_data(gdp_metric, countries)
    ax.clear()
    ax.bar(countries, gdp_data)

# Create the bar chart
fig, ax = plt.subplots()

# Display the widgets
display(gdp_metric_select)
for country in country_select.values():
    display(country)

# Connect the widgets to the update function
widgets.interactive(update_plot, gdp_metric=gdp_metric_select, countries=country_select)