import json
import os  # You need to import the 'os' module
class InputFileReader:
    def __init__(self, filePath_name):
        self.path = None
        self.tablename = None
        self.videoname = None
        self.basicEvaluationDirectory = None
        self.installationDate = None
        self.first_frame_files = []
        self.second_frame_files = []

        self.readStackAnalysis3dInputJson(filePath_name)
        self.construct_file_paths()

    def readStackAnalysis3dInputJson(self, json_filename):
        with open(json_filename, 'r') as json_file:
            data = json.load(json_file)

            self.path = data['basicPath']
            self.tablename = data['table']
            self.videoname = data['videoName']
            self.basicEvaluationDirectory= data['basicEvaluationDirectory']
            self.pointCloudsCorrectedDir = data['pointCloudsCorrectedDir']
            self.installationDate = data['installation']
            self.evaluation_id = data['evaluationId']
            self.first_frame_files = data['firstFrame']
            self.second_frame_files = data['secondFrame']

    def construct_file_paths(self):
        base_directory = f'{self.path}/{self.tablename}/{self.basicEvaluationDirectory}/{self.installationDate}/{self.videoname}/{self.evaluation_id}/{self.pointCloudsCorrectedDir}'

        self.first_frame_files = [os.path.join(base_directory, file) for file in self.first_frame_files]
        self.second_frame_files = [os.path.join(base_directory, file) for file in self.second_frame_files]

    def getFirstFrameFiles(self):
        return self.first_frame_files

    def getSecondFrameFiles(self):
        return self.second_frame_files