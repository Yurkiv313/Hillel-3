import csv
from flask import render_template
from models.parameters import Parameters


class ParametersManager:

    def __init__(self):
        self.filename = 'data/hw.csv'

    def read(self):
        with open(self.filename, newline='') as csvfile:
            parameters_list = []
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            height_f = 0.0
            weight_f = 0.0
            for row in reader:
                if len(row) != 0:
                    parameter = Parameters(row[0], row[1], row[2])
                    parameters_list.append(parameter)
                    height_f += parameter.height
                    weight_f += parameter.weight
            content_h = (height_f / len(parameters_list)) * 2.54
            content_w = (weight_f / len(parameters_list)) / 2.2046
        return render_template('mean.html', content_h=content_h, content_w=content_w)
