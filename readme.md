# CodeDropper Discord Bot

CodeDropper is a Discord bot designed to facilitate competitions and rewards for active server members. It provides a framework for generating random codes, tracking member points, and managing rewards.

## Features

- **User Registration:** Members can register using the `$register` command to participate in competitions.

- **Code Generation:** Authorized users can generate random codes with the `$gencode` command, dropping them in a designated channel.

- **Code Redemption:** Members can redeem codes with the `$redeem {code}` command to earn points.

- **Points Tracking:** The bot keeps track of points earned by each member.

- **Leaderboard:** A leaderboard displays the members with the highest points.

## Usage

1. **Registration:** Members must register using the `$register` command to participate.

2. **Code Generation:** Authorized users generate codes with `$gencode`, posting them in the configured code drop channel.

3. **Code Redemption:** Members redeem codes with `$redeem {code}` to earn points.

4. **Leaderboard:** Use `$leaderboard` to view the top members with the highest points.

## Configuration

The bot is configured using the `config.json` file. Modify the following parameters:

- `authorized_users`: List of user IDs allowed to execute `$gencode`.
  
- `codedrop_channel`: Channel ID where generated codes will be posted.
  
- `token`: Discord bot token for authorization.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/CodeDropper.git
   ```

2. Configure the bot by editing `config.json` with your Discord bot token, authorized users, and code drop channel.

3. Run the bot:

   ```bash
   python bot.py
   ```
