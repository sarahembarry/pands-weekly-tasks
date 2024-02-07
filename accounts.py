
AccountNo= input ('Please enter a 10 digit account number')

SlicedAccountNo= AccountNo[6:]

HiddenDigets= str('XXXXXX')

OutPutAccountNo= HiddenDigets+SlicedAccountNo
##LengthOfaccountNo = len(AccountNo)

##slicedaccountno = (accountno[6:10])

print (F"number is {OutPutAccountNo}")