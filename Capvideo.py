import cv2

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('C:\\Users\\liu\\Videos\\Video Test\\output.mp4',fourcc, 25.0, (640,480))

#创建窗口
cv2.namedWindow("video",cv2.WINDOW_NORMAL)
cv2.resizeWindow("video",640,480)

#打开摄像头
cap = cv2.VideoCapture("C:\\Users\\liu\\Documents\\YOLO_V8\\ultralytics-main\\runs\\detect\\predict\\trailer.avi")

while True:
    #读取视频帧
    ret,frame = cap.read()
    if not ret:
        break

    #显示视频帧
    cv2.imshow("video",frame)
    #将视频帧写入输出文件
    out.write(frame) 
    #按下q键退出
    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        break

#释放资源
cap.release()
out.release()
cv2.destroyAllWindows()