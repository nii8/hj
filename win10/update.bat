rem net stop "windows update"
net stop wuauserv
sc config wuauserv start= disabled
SchTasks /Delete /TN "\Microsoft\Windows\WindowsUpdate\Scheduled Start"
cmd /k