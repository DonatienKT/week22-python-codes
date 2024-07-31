'''
wrte a scrpit that will ask
'''

user_answer=""

while True:
    if user_answer not in ['yes', 'no']:
        user_answer=input("Do you want covid shot? Please enter (yes or no ): ").strip().lower()
    else:
        print("Valide choice")
        break 