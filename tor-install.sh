#!/bin/bash
RED='\033[0;31m'
GRN='\033[0;32m'
NC='\033[0m'
# Make sure you have the Universe repo added, which you should as it is fairly
# standard but just in case you don"t:
echo -e "${RED}> add-apt-repository universe${NC}"
sudo add-apt-repository universe
echo -e "${RED}> sudo apt update${NC}"
sudo apt update
# Install Tor (and TorBrowser)
echo -e "${RED}> sudo apt install tor torbrowser-launcher${NC}"
sudo apt install tor torbrowser-launcher
echo -e "${GRN}TOR Installed!${NC}"

# Install TorGhost
# Make sure git is installed
echo -e "${RED}> sudo apt install git${NC}"
# Clone the git repo and build it
sudo apt install git
echo -e "${RED}> git clone https://github.com/SusmithKrishnan/torghost.git${NC}"
git clone https://github.com/SusmithKrishnan/torghost.git
echo -e "${RED}> cd torghost${NC}"
cd torghost
echo -e "${RED}> chmod +x build.sh${NC}"
chmod +x build.sh
# cython3 is needed to build
echo -e "sudo apt install cython3${NC}"
sudo apt install cython3
echo -e "${RED}> ./build.sh${NC}"
./build.sh

# Tidy up
cd -
sudo rm -r torghost

echo -e "${RED}> sudo torghost${NC}"
sudo torghost

echo -e "${RED}> sudo torghost -s${NC}"
sudo torghost -s
echo -e "${RED}> sudo torghost -r${NC}"
sudo torghost -r
echo -e "${RED}> sudo torghost stop${NC}"
sudo torghost stop

exit 0
