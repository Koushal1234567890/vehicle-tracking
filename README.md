# vehicle-tracking
This project is about the combination of lane detection of vehicles, speed detection of vehicles and no. of vehicles passed and entered in to the place

1. Imports: The code imports necessary libraries like OpenCV (cv2), pandas, numpy, and YOLO from Ultralytics. It also imports a custom module called `Tracker` for object tracking.

2. Initialization: It loads a YOLO model using Ultralytics's YOLO class, which is pre-trained on the COCO dataset for object detection.

3. Mouse Event Callback Function: A callback function named `RGB` is defined to capture mouse events on the window named 'RGB'.

4. Video Capture: The code opens a video file ('veh2.mp4') for processing using OpenCV's VideoCapture.

5. Reading Class Labels: It reads class labels from a file named "coco.txt" and stores them in a list.

6. Object Tracking Initialization: Initializes a custom object tracker (`Tracker`) and sets up some variables related to object tracking.

7. Main Loop:
   - The code reads frames from the video one by one.
   - It resizes the frame to a specific size (1020x500 pixels).
   - The YOLO model predicts objects in the frame.
   - Detected objects are filtered to include only cars.
   - Object tracking is performed using the custom tracker.
   - Speed calculation and counting of vehicles crossing predefined lines are done.
   - Relevant information and lines are drawn on the frame.
   - The processed frame is displayed in a window named 'RGB'.
   - The loop continues until the user presses the 'q' key.

8. Display and Cleanup: Once the loop is terminated, the video capture is released, and OpenCV windows are closed.

Overall, this code performs real-time vehicle detection, tracking, speed estimation, and counting of vehicles crossing specific lines in a video. It's a basic implementation of a traffic monitoring system using computer vision techniques.

**LANE DETECTION**
1. Imports: The code imports necessary libraries like OpenCV (cv2) and NumPy for image processing and array manipulation.

2. Vehicle Class: Defines a `Vehicle` class representing a vehicle with a specific speed.

3. TrafficCamera Class: Defines a `TrafficCamera` class representing a traffic camera. It has a method to check the speed of vehicles in different lanes.

4. draw_lane_lines Function: Defines a function to draw lane lines on the given frame using edge detection, masking, and Hough line detection techniques.

5. Main Function (main):
   - Initializes a `TrafficCamera` object and an empty list to store vehicle objects.
   - Opens a video file for processing.
   - Creates a full-screen window to display the video frames.
   - Loops through each frame of the video:
     - Reads the frame.
     - Draws lane lines on the frame.
     - Simulates vehicle detection and assigns random speeds to vehicles in random lanes.
     - Checks the speed of vehicles using the `TrafficCamera` object.
     - Displays the frame.
     - Terminates the loop if the user presses the 'q' key.
   - Releases the video capture object and closes the display window.

6. Execution: Executes the `main` function if the script is run as the main program.

Overall, this code simulates a traffic monitoring system using computer vision techniques. It detects lane lines, simulates vehicle speeds in random lanes, and checks if vehicles are speeding using a traffic camera object.


In this way the vechicles are detected by the computer vision technology yolov8 is used in this as Artifital Intelligence techinques and this code helps us to know what are the objects are travelling through ultralytics and yolov8 and speed of the vehicles on ther road is detected by tracker and pandas are used for the analysation of the objected detected.and opencv is used to take the input video of the travelling vehicles on the road.classes are made for the detection of lanes and lines are drawn according to the lanes given in the video provided by the open cv.at the place of giving the video mp4 ve can also keep url of the closed circuit camera so that it it will continuosly track the passage of vehicles.According to lanes vehicles which are going and vehicles which are coming are also detected through while loop.As we are using YOLOv8 it only taking high resolution videos or footage because for YOLOv8 weights,.cfg and coco are not released till now. keeping high resolution cameras at the cc camera footages will help recognising the vehicles and also humans 
