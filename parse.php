<?php

if(($handle = fopen('test.csv', 'r')) !== false)
{
    $header = fgetcsv($handle);
    while(($data = fgetcsv($handle)) !== false)
    {
        // resort/rewrite data and insert into DB here
        // try to use conditions sparingly here, as those will cause slow-performance

        // I don't know if this is really necessary, but it couldn't harm;
        // see also: http://php.net/manual/en/features.gc.php
        unset($data);
    }
    fclose($handle);
}