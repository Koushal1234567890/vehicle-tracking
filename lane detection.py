import cv2
import numpy as np
import random

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class TrafficCamera:
    def __init__(self):
        self.lane_speeds = [50, 40, 30, 20]

    def check_speed(self, vehicles):
        num_lanes = len(self.lane_speeds)
        for i, vehicle in enumerate(vehicles):
            lane_index = min(i, num_lanes - 1)  # Adjust for fewer lanes detected
            if vehicle.speed < self.lane_speeds[lane_index]:
                print(f"Vehicle in lane {lane_index+1} is speeding! Speed: {vehicle.speed} mph")
            else:
                print(f"Vehicle in lane {lane_index+1} is within speed limit. Speed: {vehicle.speed} mph")

def draw_lane_lines(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Define region of interest (ROI)
    height, width = frame.shape[:2]
    roi_vertices = [
        (0, height),
        (width / 4, height / 2),
        (width * 3 / 4, height / 2),
        (width, height)
    ]
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, [np.array(roi_vertices, dtype=np.int32)], 255)
    masked_edges = cv2.bitwise_and(edges, mask)

    # Perform Hough line detection
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=100)

    # Draw lane lines on the original frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

def main():
    traffic_camera = TrafficCamera()
    vehicles = []

    # Load the video file
    video_file = 'veh2.mp4'
    cap = cv2.VideoCapture(video_file)

    # Get the screen width and height
    screen_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    screen_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a full-screen window
    cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Loop through each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Draw lane lines on the frame
        draw_lane_lines(frame)

        # Simulate vehicle detection and speed checking
        num_lanes = random.randint(1, 4)  # Randomly simulate 1 to 4 lanes
        speeds = [random.randint(1, 60) for _ in range(num_lanes)]
        vehicles.clear()  # Clear previous vehicles
        for speed in speeds:
            vehicles.append(Vehicle(speed))

        # Check the speed of vehicles in each lane
        traffic_camera.check_speed(vehicles)

        # Display the frame
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close any open windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
