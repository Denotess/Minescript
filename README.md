# Hotbar Tool Stats for Hypixel

This project provides a Python script, **`hotBarToolStats.py`**, that extracts and displays detailed information about the items in a Minecraft player’s **hotbar**.  

It is designed for use with **MineScript** and Minecraft modding APIs, making it useful for Hypixel players who want quick access to tool stats, enchantments, and item metadata.

---

## 🚀 Features

- Reads all **9 slots of the hotbar**.
- Detects whether each slot is empty or contains an item.
- Collects detailed information for each item:
  - Item **name**
  - **Registry ID**
  - **Count** (stack size)
  - **Enchantments**
  - **Lore text**
- Catches and logs errors safely (so one bad item won’t break the script).
- Returns results as a **list of dictionaries** (easy to process, display, or export).

---

## 🛠 Requirements

- [MineScript](https://github.com/MineScript) installed  
- A working Minecraft modding environment with:
  - `net.minecraft.client.Minecraft`
  - `net.minecraft.core.component.DataComponents`
  - `net.minecraft.core.registries.BuiltInRegistries`
- Python-Java integration (e.g., Jython or your environment’s bridge to Minecraft classes)

---

## 📄 Usage

1. Place `hotBarToolStats.py` in your MineScript project or mod folder.
2. Import the function in your code:

   ```python
   from hotBarToolStats import hotbarToolStats

   results = hotbarToolStats()
   for entry in results:
       print(entry)
