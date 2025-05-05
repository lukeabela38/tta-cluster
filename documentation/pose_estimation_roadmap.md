# Table Tennis Pose Estimation and Movement Analysis Roadmap

## Part 1: Project Setup & Data Preparation

1. **Define Project Objectives and Requirements**  
   - Effort: ⭐  
   - Deliverable: A brief written goal or diagram outlining the system.

2. **Collect or Choose Pose Estimation Tool**  
   - Decide: OpenPose, MediaPipe, MMPose, etc.  
   - Effort: ⭐⭐  
   - Deliverable: Tool installed and sample output verified.

3. **Acquire or Record Table Tennis Videos**  
   - Ensure videos are clear, high-resolution, and well-lit  
   - Effort: ⭐⭐  
   - Deliverable: Folder with .mp4 files for testing

4. **Extract Frames or Process Video Live**  
   - Write a function to extract frames at consistent FPS  
   - Effort: ⭐⭐  
   - Deliverable: Frame grabber module (e.g., using OpenCV)

## Part 2: Pose Extraction and Keypoint Handling

5. **Run Pose Estimation on Frames**  
   - Get keypoints for each frame and store them (e.g., as JSON)  
   - Effort: ⭐⭐–⭐⭐⭐  
   - Deliverable: Pose data saved per frame

6. **Visualize Skeleton Overlay on Video**  
   - Draw pose on original frame using OpenCV or Matplotlib  
   - Effort: ⭐⭐  
   - Deliverable: Overlaid video/skeleton preview

7. **Normalize Keypoint Coordinates**  
   - Translate & scale: Use hip or torso center as origin  
   - Effort: ⭐⭐–⭐⭐⭐  
   - Deliverable: Function to normalize poses for player-invariant analysis

## Part 3: Feature Engineering

8. **Compute Joint Angles**  
   - Use vector math to calculate angles: elbow, knee, shoulder  
   - Effort: ⭐⭐⭐  
   - Deliverable: Angle calculator module

9. **Track Joint Speeds and Trajectories**  
   - Differentiate keypoint positions over time  
   - Effort: ⭐⭐⭐  
   - Deliverable: Speed/time plots for wrist, ankle, etc.

10. **Estimate Center of Mass**  
    - Approximate from hips and shoulders  
    - Effort: ⭐⭐  
    - Deliverable: CoM path over time

11. **Build Feature Vectors for Motion Patterns**  
    - Combine angles, speeds, distances into structured data  
    - Effort: ⭐⭐⭐  
    - Deliverable: Data ready for analysis or ML

## Part 4: Movement Analysis

12. **Classify Basic Movement Types**  
    - Use rules or train a simple model to detect: forehand, backhand, footwork types  
    - Effort: ⭐⭐⭐⭐  
    - Deliverable: Movement classifier outputting labels per frame/segment

13. **Detect Key Events (e.g. Strokes, Split Steps)**  
    - Use thresholds on speed/angle changes  
    - Effort: ⭐⭐⭐  
    - Deliverable: Timeline of events

14. **Compare Players or Sessions**  
    - Calculate consistency, agility, movement range  
    - Effort: ⭐⭐  
    - Deliverable: Performance comparison charts

## Part 5: Visualization and Reporting

15. **Create Visual Dashboards**  
    - Plot movement heatmaps, angle graphs, key events over time  
    - Effort: ⭐⭐–⭐⭐⭐  
    - Deliverable: Jupyter notebook or web dashboard

16. **Document the Process and Results**  
    - Include methodology, challenges, results, visuals  
    - Effort: ⭐⭐  
    - Deliverable: Final report (PDF or notebook)

## Optional Advanced Extensions

- Multi-person tracking (doubles)
- Real-time feedback or alerts
- Feed movement features into a larger game analysis system
