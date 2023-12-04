# Visualisation 3d 

## Install Python for Windows
Firstly, if you don't have Python installed on your desktop, you can download and install it from the [official Python website](https://www.python.org/downloads/).

## Clone this Visualisation3d Repository

To use the Visualisation3D application, you should clone the repository using the following command:

  ```bash
    git clone git@bitbucket.org:rev-tec/tools.git
  ```

## Install python requirements and dependencies
You have to create a virtual environment and install the dependencies using the requirements.txt file.

1- Create a Virtual Environment:

  ```
    python -m venv my_environment
  ```
2- Activate the Virtual Environment:

  ```
    my_environment\Scripts\activate
  ```
3- Install depencencies from 'requirements.txt': 
  ```
    pip install -r requirements.txt
  ```

## Running the Application 

### Command-line Arguments

The 3D Visualization Tool supports the following command-line arguments:

- `-inputfile` or `--file`: Specifies the input file name. The default is `../0_InputFiles/StackAnalysis3D_Input.json`. You can customize the input file by providing the path to your own JSON file.

  ```
  python pointCloudVisualization3dMain.py -inputfile path/to/your/input.json
  ```
  
## Folder Structure
Before visualizing any existing Point Cloud Data (PCD) files, ensure you have the following folder structure:

- `basicPath`
  - `table`
    - `basicEvaluationDirectory`
      - `installation`
        - `videoName`
          - `evaluationId`
            - `pointCloudsCorrectedDir`
           

## Additional Information 
To do : Add Input File Details
