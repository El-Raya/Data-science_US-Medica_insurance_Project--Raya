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
    
 #functions for insurances costs
def patients_insurances_list(patients): #returns a list that has all the insurances costs from a list of patients
    patients_insurances_costs = []
    for patient in patients:
        patients_insurances_costs.append(patient.get_patient_charges())
    return patients_insurances_costs

def average_insurance_cost(insurances): # The funtion gets a list that cntains the insurance
    total_insurance = 0
    for insurance in insurances:
        total_insurance += float(insurance) # has the insurances are stored in strings we need o convert them to float number to make operations
    return total_insurance/len(insurances) # The function returns the average

# functions for patients ages
def get_all_patients_ages(patients): #Creating list containing th ages of the patients
    patients_ages_list = []
    for patient in patients:
        patients_ages_list.append(patient.age)
    return patients_ages_list

def average_age_for_patients(ages): # Calculate the average age 
    total_ages = 0.0
    for age in ages:
        total_ages += int(age)
    return total_ages/len(ages)

# sex data funtions
def split_patients_by_sex(patients): # Returns a dictionary spliting the patients by their sex
    patients_by_sex = {}
    for patient in patients:
        if patient.sex in patients_by_sex:
            patients_by_sex[patient.sex].append(patient)
        else:
            patients_by_sex[patient.sex] = [patient]
    return patients_by_sex

def how_many_males_and_females(patients_sex): # returns two variables containing the number of males and females out of a dict whit this two keys
    males = len(patients_sex["male"])
    females= len(patients_sex["female"])
    return males, females

# bmi data funtions
def split_patients_by_bmi(patients): # split the patients depending if their bmi is under, over or between certainn value of bmi
    underweight = 18.50
    normal_weight = 24.90
    overweight = 29.90
    patients_bmi_dict ={"Underweight": [], "Normal weight": [], "Overweight": [], "Obesity": []}
    
    for patient in patients:
        bmi = float(patient.bmi)
        if bmi < underweight:
            patients_bmi_dict["Underweight"].append(patient)
        elif bmi >= underweight and bmi <= normal_weight:
            patients_bmi_dict["Normal weight"].append(patient)
        elif bmi > normal_weight and bmi <= overweight:
            patients_bmi_dict["Overweight"].append(patient)
        elif bmi > overweight:
            patients_bmi_dict["Obesity"].append(patient)
    return patients_bmi_dict

def num_of_patients_bmi(patients_bmi): # returns the number of patints in each category of bmi we already defined
    num_underweight = len(patients_bmi["Underweight"])
    num_normal_weight = len(patients_bmi["Normal weight"])
    num_overweight = len(patients_bmi["Overweight"])
    num_obesity = len(patients_bmi["Obesity"])
    return num_underweight, num_normal_weight, num_overweight, num_obesity

def average_bmi(patients):
    total_bmi = 0
    for patient in patients:
        total_bmi += float(patient.bmi)
    return total_bmi/len(patients)

# children data funtions
def patients_by_num_children(patients):
    patients_children_dict = {}
    for patient in patients:
        num_children = int(patient.children)
        if num_children in patients_children_dict:
            patients_children_dict[num_children].append(patient)
        else:
            patients_children_dict[num_children] = [patient]
    return patients_children_dict

# smoker data functions
def split_patients_by_smoking(patients):
    patients_smoking_dict = {"Smoker": [], "Non-smoker": []}
    for patient in patients:
        if patient.smoker == "yes":
            patients_smoking_dict["Smoker"].append(patient)
        else:
            patients_smoking_dict["Non-smoker"].append(patient)
    return patients_smoking_dict

def how_many_patients_smoke(patients_smoking):
    smoker = len(patients_smoking["Smoker"])
    return smoker
def how_many_patients_no_smoke(patients_smoking):
    non_smoker = len(patients_smoking["Non-smoker"])
    return non_smoker

# region data funtions
def split_patients_by_region(patients):
    patients_region_dict = {}
    for patient in patients:
        if patient.region in patients_region_dict:
            patients_region_dict[patient.region].append(patient)
        else:
            patients_region_dict[patient.region] = [patient]
    return patients_region_dict
# We need to know that each of the functons separeted by the data they study may work out of a list that contains the patients info in the class Patient form as well as some of them work out from the result of other funtion of the same data

def average_insurance_cost_by_region(patients):
    global_average = average_insurance_cost(patients_insurances_list(patients))
    print("The average insurance cost is: {}. \n".format(global_average))
    patients_by_region_list = split_patients_by_region(patients)
    for region in patients_by_region_list:
        #print(patients_regions[region])
        insurances_list_region = patients_insurances_list(patients_by_region_list[region])
        #print(insurances_list)
        average_region_insurance = average_insurance_cost(insurances_list_region)
        average_dif = average_region_insurance -average_insurance 
        print("For the {} region  the average insurance cost is: {} with a difference of {} with the global average insurance cost.\n".format(region.upper(), average_region_insurance, average_dif))
        
        #this funtion can be split in different little functions that print certain info we may want as well as there can be made a lot of other functions to print other info out of the dataset
def counting_patients(patients):
    # first we count the males and females in the data given
    patients_sex_dict = split_patients_by_sex(patients)
    males, females = how_many_males_and_females(patients_sex_dict)
    print("There are {} males and {} females on the data given.\n".format(males,females))
    
    #next we count people by their bmi condition
    patients_bmi_dict = split_patients_by_bmi(patients)
    underweight_patients, normal_weight_patients, overweight_patients, obese_patients = num_of_patients_bmi(patients_bmi_dict)
    print(""" 
    There are {} patients with an underweight condition.
    There are {} patients with a normal weight.
    There are {} patients with an underweight condition.
    There are {} patients with an obesity condition.\n""".format(underweight_patients, normal_weight_patients, overweight_patients, obese_patients))
    
    # counting people by the number of children they have
    patients_children_dict = patients_by_num_children(patients)
    for children in patients_children_dict.keys():
        if children == 0:
            print("There are {} patients with no child".format(len(patients_children_dict[children])))
        elif children == 1:
            print("There is {} patients with a child".format(len(patients_children_dict[children])))
        else:
            print("There is {} patients with {} children".format(len(patients_children_dict[children]), children))
    
    # counting people by their smoker status
    patients_smoking_dict = split_patients_by_smoking(patients)
    num_smokers = how_many_patients_smoke(patients_smoking_dict)
    num_non_smokers = how_many_patients_no_smoke(patients_smoking_dict)
    print("\nThere are {} patients that smoke and {} patients dont smoke.\n".format(num_smokers, num_non_smokers))
    
    #counting people by their region
    patients_region_dict = split_patients_by_region(patients)
    for region in patients_region_dict:
        print("There are {} patients in the {} region.".format(len(patients_region_dict[region]), region.upper()))
        
    #counting males and females by their bmi condition
    for cond in patients_bmi_dict:
        condition_by_sex_dict = split_patients_by_sex(patients_bmi_dict[cond])
        male_with_cond, female_with_condi = how_many_males_and_females(condition_by_sex_dict)
        print("There are {} males and {} females with {} condition.".format(male_with_cond, female_with_condi, cond))
    
    # counting males and females by their num of children
    for children in patients_children_dict:
        children_by_sex_dict = split_patients_by_sex(patients_children_dict[children])
        male_child, female_child = how_many_males_and_females(children_by_sex_dict)
        if children == 0:
            print("\nThere are {} males and {} females with no child.".format(male_child, female_child))
        elif children == 1:
            print("There are {} males and {} females with one child.".format(male_child, female_child))
        else:
            print("There are {} males and {} females with {} children.".format(male_child, female_child, children))
            
    # counting males and females by their smoke condition
    for dict in patients_smoking_dict:
        sex_by_smoke_cond = split_patients_by_sex(patients_smoking_dict[dict])
        smoking_male, smoking_female = how_many_males_and_females(sex_by_smoke_cond)
        if dict == "Smoker":
            print("\nThere are {} males and {} females that smoke.".format(smoking_male, smoking_female))
        else:
            print("There are {} males and {} females that dont smoke.\n".format(smoking_male, smoking_female))
            
    #counting male and females by region
    for region in patients_region_dict:
        region_by_sex_dict = split_patients_by_sex(patients_region_dict[region])
        region_males, region_females = how_many_males_and_females(region_by_sex_dict)
        print("There are {} males and {} females in the {} region".format(region_males, region_females, region.upper()))
    
        
