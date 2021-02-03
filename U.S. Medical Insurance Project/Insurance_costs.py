class Patient:
    patient_id = 0
    def __init__(self, patient):
        # checking if the info to initiate the class is correct
        if type(patient) != dict:
            print("Error: patient given isnt a dictionary type")
            return None
        elif len(patient) != 7:
            print("Patient info incomplete or more info than expected")
            return None
        # initiating the class
        self.age = patient["age"]
        self.sex = patient["sex"]
        self.bmi = patient["bmi"]
        self.children = patient["children"]
        self.smoker = patient["smoker"]
        self.region = patient["region"]
        self.charges = patient["charges"]
        # There can be added info if needed, lets make sure to change the the parameters in the exceptions handler
    #If we want to convert our lass back to a dictionary , lets use this function
    def patient_to_dictionary(self):
        patient_dict ={}
        patient_dict["age"] = self.age
        patient_dict["sex"] = self.sex
        patient_dict["bmi"] = self.bmi
        patient_dict["children"] = self.children
        patient_dict["smoker"] = self.smoker
        patient_dict["region"] = self.region
        patient_dict["charges"] = self.charges