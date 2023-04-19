# Import numpy and any other required packages here:
import numpy as np
import pandas as pd

def gradeInfo(filename, numExams, hwWeight):
    

    '''
    filename is a text string containing the name and extension of a file containing student scores.  For example, `grades_example.csv`.  See the example file for details about the file structure.

    numExams is an integer.  It tells us how many exams are in the gradebook.  Exams will always be in the last column(s).

    hwWeight is a float in [0,1].  This value tells us the percentage of the overall grade that is composed of the student's average homework percentage.  The remaining percentage will be applied to the average exam percentage.  For example, if hwWeight = 0.3, then the exams are weighted by 0.7 (0.3 + 0.7 = 1.0).
    '''
    dt_frame = pd.read_csv(filename, skiprows=3)
    dt_frame = dt_frame.iloc[:-9]

     #1
   
    avg = (dt_frame['HW1'].mean() / dt_frame['HW1'].max()) * 100  

     #2
    df_sorted = dt_frame.sort_values(by='HW2', ascending=False)
    desc = df_sorted[['ID', 'HW2']].values[:, [0, 1]]
    desc[:, 1] = (desc[:, 1] / dt_frame['HW2'].max()) * 100

     #3
    greater_90 = dt_frame.loc[(dt_frame['HW1'] >= 90) & (dt_frame['HW3'] >= 90), 'ID'].to_numpy()

     #4
    lesser_80 = dt_frame.loc[(dt_frame['HW1'] <= 80) & (dt_frame['HW2'] >= 90)].shape[0]

     #5
    exam_weight = 1-hwWeight
    hw1_val = dt_frame['HW1'] / 10
    hw2_val = dt_frame['HW2'] / 5
    hw3_val = dt_frame['HW3'] / 50
    hw4_val = dt_frame['HW4'] / 40 
    sum= hw1_val+hw2_val+hw3_val+hw4_val



    hw_avg = (sum) / 4 * hwWeight
    exam_avg = dt_frame['Exam 1'] / 100 * exam_weight
    weighted_avg = (exam_avg + hw_avg) * 100
    results = np.column_stack((dt_frame['ID'], weighted_avg))
    return (avg,desc,greater_90,lesser_80,results)	# Edit this to return the appropriate results


