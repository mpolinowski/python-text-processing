with open('editfiles/raw/editfile.csv', 'r') as file:
    content = file.read()

# print(content)
# slice off trailing ;END
print(content[:-4])

cleaned_content = content[:-4]

with open('editfiles/edited/editfile_cleaned.csv', 'w') as file:
    file.write(cleaned_content)