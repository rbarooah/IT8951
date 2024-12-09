#!/bin/bash

# Must be run as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root"
    exit 1
fi

# Create eink group if it doesn't exist
groupadd -f eink

# Add current user to eink group
usermod -a -G eink $SUDO_USER

# Create udev rules
cat > /etc/udev/rules.d/99-eink.rules << 'EOL'
# SPI devices
SUBSYSTEM=="spidev", GROUP="eink", MODE="0660"
# GPIO devices
SUBSYSTEM=="gpio", GROUP="eink", MODE="0660"
SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c '\
        chown -R root:eink /sys/class/gpio && chmod -R 770 /sys/class/gpio;\
        chown -R root:eink /sys/devices/virtual/gpio && chmod -R 770 /sys/devices/virtual/gpio;\
        chown -R root:eink /sys$devpath && chmod -R 770 /sys$devpath\
'"
EOL

# Reload udev rules
udevadm control --reload-rules
udevadm trigger

# Set permissions on render_bmp
chown root:eink render_bmp
chmod 4750 render_bmp
setcap cap_sys_rawio+ep render_bmp

echo "Setup complete! Please log out and log back in for the group changes to take effect."
