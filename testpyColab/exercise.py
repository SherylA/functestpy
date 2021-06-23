from IPython.core.display import HTML, display
import pandas as pd
import numpy as np
from inspect import isfunction

from testpyColab.student import Student
import testpyColab.raw_data as raw_data

import testpyColab.displayhtml as dhtml

MSG_ERROR_INIT = "Check exercise initialization. An error occurred: {}"
MSG_ERROR_READ = "Data could not be read. An error occurred: {}"

class Exercise(object):
    """Create a Exercise.
    .. versionadded:: 1.0
    
    Attributes
    ----------
    root: str
       Data path in git hub

    student : Student
        Student that makes exercise
    
    group : int
        The student's group for data upload

    exercise_id: int
        Exercise number or identification

    number_test: list
        Exercise number tests
    """

    def __init__(self, id_exercise, names_tests, student = None):
        self.student = Student() if student is None else student
        self.id_exercise = id_exercise
        self.names_tests = names_tests
        self.failed = False

        try:
            self.root_data = raw_data.ROOT_FOR_EXERCISES[id_exercise]
            self.student.check_info()
            self.group = self.student.group
            self.number_tests = len(self.names_tests)
            self.results_tests = ['Skipped'] * self.number_tests
        except Exception as err:
            raise ValueError(MSG_ERROR_INIT.format(err))        

    def set_asserts_data(self, params):
       self.params = params

    def set_data(self, ext, read_method = 'read_csv', **kwargs):
        self.path = self.root_data + f'grupo_{self.group}.{ext}'
        self.data = None

        print(f"Loading the files located in {self.path}...")
        
        if read_method == 'read_csv':
            try:
                self.data = pd.read_csv(self.path,**kwargs)
            except Exception as err:
                print(MSG_ERROR_READ.format(err))
        elif read_method == 'read_excel':
            try:
                self.data = pd.read_excel(self.path,**kwargs)
            except Exception as err:
                print(MSG_ERROR_READ.format(err))
        elif read_method == 'open':
            # TODO: Add open method for get https:/
            pass
            
    def set_desc_test(self, desc_tests):
        self.desc_tests = desc_tests

    def set_tests(self,tests):
        self.tests = tests

    def check_success(self):
        self.success = all([t=='Success' for t in self.results_tests])

    def check_exercise(self, *args, **kwargs):
        for i, test in enumerate(self.tests):
            test(*args, **kwargs)
            if self.failed:
                self.results_tests[i] = 'Failed' 
                break
            self.results_tests[i]  = 'Success' 
        self.check_success()

    def display_result(self):  
        middle_HTML = ""
        for i in range(len(self.tests)):
            info_tests = self.names_tests[i] + self.desc_tests[i]
            middle_HTML += dhtml.rowResultTableHTML(info_tests, self.results_tests[i]) + '\n'
        display(HTML(dhtml.tableHTML(middle_HTML)))
            

class ExerciseFuncSimple(Exercise):
    """Create a exercise whose solution is a simple function
    .. versionadded:: 1.0
    """
    def __init__(self, id_exercise, student = None):
        Exercise.__init__(self, id_exercise, raw_data.NAMES_TEST_0, student)
        self.set_asserts_data(raw_data.PARAMS_00)
        self.slope = self.params['slope'][self.group - 1]
        self.intercept = self.params['intercept'][self.group - 1]
        self.set_desc_test(["", f"m = {self.slope} +/- 0.001", f"b= {self.intercept} +/- 0.1"])
        self.err = {}

    def load_data(self):
        kwargs = {'sep': ' ', 
                  'header': None}
        self.set_data('txt', **kwargs)
        self.data.columns = ['Y','X']
        self.dataY = self.data['Y'].values
        self.dataX = self.data['X'].values
        return self.data['Y'].values, self.data['X'].values

    def _check_function(self, func):
        if not isfunction(func):
            self.failed = True
    
    def _check_slope(self, func):
        try:
            m, _ = func(self.dataY,self.dataX)
            if abs(m - self.slope) > 0.001:
                self.failed = True
        except Exception as err:
            self.err['slope'] = err
            self.failed = True
            
    def _check_intercept(self, func):
        try:
            _, b = func(self.dataY,self.dataX)
            if abs(b - self.intercept)>0.1:
                self.failed = True
        except Exception as err:
            self.err['intercept'] = err
            self.failed = True

    def check_exercise(self, func):
        self.set_tests([self._check_function,self._check_slope,self._check_intercept])
        return super().check_exercise(func)
    
    def display_check_exercise(self, func):
        self.check_exercise(func)
        self.display_result()

class ExerciseFuncComplex():
    pass

class ExerciseTable():
    pass

class ExerciseData():
    pass




    
    
   
        



