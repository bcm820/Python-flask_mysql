
class Patient(object):

    id = 0

    def __init__(self, name, allergies):
        Patient.id += 1
        self.id = Patient.id
        self.name = name
        self.allergies = allergies
        self.bed = "none"
        print "Patient #{} ({})".format(str(self.id), self.name), "file created."


class Hospital(object):

    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Unable to admit {}. Capacity full.".format(patient.name)
        else:
            self.patients.append([
                patient.name,
                patient.id
            ])
            print "Patient #{} ({})".format(str(patient.id), patient.name), "was admitted to hospital."
            self.bed = patient.id
            print len(self.patients), "of", self.capacity, "beds occupied."
        return self
    
    def discharge(self, patient):
        self.patients.remove([
            patient.name,
            patient.id
        ])
        print "Patient #{} ({})".format(str(patient.id), patient.name), "was discharged from hospital."
        patient.bed = "none"
        print self.capacity - len(self.patients), "of", self.capacity, "beds available."
        return self

patient1 = Patient("Bob", "peanuts")
patient2 = Patient("Sally", "gluten")
patient3 = Patient("Jim", "none")

print "---"

hospital = Hospital("Dojo Hospital", 2)
hospital.admit(patient1).admit(patient2).admit(patient3)
hospital.discharge(patient1).admit(patient3)