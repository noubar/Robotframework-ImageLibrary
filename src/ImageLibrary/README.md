# Code Architecture Overview

**The codebase is organized into two primary folders:**

- [modules](\modules/): Contains the core logic of the library.
- [keywords](\keywords/): Handles all keywords and input error processing.


## modules
### Orchestrator
The orchestrator functions as the global memory of the library. It is responsible for:

- Determining the platform on which the code is running.
- Tracking the subprocesses initiated by the library.
- Managing user-selected strategies for picture recognition.
- Specifying where screenshots are saved and how they are named.

Each of these functionalities is encapsulated within its own class for modularity and clarity.

### Errors

The errors module contains a central exception class dedicated to handling all internal errors. It is distinct from the error handling mechanisms in the keywords folder, which deal specifically with exceptions arising from incorrect input (such as invalid arguments passed to keywords).

### Interactions

The interactions module manages all operating system interactions, including:

- File I/O operations.
- Copy-paste commands.
- Screenshot capture functions.

### Recognition

The recognition module is dedicated to image recognition logic. It includes a separate debug folder, which is exclusively used by developers for debugging purposes. This separation ensures that debugging tools do not interfere with the library’s core functionality.


## Keyword documentation
The keywords folder serves as the interface to the robot. It includes:

All supported keywords by the library.
Input error handling, ensuring that any incorrect keyword arguments or invalid inputs are properly managed.
This structure provides a clear separation between core logic and user interaction, allowing for easier maintenance and enhanced reliability of the library.
