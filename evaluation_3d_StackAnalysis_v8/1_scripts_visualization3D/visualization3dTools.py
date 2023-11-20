import plotly.graph_objects as go
import sys
sys.path.insert(0, '../2_scripts_inputTools')
from InputFileReader import InputFileReader
from InputDataReader import InputDataReader

class Combined3DPlot:
    def __init__(self, first_frame_paths, second_frame_paths):
        self.plot_list = []
        self.first_frame_paths = first_frame_paths
        self.second_frame_paths = second_frame_paths

    def create_3d_plot(self, df, color, opacity, name):
        scatter = go.Scatter3d(x=df['x'], y=df['y'], z=df['z'], mode='markers', marker=dict(color=color, opacity=opacity), name=name)
        fig = go.Figure(data=[scatter])
        return fig

    def combine_plots(self):
        fig_combined = go.Figure()

        for fig in self.plot_list:
            for trace in fig.data:
                fig_combined.add_trace(trace)

        return fig_combined

    def add_plot(self, plot_points, color, opacity, name):
        self.plot_list.append(self.create_3d_plot(plot_points, color, opacity, name))

    def create_combined_3d_plot(self):
        self.perform_operations()
        return self.combine_plots()

    def perform_operations(self):
        for pcd_file in self.first_frame_paths:
            df_reader = InputDataReader(pcd_file)
            df = df_reader.read_and_process()
            self.add_plot(df, 'purple', 1.0, '02_')

        for pcd_file in self.second_frame_paths:
            df_reader = InputDataReader(pcd_file)
            df = df_reader.read_and_process()
            self.add_plot(df, 'blue', 0.1, '58_')