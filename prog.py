import pandas as pd

if __name__ == "__main__" :
    df = pd.read_csv('data.txt', delimiter=' ', header=None, names=['Country', 'ASN','TS1', 'TS2', 'Metric A', 'Co-Server', 'Bytes', 'Send/Time'])

    df['TS1'] = df['TS1'] + df['TS2']
    df = df.drop(df.columns[3], axis=1)

    cs = df.groupby('Co-Server')
    asn = df.groupby('ASN')

    for name,group in cs:
        print(name)
        tb = sum(group['Bytes'])
        ts = sum(group['Send/Time'])
        if ts > 0:
            avg = sum(group['Bytes'])/sum(group['Send/Time'])
        else:
            avg = 'inf'
        print(avg)

    for name,group in asn:
        print(name)
        tb = sum(group['Bytes'])
        ts = sum(group['Send/Time'])
        if ts > 0:
            avg = sum(group['Bytes'])/sum(group['Send/Time'])
        else:
            avg = 'inf'
        print(avg)
        print("\n")