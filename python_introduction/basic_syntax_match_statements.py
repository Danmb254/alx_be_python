# basic syntax matching statement
day = input("Enter a day of the week (monday - sunday): ").lower()

match day:
    case "monday":
        print("Urg! mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday"|"sunday":
        print("Weekend vibes!")
    case _ :
        print("Invalid day entered.")