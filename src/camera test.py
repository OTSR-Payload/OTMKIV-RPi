from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
import time

picam2 = Picamera2()

# Configure video
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

# Create encoder
encoder = H264Encoder()

# Output file
output = FileOutput("video_10s.h264")

# Start camera
picam2.start()

# Enable continuous autofocus
picam2.set_controls({
    "AfMode": 2  # Continuous autofocus
})

# Give autofocus time to adjust before recording
time.sleep(2)

# Start recording
picam2.start_recording(encoder, output)

print("Recording started...")

time.sleep(10)

# Stop recording
picam2.stop_recording()
picam2.stop()

print("Recording finished")
