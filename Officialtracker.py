import sys
import matplotlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QCheckBox
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

#Dictionary containing GDP data for each country

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

#Function to extract the GDP data for a given metric and a list of countries

def extract_gdp_data(gdp_metric, countries):
    gdp_data_list = []
    for country in countries:
        try:
            gdp_data_list.append(gdp_data_by_country[country][gdp_metric])
        except KeyError:
            gdp_data_list.append(0)
    return gdp_data_list

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

# Set the window title and size
        self.setWindowTitle("Economic Visualization Tool")
        self.resize(800, 600)

 # Create the main widget and set it as the central widget of the main window
        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)

    def on_close(self):
       
        sys.exit()

class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        #Create the GDP metric dropdown
        self.gdp_metric_dropdown = QComboBox()
        # Add items to the GDP metric dropdown
        self.gdp_metric_dropdown.addItem("nominal_gdp")
        self.gdp_metric_dropdown.addItem("ppp_gdp")

        # Connect the GDP metric dropdown's currentIndexChanged signal to the on_gdp_metric_selected function
        self.gdp_metric_dropdown.currentIndexChanged.connect(self.on_gdp_metric_selected)

        # Create the country checkboxes
        self.country_checkboxes = {}
        for country in gdp_data_by_country:
            self.country_checkboxes[country] = QCheckBox(country)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select GDP metric:"))
        layout.addWidget(self.gdp_metric_dropdown)
        layout.addWidget(QLabel("Select countries:"))
        for checkbox in self.country_checkboxes.values():
            layout.addWidget(checkbox)
        self.setLayout(layout)

        # Create the Matplotlib figure and canvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # Add the Matplotlib canvas to the layout
        layout.addWidget(self.canvas)

        # Create the Matplotlib toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)

    def on_gdp_metric_selected(self):
        # Get the selected GDP metric
        gdp_metric = self.gdp_metric_dropdown.currentText()

        # Get the list of selected countries
        selected_countries = []
        for country, checkbox in self.country_checkboxes.items():
            if checkbox.isChecked():
                selected_countries.append(country)

        # Extract the GDP data for the selected metric and countries
        gdp_data = extract_gdp_data(gdp_metric, selected_countries)

        # Clear the current figure
        self.figure.clear()

        # Create a new axis
        ax = self.figure.add_subplot(111)

        # Plot the GDP data
        ax.bar(selected_countries, gdp_data)

        # Set the y-axis label
        ax.set_ylabel(gdp_metric)

        # Redraw the canvas
        self.canvas.draw()

if __name__ == "__main__":
    matplotlib.use("Qt5Agg")
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
