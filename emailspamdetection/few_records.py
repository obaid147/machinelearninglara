import pandas as pd

mails = pd.read_csv('/home/aamir/Desktop/datasets/spam_ham_few_records.csv')
mails.rename(columns={'v1': 'labels', 'v2': 'message'}, inplace=True)
mails['label'] = mails['labels'].map({'ham': 0, 'spam': 1})
mails = mails.drop(['labels'], axis=1)
print(mails)
