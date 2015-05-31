# Introduction #

The ROS-Cyton Module provides a ROS interface for Energid's actinSE and Robai's Cyton 7-DOF humanoid manipulators. The aim of this module is to expose actinSE  and the Cyton hardware API through ROS  .


# Overview #

Using the ROS-_actionlib_  a user can access the methods of Actin-SE and the Cyton hardware API.  The methods included allow for direct, real-time control of the Cyton robot arms in both jointspace and end-effector modes.

The module consist of six nodes named as follows:  _actinSE\_node_ ,_cyton_ ,_guide frame_ ,_hardware_ ,_send joints_ ,and _set home_ .The core node(action server) is  called _actinse_.  The _actinse_ node accepts end effector (EE) coordinates and publishes joint values and joint rates.  The node which sends EE coordinates is called the _guide frame_ node. It can be any program which is configured to send EE coordinates  to a particular topic .The _cyton_ node will subscribe to the output of the _actinse_ node  and send the valued to the cyton arm using the cyton hardware API (or the _hardware_ node).  The _set home_ node moves the cyton to a default home position .

Cyton can also be directly controlled using joint space values.  There are two nodes for doing this task, the _hardware_ node and _send joints_ node.  The _hardware_ node is an action server which will receive the joint values from the _send\_joints_ action client  and publishes to a topic.  The _cyton_ node will subscribe to the topic and move the cyton according to the joint values.


# Detailed Description #

For additional details on the control interface or Actin please see the Actin-SE API or the Cyton Hardware Interface API.

## ROS-Cyton Module Architecture ##


The ROS-Cyton module is using  actinSE and the cyton-hardware library for its operation. The module mainly consist of  _actionservers_ and _actionclients_. There are two _actionservers_ and two _actionclients_.  The first _actionserver_ is called _actinse_. It performs EE to joint-space conversion using the ActinSE Cyton IK engine. Its _actionclient_ is the _guide frame_ node.  It will send guide frame values to the _actionserver_. The second _actionserver_ is the  _hardware node_.  It is responsible for marshalling joint values from the actionClient to the **/cyton/feedback** topic.  Its actionclient is the _send joints_ node .It will send the joint values to the _hardware_ node .The user can control the cyton in two ways.


  1. End effector control

  1. Joint-space control

### End effector control ###

![http://outgoing.energid.info/ROS/wiki/images/1.png](http://outgoing.energid.info/ROS/wiki/images/1.png)

During end effector control ,the _actinse_ node acts as action server and the _guide frame_ node is the action client. The EE values are published from the _guide frame_ node to the _actinse_ node .
The _actinse_ node subscribes to the values and feeds back the resulting values in the **/cyton/feedback**  topic.


#### actinSE\_node ####

> This node acts as the _actionserver_. The node will subscribe to topics publish by the  action client.

**Subscribed Topics**

**/cyton/goal**

  1. float32[.md](.md) position - Endeffector coordinates or jointvalues
  1. float32[.md](.md) rate - Jointrates
  1. float32 time - Simulation time
  1. int32 eeindex - Endeffector type
  1. uint32 home - Home flag to move cyton to home position
  1. float32 gripper\_value - Gripper joint angle  for controlling gripper separately
  1. float32 gripper\_rate  - Gripper joint rate


**Published Topics**

**/cyton/result**
  1. float32[.md](.md) position - Joint values

**/cyton/feedback**
  1. float32[.md](.md) position - Joint Values
  1. float32[.md](.md) rate - Joint rates
  1. float32 time - Simulation time
  1. float32 gripper\_feed\_value
  1. float32 gripper\_feed\_rate

#### guide\_frame node(input node) ####

> This  node act as the action client. It will publish the following topics.

**Published Topics**

**/cyton/goal**


  1. float32[.md](.md) position - Endeffector coordinates
  1. float32[.md](.md) rate - Joint rates
  1. float32 time - Simulation time
  1. int32 eeindex - Endeffector type
  1. uint32 home - Home flag to move the cyton to home position
  1. float32 gripper\_value - Gripper joint angle  for controlling gripper separately
  1. float32 gripper\_rate - Gripper joint rate


#### cyton\_node ####

This node handles the movement of the cyton robotic arm. It uses the cyton hardware API for movement. It will subscribe to the **/cyton/feedback** topic from the _actinSE_ node and push data to the hardware.


#### set\_home ####

Moves the cyton to a default home position.  It will only work when the user is working with EE coordinates .

Execution - **rosrun cyton set\_home**

### Joint-level Control ###

#### Hardware\_node ####

![http://outgoing.energid.info/ROS/wiki/images/2.png](http://outgoing.energid.info/ROS/wiki/images/2.png)

This node handles the movement of cyton through direct joint values .It acts as an _actionserver_.  It will publish joint values to the topic **/cyton/feedback**.

**Subscribed Topics**

**/cyton/goal**

  1. float32[.md](.md) position - jointvalues
  1. float32[.md](.md) rate - Joint-rates
  1. float32 time - Simulation time
  1. int32 eeindex - Endeffector type
  1. uint32 home - Home flag to move cyton to home position
  1. float32 gripper\_value - Gripper joint angle  for controlling gripper separately
  1. float32 gripper\_rate - Gripper joint rate

**Published Topics**

**/cyton/feedback**

  1. float32[.md](.md) position :Joint Values
  1. float32[.md](.md) rate :Joint rates
  1. float32 time :Simulation time
  1. float32 gripper\_feed\_value
  1. float32 gripper\_feed\_rate

#### send\_joints ####

This node acts as an actionclient of the hardware\_node.  This will publish  joint values to topic **/cyton/goal**.

**Published Topics**

**/cyton/goal**

  1. float32[.md](.md) position - Endeffector coordinates
  1. float32[.md](.md) rate - Joint-rates
  1. float32 time - Simulation time
  1. int32 eeindex - Endeffector type
  1. uint32 home - Home flag to move cyton to home position
  1. float32 gripper\_value - Gripper joint angle  for controlling gripper separately
  1. float32 gripper\_rate - Gripper joint rate


#### cyton\_node ####

> This node handles the movement of the cyton robotic arm.  It uses the cyton hardware API for movement.  It will subscribe to the **/cyton/feedback** topic from the _actinSE_ node and send to hardware .

**Subscribed Topics**

**/cyton/feedback**

  1. float32[.md](.md) position - Joint Values
  1. float32[.md](.md) rate - Joint rates
  1. float32 time - Simulation time
  1. float32 gripper\_feed\_value
  1. float32 gripper\_feed\_rate


Here the action-client is called the _guide frame_ node. The function of the _guide frame_ node is to send guide frame values (End effector coordinates) to the _actinSE_ node .The _guide frame_ node can be any program which can send the guide frame coordinates .

# Tutorials #
This package will works well on Ubuntu 12.04 ,for other distribution it is still in testing .

**Installation**

  1. Set the PATH instruction in README file inside the cyton module folder
  1. Execute roscd cyton
  1. rosmake


**Execution
  1. Change the USBToDynamixel permission before execution**

![http://outgoing.energid.info/ROS/wiki/images/3.png](http://outgoing.energid.info/ROS/wiki/images/3.png)
**For EE control**

  1. roscd cyton
  1. cd bin
  1. rosrun cyton actinSE\_node -Starting actinSE actionserver for solving IK
  1. rosrun cyton cyton\_move\_node - It will connect to robot hardware
  1. rosrun cyton  guide\_frame\_node - Send EE values to cyton from a file called guide\_frame.txt.
  1. rosrun cyton set\_home - Setting cyton to home position

**Examples**


  1. rosrun cyton pick\_and\_place - Execute a simple pick and place operation
  1. rosrun cyton move\_end\_effector - Move end-effector with gripper movements

**Publisher and Subscriber**

  1. roscd cyton
  1. cd bin
  1. rosrun cyton actinSE\_node -Starting actinSE actionserver for solving IK
  1. rosrun cyton cyton\_move\_node - It will connect to robot hardware
  1. rosrun cyton cyton\_ee\_subscriber - Subscribe the guide frame data from the publisher
  1. rosrun cyton cyton\_publisher - Publish the guide frame data

**Publishing guide frame data from command line**

![http://outgoing.energid.info/ROS/wiki/images/command.png](http://outgoing.energid.info/ROS/wiki/images/command.png)


**For Joint Control**

  1. roscd cyton - Change folder into cyton
  1. cd bin - Change folder into cyton/bin
  1. rosrun cyton hardware\_node - Actionserver which recieves joint values and send to some other client
  1. rosrun cyton move\_hardware - Connect to cyton robot
  1. rosrun cyton send\_joints - Sending joint values and rates directly to hardware without IK
