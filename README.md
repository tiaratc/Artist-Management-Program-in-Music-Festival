Py Music Festival 2024 - Schedule Management Program

Overview

This project is create a Python program made to help organize and manage performance schedules for music festivals. It helps speed up the manual process of checking that artists and group members are not scheduled for shows that happen at the same time.

The program lets users add, view, update, delete, and check for conflicts in show schedules. It’s based on real challenges I faced while managing events with many artists.

Features

	1.	Add Show
		Users can add new shows with information like the group name, members, day, time, and hall. The program checks for duplicates and ensures the input is correct (e.g., time format).
	2.	View Shows
		Users can see all shows or filter them by group name, day, or hall. The shows are displayed in a simple table for easy reading.
	3.	Update Show
		Users can change the details of a show, such as the group name, members, day, time, and hall. The program ensures each show has unique details and checks for valid changes.
	4.	Delete Show
		Users can remove a show by its Contract ID. The program asks for confirmation to make sure the deletion is intentional.
	5.	Check for Conflicts
		The program checks if any group or member has overlapping shows at the same time. This helps avoid scheduling problems.

Tools and Libraries Used

	•	Tabulate: Displays show information in a clear table format.
	•	Colorama & Termcolor: Adds color to prompts and messages, making the app easier to use.
	•	PyInputPlus: Ensures safe and correct input from users.

How to Use

	1.	Login: The app has two roles: Admin and Regular. Admins can do everything (add, view, update, delete shows, and check conflicts), while Regular users can only view shows and check for conflicts.
	2.	Menu: Admin users can add, view, update, delete shows, and check for conflicts. Regular users can only view shows and check for conflicts.

Real-World Inspiration

This project is based on my experience managing music festivals, where hundreds of artists perform over several days in lots of different stages. The program helps prevent conflicts in the schedule and makes event planning smoother and easier.
