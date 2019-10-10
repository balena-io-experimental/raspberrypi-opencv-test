# RaspberryPi Camera Device Test

This project uses opencv to read a frame from the default camera device (`/dev/video0`)

Set the following  configuration variables:

* `BALENA_HOST_CONFIG_start_x` = `1`
* `BALENA_HOST_CONFIG_gpu_mem` = `144` ( *this value may need to change based on what RPi you are using* )
