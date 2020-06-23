import math
import matplotlib.pyplot as plt


class projectile:
    """y = verticalDisplacement, x = horizontalDisplacement"""

    def __init__(self, initialVelocity, angleOfProjection, accelerationDueToGravity=10):
        self.initialVelocity = float(initialVelocity)
        self.angleOfProjection = float(
            angleOfProjection * (math.pi / 180)
        )  # Converting to Radian Measure
        self.accelerationDueToGravity = float(accelerationDueToGravity)
        self.intialHorizontalVelocity = float(
            self.initialVelocity * math.cos(self.angleOfProjection)
        )
        self.intialVerticalVelocity = float(
            self.initialVelocity * math.sin(self.angleOfProjection)
        )
        self.timeOfFlight = float(
            2 * self.intialVerticalVelocity / self.accelerationDueToGravity
        )
        self.range = float(self.intialHorizontalVelocity * self.timeOfFlight)
        self.range = float(self.intialHorizontalVelocity * self.timeOfFlight)
        self.maxHeight = float(
            (self.intialVerticalVelocity ** 2) / (2 * self.accelerationDueToGravity)
        )

    def x(self, atTime):
        if atTime < self.timeOfFlight:
            return self.intialHorizontalVelocity * atTime
        else:
            return self.range

    def y(self, atTime):
        if atTime < self.timeOfFlight:
            return self.intialVerticalVelocity * atTime - (1 / 2) * (
                self.accelerationDueToGravity
            ) * (atTime ** 2)
        else:
            return 0

    def plot(self, timeStep):
        currentTime = 0
        timeOfFlight = self.timeOfFlight
        horizontalDisplacement = []
        verticalDisplacement = []
        while currentTime <= timeOfFlight:
            horizontalDisplacement.append(self.x(currentTime))
            verticalDisplacement.append(self.y(currentTime))
            currentTime += timeStep
        # PLOT STUFF WILL BE HERE
        # print(horizontalDisplacement)
        # print(verticalDisplacement)
        print(f"Range: {self.range}")
        print(f"Max Height: {self.maxHeight}")
        plt.scatter(horizontalDisplacement, verticalDisplacement)
        plt.xlabel("Horizontal Displacement")
        plt.ylabel("Vertical Displacement")
        # plt.text(self.range - 2, 0, f"Range: {self.range}")
        plt.show()


p1 = projectile(
    float(input("Enter: Initial Velocity=> ")),
    float(input("Enter: Angle Of Projection=> ")),
    float(input("Enter: Acceleration Due To Gravity=> ")),
)
p1.plot(float(input("Enter: Time Interval=> ")))
print(p1.range, p1.timeOfFlight)
