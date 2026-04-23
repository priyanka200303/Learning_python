import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

# Load image
img = mpimg.imread(r"C:\Users\priya\Desktop\Internship\Hanuman ji.png")

fig, ax = plt.subplots()
ax.imshow(img)

# Rectangle size
width = 300
height = 200

# Click event function
def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        x = int(event.xdata)
        y = int(event.ydata)

        # Print coordinates in terminal
        print(f"Clicked at: x={x}, y={y}")

        # Draw rectangle
        rect = patches.Rectangle((x, y), width, height,
                                 edgecolor='red', facecolor='green', linewidth=2)
        ax.add_patch(rect)

        plt.draw()

# Connect mouse click
fig.canvas.mpl_connect('button_press_event', onclick)

plt.title("Click to create 200x300 ROI")
plt.axis("on")
plt.show()