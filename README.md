# Description: 
This container normalizes the data contained in the file published by Binary Edge at https://api.binaryedge.io/v1/minions into a format that can be consumed as an EDL by the Palo Alto NGFW.  The output is written to /tmp/minionsparser/minions.edl.txt.

# Requirements
This contianer is designed to run on Docker and requries either Docker or Docker Desktop.  

# Deployment and Use
1. Clone the Repsitory.
2. Build with `docker compose`
    - Run `docker compose up -d`
2. Build with `docker build`
    - Run `docker build -t minionsparser .`
    - Run `docker run -it --mount type=bind,source=/tmp/minionsparser/,target=/tmp/minionsparser --rm --name minionsparser-ded minionsparser`
3. Check /tmp/minionsparser for output

# Support Policy

This container is provided under an **as-is, best effort,** support policy. This container and all code should be seen as community supported.  We will contribute our expertise as and when possible. 

Palo Alto Networks **does not** provide technical support or help in using or troubleshooting the components of this project through its normal support options such as Palo Alto Networks support teams, or ASC (Authorized Support Centers) partners and backline support options. The underlying product used in conjunction with this container (Palo Alto Networks NGFW and EDLs) is supported by Palo Alto Networks according to support entitlements, but the support is only for the product functionality and not for help in deploying or using this container itself. 
