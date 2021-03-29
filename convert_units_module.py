def convert_units(all_inputs):
"""
    Convert value input by uset from one unit to another

    inputs: dict
    all_inputs["from_input"] = Units user wishes to convert from
    all_inputs["to_input"] = Units user wishes to convert to
    all_inputs["value_input"] = Value user wishes to convert

    outputs: dict
    sql_where = SQL where statement uset to query the database for the right conversion factor
    conversion_type = from unit (to) to unit ie kilometre to mile
    conversion_value = value of user input after conversion
    string_output = converson_type: conversion_value
"""

    input_value = all_inputs["value_input"]
    convert_from = all_inputs["from_input"]
    convert_to = all_inputs["to_input"]
    
    sql_where = "WHERE ([convert_from] = '" + str(convert_from) + "' OR [convert_from_short] = '" + str(convert_from) + "') "\
        "AND ([convert_to] = '" + str(convert_to) + "' OR [convert_to_short] = '" + str(convert_to) + "')"
    
    # Use database instead of dict
    import sqlite3
    db_path = "/Users/susulone/Ohjelmointi/ConverterApp/lengthConverter/unit_converter.db"
    database_connection = sqlite3.connect(db_path)
    database_cursor = database_connection.cursor()
    database_cursor.execute("SELECT [convert_from], [convert_to], [factor] FROM [conversion_factors]" + sql_where + ";")
    found_data = database_cursor.fetchall()

    if len(found_data) > 0:
        conversion_factor = float(found_data[0][2])
        from_unit = str(found_data[0][0])
        to_unit = str(found_data[0][1])
        
        conversion_type = str(from_unit) + " to " + str(to_unit)
        conversion_value = float(input_value)

        string_output = "{conv_type}: {conv_value:.2f}".format(conv_type = conversion_type, conv_value = conversion_value * conversion_factor)

    else:
        string_output = "Your inputs don't make any sence."

    function_outputs = dict()
    function_outputs ["sql_where"] = sql_where
    function_outputs ["conversion_type"] = conversion_type
    function_outputs ["conversion_value"] = conversion_value
    function_outputs ["string_output"] = string_output

    return function_outputs