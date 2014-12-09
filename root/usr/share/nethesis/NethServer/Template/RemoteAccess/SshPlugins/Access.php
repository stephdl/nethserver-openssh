<?php

/* @var $view Nethgui\Renderer\Xhtml */


echo $view->panel()
    ->insert($view->checkBox('rootLogin', 'yes'))
    ->insert($view->checkBox('passwordAuth', 'yes'))

;
