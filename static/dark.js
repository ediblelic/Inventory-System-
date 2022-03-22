let lightmode = document.getElementById('sunoff')
let darkmode = document.getElementById('dark')
let class_dark = localStorage.getItem('dark-mode')



const enableDarkMode = () => {
    document.body.classList.add("dark-mode");
    localStorage.setItem("dark-mode", "enabled");
    document.getElementById('sunoff').style.visibility = 'visible'
    document.getElementById('light').style.visibility = 'hidden'
   
    document.getElementById('dark').style.visibility = 'hidden'
    document.getElementById('darkon').style.visibility = 'visible'

   
}

const disableDarkMode = () => {
 
    document.body.classList.remove('dark-mode');
    localStorage.setItem('DarkMode', null);
    document.getElementById('sunoff').style.visibility = 'hidden'
    document.getElementById('light').style.visibility = 'visible'
   
    document.getElementById('dark').style.visibility = 'visible'
    document.getElementById('darkon').style.visibility = 'hidden'

    
}   

darkmode.addEventListener('click',() =>{

	enableDarkMode();
	

})
lightmode.addEventListener('click',() =>{

	disableDarkMode()
	TransitionEvent(1)

})

if (darkmode === "enabled"){
    enableDarkMode()
}
