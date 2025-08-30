def read_and_modify_file():
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Create a new filename for the output
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ File processed successfully. Modified content saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f" Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f" Error: Could not read or write to the file '{input_filename}'.")

# Run the function
read_and_modify_file()
