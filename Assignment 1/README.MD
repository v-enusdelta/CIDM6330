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
The **Centralized Reporting System** is a web-based, object-oriented system that captures information related to a public health agency’s strategic priorities in the form of items. Items are either created or mirrored from other data sources (e.g., electronic health records, federal grant reporting, human resources, etc.) and assigned to reporters to provide periodic updates. There are four major modules: reporting system, database, web portal, and application administration (admin). Each module is integrated by a variety of tools including data pipelines, APIs, external data analysis software, scheduled jobs, and web applications. A critical component of this system are customized APIs which connect to a variety of agency databases that respect HIPAA controls and security.

The goals of this system are to:  
* Streamline and automate reporting from siloed data sources by creating data pipelines to a centralized server.
* Enable transparency on progress of agency strategic priorities by creating dashboards and reports
* Automate reporting for non-mirrored data sources by creating an email request system
* Enable data analysts to use external tools on the centralized database by creating an API
* Create and maintain a flexible history of progress on agency strategic priorities by enabling custom-views, re-labeling, and data inventory controls

### 3.2 UX Notes
UX Activity Diagram for CU 01
![UX Activity diagram for CU 01](https://github.com/v-enusdelta/CIDM6330/blob/main/Assignment%201/ux-flow-cu01.jpg)

### 3.3 Interfaces (Controls)
#### Wireframe Diagrams for CU 01
![CU01 wireframe diagram home screen](https://github.com/v-enusdelta/CIDM6330/blob/main/Assignment%201/cu01-uiWireframe01.drawio.png)
![CU01 wireframe diagram all assignments](https://github.com/v-enusdelta/CIDM6330/blob/main/Assignment%201/cu01-uiWireframe02.drawio.png)

#### User Controls by Role
**1. Reporter**
  - `All Assignments` (Button) → Displays all assigned items on a separate webpage.
  - `Update` (Button) → Submits a progress update to an item.

**2. Administrator**
  - `Assign` (Button) → Assigns an item to the specified user.
  - `Create Item` (Form) → Creates a new item.
  - `Request External Data` (Form) → Creates a request to an external data source
  - `Import External Data` (Button) → Initiates process to import a data source. 

**3. Analyst**
  - `Create Dashboard` (Form) → Creates a blank, new dashboard.
  - `Export` (Button) → Exports data into a variety of file types.

### 3.4 Behaviors
#### 3.4.1 [Feature/Package A]
#### 3.4.2 [Feature/Package B]
