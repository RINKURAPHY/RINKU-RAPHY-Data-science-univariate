# This is Univariate.py

class Univariate:
    def quanQual(self, dataset):  # Method definition must be indented under the class
        quan = []  # Indented code inside the method
        qual = []  # Indented code inside the method

        for columnName in dataset.columns:  # The for loop should be indented
            if dataset[columnName].dtype == 'O':  # If statement inside the loop must be indented
                qual.append(columnName)  # Indented action under the 'if' statement
            else:
                quan.append(columnName)  # Indented action under the 'else' statement

        return quan, qual  # The return statement must also be indented within the method


    