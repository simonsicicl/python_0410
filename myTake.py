import cv2

def capture_images(camera_index=0, num_images=5, save_path='captured_images'):
    # Create a VideoCapture object to capture images from the camera
    cap = cv2.VideoCapture(camera_index)
    
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return
    
    # Create the save_path directory if it doesn't exist
    import os
    os.makedirs(save_path, exist_ok=True)
    
    print(f"Capturing {num_images} images from camera {camera_index}...")
    i = 0
    while i < num_images:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Failed to capture image {i+1}.")
            continue
        dstx = cv2.Sobel(frame,cv2.CV_32F,1,0)
        dsty = cv2.Sobel(frame,cv2.CV_32F,0,1)
        dstx = cv2.convertScaleAbs(dstx)
        dsty = cv2.convertScaleAbs(dsty)
        dst = cv2.addWeighted(dstx,0.5,dsty,0.5,0)
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) != ord('c'):
            continue
        if cv2.waitKey(1) == ord('q'):
            break
        frame_path = os.path.join(save_path, f"frame_{i+1}.jpg")
        cv2.imwrite(frame_path, frame)
        dstx_path = os.path.join(save_path, f"dstx_{i+1}.jpg")
        cv2.imwrite(dstx_path, dstx)
        dsty_path = os.path.join(save_path, f"dsty_{i+1}.jpg")
        cv2.imwrite(dsty_path, dsty)
        dst_path = os.path.join(save_path, f"dst_{i+1}.jpg")
        cv2.imwrite(dst_path, dst)
        
        # Save the captured image
        i = i + 1
    
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
    print("Capture completed.")

if __name__ == "__main__":
    # You can adjust the parameters here as per your requirement
    capture_images(camera_index=0, num_images=5, save_path='captured_images')
