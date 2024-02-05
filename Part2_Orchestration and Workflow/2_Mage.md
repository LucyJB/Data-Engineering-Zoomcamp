#### Mage

As mentioned in [Orchestration](https://github.com/LucyJB/Data-Engineering-Zoomcamp/blob/main/Part2_Orchestration%20and%20Workflow/1_Orchestration.md) , **Mage** is one of many tools used as an orchestration solution.

* Mage is an open-source pipeline tool for orchestrating, transforming and integrating data.

*Mage diagram*
<img width="715" alt="Screenshot 2024-02-05 at 20 52 42" src="https://github.com/LucyJB/Data-Engineering-Zoomcamp/assets/76856081/78a929f2-45dc-4ec5-87c2-31678574a7b7">

* Mage accelerates pipeline development
  * Hybrid environment
    * Use GUI for interactive development (or use VSCode)
    * Use blocks as testable, reuseable pieces of code.
   
  * Improved DevEx
    * Code and test in parallel
    * Reduce your dependencies, switch tools less, be efficient.
   
* In-line testing and debugging
  * Familiar, notebook-style format
* Fully-featured observability
  * Transformation in one place: dbt models (yay!), streaming and more
* DRY principles (don't repeat yourself)
  * No more DAGs with duplicate functions and weitd imports
  * DEaaS (Data Engineerring as a service)
 
  #### Mage Structure
  
   <img width="715" alt="Screenshot 2024-02-05 at 21 05 51" src="https://github.com/LucyJB/Data-Engineering-Zoomcamp/assets/76856081/07809cfc-2095-48e0-8044-1c34f557473c">

* Projects
  * Forms the basis for the work done in Mage - a Github repo
  * Contains the code for all of my pipelines, blocks and other assets.
  * A Mage instance has one or more projects    

* Pipelines
  * A workflow that executes some data operation - maybe extracting, transforming, and loading data from an API - also known as DAGs on other platforms.
  * In Mage, pipelines can contain Blocks which are written in SQL, Python or R and charts
  * Each pipeline is represented by a YAML file in the 'pipelines' folder of your project.

* Blocks
  * Files (eg sql, python, r)  that can be executed independently or within a pipeline.
  * Blocks form Directed Acyclic Graphs (DAGs), which we call pipelines
  * A block won't start running in a pipeline until all its upstream dependencies are met.
  * They are reusable, atomic pieces of code that perform certain actions.
  * Changing one block will change it everywhere it's used - however it is easy to detach blocks to seperate instances if necessary which saves on repeating code several times.
  * Blocks perfoem a variety of actions, from simple data transformations to complex machine learning models.
 
#### Anatomy of a Block 
<img width="685" alt="Screenshot 2024-02-05 at 21 24 48" src="https://github.com/LucyJB/Data-Engineering-Zoomcamp/assets/76856081/6b47ad44-cab7-405c-bd95-36711a714322">

*Sample dataframe in a block*


