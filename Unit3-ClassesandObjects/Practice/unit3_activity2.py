from dataclasses import dataclass

@dataclass
class Employee:
    name:str
    job_title:str
    hourly:bool
    pay_in_cents:int

    def hourly_pay(self):
        if self.hourly:
            print(f"{self.name}'s pay for 80 hours: ${((self.pay_in_cents * 80)/100):.2f}")
    
    def salary_pay(self):
        if not self.hourly:
            print(f"{self.name}'s pay for 2 weeks: {((self.pay_in_cents/26)/100):.2f}")

    def paycheck(self):
        if self.hourly:
            self.hourly_pay()
        else:
            self.salary_pay()

employee = Employee("Nick", "Mafia Boss", True, 1000)
employee.paycheck()
