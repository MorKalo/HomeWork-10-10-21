grade=int(input('pl insert a grade for a student'))
if grade<84:
    if grade<=55:
        print('הציון הוא בלתי מספיק')
    else:
        if grade<=64:
            print('הציון הוא  מספיק')
        else:
            if grade<=74:
                print('הציון הוא כמעט טוב')
            else:
                print('הציון הוא טוב')
else:
    if grade<=94:
        print('הציון הוא טוב מאוד')
    else:
        print('הציון הוא מצויין')