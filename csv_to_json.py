import pandas as pd
import argparse
import sys

def convert_csv_to_json(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        df.to_json(output_file, orient='records', lines=True)
        print(f"Successfully converted '{input_file}' to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert a CSV file to JSON format.')
    parser.add_argument('input_csv', help='Path to the input CSV file')
    parser.add_argument('output_json', help='Path to save the output JSON file')

    args = parser.parse_args()

    convert_csv_to_json(args.input_csv, args.output_json)

if __name__ == '__main__':
    main()
