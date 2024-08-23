weight=float(input("enter your 'weight' in kilograms  "))
height=float(input("enter your height in meters  "))
BMI= round(weight/height**2,4)
BMI_prime= round(BMI/25,4)
if BMI<16.0 or BMI_prime<0.64:
    print("you are 'under weight'(that means you have 'severe thinness' stage)")
elif (BMI==16.0 or BMI<=16.9) or (BMI_prime==0.64 or BMI_prime<=0.67):
    print("you are 'under weight'(that means you have 'moderate thinness' stage)")
elif (BMI==17.0 or BMI<=18.4) or (BMI_prime==0.68 or BMI_prime<=0.73):
    print("you are 'under weight' (that means you have 'mild thinness' stage)")
elif (BMI==18.5 or BMI<=24.9) and (BMI_prime==0.74 or BMI_prime<=0.99):
    print("you have 'normal range weight' ")
elif (BMI==25.0 or BMI<=29.9) and (BMI_prime==1.00 or BMI_prime<=1.19):
    print("you are 'over weight'(that means you have 'pre-obese' stage)")
elif (BMI==30.0 or BMI<=34.9) and (BMI_prime==1.20 or BMI_prime<=1.39):
    print("you are 'obessed' (class-I)")
elif (BMI==35.0 or BMI<=39.9) and (BMI_prime==1.40 or BMI_prime<=1.50):
    print("you are 'obessed'(class-II)")
elif (BMI==40.0) and (BMI_prime<=60):
    print("you are 'obessed'(class-III)")
