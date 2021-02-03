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
    def __repr__(self):
       return """ Patients Info:
        AGE: {age}
        SEX: {sex}
        BMI: {bmi}
        Number of children: {children}
        Smoker: {smoker}
        Region: {region}
        Insurance Costs: {charges}""".format(age = self.age, sex = self.sex, bmi = self.bmi, children = self.children, smoker = self.smoker, region = self.region, charges = self.charges)
 
    #If we want to convert our class back to a dictionary , lets use this function
    def patient_to_dictionary(self):
        patient_dict ={}
        patient_dict["age"] = self.age
        patient_dict["sex"] = self.sex
        patient_dict["bmi"] = self.bmi
        patient_dict["children"] = self.children
        patient_dict["smoker"] = self.smoker
        patient_dict["region"] = self.region
        patient_dict["charges"] = self.charges
        return patient_dict
    
    # THis next methods return the data asked for from the Patient class
    def get_patient_age(self):
        return self.age
        
    def get_patient_sex(self):
        return self.sex
    
    def get_patient_bmi(self):
        return self.bmi
    
    def get_patient_children(self):
        return self.children
    
    def get_patient_smoker(self):
        return self.smoker
    
    def get_patient_region(self):
        return self.region
    
    def get_patient_charges(self):
        return self.charges
    