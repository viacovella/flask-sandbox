# flask-sandbox
A sandbox for a single page application showing submission ranks

The app:
* reads a db of submissions
* selects for each group the last one submitted
* shows a ranked list on the screen.

The database:
* contains one table: "submission", reflecting the Submission model
* it can be updated by posting json files using a bash script
