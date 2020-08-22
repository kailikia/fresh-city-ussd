<?php
namespace ussd\module\Model;
use Magento\Framework\Model\AbstractModel;
class Example extends AbstractModel
{
    /**
     * Define resource model
     */
    protected function _construct()
    {
    $this->_init('ussd\module\Model\ResourceModel\USSD');
    }
}