
const videoframe = document.getElementById('videoElement');

const openCamera = () => {
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia){
        navigator.mediaDevices.getUserMedia({video:true})
        .then((stream) => {
            videoframe.srcObject = stream;

        })
        .catch((error) => {
            console.error('Error accessing camera: ', error);
        });
    }
    else{
        console.error('getUserMedia is not supported in this browser');
    }
};

const getImageDataUrl = () => {
    const canvasElement = document.createElement('canvas');
    canvasElement.width = videoframe.width;
    canvasElement.height = videoframe.height;
    const canvasContext = canvasElement.getContext('2d');
    canvasContext.drawImage(videoframe,0,0,canvasElement.width,canvasElement.height);
    const imageData = canvasElement.toDataURL();
    return imageData
    // console.log(imageData);
};

const timeCounter = (last_update_time) => {
    const currentDate = new Date().toISOString();
    console.log(currentDate);
    console.log(typeof(currentDate));

    const date1 = new Date(currentDate);
    const date2 = new Date(last_update_time);

    const timeDifference = date1 - date2;
    const timeDifferenceInSeconds = timeDifference / 1000;
    return timeDifferenceInSeconds
}

const markAttendence = () => {
    const markAttendenceUrl = "/api/attendence/"
    const matchFacesUrl = "/api/face_recognition/"
    const lastUpdateUrl = "/api/last_update/"
    const employeeUrl = "/api/getEmployee/"
    const emp_photo = document.getElementById('emp_photo');
    const emp_name = document.getElementById('employee_name');
    const emp_id = document.getElementById('employee_id');
    const attendence_status = document.getElementById('attendence_status');
    const image_url = getImageDataUrl();
    const data = {"image_url": image_url}

    fetch(matchFacesUrl,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
            console.log("reco");
            employee_id = result['result']
            console.log(employee_id);
            const data = {'employee_id': employee_id}
            

            fetch(lastUpdateUrl,{
                method:'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(update => {
                let last_update = (update['last_update']);
                timeDifferenceInSeconds = timeCounter(last_update)

                if(timeDifferenceInSeconds > 60){
                    fetch(markAttendenceUrl,{
                method:'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(data)


            })
            .then(response => response.json())
            .then(res => {
                console.log(res);
                // const employee_name = res['employee_name']
                fetch(employeeUrl,{
                    method:'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify(data) 
                })
                .then(response => response.json())
                .then(employee =>{
                    
                    emp_photo.src = employee['employee_photo'];
                    emp_name.innerText = employee['employee_name'];
                    emp_id.innerText = employee['employee_id'];
                    attendence_status.innerText = 'MARKED';
                    attendence_status.style.backgroundColor = "green";

                    setTimeout(() => {
                        console.log('Delayed action after 2 seconds');
                      }, 10000);


                })
                console.log("marked");
            })

                }
            else if(timeDifferenceInSeconds<60){
                fetch(employeeUrl,{
                    method:'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify(data) 
                })
                .then(response => response.json())
                .then(employee =>{
                emp_photo.src = employee['employee_photo'];
                    emp_name.innerText = employee['employee_name'];
                    emp_id.innerText = employee['employee_id'];
                    attendence_status.innerText = 'ALREADY MARKED';
                    attendence_status.style.backgroundColor = "yellow";
                })
                    
                }
                else{
                    emp_photo.src = "https://picsum.photos/200";
                    emp_name.innerText = '';
                    emp_id.innerText = '';
                    attendence_status.innerText = 'Detecting';
                    attendence_status.style.backgroundColor = "red";
                }
            })

            

    })

};

openCamera();
setInterval(markAttendence,2000);