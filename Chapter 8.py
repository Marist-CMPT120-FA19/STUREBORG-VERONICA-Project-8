def main():
    heatingdays = 0
    coolingdays = 0
    temperature = input("Enter average temperatures separated by commas:")
    temperature= temperature.split(",")
    for i in temperature:
        if float(i) < 60 or float(i) > 80:
            if float(i) < 60:
                heatingdays+=(60-(float(i)))
            else:
                coolingdays+= ((float(i))-80)
    print("The number of heating-days is" , heatingdays)
    print("The number of cooling-days is" , coolingdays)
main()



