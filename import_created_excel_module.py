import  os
import census2010

census2010.allData['AK']['Anchorage']    # Access the AK dictionary key and the Anchorage dictionary key
anchoragePop = census2010.allData['AK']['Anchorage']['pop']    #  AK dictionary-> Anchorage dictionary-> to access the pop value in the anchorage dictionary and save to variable
print('The 2010 population of Anchorage was ' + str(anchoragePop))  #print the dictionary value that is saved in variable
