<?php
namespace <vendor>\<module>\Model\Resource;
class Example extends \Magento\Framework\Model\ResourceModel\Db\AbstractDb
{
    /**
     * Define main table
     */
    protected function _construct()
    {
    $this->_init('ussd', 'id');   //here id is the primary key of custom table
    }
}