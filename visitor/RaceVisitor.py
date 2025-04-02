from races import Elf


class RaceVisitor:
    def visitElf(self, elf: Elf, action: str):
        if action == "darkVision":
            return elf.darkVision()
        # return elf.darkVision(opponent, distance)
        raise ValueError("Unknown action")
