# Full Unitree Go2 WebRTC Driver

This repository contains a Python implementation of the WebRTC driver to connect to the Unitree Go2 Robot.

- High level control of the dog through WebRTC (like the Unitree Go app)
- No jailbreak or firmware manipulation required.
- Compatible with Go2 AIR/PRO/EDU models.

![Description of the image](./images/screenshot_1.png)

## Installation

```bash
pip install go2-webrtc-connect
```

For audio and video:

```bash
pip install "go2-webrtc-connect[audio,video]"
```

## Supported Firmware Versions

The currently supported Go2 firmware packages are:

- 1.1.1 - 1.1.4 (latest available)
- 1.0.19 - 1.0.25

Use the Unitree Go2 app to check your firmware version.

## Audio Support

There is an audio (sendrecv) channel in WebRTC that you can connect to.

This is supported only on Go2 Pro and Edu. Check out the examples in the `/examples/audio` folder.

1. Install `portaudio19-dev`.

```bash
# On Linux
sudo apt update && sudo apt install portaudio19-dev
```

```bash
# On MacOS
brew update && brew install portaudio19-dev
```

2. Use the `audio` optional dependencies

```bash
uv run --extra audio  examples/audio/mp3_player/play_mp3.py
```

## Video Support

There is video (recvonly) channel in WebRTC. Use the `video` optional dependencies for this.

```bash
uv run --extra audio  examples/audio/mp3_player/play_mp3.py
```

## Lidar support

There is a lidar decoder built in, so you can handle decoded PoinClouds directly. Check out the examples in the `/examples/data_channel/lidar` folder.

## Connection Methods

The driver supports three types of connection methods:

1. **AP Mode**: Go2 is in AP mode, and the WebRTC client is connected directly to it:

   ```python
   Go2WebRTCConnection(WebRTCConnectionMethod.LocalAP)
   ```

2. **STA-L Mode**: Go2 and the WebRTC client are on the same local network. An IP or Serial number is required:

   ```python
   Go2WebRTCConnection(WebRTCConnectionMethod.LocalSTA, ip="192.168.8.181")
   ```

   If the IP is unknown, you can specify only the serial number, and the driver will try to find the IP using the special Multicast discovery feature available on Go2:

   ```python
   Go2WebRTCConnection(WebRTCConnectionMethod.LocalSTA, serialNumber="B42D2000XXXXXXXX")
   ```

3. **STA-T mode**: Remote connection through remote Unitrees TURN server. Could control your Go2 even being on the diffrent network. Requires username and pass from Unitree account

   ```python
   Go2WebRTCConnection(WebRTCConnectionMethod.Remote, serialNumber="B42D2000XXXXXXXX", username="email@gmail.com", password="pass")
   ```

## Multicast scanner

The driver has a built-in Multicast scanner to find the Unitree Go2 on the local network and connect using only the serial number.

## Usage

Example programs are located in the /examples directory.

### Thanks

A big thank you to TheRoboVerse community! Visit us at [TheRoboVerse](https://theroboverse.com) for more information and support.

Special thanks to the [tfoldi WebRTC project](https://github.com/tfoldi/go2-webrtc) and [abizovnuralem](https://github.com/abizovnuralem) for adding LiDAR support and [MrRobotow](https://github.com/MrRobotoW) for providing a plot LiDAR example.

### Support

This project is originally a fork from [the repo of legion1581](https://github.com/legion1581/go2_webrtc_connect). Please consider buying the author a coffee:

<a href="https://www.buymeacoffee.com/legion1581" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
