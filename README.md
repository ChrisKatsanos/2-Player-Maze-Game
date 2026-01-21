# 🧩 2-Player Pygame Maze
A two player and fun maze game to play with a friend!🕹️

A 2-player maze game made with **Python + Pygame**.  
Two players race through a maze to reach the **finish square**. Each player has their own timer, and touching the finish resets their position and timer.

---

## 🎮 Gameplay

- **Player 1** moves with **Arrow Keys**
- **Player 2** moves with **WASD**
- Avoid walls (you get pushed back if you collide)
- Reach the **finish (blue square)** to record your time
- After reaching the finish:
  - the player resets to their start position
  - the timer for that player resets and starts again

---

## 🕹 Controls

### Player 1
- `↑` Up
- `↓` Down
- `←` Left
- `→` Right

### Player 2
- `W` Up
- `S` Down
- `A` Left
- `D` Right

---

## ⏱ Timers

- Each player has their own timer displayed at the top:
  - `Timer1` for Player 1
  - `Timer2` for Player 2
- When a player reaches the finish, their time is calculated and shown, then the timer restarts.

---

## 🧱 Obstacles / Walls

The maze includes:
- Outer boundary walls (top/bottom/left/right)
- Multiple inner red walls
- **Moving wall** controlled by a thread (`move()`)
- **Resizing wall** controlled by a thread (`resize()`)

This makes the maze harder because some obstacles change over time.

---

## 🖼 Assets (Images Required)

This game loads 2 PNG images for the players:

- `player1-removebg-preview.png`
- `player_2-removebg-preview.png`

✅ These files must be inside the same folder as the Python script, otherwise the game will crash.

---

## 🛠 Requirements

- Python 3.x
- Pygame

Install Pygame with:

```bash
pip install pygame

-▶️ How to Run 
 1) Clone the repository
git clone https://github.com/your-username/your-repo-name.git

 2) Go into the project folder
cd your-repo-name

 3) Install pygame
pip install pygame

 4) Run the game (change the filename if yours is different)
python main.py

 5) Make sure these image files are in the same folder:
#    - player1-removebg-preview.png
#    - player_2-removebg-preview.png
