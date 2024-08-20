function ShowPopBox(Box){
    const popBox = document.getElementById('pop-box')
    if (Box == 'Schedule'){
        const scheduleBox = document.getElementById('schedule-box')
        scheduleBox.style.display = 'flex'
    }
    else if(Box == 'Delete'){
        const deleteBox = document.getElementById('delete-box')
        deleteBox.style.display = 'flex'
    }
    else if(Box == 'Confirm'){
        const confirmBox = document.getElementById('confirm-box')
        confirmBox.style.display = 'flex'
    }
    popBox.style.display = 'flex'
    document.body.style.overflow = 'hidden';
    document.body.style.height = '100vh';
}

function ClosePopBox(Box){
    const popBox = document.getElementById('pop-box')
    if (Box == 'Schedule'){
        const scheduleBox = document.getElementById('schedule-box')
        scheduleBox.style.display = 'none'
        document.getElementById('error-box').style.display = 'none'
    }
    else if(Box == 'Delete'){
        const deleteBox = document.getElementById('delete-box')
        deleteBox.style.display = 'none'
    }
    else if(Box == 'Confirm'){
        const confirmBox = document.getElementById('confirm-box')
        confirmBox.style.display = 'none'
    }
    popBox.style.display = 'none'
    document.body.style.overflow = '';
    document.body.style.height = 'fit-content';
}

function ChangeSchedule( Order_Id, Order_Name, Order_Place, Order_Date){
    document.getElementById('sch-head-name').innerText = Order_Name
    document.getElementById('sch-head-place').innerText = Order_Place
    document.getElementById('date_id').value = Order_Id
    document.getElementById('sch-head-date').innerHTML = 'Ordered On : ' + Order_Date

    ShowPopBox('Schedule')

}

function DeleteOrder( Order_Id, Order_Name, Order_Place, Order_Date){
    document.getElementById('del-head-name').innerText = Order_Name
    document.getElementById('del-head-place').innerText = Order_Place 
    document.getElementById('del-head-date').innerHTML = 'Ordered On : ' + Order_Date
    document.getElementById('order_id').value = Order_Id
    ShowPopBox('Delete')
}

function submit(id){
    if(id == 'schedule_form' ){
        const scheduleDate = document.getElementById('schedule_date').value;
        const errorBox = document.getElementById('error-box');
        const today = new Date();
        const currentDate = today.toISOString().split('T')[0];
        if (scheduleDate <= currentDate || !scheduleDate) {
            errorBox.style.display = 'flex';
            return;
        } 
    }
    let form = document.getElementById(id)
    form.submit();
}