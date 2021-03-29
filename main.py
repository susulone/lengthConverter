#version 8

app_status = ""

while app_status != "e":

    value_input = input("Please enter the value you wish to convert: ")

    from_input = input("Unit to Convert from: ")
    to_input = input("Unit to Convert to: ")
    
    sql_where = "WHERE ([convert_from] = '" + str(from_input) + "' OR [convert_from_short] = '" + str(from_input) + "') "\
        "AND ([convert_to] = '" + str(to_input) + "' OR [convert_to_short] = '" + str(to_input) + "')"
    
    import sqlite3
    db_path = "/Users/susulone/Ohjelmointi/ConverterApp/lengthConverter/unit_converter.db"
    database_connection = sqlite3.connect(db_path)
    database_cursor = database_connection.cursor()

    database_cursor.execute("SELECT [factor] FROM [conversion_factors]" + sql_where + ";")
    found_data = database_cursor.fetchall()

    if len(found_data) > 0:
        conversion_factor = float(found_data[0][0])

        conversion_value = float(value_input)
        conversion_type = str(from_input) + "-" + str(to_input)
        
        print("{conv_type}: {conv_value:.2f}".format(conv_type = conversion_type, conv_value = conversion_value * conversion_factor))
        
    else:
        print("Your inputs don't make any sence.")

    app_status = input("Press any key to do another conversion or press 'e' to exit.")
