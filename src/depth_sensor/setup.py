from setuptools import find_packages, setup

package_name = 'depth_sensor'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='niranjan',
    maintainer_email='niranjan@todo.todo',
    description='Tiburon ROV depth sensor simulation',
    license='MIT',
    entry_points={
    'console_scripts': [
        'depth_sensor_node = depth_sensor.depth_sensor_node:main',
        'navigation_node = depth_sensor.navigation_node:main',
    ],
},
)