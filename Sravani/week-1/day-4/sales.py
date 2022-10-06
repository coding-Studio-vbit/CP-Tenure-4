def maxRevenue(salesRecord):
    out = []
    for i in salesRecord:
        out.append(max(i))
    return out


salesRecord = []
salesRecord_rows,salesRecord_cols = map(int,input.split())
for idx in range(salesRecord_rows):
    salesRecord.append(list(map(int,input().split())))
result = maxRevenue(salesRecord)
print(" ".join([str(res) for res in result] ))    