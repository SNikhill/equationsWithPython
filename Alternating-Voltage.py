import matplotlib.pyplot as plt
import math


class voltageGraph:
    def __init__(self, frequency, peakVolatge):
        self.frequency = frequency
        self.peakVolatge = peakVolatge
        self.angularFrequency = (2 * math.pi) * self.frequency

    def startPlot(self):
        timeLimitPrecision = 3
        self.recommendedTimeLimit = round(10 * (1 / self.frequency), timeLimitPrecision)
        while self.recommendedTimeLimit == 0 and timeLimitPrecision < 7:
            self.recommendedTimeLimit = round(
                10 * (1 / self.frequency), timeLimitPrecision
            )
            timeLimitPrecision += 1
        if timeLimitPrecision >= 7:
            print(
                f"\n\n\n\n\n\nFrequency is too high. Restarting the Program \n\n\n\n\n\n"
            )
            return False
        print(f"\n \033[1m Recommended Time Limit: \033[0m {self.recommendedTimeLimit}")
        self.timeLimit = float(input("Enter: Time Limit (s)=> "))
        print(
            f"\n \033[1m Recommended Time Step \033[0m {round(self.recommendedTimeLimit * 10**(-3), timeLimitPrecision + 3)}"
        )
        self.timeStep = float(input("Enter: Time Step => "))
        self.plot()

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


def initiateObject():
    v1 = voltageGraph(
        float(input("Enter: Frequency (Hz) => ")),
        float(input("Enter: Peak Voltage (V)=> ")),
    )
    if v1.startPlot() == False:
        return initiateObject()


initiateObject()

