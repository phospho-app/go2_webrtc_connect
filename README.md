# Full Unitree Go2 WebRTC Driver

This repository contains a Python implementation of the WebRTC driver to connect to the Unitree Go2 Robot.

- High level control of the dog through WebRTC (like the Unitree Go app)
- No jailbreak or firmware manipulation required.
- Compatible with Go2 AIR/PRO/EDU models.

![Description of the image](./images/screenshot_1.png)

## Installation

1. Clone this repository **with submodules**. If you get the error **Data channel did not open in time**, you likely didn't clone submodules.

```bash
git clone --recurse-submodules https://github.com/legion1581/go2_webrtc_connect.git
cd go2_webrtc_connect
```

2. (Optional) Install `portaudio19-dev`. This is only used for sound capabilities for Go2 Pro and Edu.

```bash
# On Linux
sudo apt update && sudo apt install portaudio19-dev
```

```bash
# On MacOS
brew update && brew install portaudio19-dev
```

3. We'll use [uv](https://github.com/astral-sh/uv) to manage python dependencies. Make sure it's installed.

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

4. Turn on the Go2. Get the IP of your Go2 using the Unitree Go2 app. Then, close the app and disconnect from your dog. Change the scripts to put your Go2 IP address.

Then, run scripts using `uv`.

```bash
uv run examples/data_channel/lowstate/lowstate.py
```

## Supported Versions

The currently supported Go2 firmware packages are:

- 1.1.1 - 1.1.4 (latest available)
- 1.0.19 - 1.0.25

Use the Unitree Go2 app to check your firmware version.

## Audio and Video Support

There are video (recvonly) and audio (sendrecv) channels in WebRTC that you can connect to. Check out the examples in the `/example` folder.

## Lidar support

There is a lidar decoder built in, so you can handle decoded PoinClouds directly. Check out the examples in the `/example` folder.

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

Example programs are located in the /example directory.

### Thanks

A big thank you to TheRoboVerse community! Visit us at [TheRoboVerse](https://theroboverse.com) for more information and support.

Special thanks to the [tfoldi WebRTC project](https://github.com/tfoldi/go2-webrtc) and [abizovnuralem](https://github.com/abizovnuralem) for adding LiDAR support and [MrRobotow](https://github.com/MrRobotoW) for providing a plot LiDAR example.

### Support

If you like this project, please consider buying the author a coffee:

<a href="https://www.buymeacoffee.com/legion1581" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
