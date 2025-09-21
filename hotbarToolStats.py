import minescript as m
from java import JavaClass

Minecraft = JavaClass("net.minecraft.client.Minecraft")
DataComponents = JavaClass("net.minecraft.core.component.DataComponents")
BuiltInRegistries = JavaClass("net.minecraft.core.registries.BuiltInRegistries")

mc = Minecraft.getInstance()

def hotbarToolStats(target=None):
    inv = m.player_inventory()
    results = []

    for i, _ in enumerate(inv):
        if i > 8:
            break

        try:
            stack = mc.player.getInventory().getItem(i)
            if stack.isEmpty():
                results.append({"slot": i, "empty": True})
                continue

            # readable dict
            entry = {
                "slot": i,
                "name": stack.getHoverName().getString(),
                "registry_id": str(BuiltInRegistries.ITEM.getKey(stack.getItem())),
                "count": stack.getCount(),
            }

            try:
                ench = stack.get(DataComponents.ENCHANTMENTS)
                entry["enchantments"] = str(ench) if ench else None
            except:
                entry["enchantments"] = None

            try:
                lore = stack.get(DataComponents.LORE)
                entry["lore"] = [line.getString() for line in lore.lines()] if lore else None
            except:
                entry["lore"] = None

            results.append(entry)

        except Exception as e:
            results.append({"slot": i, "error": str(e)})

    return results