uploader_element = document.getElementById('uploader');
file_button = document.getElementById('employee_photo');



// Profile Picture Handler

const handleProfilePicture = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
        const dataUrl = event.target.result;
        document.getElementById('profilePicDisplay').src = dataUrl;
    };
    reader.readAsDataURL(file);
};

uploader_element.addEventListener('click', () => {
    file_button.click();
});

file_button.addEventListener('change', handleProfilePicture);

// Registation Form Handler

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie name matches 'csrftoken'
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const handleRegistrationSuccess = () => {

    formWrapper = document.getElementById('form_wrapper');
    form = document.getElementById('registation_form');
    registration_success = document.createElement('div');
    registration_success.className = 'registation_success';
    registration_success.innerHTML = ` <div class="registation_success">
    <h1>Registation Success</h1>
    <a href="/faceapp/home/" class="btn submit_btn">Home</a>
</div>`
formWrapper.replaceChild(registration_success,form)
};

const handleRegistrationForm = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    employee_photo = document.getElementById('profilePicDisplay').getAttribute('src');
    employee_id = formData.get('employee_id');
    employee_name = formData.get('employee_name');
    employee_email = formData.get('employee_email');
    employee_mobile = formData.get('employee_mobile');
    employee_designation = formData.get('employee_designation');
    employee_address = formData.get('employee_address');

    url = "http://127.0.0.1:8000/api/employee/"
    url_encoding = "http://127.0.0.1:8000/api/update_face_encoding/"

    const data = {
        "employee_id": employee_id,
        "employee_name": employee_name,
        "employee_email": employee_email,
        "employee_mobile": employee_mobile,
        "employee_photo": employee_photo,
        "employee_designation": employee_designation,
        "employee_address": employee_address
    }

    const encoding_data = {
        "employee_id": employee_id,
        "employee_photo": employee_photo
    }

    const registerData = fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
            console.log("Registation successful");
            console.log(result);

            fetch(url_encoding, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(encoding_data)
            })

            
        });
    handleRegistrationSuccess();
    
       


};





const registration_form = document.getElementById('registation_form');

registration_form.addEventListener('submit', handleRegistrationForm);

