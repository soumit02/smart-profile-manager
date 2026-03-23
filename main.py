# created a dictionary where everyone's profile will be saved
profiles = {}

while True:
    # Interface design
    print("\n" + "="*40)
    print("   SMART PROFILE & SKILL MANAGER")
    print("="*40)
    print("1. Add New Profile")
    print("2. View a Profile")
    print("3. Exit")
    print("="*40)
    
    choice = input("Select your choice (1/2/3): ")
    
    if choice == '1':
        name = input("\nEnter the name: ").title()
        if name in profiles:
            print("\nAlready exists!")
        else:
            # Birth year and blood group
            dob = input("Enter the Birth Year: ")
            blood_group = input("Enter the Blood Group: ")
            basic_info = (dob, blood_group) 
        
            # Project name
            projects_input = input("Write your projects name: ")
            projects_list = projects_input.split(",") 
        
            # skills
            skills_input = input("Write down your skills: ").lower()
            skills_set = set(skills_input.split(",")) 
        
            # Saving all data together in one profile
            profiles[name] = {
                "Basic Info": basic_info,
                "Projects": [proj.strip() for proj in projects_list], # List comprehension for clean spacing
                "Skills": {skill.strip() for skill in skills_set} # Set comprehension
            }
            print(f"\n{name}'s profile has been successfully created!")


    elif choice == '2':
        search_name = input("\nEnter the name of the person you want to view the profile of: ").title()
        
        # Checking whether a profile exists
        if search_name in profiles:
            user_data = profiles[search_name]
            print("\n" + "-"*30)
            print(f"Profile of {search_name}")
            print("-"*30)
            # Showing data from a tuple
            print(f"Birth Year: {user_data['Basic Info'][0]}")
            print(f"Blood Group: {user_data['Basic Info'][1]}")
            
            # Displaying data from List
            print("\nProjects:")
            for project in user_data['Projects']:
                print(f"  - {project}")
                
            # Displaying data from Set
            print("\nSkills:")
            for skill in user_data['Skills']:
                print(f"   {skill}")
            print("-"*30)
        else:
            print(f"Sorry, no profile was found with the name '{search_name}'.")

    elif choice == '3':
        print("\nThe program is closing. Thank you!")
        break
        
    else:
        print("\nIncorrect input! Please press 1, 2 or 3.")