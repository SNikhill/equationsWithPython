import matplotlib.pyplot as plt
import math


class voltageGraph:
    def __init__(self, frequency, peakVolatge):
        self.frequency = frequency
        self.peakVolatge = peakVolatge
        self.angularFrequency = (2 * math.pi) * self.frequency
        self.recommendedTimeLimit = round(10 * (1 / self.frequency), 9)
        self.recommendedTimeStep = round(self.recommendedTimeLimit * (10 ** (-3)), 12)
        print(f"\n \033[1m Recommended Time Limit: \033[0m {self.recommendedTimeLimit}")
        self.timeLimit = float(input("Enter: Time Limit (s)=> "))
        print(f"\n \033[1m Recommended Time Step \033[0m {self.recommendedTimeStep}")
        self.timeStep = float(input("Enter: Time Step => "))

    def voltage(self, atTime):
        return self.peakVolatge * math.sin(self.angularFrequency * atTime)

    def plot(self):
        currentTime = 0
        tillTime = self.timeLimit
        timeStep = self.timeStep
        print(
            "\n\n\nThere might be some precision difference in your calculations and the result\n\n\n"
        )
        timeValues = []
        voltageValues = []
        while currentTime <= tillTime:
            timeValues.append(currentTime)
            voltageValues.append(self.voltage(currentTime))
            currentTime += timeStep

        plt.plot(
            timeValues,
            voltageValues,
            label="Alternating Voltage (V)",
            linestyle="-",
            color="orange",
        )

        plt.plot(timeValues, [0] * len(timeValues), color="black", label="Time (s)")
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        plt.legend()
        plt.show()
        plt.close()


print(
    "\n\n\n\n \033[1m Alternating Voltage.\033[0m\n\nUSE SI UNITS ONLY. (Metre, Newton, Second, Hertz, Volts) \n\n\n\n"
)
v1 = voltageGraph(
    float(input("Enter: Frequency (Hz) => ")),
    float(input("Enter: Peak Voltage (V)=> ")),
)

v1.plot()

