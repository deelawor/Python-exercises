while True:
    gate = input("Which Logic Gate do you wish to operate? ")
    print("NOTE: For Not Gate only one input can be processed at a time." + "\n" + " Carry Not Gate individually for both inputs. ")
    switch1 = input("Enter either \"0\" or \"1\" as first input")
    switch2 = input("Enter either \"0\" or \"1\" as second input")



    def and_gate(switch1, switch2):
        operation = int(switch1) * int(switch2)
        return operation


    def or_gate(switch1, switch2):
        if switch1 == "1" and switch2 == "1":
            operation = (int(switc1) + int(switch2) - 1)
            return operation
        else:
            operation = int(sitch1) + int(switch2)
            return operation

    def not_gate_switch1(switch1):
        if switch1 == "0":
            operation = 0 + 1
            return operation
        else:
            operation = 1
            return operation

    def not_gate_switch2(switch2):
        if switch2 == "0":
            operation = 0 + 1
            return operation
        else:
            operation = 1
            return operation

    def nand_gate(switch1, switch2):
        if switch1 == "1" and switch2 == "1":
            operation= 1 - 1
            return operation
        elif switch1 == "0" and switch2 == "0":
            operation = 0 + 1
            return operation
        else:
            operation = 0 + 1
            return operation

    def nor_gate(switch1, switch2):






