class Mechine(object):
    def run(self):
        print("the mechine is running.")
class computer(Mechine):
    def run(self):
        print("the computer is running")
class TV(Mechine):
    def run(self):
        print("the TV is running")

def run_twice(mechine):
    mechine.run()
    mechine.run()
run_twice(Mechine())
run_twice(computer())
run_twice(TV())