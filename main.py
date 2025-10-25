import os
import subprocess
import logging

from devops_scripts.utils import create_logger

def deploy_container(image_name, container_name):
    """Deploy a container on a remote server."""
    logger = create_logger(__name__)

    try:
        # Create a Dockerfile for the image
        with open('Dockerfile', 'w') as f:
            f.write(f'START\nFROM {image_name}\nCMD ["echo", "Hello, World!"]\n')

        # Build the Docker image
        subprocess.run(['docker', 'build', '-t', image_name, '.'], check=True)

        # Push the image to Docker Hub
        subprocess.run(['docker', 'push', image_name], check=True)

        # Create a container from the image
        subprocess.run(['docker', 'run', '-d', '--name', container_name, image_name], check=True)

        logger.info(f'Container {container_name} deployed successfully.')
    except subprocess.CalledProcessError as e:
        logger.error(f'Failed to deploy container: {e}')
    finally:
        # Clean up
        if os.path.exists('Dockerfile'):
            os.remove('Dockerfile')

def main():
    image_name = 'my-devops-image'
    container_name = 'my-devops-container'

    deploy_container(image_name, container_name)

if __name__ == '__main__':
    main()