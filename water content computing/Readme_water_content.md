# Water Content Calculation

The Water Content window in this PyQt5-based application allows users to perform water content calculations on inverted model data using the PyGIMLi library. Water content calculation is a crucial and final step in modeling, where you can determine the distribution of soil water content based on the resistivity obtained from the inversion model and the relationship between resistivity and water content at different temperatures. This readme provides an overview of the Water Content window and its functionalities.

## Applying Water Content Calculation

To perform water content calculation with the specified temperature, follow these steps:

Click the "Import" button in the "Data" tab to input your geophysical data and select the data file.

Create a mesh in the "Domain and Mesh" window.

Adjust the parameters in the "Inversion" tab to complete the inversion calculation.

In the "Water Content" tab, adjust the temperature value or import a temperature field file for water content calculation.

Click the "Calculate" button to start the calculation process. The program will generate a two-dimensional distribution of water content based on the temperature's influence.


