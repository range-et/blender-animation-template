# Blender imports
import bpy
import time
import os
# Add other imports and functions here
import math
import mathutils


#### THESE ARE SOME HELPER FUNCTIONS

# This is a helper function that takes in a messaage and shows a tiny 
# Popup window use for debugging and as an alternative for print statements
def debug_log(message="", title="Debug Box", icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

# This is the main animate function
def animate(start_frame, end_frame, debug=False):
    ### DONT CHANGE THIS UNLESS YOU KNOW WHAT YOU'RE DOING
    # Get the list of objects to animate
    # For example, you can select all objects or use a specific group
    objects_to_animate = [obj for obj in bpy.context.scene.objects]

    # Clear existing keyframes for these objects
    for obj in objects_to_animate:
        obj.animation_data_clear()
    
    # Loop through each frame
    for frame in range(start_frame, end_frame + 1):
        # Set the current frame
        bpy.context.scene.frame_set(frame)
    
        # Loop through each object and perform operations
        for obj in objects_to_animate:
            
            #### PERFORM OBJECT BASED OPERATIONS HERE
            #### INSERT CODE BELOW THIS LINE
            #########################################
            
            
            # In this example I'm slowing things down by a factor of 10
            # Example code, move the cube up and down
            if obj.name == "Cube":
                obj.location.z = 10*math.sin(frame / 10) 
                # Add keyframes for this
                obj.keyframe_insert(data_path="location", index=-1)
                
            
            # Move the camera in a circular motion, with a rotation constrain
            if obj.name == "Camera":
                obj.location.x = 10 * math.sin(frame / 10)
                obj.location.y = 10 * math.cos(frame / 10)
                obj.location.z = 5  # Add some height to the camera

                # Define the point to look at (in this case, it's the origin)
                look_at_point = mathutils.Vector((0, 0, 0))

                # Calculate the direction vector from the camera to the look_at_point
                direction = look_at_point - obj.location

                # Use the track_to method to point the camera at the look_at_point
                obj.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()

                # Keyframe the location and rotation
                obj.keyframe_insert(data_path="location", index=-1)
                obj.keyframe_insert(data_path="rotation_euler", index=-1)
            

            #########################################
            #### DONT CHANGE CODE BELOW THIS LINE
        
    # Set the timeline back to the start frame
    bpy.context.scene.frame_set(start_frame)


# call the function to start animating
# Set start and end frames
start_frame = 1 # start frame 
end_frame = 250 # end frame

animate(start_frame, end_frame)