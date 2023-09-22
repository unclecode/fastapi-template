# Design

### Color Scheme
- Dark Blue (#0D3B66): Primary color
- Light Blue (#119DA4): Secondary color
- White (#FFFFFF): Background
- Grey (#C0C0C0): Text

### Typography
- Titles: Open Sans, Bold
- Body Text: Roboto, Regular
- Menu and Buttons: Lato, Semi-bold

### Iconography
- Simple and flat icons for navigation and actions
- AI-themed icons where applicable to denote automation

### Layout and Screens

#### 1. Homepage
- Top Bar: Logo on the left, "+" on the right
- Bottom Toolbar: "Home", "My Courses", "About Us", "AI Assistant"
- Main Section: Marketing and News Feed

#### 2. My Courses
- List of Courses: Presented in rows with title, number of modules, lessons, and steps, and a 'Tilted Triangle' icon to navigate to the dedicated course page

#### 3. Create New Course
- Two Options: Form interface and Chat Interface with AI assistant
- Input Fields/Form: Collect specific parameters based on the `CourseRequest` class
- Chat Interface: AI assistant guides the user through the course creation process
- Common Confirmation Page: Summary and final confirmation

#### 4. Course Generation Status
- Integrated in 'My Courses': Show the status of the course (e.g., "Under Generation") next to the course name

#### 5. Course Dedicated Page
- Course Header: Title, brief description, and button to open the course in the LMS
- Nested Navigation: Modules > Lessons > Steps
- Content Area: Descriptions, videos, quizzes, etc., depending on the step type

#### 6. AI Assistant
- Simple chat interface with input box and send button
- Messages between AI and user displayed above

#### 7. About Us
- Hero Image at the top
- List of clickable items leading to detailed pages, including "Company Overview", "Mission and Vision", "Team", "Contact Us", "Request Demo", and "Investor Application"

### Additional Features
- Email Collection: During the first interaction, collect email for contact purposes
- Email Notifications: Sent when the course is ready
- Future Login: Using the collected email and an auto-generated password


# Original Design Overview
## Home Page
```text
+---------------------------------------------------+
| [Logo]                                       "+"  |
+---------------------------------------------------+
|                                                   |
|                    Feeds Page                     |
|                                                   |
|     - Marketing Materials                         |
|     - News                                        |
|     - Updates                                     |
|                                                   |
+---------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant |
+---------------------------------------------------+
```

## Create Course Page - Form
```text
+--------------------------------------------------+
| <  [Logo]                                        |
+--------------------------------------------------+
|                                                  |
| Create New Course                                |
|                                                  |
| Course Name: [Input Field]                       |
| Age Group: [Dropdown]                            |
| Difficulty Level: [Dropdown]                     |
| Keywords: [Tag Input]                            |
| Prerequisites: [Text Area]                       |
| Number of Modules: [Input Field]                 |
| Is Project Based?: [Checkbox]                    |
| Project All Along?: [Checkbox]                   |
|                                                  |
| Optional Fields                                  |
| Focus Area: [Input Field]                        |
| Project Description: [Text Area]                 |
| Domain of Interest: [Input Field]                |
| External Context: [Text Area]                    |
|                                                  |
| [Submit Button]                                  |
+--------------------------------------------------+
```

## Create Course Page - Chat
```text
+--------------------------------------------------+
| <  [Logo]                                        |
+--------------------------------------------------+
|                                                  |
| Create New Course                                |
|                                                  |
| Chat Area:                                       |
| [AI]: What would you like to name your course?   |
| [User]: Game Development with Pygame             |
| [AI]: Great name! What age group is this for?    |
| [User]: 13-16                                    |
| [AI]: Got it! Are you ready to proceed?          |
|                                                  |
| ------------------------------------------------ |
| [Input Box]                             [Send]   |
+--------------------------------------------------+
```

## Create Course Page - Acknowledgement
```text
+--------------------------------------------------+
| <  [Logo]                                        |
+--------------------------------------------------+
|                                                  |
| Acknowledgment                                   |
|                                                  |
| Thank you for creating a course!                 |
|                                                  |
| Your course has been submitted successfully      |
| and is under generation.                         |
|                                                  |
| Next Steps:                                      |
| You will receive an email once your course       |
| is ready.                                        |
| [Go to My Courses]                               |
|                                                  |
+--------------------------------------------------+
```

## My Courses Page
```txt
+--------------------------------------------------+
| [Logo]                                     "+"   |
+--------------------------------------------------+
|                                                  |
| My Courses                                       |
|                                                  |
| Course 1   [Status: Generating]               >  |
| 5 Modules, 15 Lessons, 45 Steps                  |
| -------------------------------------------------|
| Course 2   [Status: Complete]                 >  |
| 3 Modules, 9 Lessons, 27 Steps                   |
| -------------------------------------------------|
| Course 3   [Status: Complete]                 >  |
| 4 Modules, 12 Lessons, 36 Steps                  |
| -------------------------------------------------|
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+

```

### Course Page
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
| Course Name: [Course Name]                       |
| Description: [Brief Description]                 |
| Objectives:                                      |
| - Objective 1                                    |
| - Objective 2                                    |
| Age Group: [Age Group]                           |
| Difficulty: [Difficulty]                         |
| Keywords: [Keyword 1, Keyword 2]                 |
| Prerequisites: [Prerequisites]                   |
| Project Description: [Project Description]       |
|                                                  |
| [Open in Learning Management System Button]      |
|                                                  |
| Modules                                          |
|                                                  |
| Module 1                                      >  |
| 5 Lessons, 15 Steps                              |
| -------------------------------------------------|
| Module 2                                      >  |
| 4 Lessons, 12 Steps                              |
| -------------------------------------------------|
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```

### Module Page
```txt
+--------------------------------------------------+
| [Logo]                                     "+"   |
+--------------------------------------------------+
|                                                  |
| Module Name: [Module Name]                       |
| Description: [Brief Description]                 |
| Objectives:                                      |
| - Objective 1                                    |
| - Objective 2                                    |
| Keywords: [Keyword 1, Keyword 2]                 |
|                                                  |
| Lessons                                          |
|                                                  |
| Lesson 1                                      >  |
| 5 Steps                                          |
| -------------------------------------------------|
| Lesson 2                                      >  |
| 3 Steps                                          |
| -------------------------------------------------|
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```

### Lesson Page
```txt
+--------------------------------------------------+
| [Logo]                                     "+"   |
+--------------------------------------------------+
|                                                  |
| Lesson Name: [Lesson Name]                       |
| Description: [Brief Description]                 |
| Objectives:                                      |
| - Objective 1                                    |
| - Objective 2                                    |
| Keywords: [Keyword 1, Keyword 2]                 |
| Prerequisites: [Prerequisites]                   |
| Duration: [Duration]                             |
| Additional Resources:                            |
| - Resource 1                                     |
| - Resource 2                                     |
|                                                  |
| Layout Plan: [Name]                              |
| Objective: [Objective]                           |
| Reason: [Reason]                                 |
|                                                  |
| Steps                                            |
|                                                  |
| Step 1 - Lecture                              >  |
| -------------------------------------------------|
| Step 2 - Quiz                                 >  |
| -------------------------------------------------|
| Step 3 - Video                                >  |
| -------------------------------------------------|
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```

### Step Page - Lecture
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
| Step 1 - Type: Lecture                           |
|                                                  |
| Topic: [Topic Name]                              |
|                                                  |
| Content:                                         |
| [Lecture content goes here]                      |
|                                                  |
|                                                  |
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```

### Step Page - Quiz
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
| Step 2 - Type: MCQ                               |
|                                                  |
| Question: [Question Text Here]                   |
|                                                  |
| Answers:                                         |
| [ ] Option 1                                     |
| [ ] Option 2                                     |
| [ ] Option 3                                     |
| [ ] Option 4                                     |
|                                                  |
| [Show Hint]                                      |
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```

### Step Page - Fill in the Blanks
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
| Step 3 - Type: FIB                               |
|                                                  |
| Question: [Question Text with a ___ for blank]   |
|                                                  |
| Answer: [Input Field]                            |
|                                                  |
| [Show Hint]                                      |
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```

### Step Page - Code
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
| Step 4 - Type: Code                              |
|                                                  |
| Question: [Coding Question Here]                 |
|                                                  |
| File Tabs: [HTML] [JavaScript] [CSS]             |
|                                                  |
| Read-Only Code Editor:                           |
| [Syntax-highlighted Pre-filled Code]             |
|                                                  |
|                                                  |
| [Show Hints]                                     |
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```

### Step Page - Video
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
| Step 5 - Type: Video                             |
|                                                  |
| Video Player:                                    |
| [Embedded Video Player Here]                     |
|                                                  |
|                                                  |
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```

### Step Page - Conversation
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
| Step 6 - Type: Conversation                      |
|                                                  |
| Chat Area:                                       |
| [Student]: Hello!                                |
| [AI]: Hi there! What would you like to discuss?  |
| [Student]: Let's talk about climate change.      |
| [AI]: Sure, what aspect interests you the most?  |
|                                                  |
|                                                  |
| -------------------------------------------------|
| [Input Box]                             [Send]   |
+--------------------------------------------------+
```

## AI Assistant
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
| AI Assistant                                     |
|                                                  |
| Chat Area:                                       |
| [AI]: How may I assist you today?                |
| [User]: Tell me more about your courses.         |
| [AI]: We offer a variety of courses in...        |
|                                                  |
| ------------------------------------------------ |
| [Input Box]                             [Send]   |
+--------------------------------------------------+
```

## About Us Page
```txt
+--------------------------------------------------+
| <  [Logo]                                  "+"   |
+--------------------------------------------------+
|                                                  |
|    [------------- Hero Image ---------------]    |
|                                                  |
| About Us                                         |
|                                                  |
| Company Overview                              >  |
| -------------------------------------------------|
| Mission and Vision                            >  |
| -------------------------------------------------|
| Team                                          >  |
| -------------------------------------------------|
| Contact Us                                    >  |
| -------------------------------------------------|
| Request Demo                                  >  |
| -------------------------------------------------|
| Investor Application                          >  |
| -------------------------------------------------|
|                                                  |
+--------------------------------------------------+
| Home  |  My Courses  |  About Us  |  AI Assistant|
+--------------------------------------------------+
```