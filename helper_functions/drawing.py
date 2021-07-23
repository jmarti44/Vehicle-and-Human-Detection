def draw_roi(current_frame, width, height, is_vehicle_detected, ROI_Line):
    if ROI_Line == 'vertical':
        roi_start = (int(width / 2), 0)
        rot_end = (int(width / 2), height)
    else:
        roi_start = (0, int(height / 2))
        rot_end = (width, int(height / 2))

    if is_vehicle_detected is True:
        cv2.line(current_frame, roi_start, roi_end, (0, 0, 0xFF), 5)
    else:
        cv2.line(current_frame, roi_start, roi_end, (0, 0xFF, 0), 5)


def draw_detection_boxes(boxes, current_frame):
    H, W, _ = current_frame.shape
    for x in range(boxes):
        y1, x1, y2, x2 = boxes[x]
        x1 *= W
        x2 *= W
        y1 *= H
        y2 *= H
        cv2.rectangle(current_frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)


def draw_counter(current_frame, total_vehicles_detected):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
        current_frame,
        'Detected Vehicles: ' + str(total_vehicles_detected),
        (10, 35),
        font,
        0.8,
        (0, 0xFF, 0xFF),
        2,
        cv2.FONT_HERSHEY_SIMPLEX,
    )
