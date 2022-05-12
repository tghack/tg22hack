# nonhosted-template
> Author: Kritt

## PatchNotes

## Chall
### Description
SecOpsCommand have gotten information from a third party indicating that the threat actor we call FerRAT downloads software from GitHub to the victims machine after initial access.
The third party did not specify the software, and is gone for easter holiday.
Based on information from the report, can you figure out the software name?
Remember to add TG22{...} around the solution.

### Solution
List of software available on Github as stated by Mitre (simple ctrl+f "github" on their software page):
- Software page: https://attack.mitre.org/software/
- ctrl + f "github" highlights these badboys: S0250, S0378, S0363, S0192, S0262, S0358, S0349

List of software overlapping with any technique from the report that is also mentioned to be listed on Github:
- S0363, also known as Empire

In other words, Empire is the only tool supporting techniques from the report, which is also to be found on Github according to Mitre.
