#!/bin/bash
fallocate -l 1G /tmp/swapfile
chmod 600 /tmp/swapfile
mkswap /tmp/swapfile
swapon /tmp/swapfile
uvicorn main:app --host 0.0.0.0 --port 10000