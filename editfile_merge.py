from pathlib import Path

source = Path('editfiles/raw')
destination = 'editfiles/edited/editfile_merged.csv'
header = 'Login email;Identifier;One-time password;Recovery code;First name;Last name;Department;Location'

# create merge file and add header
with open(destination, 'w') as file:
    file.write(header + "\n")

# get file path of raw files
for filepath in source.iterdir():
    with open(filepath, 'r') as file:
        # read files in source one by one
        content = file.read()
        # remove ;END
        cleaned_content = content[:-4]
        print(cleaned_content)
    with open(destination, 'a') as file:
        # append read content to destination file
        file.write(cleaned_content + "\n")