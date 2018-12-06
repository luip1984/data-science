import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import sys
import unicodedata

# Get all unicode characters
all_chars = (chr(i) for i in range(sys.maxunicode))
# Get all non printable characters
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) == 'Cc')
# Create regex of above characters
control_char_re = re.compile('[%s]' % re.escape(control_chars))

def splitAppend(inputArray, separator):
    outputArray = []
    for item in  inputArray:
        values = str.split(item, separator)
        for value in values:
            outputArray.append(value.strip())
    return outputArray

def splitString(input, separators):
    outputArray = str.split(input, separators[0])
    for index in range(1, len(separators)):
        outputArray = splitAppend(outputArray,separators[index])
    return outputArray

def processIdColumn():
    pmids = []
    pmid_regex = re.compile('(PMID)?[\\.0-9]+')
    pmcids = []
    pmcid_regex = re.compile('P?MC(ID)?[0-9]+')
    for (index,value) in enumerate(df["ID"]):
        if isinstance(value, float):
            if np.isnan(value):
                #print('value is nan')
                #df["ID"][index] = None
                pmids.append(None)
                pmcids.append(None)
            else:
                pmids.append(str(value))
                pmcids.append(None)
        else:
            values = splitString(value, [ ' ', ',', "'", '"', "/", ':', '-', '(', ')' ])
            values = list(map(lambda x: x.strip(), values))
            values = list(filter(lambda x: x != '', values))
            pmid = ''
            pmcid = ''
            hasEPub = False
            shortId = False
            for part in values:
                if part.lower() == 'epub':
                    hasEPub = True
                if pmcid_regex.match(part):
                    #print('pmcid:', part)
                    if len(part) > 4:
                        pmcid = part
                    else:
                        shortId = True
                elif pmid_regex.match(part):
                    #print('pmid:', part)
                    if len(part) > 4:
                        pmid = part
                    else:
                        shortId = True
            #if hasEPub or shortId or (pmid == '' and pmcid == ''):
            #    print(pmid, pmcid, values, value)
            if pmid == '':
                pmids.append(None)
            else:
                pmids.append(pmid)
            if pmcid == '':
                pmcids.append(None)
            else:
                pmcids.append(pmcid)

    df['PMID'] = pmids
    df['PMCID'] = pmcids

def processPublisherColumn(df, publisher_mapping):
    publishers = []
    for (index,value) in enumerate(df["Publisher"]):
        rows = publisher_mapping[publisher_mapping.source.str.lower().isin([value.lower()])]
        #rows = publisher_mapping.loc[publisher_mapping['source'] == value.lower()]
        if len(rows) > 0:
            publishers.append(rows.values[0,1])
            #print(value, rows.values[0,1])
        else:
            publishers.append(None)
            print('Publisher mapping not found.', value)
    df['MappedPublisher'] = publishers
    df[['PMID', 'PMCID', "MappedPublisher", 'Journal_Title', 'Article_Title', 'COST']].to_csv('welcome2013_2.csv')

def processJournalColumn(df, journal_mapping):
    journals = []
    for (index,value) in enumerate(df["Journal_Title"]):
        #print(value)
        rows = journal_mapping[journal_mapping.source.str.upper().isin([value.upper()])]
        #rows = journal_mapping.loc[journal_mapping['source'] == value.lower()]
        if len(rows) > 0:
            journals.append(rows.values[0,1])
            #print(value, rows.values[0,1])
        else:
            journals.append(None)
            print('Journal mapping not found.', value)
    df['MappedJournal'] = journals
    df[['PMID', 'PMCID', "MappedPublisher", "MappedJournal", 'Article_Title', 'COST']].to_csv('welcome2013_3.csv')

#df = pd.read_csv('test2.csv', encoding='latin', keep_default_na=False)
#for (index,value) in enumerate(df["source"]):
#    df["source"][index] = control_char_re.sub('', value).strip()
#print(df)

df = pd.read_csv('welcome2013.csv', encoding='latin', keep_default_na=False)

publisher_mapping = pd.read_csv('publisher_mapping.csv', encoding='latin')
journal_mapping = pd.read_csv('Journal_Mapping.csv', encoding='latin')
df.rename(index=str, columns={"PMID/PMCID": "ID", 'Publisher': 'Publisher', "Journal title": "Journal_Title", 'Article title': 'Article_Title','COST (£) charged to Wellcome (inc VAT when charged)': 'COST'}, inplace=True)
print(df.columns)

for (index,value) in enumerate(df["Journal_Title"]):
    df["Journal_Title"][index] = control_char_re.sub('', value).strip()

processIdColumn()
processPublisherColumn(df, publisher_mapping)
processJournalColumn(df, journal_mapping)

#print(df[["Publisher", 'PMID', 'PMCID']])
