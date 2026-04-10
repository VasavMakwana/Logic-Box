def main():
    
    print("Welcome to the Student Data Organizer!")
    print("Features: Generate patterns, analyze number ranges, or just explore Python logic.")
    print("-" * 30)

    while True:
        
        print("\n--- Main Menu ---")
        print("1. Pattern Generation (Right-Angled Triangle)")
        print("2. Number Analysis (Range Stats)")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")

        if choice == '1':
            
            try:
                rows = int(input("Enter the number of rows for the triangle: "))
                
                if rows <= 0:
                    print("Please enter a positive integer.")
                    continue
                
                print(f"\nGenerating {rows}-row triangle:")
                for i in range(1, rows + 1):
                    for j in range(i):
                        print("*", end=" ")
                    print() 
            except ValueError:
                print("Invalid input. Please enter a numeric value for rows.")

        elif choice == '2':
            
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                
                
                if end < start:
                    print("Error: The end of the range must be greater than or equal to the start.")
                    continue

                odd_numbers = []
                even_numbers = []
                total_sum = 0

                for num in range(start, end + 1):
                    total_sum += num
                    if num % 2 == 0:
                        even_numbers.append(num)
                    else:
                        odd_numbers.append(num)
                    
                    
                    if num == 0: 
                        pass 

                print(f"\nAnalysis for range {start} to {end}:")
                print(f"Even Numbers: {even_numbers}")
                print(f"Odd Numbers: {odd_numbers}")
                print(f"Sum of all numbers: {total_sum}")

            except ValueError:
                print("Invalid input. Please enter integers for the range.")

        elif choice == '3':
            
            print("\nThank you for using the Student Data Organizer. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()