import re
from collections import Counter
# ^count occurances of each word
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        # make PdfReader as an object
        # sctict = raises an exception if problems with reading a pdf file
        reader = PdfReader(pdf, strict=False)

        # display the pages to the user
        print('Pages:', len(reader.pages))
        print('_' * 10) # divider

        # pdf_text: list[str] = [page for page in reader.pages]
        # this doesnt return us a string
        # write a whole expression
        # then use methods assosiated with the page
        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        # returns us pages where the text of each page in a list
        # return pages back to the user
        return pdf_text

def count_words(text_list: list[str])  -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        # we are looking for these symbals in our string ,;?!.-
        # we want our word without explamation mark etc
        # print(split_text)
        # for empty spaces in count_words we doing the if check
        all_words += [word for word in split_text if word]

    return Counter(all_words)

def main():
    extracted_text: list[str] = extract_text_from_pdf('sample.pdf')
    # print(extracted_text)
    for page in extracted_text:
        print(page)
    #count_words(extracted_text)
    counter: Counter = count_words(text_list=extracted_text)

    for word, mentions in counter.most_common(20):
        print(f'{word:10}: {mentions} times')

if __name__ =='__main__':
    main()