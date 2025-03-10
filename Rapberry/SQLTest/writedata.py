import psycopg2

try:
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        user="postgres",
        host="localhost",
        database="Acurev1313_ModbusAddress",
        password="Tono2002",  # luis: Tono2002 //Arturo: 2705
        port=5432
    )
    print('Connected to the database.')

    # Function to insert data into a specified table
    def write_meas(table_name):
        with conn.cursor() as cur:
            # Format the table name in the query string
            insert_query = f"""
            INSERT INTO {table_name} (
                amps_total,
                amps_phase_a,
                amps_phase_b,
                amps_phase_c,
                voltage_ln_average,
                phase_voltage_an,
                phase_voltage_bn,
                phase_voltage_cn,
                voltage_ll_average,
                phase_voltage_ab,
                phase_voltage_bc,
                phase_voltage_ca,
                frequency,
                total_real_power,
                watts_phase_a,
                watts_phase_b,
                watts_phase_c,
                ac_apparent_power_va,
                va_phase_a,
                va_phase_b,
                va_phase_c,
                reactive_power_var,
                var_phase_a,
                var_phase_b,
                var_phase_c,
                power_factor,
                pf_phase_a,
                pf_phase_b,
                pf_phase_c,
                total_real_energy_exported,
                total_watt_hours_exported_in_phase_a,
                total_watt_hours_exported_in_phase_b,
                total_watt_hours_exported_in_phase_c,
                total_real_energy_imported,
                total_watt_hours_imported_phase_a,
                total_watt_hours_imported_phase_b,
                total_watt_hours_imported_phase_c,
                total_va_hours_exported,
                total_va_hours_exported_phase_a,
                total_va_hours_exported_phase_b,
                total_va_hours_exported_phase_c,
                total_va_hours_imported,
                total_va_hours_imported_phase_a,
                total_va_hours_imported_phase_b,
                total_va_hours_imported_phase_c,
                total_var_hours_imported_q1,
                total_var_hours_imported_q1_phase_a,
                total_var_hours_imported_q1_phase_b,
                total_var_hours_imported_q1_phase_c,
                total_var_hours_imported_q2,
                total_var_hours_imported_q2_phase_a,
                total_var_hours_imported_q2_phase_b,
                total_var_hours_imported_q2_phase_c,
                total_var_hours_exported_q3,
                total_var_hours_exported_q3_phase_a,
                total_var_hours_exported_q3_phase_b,
                total_var_hours_exported_q3_phase_c,
                total_var_hours_exported_q4,
                total_var_hours_exported_q4_phase_a,
                total_var_hours_exported_q4_phase_b,
                total_var_hours_exported_q4_phase_c
            ) 
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
            """

            # Define the data to be inserted (use None for null values)
            data_to_insert = (
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
            )

            # Execute the query
            cur.execute(insert_query, data_to_insert)

            # Commit the transaction to save the changes
            conn.commit()
            print(f"Data inserted into {table_name} successfully.")
    
    # Call the function with your table name
    write_meas('power_meter_readings')

except Exception as error:
    print(f"Error executing query: {error}")

finally:
    # Close the connection
    if conn:
        conn.close()
        print('Connection closed.')
