import pandas


def convert_csv_to_json(file):
    try:
        csv_data = pandas.read_excel(file)
        json_data = csv_data.to_json(orient="records", indent=4)
        with open("record.json", mode="w") as f:
            f.write(json_data)
        print("Csv succesfully converted to json")
    except Exception as e:
        print(f"An error ocuured: {e}")


if __name__ == "__main__":
    csv_file = input("Enter the file name:   ")
    convert_csv_to_json(csv_file)
