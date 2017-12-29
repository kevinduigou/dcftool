import math


def computeIntrinsicValue(dictValues):
	
	
	currentFCF = dictValues["Current FCF"] #million of dollar
	print ("Current Cash Flow: %f"%(currentFCF))
	outstandingNumberOfShare = dictValues["Outstanding Number Of Shares"] # million
	
	companyNetDebt = 0  # millionOfDollar
	
	estimateGrowthShortTerm = dictValues["Estimate Growth Short Term"]
	
	shortTermNbYears = dictValues["Short Term Nb of Year"]
	
	#estimateGrowthMidleTerm = 1.05
	
	#middleTermNbYears = 0
	
	estimateGrowthLongTerm = 1.03
	
	discountRate = dictValues["Discount Rate"]
	
	#Build the list of estimated Growth per year
	estimateGrowthList = []
	
	
	for y in range(0,shortTermNbYears):
		estimateGrowthList.append(estimateGrowthShortTerm)
	
	# for y in range(0,middleTermNbYears):
		# estimateGrowthList.append(estimateGrowthMidleTerm)
	
	
	
	# Gordon Growth Model: Terminal value = projected cash flow for final year (1 + long-term growth rate) / (discount rate - long-term growth rate).
	# Read more: Discounted Cash Flow (DCF) https://www.investopedia.com/terms/d/dcf.asp#ixzz52dpIv8ga
	
	projectedCashFlowForFinalYear = currentFCF
	print("Estimate Growth List",estimateGrowthList)
	for growthPerYear in estimateGrowthList:
		projectedCashFlowForFinalYear =  projectedCashFlowForFinalYear * growthPerYear
	
	
	#DPCF = projectedCashFlowForFinalYear  * estimateGrowthLongTerm / (discountRate - estimateGrowthLongTerm + 1)
	DPCF = currentFCF * math.pow(estimateGrowthShortTerm,shortTermNbYears +1)  * estimateGrowthLongTerm / (discountRate - estimateGrowthLongTerm + 1) / math.pow(1 + discountRate,shortTermNbYears +1)
	
	
	DFCFperYear = []
	DFCFperYear.append(currentFCF)
	for growthPerYear in estimateGrowthList:
		nextFreeCashFlow = DFCFperYear[-1] * growthPerYear
		DFCFperYear.append(nextFreeCashFlow)
	
	
	DFCFperYear.pop(0)
	
	print ("DFCF for next %i Years"%(shortTermNbYears), DFCFperYear)
	
	
	#DCF of Company X = (55 / 1.081) + (60.5 / 1.082) + (63.53 / 1.083) + (66.70 / 1.084) + (70.04 / 1.085) + (1,442.75 / 1.085) = 1231.83
	SumOfDFCF = 0
	i = 0
	for estimateFreeCashFlow in DFCFperYear:
	
		i += 1
		SumOfDFCF += (estimateFreeCashFlow / (math.pow(1 + discountRate , i)))
		
		#print ("%f / (%f)"% (estimateFreeCashFlow,math.pow(1 + discountRate , i)))
		
	print ("Sum of DFCF: %f"%(SumOfDFCF))
	
	
	print ("Discontinued Perpetuity Cash Flow: %f"%(DPCF))
	
	print ("Estimated intrinsic Value: %f"%(((SumOfDFCF + DPCF))/outstandingNumberOfShare))

def computeCashFlowGrowth(pastCashFlow,currentCashFlow,nbOfYearBetweenBoth):
	return math.pow(currentCashFlow/pastCashFlow,1/nbOfYearBetweenBoth)

if __name__ == "__main__":
	
	
	
	dictValues = {"GOOG" : {"Current FCF": 25820,"Outstanding Number Of Shares": 694.80, "Estimate Growth Short Term" : 1.18, "Short Term Nb of Year": 5,"Discount Rate": 1.0849},
	"FB" : {"Current FCF": 11617	,"Outstanding Number Of Shares": 2905.81, "Estimate Growth Short Term" : 1.30, "Short Term Nb of Year": 6,"Discount Rate": 1.0619},
	"CAPMF" : {"Current FCF": 1122		,"Outstanding Number Of Shares": 167.91, "Estimate Growth Short Term" : 1.08, "Short Term Nb of Year": 8,"Discount Rate": 1.0671},
	"BABA" : {"Current FCF": 62780		,"Outstanding Number Of Shares": 2565.83, "Estimate Growth Short Term" : 1.30, "Short Term Nb of Year": 6,"Discount Rate": 1.10}}
	#Parameters to compute the intrinsic value
	
	selectedTicker = "BABA"
	
	print ("### %s Intrinsic Value Estimation ###"%(selectedTicker))
	computeIntrinsicValue(dictValues[selectedTicker])
	
	
	

	

	

