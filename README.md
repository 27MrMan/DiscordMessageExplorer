# Discord Message Explorer

This program is to find and display statistics from discord messages
For example, from servers or group DMs.

Project currently just started. Very much incomplete.

# Status

Currently, most objectives are complete. Feel free to create an issue and suggest new plots :)
However, I am slowly working in the background to create a CSV Parser in Rust (current one is in python and is quite slow), probably will be added in the next major release.

# How to use

- Download the source code, and extract into one folder.
- Download the requrired packages with pip, and then somehow acquire a .csv file with all the discord messages of a group DM, etc (I used DiscordChatExporter with .csv).
- Then, rename that file to 'data.csv'
- Run the program, and in the 'Words' tab, you can enter any word, and it will display a chart with the statics of how much each user uses that word.
- Similarily, you can play around with the other tabs and checkboxes, or check the commit messages to see exactly what they do.

# Build Instructions
- The python part does not need any building, but for the rust program, just run 'cargo build --release' while 'cd'd into the /csvreader/ directory.

# Completed Objectives
- Most messages sent leaderboard
- Message occurance per total messages
- Most used word leaderboard
- Rate of usage over time + usage overview
