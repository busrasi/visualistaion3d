
from dash import Dash, dcc, html, Input, Output
import sys
sys.path.insert(0, '../2_scripts_inputTools')
from InputFileReader import InputFileReader
import visualization3dTools as Visualization3dTools

if __name__ == '__main__':
    input_filename = '../0_InputFiles/StackAnalysis3D_Input.json'
    input_reader = InputFileReader(input_filename)

    first_frame_paths = input_reader.getFirstFrameFiles()
    second_frame_paths = input_reader.getSecondFrameFiles()

    combined_plotter = Visualization3dTools.Combined3DPlot(first_frame_paths, second_frame_paths)

    fig_combined = combined_plotter.create_combined_3d_plot()

    app = Dash(__name__)

    app.layout = html.Div([
        html.H4('Combined 3D Scatter Plot'),
        dcc.Graph(
            id="scatter-3d-plot",
            figure=fig_combined,
            style={'width': '100%', 'height': '1000px'}
        )
    ])

    fig_combined.update_layout(scene_aspectmode='manual',
                  scene_aspectratio=dict(x=110, y=55, z=4),
                  scene_camera=dict(
                      center=dict(x=0, y=0, z=0),
                      eye=dict(x=110, y=55, z=4)
                  )
    )

    app.run_server(debug=True)