<?php

/* @var $view Nethgui\Renderer\Xhtml */


echo $view->panel()
    ->insert($view->radioButton('access', 'private'))
    ->insert($view->radioButton('access', 'public'))
    ->insert($view->checkBox('rootLogin', 'yes'))
    ->insert($view->checkBox('passwordAuth', 'yes'))

;