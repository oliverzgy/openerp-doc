.. i18n: Running Automated Test Cases
.. i18n: ----------------------------
..

运行一个自动分析案例
----------------------------

.. i18n: We can check all the queries on :ref:`CLI <CLI-link>` by making a file with queries to be tested with the syntax given in :ref:`CLI <CLI-link>`
..

我们可以在命令行上核对所有的查询 :ref:`CLI <CLI-link>`可以使用给定的语法测试经过查询生成的文件 :ref:`CLI <CLI-link>`

.. i18n: For example we can create *test_query* file with the content like 
..

例如我们可以创建 一个名为*test_query* 的类似下面内容的文件 

.. i18n: .. :ref:`test_query <test_query-link>`
..

.. :ref:`test_query <test_query-link>`

.. i18n: -------
..

-------

.. i18n: ::
.. i18n: 
.. i18n:   DATABASE='terp'
..

::

  DATABASE='terp'

.. i18n: ::
.. i18n: 
.. i18n:   ./tinybi.py -d ${DATABASE} -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select <br />{[user].[all]} on rows, {[measures].[credit_limit],[measures].[count]} <br />on columns from res_partner"
..

::

  ./tinybi.py -d ${DATABASE} -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select <br />{[user].[all]} on rows, {[measures].[credit_limit],[measures].[count]} <br />on columns from res_partner"

.. i18n: ::
.. i18n: 
.. i18n:   ./tinybi.py -d ${DATABASE} -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select <br /> {[measures].[credit_limit],[measures].[count]} on rows, {[user].[all],[user].children} <br /> on columns from res_partner"
..

::

  ./tinybi.py -d ${DATABASE} -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select <br /> {[measures].[credit_limit],[measures].[count]} on rows, {[user].[all],[user].children} <br /> on columns from res_partner"

.. i18n: -------
..

-------

.. i18n: The file can be run at the command prompt. It will give output on success or an error message on failure
..

这个文件可以在命令提示符下运行.就会输出成功或失败的错误信息

.. i18n: The output of this file can be viewed CubeCliExample test_query
..

通过多维示例视窗可以查看test_query的输出结果
