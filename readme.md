CodeDropper
I created this basic bot functionality to allow for custom competitions and incentives. I will be adding more features and enhancements over time. For now, it handles the core logic - generating codes, tracking points, and facilitating rewards. Please reach out with any feedback!

CodeDropper is a Discord bot I created to facilitate competitions and rewards for active server members.
Features
• Generates random codes that members can redeem for points
• Tracks points earned by each member
• Restricts code generation to authorized users
• Drops codes in a designated channel

Usage
• Members register with $register to participate
• Authorized users generate codes with $gencode
• Codes are posted in the configured code drop channel
• Members redeem codes with $redeem {code} to earn points
• Leaderboard displays members with top points

Configuration
• authorized_users - List of user IDs allowed to execute $gencode
• codedrop_channel - Channel ID where generated codes will be posted
• token - Discord bot token for authorization

CodeDropper has many potential uses:
• Run competitions rewarding roles/prizes to top point earners
• Incentivize activity by rewarding redeeming codes
• Engage members with unpredictable code drops
• Build excitement and engagement in the server
