import math
import matplotlib.pyplot as plt


class projectile:
    """y = verticalDisplacement, x = horizontalDisplacement
    There might be some precision difference in the results."""

    def __init__(self, initialVelocity, angleOfProjection, accelerationDueToGravity):
        self.initialVelocity = initialVelocity
        self.angleOfProjection = (
            angleOfProjection * math.pi / 180
        )  # Converting to Radian Measure
        self.accelerationDueToGravity = accelerationDueToGravity
        self.intialHorizontalVelocity = round(
            self.initialVelocity * math.cos(self.angleOfProjection)
        )
        self.intialVerticalVelocity = round(
            self.initialVelocity * math.sin(self.angleOfProjection)
        )
        self.timeOfFlight = (
            2 * self.intialVerticalVelocity / self.accelerationDueToGravity
        )
        self.range = self.intialHorizontalVelocity * self.timeOfFlight
        self.maxHeight = (self.intialVerticalVelocity ** 2) / (
            2 * self.accelerationDueToGravity
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
        print(
            "\n\n\nThere might be some precision difference in your calculations and the result\n\n\n"
        )
        horizontalDisplacement = []
        verticalDisplacement = []
        while currentTime <= timeOfFlight:
            horizontalDisplacement.append(self.x(currentTime))
            verticalDisplacement.append(self.y(currentTime))
            currentTime += timeStep

        # For Details

        plt.scatter(
            0, 0, color="orange", label=f"Range: {round(self.range)} m"
        )

        plt.scatter(
            0, 0, color="orange", label=f"Max Height: {self.maxHeight} m"
        )

        plt.scatter(
            0, 0, color="orange", label=f"Time Of Flight: {self.timeOfFlight} s"
        )

        # For Trajectory

        plt.plot(
            horizontalDisplacement,
            verticalDisplacement,
            color="orange",
            label=f"Trajectory"
        )

        plt.xlabel("Horizontal Displacement")
        plt.ylabel("Vertical Displacement")
        plt.legend()
        plt.show()


print("\n\n\n\n \033[1m Projectile Fired At An Angle.\033[0m\n\nUSE SI UNITS ONLY. (Metre, Newton, Second, Metre/Second) \n\n\n\n")
p1 = projectile(
    float(input("Enter: Initial Velocity (m/s)=> ")),
    float(input("Enter: Angle Of Projection (degree measure)=> ")),
    float(input("Enter: Acceleration Due To Gravity => ")),
)
p1.plot(float(input("Enter: Time Interval (s)=> ")))
