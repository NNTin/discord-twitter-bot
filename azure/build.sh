#!/usr/bin/env bash
for docker_arch in amd64 arm32v6 arm64v8; do
  case ${docker_arch} in
    amd64   ) qemu_arch="x86_64" ;;
    arm32v6 ) qemu_arch="arm" ;;
    arm64v8 ) qemu_arch="aarch64" ;;
  esac
  cp Dockerfile.cross ../Dockerfile.${docker_arch}
  sed -i "s|__BASEIMAGE_ARCH__|${docker_arch}|g" ../Dockerfile.${docker_arch}
  sed -i "s|__QEMU_ARCH__|${qemu_arch}|g" ../Dockerfile.${docker_arch}
  if [ ${docker_arch} == 'amd64' ]; then
    sed -i "/__CROSS_/d" ../Dockerfile.${docker_arch}
  else
    sed -i "s/__CROSS_//g" ../Dockerfile.${docker_arch}
  fi
done