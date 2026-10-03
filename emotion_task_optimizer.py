# main.py
import time
import cv2
from tasks import get_user_tasks
from algorithms import csp_filter, greedy, hill_climbing, stochastic, mini_a_star
from emotion_detector import detect_emotion_from_frame, start_camera

def task_mode(tasks):
    cap, detector = start_camera()
    current_task = None
    print("\nTASK MODE ACTIVATED. Press 'q' to quit.\n")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break
            
            emotion = detect_emotion_from_frame(frame, detector)
            print(f"Emotion detected: {emotion}")
            
            valid_tasks = csp_filter(tasks, emotion)
            if not valid_tasks:
                print("No valid tasks for this emotion. Taking break.")
                time.sleep(5)
                continue
            
            task_greedy = greedy(valid_tasks)
            task_hill = hill_climbing(valid_tasks, current_task if current_task else task_greedy)
            task_stochastic = stochastic(valid_tasks)
            tasks_a_star = mini_a_star(valid_tasks)
            
            if emotion in ["angry","sad","tired"]:
                print("\nDistress detected! Take a break for 30 seconds.")
                time.sleep(30)
                print("Break ended. Choose next action.\n")
            
            current_task = task_greedy
            print(f"Next Task Recommendation (Greedy): {current_task.name}")
            
            time.sleep(30)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

def main():
    tasks = get_user_tasks()
    choice = input("\nStart Task Mode? (y/n): ")
    if choice.lower() == "y":
        task_mode(tasks)
    else:
        print("Exiting program.")

if __name__ == "__main__":
    main()
