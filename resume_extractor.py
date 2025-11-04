
import re, os, json

def extract_info_from_text(text):
    # Email regex
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    # Phone regex: matches various international/local formats
    phone_pattern = r'(?:\+?\d{1,3}[\s-]?)?(?:\(\d{2,4}\)[\s-]?|\d{2,4}[\s-])?\d{3,4}[\s-]?\d{3,4}'
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    # clean phones (remove empty/malformed)
    phones = [p.strip() for p in phones if len(re.sub(r'\D','',p))>=7]
    return {{'emails': list(set(emails)), 'phone_numbers': phones}}

def main():
    input_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_resumes')
    input_folder = os.path.abspath(input_folder)
    output = {{}}
    for fname in os.listdir(input_folder):
        if not fname.lower().endswith('.txt'): continue
        path = os.path.join(input_folder, fname)
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        output[fname] = extract_info_from_text(text)

    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'output'), exist_ok=True)
    out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output', 'output.json'))
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4)
    print('Extraction complete. Saved to', out_path)

if __name__ == '__main__':
    main()
