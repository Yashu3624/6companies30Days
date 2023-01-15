class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        for i , n1 in enumerate(transactions):
            name1 , time1 , amount1 , city1  = n1.split(',')
            if int(amount1) > 1000:
                invalid.append(n1)
                continue
            for j , n2 in enumerate(transactions):
                if i!=j:
                    name2 , time2 , amount2 , city2 = n2.split(',')
                    if name1 == name2 and city1!=city2 and abs(int(time1)-int(time2))<=60:
                        invalid.append(n1) 
                        break
        return invalid


        