import matplotlib.pyplot as plt

# USE SI UNITS ONLY. (Metre, Newton, Coulomb)


class insulatedSphere:
    """Medium: Vacuum. Displacement with respect to centre of the sphere"""

    def __init__(self, netCharge, radius, testChargePosition):
        self.netCharge = netCharge
        self.radius = radius
        self.testChargePosition = testChargePosition
        self.coulombConstant = 9 * (10 ** 9)

    def electricField(self, atPosition):
        if atPosition < self.radius:
            return (
                self.coulombConstant * self.netCharge / (self.radius ** 3)
            ) * atPosition
        elif atPosition >= self.radius:
            return (self.coulombConstant * self.netCharge) / (atPosition ** 2)

    def plot(self, displacementInterval):
        currentPosition = 0  # At Centre
        limit = self.testChargePosition
        electricFieldValue = []
        positions = []

        while currentPosition <= limit:
            electricFieldValue.append(self.electricField(currentPosition))
            positions.append(currentPosition)
            currentPosition += displacementInterval

        plt.xlabel("Position (m)")
        plt.ylabel("Magnitude of Electric Field (N/C)")

        plt.plot(
            positions,
            electricFieldValue,
            color="#ffb836",
            label="Variation of Electric Field",
        )
        plt.scatter(
            self.testChargePosition,
            self.electricField(self.testChargePosition),
            color="Orange",
            label=f"At Test Position: {round(self.electricField(self.testChargePosition), 2)} N/C",
        )
        plt.legend()
        plt.show()


print("\n\n\n\n USE SI UNITS ONLY. (Metre, Newton, Coulomb) \n\n\n\n")
sphere1 = insulatedSphere(
    float(input("Enter: Net Charge on Sphere =>")),
    float(input("Enter: Radius of the Sphere =>")),
    float(input("Enter: Distance of Test Charge from the Centre =>")),
)
sphere1.plot(float(input("Enter: Displacement Interval =>")))
