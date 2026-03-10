def analyze( objects, face_detected, hand_raised):

    # Case 1: Student left camera
    if "person" in objects and "cell phone" in objects:
        behavior = "Student is using phone"
    # case 2: student is out of the camera
    elif "person" not in objects:
        behavior = "Student is not active in class"
    
    # Case 3: Face not visible
    elif not face_detected:
        behavior = "Student looking away from camera"
    
    #case 4: if student raised hand
    elif hand_raised:
        behavior = "Student raised hand"

    # Case 5: Normal behavior
    else:
        behavior = "Student attentive"

    return behavior