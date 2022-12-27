import sys
import matplotlib
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QCheckBox, QGraphicsOpacityEffect
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

        self.setWindowIcon(QtGui.QIcon('path/to/icon/file.png'))
        
        # Create welcome screen widget
        self.welcome_widget = QWidget()
        self.welcome_widget.setStyleSheet("background-color: black;")
        
        # Set the window icon
        self.setWindowIcon(QtGui.QIcon('globalw.png'))
        # Set the window title and size
        self.setWindowTitle("Economic Visualization Tool")
        self.setWindowIconText("Economic Visualization Tool")
        self.resize(800, 600)
        
        # Create the main widget and set it as the central widget of the main window
        self.main_widget = MainWidget(self)
        
        # Add welcome screen widget as the central widget
        self.setCentralWidget(self.welcome_widget)
        
        # Create welcome label and add it to the welcome screen widget
        self.welcome_label = QLabel("Welcome to the Economic Visualization Tool")
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setStyleSheet("color: white; font-size: 24px;")
        self.welcome_widget.layout = QVBoxLayout()
        self.welcome_widget.layout.addWidget(self.welcome_label)
        self.welcome_widget.setLayout(self.welcome_widget.layout)
        
        # Create fade animation for welcome screen
        self.fade_animation = QtCore.QPropertyAnimation(self.welcome_widget, b"windowOpacity")
        self.fade_animation.setDuration(3000)
        self.fade_animation.setStartValue(1)
        self.fade_animation.setEndValue(0)
        self.fade_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        
        # Connect fade animation finished signal to show_main_widget slot
        self.fade_animation.finished.connect(self.show_main_widget)
        
        # Start fade animation
        self.fade_animation.start()
        
    def show_main_widget(self):
        # Set main widget as the central widget
        self.setCentralWidget(self.main_widget)

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
        
        # Connect the country checkboxes' stateChanged signal to the on_country_selected function
        for checkbox in self.country_checkboxes.values():
            checkbox.stateChanged.connect(self.on_country_selected)
        
        # Create the figure and canvas to display the GDP data
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        # Create the navigation toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        # Create the layout and add the GDP metric dropdown, country checkboxes, canvas, and toolbar
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.gdp_metric_dropdown)
        for checkbox in self.country_checkboxes.values():
            self.layout.addWidget(checkbox)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.toolbar)
        self.setLayout(self.layout)
        # Create fade animation for welcome screen
        self.fade_animation = QtCore.QPropertyAnimation(self.welcome_widget, b"windowOpacity")
        self.fade_animation.setDuration(3000)
        self.fade_animation.setStartValue(1)
        self.fade_animation.setEndValue(0)
        self.fade_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        
        # Connect fade animation finished signal to show_main_widget slot
        self.fade_animation.finished.connect(self.show_main_widget)
        
        # Start fade animation
        self.fade_animation.start()
        
    def show_main_widget(self):
        # Set main widget as the central widget
        self.setCentralWidget(self.main_widget)

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
        
        # Connect the country checkboxes' stateChanged signal to the on_country_selected function
        for checkbox in self.country_checkboxes.values():
            checkbox.stateChanged.connect(self.on_country_selected)
        
        # Create the figure and canvas to display the GDP data
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        # Create the navigation toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        # Create the layout and add the GDP metric dropdown, country checkboxes, canvas, and toolbar
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.gdp_metric_dropdown)
        for checkbox in self.country_checkboxes.values():
            self.layout.addWidget(checkbox)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.toolbar)
        self.setLayout(self.layout)
        # Initialize the plot with nominal GDP data for all countries
        self.on_gdp_metric_selected()
        
    def on_gdp_metric_selected(self):
        # Extract the GDP data for the selected metric and all selected countries
        gdp_metric = self.gdp_metric_dropdown.currentText()
        selected_countries = [country for country, checkbox in self.country_checkboxes.items() if checkbox.isChecked()]
        gdp_data = extract_gdp_data(gdp_metric, selected_countries)
        
        # Clear the figure and plot the GDP data
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(selected_countries, gdp_data)
        ax.set_ylabel(gdp_metric)
        self.canvas.draw()
        
    def on_country_selected(self):
        # Update the plot when a country checkbox is selected
        self.on_gdp_metric_selected()

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
