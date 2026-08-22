import argparse
from lerobot.cameras.opencv import OpenCVCamera, OpenCVCameraConfig
from lerobot.cameras import ColorMode, Cv2Rotation, Cv2Backends


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Test OpenCVCamera")
    parser.add_argument("--index_or_path", type=str, default='/dev/video0', help="Camera index or path (default: /dev/video0)")
    parser.add_argument("--fps", type=int, help="Frames per second")
    parser.add_argument("--width", type=int, help="Frame width")
    parser.add_argument("--height", type=int, help="Frame height")
    parser.add_argument("--color_mode", type=str, choices=[mode.name for mode in ColorMode], help="Color mode")
    parser.add_argument("--rotation", type=str, choices=[rotation.name for rotation in Cv2Rotation], help="Rotation")
    args = parser.parse_args()

    kwargs = {k: v for k, v in vars(args).items() if v is not None}
    kwargs['backend'] = Cv2Backends.V4L2 # Fix the bad file descriptor error by setting the backend to V4L2 for Linux systems 
    config = OpenCVCameraConfig(**kwargs)
    print(f"Using OpenCVCameraConfig: {config}")

    with OpenCVCamera(config) as camera:

        frame = camera.read()
        print(f"read() call returned frame with shape:", frame.shape)

        try:
            for i in range(10):
                frame = camera.async_read(timeout_ms=1000)
                print(f"async_read call returned frame {i} with shape:", frame.shape)
        except TimeoutError as e:
            print(f"No frame received within timeout: {e}")

        # Instantly return a frame - returns the most recent frame captured by the camera
        try:
            initial_frame = camera.read_latest(max_age_ms=1000)
            for i in range(10):
                frame = camera.read_latest(max_age_ms=1000)
                print(f"read_latest call returned frame {i} with shape:", frame.shape)
                print(f"Was a new frame received by the camera? {not (initial_frame == frame).any()}")
        except TimeoutError as e:
            print(f"Frame too old: {e}")
