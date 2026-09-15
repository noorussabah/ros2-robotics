from setuptools import find_packages, setup

package_name = 'robot_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='noor',
    maintainer_email='noor@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [            'battery_publisher = robot_basics.battery_publisher:main',
            'battery_monitor = robot_basics.battery_monitor:main',
'calculator_server = robot_basics.calculator_server:main',
'calculator_client = robot_basics.calculator_client:main',
'square_driver = robot_basics.square_driver:main',
'lidar_monitor = robot_basics.lidar_monitor:main',
        ],
    },
)
