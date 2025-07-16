# String methods str.removeprefix() and str.removesuffix()

url = 'https://example.com'
cleaned_url = url.removeprefix('https://') # Removes the 'https://' prefix from the URL leaving use just the domain of the URL
print(cleaned_url)
# removeprefix() is useful when you want to clean up URLs or other strings that have a common prefix, such as 'http://' or 'https://', making it easier to work with the core part of the string.

filename = 'report_2024.pdf'
cleaned_filename = filename.removesuffix('.pdf') # removes the '.pdf' suffix from the filename leaving just the name of the file
print(cleaned_filename)
# removesuffix() is particularly used when you want to remove a specific file extension from a filename without affecting the rest of the string.
# This is useful when you want to process filenames without their extensions, such as when generating reports or logs.
