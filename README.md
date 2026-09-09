# LeRobot Fablab Riviera

About robot learning: https://huggingface.co/spaces/lerobot/robot-learning-tutorial

## Hardware

- Distribution: Pop!_OS
- Graphics card: GTX 1080 Ti (11 GB VRAM)
- Robotic arm: SO-ARM101 open source kit, designed by TheRobotStudio and integrated into Hugging Face's LeRobot ecosystem
   - https://huggingface.co/docs/lerobot/main/en/so101
- Camera: CMOS IMX291 sensor (USB, UVC protocol, no driver needed)

## LeRobot

https://huggingface.co/docs/lerobot/index

- Models, datasets and tools
- Built on PyTorch
- A set of pretrained models
- lerobot: open source library
a    - LeRobotDataset: standardized dataset format

## Installing the lerobot library

Full tutorial available here: https://huggingface.co/docs/lerobot/main/en/installation

1. Create a conda environment with the required Python version
   `conda create -y -n lerobot python=3.12`

2. Activate the conda environment
   `conda activate lerobot`

3. TorchCodec is supported on Pop!_OS (Linux x86_64). So install ffmpeg in the conda environment
   `conda install ffmpeg -c conda-forge`

4. Clone the LeRobot repository then move into it
   `git clone https://github.com/huggingface/lerobot.git`
   `cd lerobot`

5. Install the library in editable mode, with all dependencies (policies, environments, hardware, dev tools). Remember to activate the conda environment before this step.
   `pip install -e ".[all]"`

If you run into build errors, you may need additional system dependencies (cmake, build-essential, ffmpeg libraries). On Linux:
`sudo apt-get install cmake build-essential python3-dev pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev`

https://huggingface.co/docs/lerobot/main/en/so101

## Imitation learning

https://huggingface.co/docs/lerobot/il_robots

### Record a dataset

Find your camera `lerobot-find-cameras opencv # or realsense for Intel Realsense cameras`


