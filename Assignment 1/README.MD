# Software Requirements Specification (SRS) 
## for 
# Centralized Reporting System 
### Version 1.0
### Prepared by Kristella Lepak
### Instructor: Dr. Jeffry Babb
#### West Texas A&M University
---
## 1. Introduction
### 1.1 Purpose
The purpose of this document is to build a web-based system to collect, track, analyze and produce reports about internal progress on a public health agency strategic plan.
### 1.2 Table of Contents
1. Introduction
   1. Purpose
   2. Table of Contents
2. Requirements Statements
   1. User Stories
   2. Use Cases
   3. Features
   4. Gherkin Validation
3. Specifications
   1. Concept
   2. UX Notes
   3. Interfaces (Controls)
   4. Behaviors
      1. Feature/Package A
      2. Feature/Package B
---
## 2. Requirements
### 2.1 User Stories
As a reporter, I want to see all the items I am responsible for updating so that I am aware of my responsibilities.

As an analyst, I want to see live updates on all selected items so that I can identify items that need attention.

As an admin, I want to send automatic email requests for updates to reporters so that I do not have to send manual email requests.

### 2.2 Use Cases
Figure 1. Business use case. Reporter view all assigned items.  
**ID:** CU 01  
**Preconditions:** User is assigned to items.  
**Postconditions:** None  

| User Intention | System Responsibility |
| --- | --- |
| Reporter logs into system view | Verifies login credentials |
| Selects ‘All Assignments’ | Loads a cached query view of all assigned items |
| Exits view | Return to user home page | 
### 2.3 Features
* Reporter-users can see all assigned items they are responsible for updating

### 2.4 Gherkin Validation
**Feature:** Reporter-users can see all assigned items they are responsible for updating

**Scenario:** Reporter-users see only their assigned items  
  Given Repoter A is assigned items  
  When Reporter A selects ‘All Assignments’  
  Then Reporter A sees all their assigned items

---
## 3. Specifications
### 3.1 Concept
### 3.2 UX Notes
### 3.3 Interfaces (Controls)
### 3.4 Behaviors
#### 3.4.1 [Feature/Package A]
#### 3.4.2 [Feature/Package B]
