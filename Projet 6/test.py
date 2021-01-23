import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


temps = [
    (5, 30, 5),
    (5, 30, 17),
    (5, 30, 29),
    (5, 30, 43),
    (5, 30, 56)
]

abscisses = [t[0] * 3600 + t[1] * 60 + t[2] for t in temps]
ordonnees = [1, 2, 3, 4, 5]

fig, ax = plt.subplots()
plt.plot(abscisses, ordonnees)

formatter = ticker.FuncFormatter(lambda s, x: time.strftime('%H:%M:%S', time.gmtime(s)))
ax.xaxis.set_major_formatter(formatter)


plt.show()
