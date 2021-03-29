# Access the engine
from convert_units_module import convert_units

app_status = ""

while app_status != "e":

    value_input = input("Please enter the value you wish to convert: ")

    from_input = input("Unit to Convert from: ")
    to_input = input("Unit to Convert to: ")

    # Set up the engine installation
    user_inputs = {"value_input" : value_input, "from_input" : from_input, "to_input" : to_input,}
    conversion_outputs = dict()

    # Call the engine
    conversion_outputs = convert_units(user_inputs)
    print(conversion_outputs["string_output"])

    app_status = input("Press any key to do another conversion or press 'e' to exit.")
