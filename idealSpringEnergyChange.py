import matplotlib.pyplot as plt


class spring:
    """Considering the mean position at: Origin. 
       Assuming the Potential Energy at Origin to be Zero"""

    def __init__(self, springConstant, displacedBy):
        self.springConstant = float(springConstant)
        self.maxDisplacement = float(displacedBy)
        self.mechanicalEnergy = float(
            0.5 * self.springConstant * (self.maxDisplacement ** 2)
        )

    def potentialEnergyChange(self, atPosition):
        if (
            atPosition >= (-1) * self.maxDisplacement
            and atPosition <= self.maxDisplacement + 1
        ):
            return float(0.5 * self.springConstant * (atPosition ** 2))

    def kineticEnergy(self, atPosition):
        if (
            atPosition >= (-1) * self.maxDisplacement
            and atPosition <= self.maxDisplacement + 1
        ):
            return float(self.mechanicalEnergy - self.potentialEnergyChange(atPosition))

    def plot(self, displacementInterval):
        currentPosition = negativeLimit = (-1) * self.maxDisplacement

        positiveLimit = self.maxDisplacement
        print(
            "\n\n\nThere might be some precision difference in your calculations and the result\n\n\n"
        )
        potentialEnergyValue = []
        kineticEnergyValue = []
        mechanicalEnergyValue = []
        positions = []
        while currentPosition >= negativeLimit and currentPosition <= positiveLimit:
            potentialEnergyValue.append(self.potentialEnergyChange(currentPosition))
            kineticEnergyValue.append(self.kineticEnergy(currentPosition))
            mechanicalEnergyValue.append(self.mechanicalEnergy)
            positions.append(currentPosition)
            currentPosition += displacementInterval
        plt.xlabel("Position (metre)")
        plt.ylabel("Energy (Joule)")
        plt.plot(
            positions,
            mechanicalEnergyValue,
            color="black",
            label=f"Total Mechanical Energy ({self.mechanicalEnergy} J)",
        )
        plt.plot(positions, kineticEnergyValue, color="red", label="Kinetic Energy")
        plt.plot(
            positions, potentialEnergyValue, color="green", label="Potential Energy"
        )
        plt.legend()
        plt.show()


print("\n\n\n\n USE SI UNITS ONLY. (Metre, Newton, Second) \n\n\n\n")
s1 = spring(
    float(input("Enter: Spring Constant =>")), float(input("Enter: Displaced By =>"))
)
s1.plot(float(input("Enter: Displacement Interval =>")))

