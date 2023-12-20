import yaml

# Constant paths for train and val
train_path = "data\\train"
val_path = "data\\val"
nc_input = input("Enter the value for 'nc': ")
names_input = input("Enter the values for 'names' (comma-separated): ")

# Create a dictionary with the constant paths and user-input values
yaml_data = {
    "train": train_path,
    "val": val_path,
    "nc": int(nc_input),
    "names": names_input.split(',')
}


# Write the dictionary to a YAML file
with open("config.yaml", "w") as yaml_file:
    yaml.dump(yaml_data, yaml_file, default_flow_style=False)

print("YAML file created: config.yaml")
