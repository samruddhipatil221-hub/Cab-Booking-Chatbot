
import random


routes = {
    1: {
        "source": "Pune Station",
        "destination": "Shivajinagar",
        "distance": 5
    },
    2: {
        "source": "Swargate",
        "destination": "Kothrud",
        "distance": 8
    },
    3: {
        "source": "Hinjawadi",
        "destination": "Wakad",
        "distance": 10
    }
}


cab_rates = {
    1: {"name": "Auto", "rate": 12},
    2: {"name": "Sedan", "rate": 18},
    3: {"name": "SUV", "rate": 25}
}


def book_ride():
    print("\n========== BOOK YOUR RIDE ==========")

    # Choose cab type
    print("\nChoose Cab Type:")
    for key, cab in cab_rates.items():
        print(f"{key}. {cab['name']} - Rs.{cab['rate']}/km")

    try:
        cab_choice = int(input("Enter your cab choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if cab_choice not in cab_rates:
        print("Invalid cab choice!")
        return

    selected_cab = cab_rates[cab_choice]

    
    print("\nAvailable Routes:")
    for key, route in routes.items():
        print(
            f"{key}. {route['source']} to "
            f"{route['destination']} - {route['distance']} km"
        )

    try:
        route_choice = int(input("Enter your route number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if route_choice not in routes:
        print("Invalid route choice!")
        return

    selected_route = routes[route_choice]

   
    distance = selected_route["distance"]
    rate = selected_cab["rate"]
    fare = distance * rate

    print("\n========== RIDE DETAILS ==========")
    print(f"Source      : {selected_route['source']}")
    print(f"Destination : {selected_route['destination']}")
    print(f"Cab Type    : {selected_cab['name']}")
    print(f"Distance    : {distance} km")
    print(f"Rate        : Rs.{rate}/km")
    print(f"Total Fare  : Rs.{fare}")

  
    while True:
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirmation = input("Enter your choice: ").strip()

        if confirmation == "1":
            otp = random.randint(1000, 9999)
            print("\nBooking Confirmed Successfully!")
            print(f"Your 4-digit OTP is: {otp}")
            print("Please share the OTP with your driver.")
            print("Cancellation is not allowed after OTP sharing.")
            return

        elif confirmation == "2":
            print("\nRide cancelled successfully.")
            print("No OTP has been generated or shared.")
            return

        else:
            print("Invalid choice! Please enter 1 or 2.")


while True:
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        book_ride()

    elif choice == "2":
        print("\nThank you for using Cab Booking Chatbot!")
        print("Have a safe journey!")
        break

    else:
        print("Invalid menu choice! Please select 1 or 2.")
