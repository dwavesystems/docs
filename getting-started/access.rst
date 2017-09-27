.. _Access:

===================================
Accessing the |dwave_short| System
===================================

System Access and User Roles
===================================

Access to the D-Wave system is controlled by membership in *projects* configured in the system.
When you are assigned to a project, you get access to resources such as the solvers that are associated with it.
The tokens that you use to submit problems are allocated per project.

* Users---Authorized to run and manage their own problems in the system.
* Project managers---Authorized to manage shared datasets.
* Resource managers---Authorized to set up users, projects, and quotas; this role is currently available only to D-Wave Support personnel.

Log On to Qubist
==================

The Qubist web user interface is your point of entry to the D-Wave system.
For best performance, access |ui| using the latest stable version of one of the following browsers:

* Google Chrome
* Safari

To log on:

1. Go to the URL for your system.
2. From the Qubist home page, click any link.
3. When prompted, enter your user name and password.
   If necessary, you can request a password reset from the **Login** page.

Find Solvers
====================

You need to specify a solver when submitting a problem to the system.
To find the names of the solvers that you have access to, check the |ui| Home page.
To see the detailed properties of a solver and the problem parameters it accepts,
click on its name for more information.

Create an API Token
====================

To submit a problem to the |dwave_short| system, you require an API *token*,
which the system uses to authenticate the client session when
connecting to the remote environment. Because we use tokens for authentication,
user names and passwords are not required in code. Furthermore, because tokens are
associated with the projects defined in the system, they allow problems to be tracked
by project. You can generate as many tokens as you need through |ui|.

1. From any page, click your user name in the top menu bar and select **API Tokens**.
2. On the Token Management page, click **Create Token**.
3. In the Create New Token dialog box, select your project from the list and click **Create**.
   The system generates a token associated with the project.
   The token is a lengthy string; you will cut and paste it when you are ready to submit a problem to the system.
