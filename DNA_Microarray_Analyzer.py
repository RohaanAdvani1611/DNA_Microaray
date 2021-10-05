# 1. IMPORT NECESSARY LIBRARIES:
import cv2
import numpy as np
import argparse

# 2. READ DNA MICRO ARRAY SAMPLE
img = cv2.imread("MAT1.PNG")

# 3. USE CANNY EDGE DETECTION TO DETECT EDGES OF THE ORIGINAL PROBE SAMPLE
edged_og = cv2.Canny(img, 30, 200)

# 4. APPLY GAUSSIAN BLUR TO REMOVE NOISE
edged_og = cv2.GaussianBlur(edged_og, (5, 5), 2, 2)

# 5. DETECT THE NUMBER OF COUNTOURS IN THE ORIGINAL EDGED MICRO ARRAY
contours_og, hierarchy_og = cv2.findContours(edged_og, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 6. DRAW THE ABOVE DETECTED CONTOURS UPON THE IMAGE
cv2.drawContours(edged_og, contours_og, -1, (0, 255, 0), 3)

# 7. PRINT THE NUMBER OF CONTOURS FOUND IN THE ORIGINAL EDGED MICRO ARRAY
print("Number of Probes found in Original Sample = " + str(len(contours_og)))

# 8. APPLY THRESHOLD TO REMOVE PROBES WITH DNA STRANDS NOT PRESENT IN EITHER HEALTHY OR INFECTED CELLS
ret, fil = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 9. USE CANNY EDGE DETECTION TO DETECT EDGES OF THE FILTERED PROBE SAMPLE
edged_fil = cv2.Canny(fil, 30, 200)

# 10. APPLY GAUSSIAN BLUR TO REMOVE NOISE
edged_fil = cv2.GaussianBlur(edged_fil, (5, 5), 2, 2)

# 11. DETECT THE NUMBER OF COUNTOURS IN THE FILTERED EDGED MICRO ARRAY
contours_fil, hierarchy_fil = cv2.findContours(edged_fil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 12. DRAW THE ABOVE DETECTED CONTOURS UPON THE IMAGE
cv2.drawContours(edged_fil, contours_fil, -1, (0, 255, 0), 3)

# 13. PRINT THE NUMBER OF CONTOURS FOUND IN THE FILTERED EDGED MICRO ARRAY
print("Number of Probes found in Filtered Sample = " + str(len(contours_fil)))

# 14. CONVERT SAMPLE ARRAY FROM BGR TO LAB COLOUR SPACE FOR IDENTIFICATION OF HYBRID STRANDS
lab = cv2.cvtColor(fil, cv2.COLOR_BGR2Lab)

# 15. USE inRange() FN TO GET THE PROBES IN THE MICRO ARRAY CORRESPONDING TO INFECTED CELLS
infected = cv2.inRange(lab, np.array([20, 150, 150]), np.array([190, 255, 255]))

# 16. USE GAUSSIAN BLUR TO REDUCE NOISE IN IMAGE TO IDENTIFY THE INFECTED DNA STRAND PROBES CORRECTLY
infected = cv2.GaussianBlur(infected, (7, 7), 2, 2)

# 17. USE CANNY EDGE DETECTION TO DETECT EDGES OF THE INFECTED PROBE SAMPLE
edged_inf = cv2.Canny(infected, 30, 200)

# 18. USE GAUSSIAN BLUR TO REMOVE NOISE IN IMAGE TO IDENTIFY THE INFECTED DNA STRAND PROBES CORRECTLY
edged_inf = cv2.GaussianBlur(edged_inf, (7, 7), 2, 2)

# 19. DETECT THE NUMBER OF COUNTOURS IN THE INFECTED EDGED MICRO ARRAY
contours_inf, hierarchy_inf = cv2.findContours(edged_inf, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 20. DRAW THE ABOVE DETECTED CONTOURS UPON THE IMAGE
cv2.drawContours(edged_inf, contours_inf, -1, (0, 255, 0), 3)

# 21. PRINT THE NUMBER OF CONTOURS FOUND IN THE INFECTED EDGED MICRO ARRAY
print("Number of Infected DNA Probes found = " + str(len(contours_inf)))

# 22. USE inRange() FN TO GET THE PROBES IN THE MICRO ARRAY CORRESPONDING TO HEALTHY CELLS
healthy = cv2.inRange(lab, np.array([100, -50, 60]), np.array([255, 140, 215]))

# 23. USE BLUR TO REDUCE NOISE IN IMAGE TO IDENTIFY THE HEALTHY DNA STRAND PROBES CORRECTLY
healthy = cv2.GaussianBlur(healthy, (7, 7), 2, 2)

# 24. USE CANNY EDGE DETECTION TO DETECT EDGES OF THE HEALTHY PROBE SAMPLE
edged_hlty = cv2.Canny(healthy, 30, 200)

# 25. USE GAUSSIAN BLUR TO REMOVE NOISE IN IMAGE TO IDENTIFY THE HEALTHY DNA STRAND PROBES CORRECTLY
edged_hlty = cv2.GaussianBlur(edged_hlty, (7, 7), 2, 2)

# 26. DETECT THE NUMBER OF COUNTOURS IN THE HEALTHY EDGED MICRO ARRAY
contours_hlty, hierarchy_hlty = cv2.findContours(edged_hlty, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 27. DRAW THE ABOVE DETECTED CONTOURS UPON THE IMAGE
cv2.drawContours(edged_hlty, contours_hlty, -1, (0, 255, 0), 3)

# 28. PRINT THE NUMBER OF CONTOURS FOUND IN THE HEALTHY EDGED MICRO ARRAY
print("Number of Healthy DNA Probes found = " + str(len(contours_hlty)))

# 29. DISPLAY ALL IMAGES TO UNDERSTAND STEP BY STEP OUTPUT
cv2.imshow("Original DNA Micro Array", img)
cv2.imshow("Original Edged DNA Micro Array", edged_og)
cv2.imshow("Filtered DNA Micro Array", fil)
cv2.imshow("Filtered Edged DNA Micro Array", edged_fil)
cv2.imshow("LAB Colour space Sample", lab)
cv2.imshow("Infected Strand Probes", infected)
cv2.imshow("Edged Infected Array", edged_inf)
cv2.imshow("Healthy Strand Probes", healthy)
cv2.imshow("Edged Healthy Array", edged_hlty)

# 30. ADD WAIT KEY SO THAT WE CAN END PROGRAM MANUALLY AND DESTROY WINDOWS
cv2.waitKey(0)
cv2.destroyAllWindows()
