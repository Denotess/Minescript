import minescript as m
from java import JavaClass

Minecraft = JavaClass("net.minecraft.client.Minecraft")
DataComponents = JavaClass("net.minecraft.core.component.DataComponents")
BuiltInRegistries = JavaClass("net.minecraft.core.registries.BuiltInRegistries")

mc = Minecraft.getInstance()

def hotbarToolStats():
    results = []
    appendResult = results.append

    mcPlayer = mc.player
    invObj = mcPlayer.getInventory()
    getItemAt = invObj.getItem
    itemRegistry = BuiltInRegistries.ITEM
    dcEnchant = DataComponents.ENCHANTMENTS
    dcLore = DataComponents.LORE

    for i in range(9):
        try:
            stack = getItemAt(i)

            if stack.isEmpty():
                appendResult({"slot": i, "empty": True})
                continue

            item = stack.getItem()
            rid = itemRegistry.getKey(item)
            entry = {
                "slot": i,
                "name": stack.getHoverName().getString(),
                "registry_id": str(rid),
                "count": stack.getCount(),
            }

            try:
                ench = stack.get(dcEnchant)
                entry["enchantments"] = str(ench) if ench else None
            except Exception:
                entry["enchantments"] = None

            try:
                loreVal = stack.get(dcLore)
                if loreVal:
                    # convert each line to plain string
                    entry["lore"] = [ln.getString() for ln in loreVal.lines()]
                else:
                    entry["lore"] = None
            except Exception:
                entry["lore"] = None

            appendResult(entry)

        except Exception as e:
            appendResult({"slot": i, "error": str(e)})

    return results