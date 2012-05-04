<?php
namespace NethServer\Module\User\Plugin;

/*
 * Copyright (C) 2011 Nethesis S.r.l.
 * 
 * This script is part of NethServer.
 * 
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

use Nethgui\System\PlatformInterface as Validate;

/**
 * @todo describe class
 */
class Ssh extends \Nethgui\Controller\Table\AbstractAction
{
    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Service', 10);
    }
    
    public function bind(\Nethgui\Controller\RequestInterface $request)
    {
        $key = \Nethgui\array_head($request->getPath());
        $this->declareParameter('ssh', Validate::BOOLEAN, array(array($this->getAdapter(), $key, 'Shell')));
        parent::bind($request);
    }

    public function readSsh($dbValue)
    {
        if ($dbValue == '/bin/bash') {
            return '1';
        }

        return '';
    }

    public function writeSsh($formInput)
    {
        if ($formInput == '1') {
            return array('/bin/bash');
        }

        return array('/bin/false');
    }

}
