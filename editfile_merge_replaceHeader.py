source = 'editfiles/edited/editfile_merged_wHeader.csv'
destination = 'editfiles/edited/editfile_merged_modified_Header.csv'

# read lines into list
with open(source, 'r') as file:
    content = file.readlines()

# take first list item and replace
content[0] = 'Email;ID;Password;Recovery;Name;Family;Department;Location' + '\n'

# write to file
with open(destination, 'w') as file:
    file.writelines(content)