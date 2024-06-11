## Inverse Model Computing
The Inversion window in this PyQt5-based application allows users to perform inversion on geophysical data using the PyGIMLi library. Inversion is a crucial step, where you can estimate resistivity based on measured data. 

### Applying Inversion

To apply inversion with the specified parameters, follow these steps:

Input your geophysical data by clicking the "Import" button in the "Data" tab and selecting the data file.

Create the mesh in the "Domain and Mesh" window

Configure the inversion parameters (MaxIter, λ, dPhi) using the provided spinboxes in the "Inversion" tab.

Click the "Apply" button to start the inversion process. The algorithm will iteratively refine the model to match the observed data.

The inversion results: resistivity of the selected mesh will display in the middle of the window.