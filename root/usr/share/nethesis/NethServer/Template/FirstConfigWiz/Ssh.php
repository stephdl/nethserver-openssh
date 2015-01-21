<?php

include "WizHeader.php";

echo "<div class='wspreline'>";
echo $T("SSH_WizDescription", iterator_to_array($view));
echo "</div>";
echo "<div class='wspreline ui-state-warning ui-state-highlight sshwiz-highlight'><i class='fa'></i>";
echo $T("SSH_WizWarning", iterator_to_array($view));
echo "</div>";
echo $view->textInput('port');

$view->includeCSS("
  .sshwiz-highlight {
     border: 1px solid #f8893f;
     color: #592003;
     background-color: #fee4bd;
     margin: 8px;
     padding: .8em;
     display: inline-block;
  }

  .sshwiz-highlight > i {flex-shrink: 0;}
  .sshwiz-highlight > i:before { content: \"\\f071\"; font-size: 1.2em; width: 1.5em; padding: 5px;}
  .sshwiz-highlight > span { padding-left: .8em }

");


include "WizFooter.php";

