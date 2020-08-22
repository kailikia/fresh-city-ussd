<?php
namespace <vendor>\<module>\Model\ResourceModel\Example;

class Collection extends \Magento\Framework\Model\ResourceModel\Db\Collection\AbstractCollection
{
    /**
     * Define model & resource model
     */
    protected function _construct()
    {
    $this->_init(
        '<vendor>\<module>\Model\Example',
        '<vendor>\<module>\Model\ResourceModel\Example'
    );

    }
}