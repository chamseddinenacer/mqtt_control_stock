from pyniryo import *
client = NiryoRobot("10.10.10.10")  
client.connect()
client.calibrate(CalibrateMode.AUTO)

place_pose=PoseObject(
    x= -0.039, y=0.309,z=0.215,
    roll=0.215,pitch =1.486,  yaw=1.486,
)

client.move_pose(*place_pose.to_list())
client.update_tool
client.grasp_with_tool()
client.release_with_tool()