stack=[]
isMatched=True

bracket=1
while isMatched:
	bracket=input("input bracket: ")
	if bracket=="":
		break
	if bracket=="{" or bracket=="(" or bracket=="[":
		stack.append(bracket)
	if bracket=="}" or bracket==")" or bracket=="]":
		if len(stack)==0:
			print("Unmatched closing bracket")
			isMatched=False
		else:
			match=stack[-1]
			stack.pop()
			isMatched=((bracket=="}" and match=="{") or (bracket==")" and match=="(") or (bracket=="]" and match=="["))
			if not isMatched:
				print("unmatched bracket")
if len(stack)!=0:
	print("unmatched opening bracket")
		
