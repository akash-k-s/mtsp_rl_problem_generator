

class problem_statement():
    def __init__(self):
        super().__init__('problem_statement')
        self.workspace_dim = []
        self.payload_masses = []
        self.drone_capacities = []
        self.number_drones
        self.number_payload
        self.paylaod_list
        self.drones_list

    def set_workspace_dim(self,x,y):
        self.set_workspace_dim = [x,y]
    
    def return_workspace_dim(self):
        return self.set_workspace_dim
    
    def set_payload_masses(self,masses):
        for i in range(len(masses)):
            self.payload_masses[i] = masses[i]
    
    def return_payload_masses(self):
        return self.payload_masses
    
    
            