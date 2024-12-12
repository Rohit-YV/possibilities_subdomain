# Take user input for the domain, wordlist file path, and output file path
scope = input("Enter the domain (e.g., example.com): ").strip()
wordlist_path = input("Enter the path to the wordlist file: ").strip()
output_path = input("Enter the path to save the output file: ").strip()

# Read the wordlist file
try:
    with open(wordlist_path, 'r') as file:
        wordlist = file.read().split('\n')
except FileNotFoundError:
    print(f"Error: File not found at '{wordlist_path}'")
    exit()

# Generate subdomains and write to the output file
try:
    with open(output_path, 'w') as outfile:
        for word in wordlist:
            if not word.strip():
                continue
            subdomain = f"{word.strip()}.{scope}"
            print(subdomain)  # Print to console (optional)
            outfile.write(subdomain + '\n')  # Write to file
    print(f"Subdomains have been saved to '{output_path}'")
except Exception as e:
    print(f"Error: Unable to write to file '{output_path}'. {e}")
