# Discord Message Explorer

This program is to find and display statistics from discord messages
For example, from servers or group DMs.

Project currently under construction, basic functions work.

# Status

Currently, most objectives are complete. Feel free to create an issue and suggest new plots :)
Recently got a code parser written in rust, please make an issue if it has problems.
May start working on a tkinter based GUI instead of pygame soon

# How to use

- Download the source code, and extract into one folder.
- Download the requrired packages with pip, and then somehow acquire a .csv file with all the discord messages of a group DM, etc (I used DiscordChatExporter with .csv).
- Then, rename that file to 'data.csv'
- Run the program, and in the 'Words' tab, you can enter any word, and it will display a chart with the statics of how much each user uses that word.
- Similarily, you can play around with the other tabs and checkboxes, look at the tooltips for help, or check the commit messages to see exactly what they do.


# Completed Objectives
- Most messages sent leaderboard
- Message occurance per total messages
- Most used word leaderboard
- Rate of usage over time + usage overview
- Rust Parser
- Helpful tooltip
