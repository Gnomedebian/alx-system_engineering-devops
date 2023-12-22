# creating a manifest that kills a process: killmenow
exec { 'killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow', }
