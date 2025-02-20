import pandas as pd

def csv_to_adif(csv_file, adif_file):
    # Read CSV file
    df = pd.read_csv(csv_file)

    # Open ADIF file for writing
    with open(adif_file, "w", encoding="utf-8") as f:
        f.write("Generated by CSV to ADIF Converter\n<EOH>\n")  # ADIF header

        for _, row in df.iterrows():
            adif_entry = ""
            for col, value in row.items():
                if pd.notna(value):  # Ignore NaN values
                    adif_entry += f"<{col.upper()}:{len(str(value))}>{value} "
            adif_entry += "<EOR>\n"  # End of record
            f.write(adif_entry)

    print(f"Conversion complete! ADIF file saved as {adif_file}")

# Example usage
csv_to_adif("4X4KX_Log.csv", "output.adi")
