# Issue Overview
On March 18, 2023, between 11:00 AM and 12:20 PM, an incident transpired wherein unauthorized root access was inadvertently granted within the container environment due to the default configuration, which operated all processes under the root user.

## Chronological Events
11:10 AM: A developer mistakenly executed a command during routine tasks within the container environment, resulting in unintended consequences.
11:15 AM: The execution of the rm -rf / command within the container led to the deletion of critical system files and data.
11:15 AM: System monitoring tools detected abnormal activity within the container environment, prompting an immediate alert.
11:20 AM: Immediate measures were taken to cease all container operations and evaluate the extent of damage incurred.
11:24 AM: Confirmation was made that the root directory and essential system files were irretrievably deleted due to the erroneous command.

## Root Cause and Resolution
The principal cause of this incident stemmed from the default container environment configuration, which granted excessive privileges by running all processes under the root user. This setup enabled users within the container to execute commands with unrestricted access to system resources.

## Corrective and Preventative Measures
Following the unauthorized root access incident, prompt corrective actions were initiated, including halting container operations, commencing data recovery endeavors, and conducting a comprehensive incident analysis. To mitigate similar occurrences, a user-specific command execution script was devised, adhering to least privilege principles and diminishing reliance on root access. Additionally, ongoing evaluations of container security configurations, implementation of role-based access control, continuous monitoring, and user training initiatives were introduced to bolster security measures and cultivate a proactive security culture within the organization. These efforts collectively aim to reduce risks, enhance container security, and diminish the probability of future unauthorized access incidents.

