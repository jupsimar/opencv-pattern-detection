import heatmap
import cv2

def use_heatmap(image, box_centers):
    hm = heatmap.Heatmap()
    img = hm.heatmap(box_centers, dotsize=200, size=(image.shape[1], image.shape[0]), opacity=128, area=((0, 0), (image.shape[1], image.shape[0])))
    return img

img = "/path/to/image.jpg"
centers = [(10, 20), (30, 40) ] # centers of heatmaps
frame = cv2.imread(img) # origin image
hm = use_heatmap(frame)
heatmap = cv2.imread(hm) # heatmap image
overlay = frame.copy()
alpha = 0.5 # set convering image transparency 
cv2.rectangle(overlay, (0, 0), (frame.shape[1], frame.shape[0]), (255, 0, 0), -1) # set blue as the background 
cv2.addWeighted(overlay, alpha, frame, 1-alpha, 0, frame) # overlap background with original image
cv2.addWeighted(heatmap, alpha, frame, 1-alpha, 0, frame) # overlap heatmap with original image
cv2.imshow('frame', frame)
cv2.waitKey(0)
