import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread("/home/mdl/priyanka/snap_1080p_11-15-43-016.png")

x=100
y=300
roi = img[y:y+200, x:x+300]
plt.imshow(roi)
plt.axis("on")
plt.title("200 x 300 ROI")

def click(event):
    print(int(event.xdata), int(event.ydata))

plt.connect("button_press_event", click)
plt.show()


