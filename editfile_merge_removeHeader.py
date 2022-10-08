from pathlib import Path

source = Path('editfiles/raw_header')
destination = 'editfiles/edited/editfile_merged_wHeader.csv'
merged = ''

# loop over file path of raw files
for index, filepath in enumerate(source.iterdir()):
    with open(filepath, 'r') as file:
        # read lines and write to list
        content = file.readlines()
        # remove line containing header
        content_woHeader = content[1:]
        # but keep the first header
        if index == 0:
            # use join to turn list into string
            merged = merged + ''.join(content) + '\n'
        else:
            merged = merged + ''.join(content_woHeader) + '\n'

    with open(destination, 'w') as file:
        # write read content to destination file
        file.write(merged)