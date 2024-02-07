
AccountNo= input ('Please enter a 10 digit account number')

SlicedAccountNo= AccountNo[6:]

HiddenDigets= str('XXXXXX')

OutPutAccountNo= HiddenDigets+SlicedAccountNo
##LengthOfaccountNo = len(AccountNo)



print (F"number is {OutPutAccountNo}")