May 20 Laura:
1.  Each individual question is wrapped by `<div>` and uses class `.form-group`
    - Includes spacing format and handles the seperator line between questions
2.  Question titles use `.question-label`, and are `<label>` items
3.  All "next" buttons use class `.next-btn`, maybe submit btn can use this css too?
4.  How I handled switching form parts: 
    - package all data into json -> localstorage to store data with keywords matching page name -> set window location to the route of the next section for the form