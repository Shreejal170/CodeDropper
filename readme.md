# CodeDropper Discord Bot

CodeDropper is a Discord bot designed to facilitate competitions and rewards for active server members. It provides core functionality for generating random codes, tracking member points, and managing rewards.

## Features

- **Code Generation:** Authorized users can generate random codes using `$gencode`. These codes can be redeemed by members for points.

- **Points Tracking:** The bot tracks points earned by each member, storing the data in a "users.json" file.

- **Restricted Code Generation:** Code generation is restricted to authorized users to maintain control and prevent abuse.

- **Code Drops:** Generated codes are posted in a designated channel, configured in `config.json` as `codedrop_channel`.

## Usage

1. **Member Registration:** To participate, members must register using the `$register` command.

2. **Code Generation:** Authorized users generate codes with `$gencode`, posting them in the configured code drop channel.

3. **Code Redemption:** Members redeem codes using `$redeem {code}` to earn points.

4. **Leaderboard:** View the top members with the highest points using `$leaderboard`.

## Configuration

Configure the bot by editing the `config.json` file:

- `authorized_users`: List of user IDs allowed to execute `$gencode`.
  
- `codedrop_channel`: Channel ID where generated codes will be posted.
  
- `token`: Discord bot token for authorization.

## Potential Uses

CodeDropper can be used for various purposes:

- Run competitions with rewards for top point earners.
  
- Incentivize activity by rewarding members for redeeming codes.
  
- Engage members with unpredictable code drops.
  
- Build excitement and engagement within the server.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Shreejal170/CodeDropper.git
   ```

2. **Configure the Bot:**

   Edit `config.json` with your Discord bot token, authorized users, and code drop channel.

3. **Run the Bot:**

   ```bash
   python bot.py
   ```
