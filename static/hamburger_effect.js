let menu = document.getElementById('menu');
let active = true;

menu.addEventListener('click',() =>
{
    
    if (active === true){
    
     
    document.getElementById('side_bar').style.transform = 'translateX(-100%)';
    document.getElementById('main-section').style.transform = 'translateX(-30%)';
    
    active = false
    }
    
    else {
        
        document.getElementById('side_bar').style.transform = 'translateX(0%)';
        document.getElementById('main-section').style.transform = 'translateX(0%)';
        active = true
        
    };
    
});