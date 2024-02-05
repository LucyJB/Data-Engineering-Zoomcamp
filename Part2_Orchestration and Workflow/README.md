### Notes for topics covered this week:

#### Orchestration

* A large part of data engineering is Extracting, Transforming and Loading between sources.

* Orchestration is a process of dependency management, facilitated through automation. The data orchestrator manages scheduling, triggering, monitoring and even resource allocation.

**A good Orchestrator tool is like a good conductor in an orchestra, constantly managing the correct cadence, tempo, understanding the 'symphony'**

* This Orchestration workflow is done in a sequence of steps.

* A good orchestrator handles:
  * Workflow management - define schedules, manages workflows and dependencies.
  * Automation - Automate as much as possible
  * Error handling and recovery of missing data
  * Monitoring and alerting
  * Resource optimistation - best route for managing where jobs are executed
  * Observability - visibility into every part of the data pipeline
  * Debugging - able to debug pipelines easily
  * Compliance/Auditing - an orchestrator should help with this.

* A good orchestrator prioritises:
  *Developer Experience*
    * Flow State - if you are constantly switching between tools then that isn't an ideal flow
    * Feedback Loops - need to get tangible feedback straightaway
    * Cognitive Load

* **Mage** is one of many tools used as an orchestration solution.

**There is no perfect solution and the right solution for your use case may be different to someone else's**

* Part of being an engineer is figuring out how your situation is different, and then doing the research to finding out how yours is different.

*Mage Workflow image* 
<img width="685" alt="Screenshot 2024-02-05 at 12 24 59" src="https://github.com/LucyJB/Data-Engineering-Zoomcamp/assets/76856081/21adccea-3bb3-43cf-9a98-d01320ca1ca9">

* Use of Docker and Mage together to Extract, Transform and Load sample dataset

*Image of Data Engineering Lifecycle*
<img width="755" alt="Screenshot 2024-02-05 at 12 35 13" src="https://github.com/LucyJB/Data-Engineering-Zoomcamp/assets/76856081/b725c117-9756-4822-82a5-d517223d5a98">
