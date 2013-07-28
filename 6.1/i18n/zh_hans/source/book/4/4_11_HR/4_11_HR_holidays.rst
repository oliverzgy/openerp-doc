
.. i18n: .. index::
.. i18n:    single: Human Resources; holidays
.. i18n: ..
..

.. index::
   single: Human Resources; holidays
..

.. i18n: Holiday Management
.. i18n: ==================
..

假期管理
==================

.. i18n: You can manage leaves taken by employees using the :mod:`hr_holidays`
.. i18n: module. The configuration wizard to install this module is shown below:
..

你可以使用 :mod:`hr_holidays` 模块来管理员工假期，这个模块的安装配置向导如下图所示:

.. i18n: .. figure::  images/config_wiz_holidays.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuration wizard to install hr_holidays module*
..

.. figure::  images/config_wiz_holidays.png
   :scale: 75
   :align: center

   *hr_holidays模块安装配置向导*

.. i18n: Using the menu :menuselection:`Human Resources --> Holidays --> Leave Requests` an employee can request a leave.
..

员工请假可以使用菜单 :menuselection:`人力资源 --> 假期 --> 准假申请` :menuselection:`Human Resources --> Holidays --> Leave Requests` 来实现。

.. i18n: Leaves requests can be recorded by employees and validated by their managers.
.. i18n: Once a leave request is validated, it appears automatically in the agenda of the employee.
.. i18n: You can define several allocation types (paid holidays, sickness, etc.) and manage allocations
.. i18n: per type.
..

请假申请由员工建立，并由他们的主管来审核。一旦申请被审核通过，它就会自动出现在员工的日程表上。
你可以定义多种准假方式（如有薪假期，病假等）然后分别进行管理。

.. i18n: OpenERP can provide the following features for efficient holiday management process:
..

OpenERP 为高效的假期管理流程提供了如下的功能:

.. i18n: * It helps you to manage leaves and leave requests.
.. i18n: * Synchronisation with an internal agenda (use of :mod:`crm`) is possible:
.. i18n:   in order to automatically create a case when a holiday request is accepted,
.. i18n:   you have to link the holidays status to a case section.
.. i18n: * You can set up colour preferences according to your leave type, for example, `Sick Leave` should be red in reports.
.. i18n: * An employee can request for more days off, by making a new Allocation Request through :menuselection:`Human Resources --> Holidays --> Allocation Requests`.
..

* 帮助你管理假期及假期申请。
* 与内部议程同步（使用 `客户关系管理` :mod:`crm` 模块）是可能的: 你必须将准假状态与事实部分相连接，这样才可以当一个准假
  申请被接受时它将自动生成事实。
* 你可以根据你的假期类型设置不同的颜色，如“病假”可以在报表中显示为红色。
* 员工可以通过 :menuselection:`人力资源 --> 假期 --> 分配准假` :menuselection:`Human Resources --> Holidays --> Allocation Requests` 申请新的分配准假，从而申请更多的假期。

.. i18n: The statistical report for leaves can be seen using the
.. i18n: :menuselection:`Human Resources --> Reporting --> Holidays --> Leaves Analysis` menu.
..

使用菜单 :menuselection:`人力资源 --> 报表 --> 假期 --> 假期分析` :menuselection:`Human Resources --> Reporting --> Holidays --> Leaves Analysis` 可以查看假期统计报表。

.. i18n: .. index::
.. i18n:    single: holidays; leave types
..

.. index::
   single: holidays; leave types

.. i18n: Define different leave types
.. i18n: ----------------------------
..

定义不同的休假类型
----------------------------

.. i18n: You can define various leave types which can be availed of by an employee during a request for leave. To define a new leave type, navigate to :menuselection:`Human Resources --> Configuration --> Holidays --> Leave Type` and click :guilabel:`New`.
..

你可以定义不同的请假类型，便于员工区分其请假申请。定义一个新的请假类型，点击菜单 :menuselection:`人力资源 --> 设置 --> 假期 --> 请假类型`, 
然后点击 :guilabel:`新建` 按钮。

.. i18n: .. figure::  images/holidays_leave_type.png
.. i18n:    :scale: 80
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Leave Type form*
..

.. figure::  images/holidays_leave_type.png
   :scale: 80
   :align: center

   *请假类型表单*

.. i18n: You can configure the following information:
..

你可以设置如下的信息：

.. i18n: * :guilabel:`Leave Type` : A name for the leave type.
.. i18n: * :guilabel:`Colour in Report` : A colour that will be used in the leaves summary report.
.. i18n: * :guilabel:`Meeting` : If you select a meeting, once a leave is validated, an event will be created in the calendar.
.. i18n: * :guilabel:`Apply Double Validation` : If ``True``, then the request will require a second validator.
.. i18n: * :guilabel:`Allow to Override Limit` : If ``True``, the employee will be allowed to take more leaves than the maximum limit.
..

* :guilabel:`请假类型` : 请假类型的名称。
* :guilabel:`报表中的颜色` : 请假摘要报表中显示的颜色。
* :guilabel:`会议`: 如果你选择了一个会议，一旦此申请被审核通过，日历中就会创建一个事件。
* :guilabel:`二次审核` : 如果勾选此项，则此类型的申请均需要做二次审核。
* :guilabel:`允许不顾限制` : 如果勾选此项，则此类型的申请中，员工享受的假期可以超过最大的限制值。

.. i18n: After entering the leave type information, click :guilabel:`Save`.
..

完成信息输入后，请点击 :guilabel:`保存` 按钮。

.. i18n: .. index::
.. i18n:    single: holidays; manage requests and approvals
..

.. index::
   single: holidays; manage requests and approvals

.. i18n: Manage Holiday requests and approvals
.. i18n: -------------------------------------
..

管理假期申请和批准
-------------------------------------

.. i18n: An employee can request for leave from :menuselection:`Human Resources --> Holidays --> Leave Requests`. In a new :guilabel:`Leave Requests` form, you may enter the following:
..

员工可以在 :menuselection:`人力资源 --> 假期 --> 准假申请` :menuselection:`Human Resources --> Holidays --> Leave Requests` 中请假。你要在一个新的准假申请表中填入以下信息.

.. i18n: * :guilabel:`Description` : Reason for leave.
.. i18n: * :guilabel:`Leave Category` : Either ``By Employee`` or ``By Employee Category``.
.. i18n: * :guilabel:`Employee` : If leave category is ``By Employee``, you must select an employee who places this request.
.. i18n: * :guilabel:`Category` : If leave category is ``By Employee Category``, you must select an employee category which places this request.
.. i18n: * :guilabel:`Leave Type`: Select a pre-defined type of leave.
.. i18n: * :guilabel:`Start Date` : Leave start date.
.. i18n: * :guilabel:`End Date` : Leave end date.
.. i18n: * :guilabel:`Number of Days` : It is calculated based on the :guilabel:`Start Date` and the :guilabel:`End Date`.
..

* :guilabel:`说明` : 请假原因.                                                              
* :guilabel:`模式` : ``按员工`` 或者 ``按员工分类`` .                                       
* :guilabel:`员工` : 如果准假分类是 ``员工`` ，你必须选择一个 ``员工`` .                    
* :guilabel:`分类` : 如果请假分类是 ``员工分类`` ，你必须选择 ``员工分类`` .                
* :guilabel:`准假类型`: 选择提前设置好的准假类型.                                           
* :guilabel:`开始日期` : 请假开始时间.                                                      
* :guilabel:`结束日期` : 请假结束时间.                                                      
* :guilabel:`天数` : 共请假天数(据 :guilabel:`开始日期` 与 :guilabel:`结束日期` 计算所得) . 
                                                                                            
.. i18n: .. figure::  images/employee_leave_request_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Leave Requests form*
..

.. figure::  images/employee_leave_request_form.png
   :scale: 75
   :align: center

   *Leave Requests form*

.. i18n: The employee can click :guilabel:`Confirm` to make the leave request available to his manager for approval. The employee's manager can find leave requests awaiting approval by navigating to :menuselection:`Human Resources --> Holidays --> Leave Requests` and clicking :guilabel:`Clear` and :guilabel:`To Approve` filter button. The manager can select a pending request to open its form view and click :guilabel:`Refuse` to reject the request or :guilabel:`Approve` to accept the request. If the selected leave type has :guilabel:`Apply Double Validation` set to ``True``, then another action by a second manager will be required to give the request its final state, from ``Waiting Second Approval`` to either ``Approved`` or ``Refused``.
..

员工点击 :guilabel:`确认` 后将准假申请提交给他的领导等待审批。经理可以在 :menuselection:`人力资源 --> 假期 --> 准假申请` :menuselection:`Human Resources --> Holidays --> Leave Requests` （还是“要审批的请假申请”）”中
找到等待审批的员工准假申请，可以点击 :guilabel:`清除` 或者 :guilabel:`过滤器` 。经理可以打开一个待审批的申请然后点击 :guilabel:`拒绝` 按钮拒绝申请或者点击
:guilabel:`审批` 按钮批准申请。如果是 :guilabel:`双重验证` 类型的准假申请，最后审批的经理将决定申请的最终结果，申请将从最后的 ``待审批`` 变为 ``已审批`` 或者 ``拒绝`` 。
 
.. i18n: .. index::
.. i18n:    single: holidays; previous requests
..

.. index::
   single: holidays; previous requests

.. i18n: Track previous Holiday requests
.. i18n: -------------------------------
..

跟踪前面的请假
-------------------------------

.. i18n: Previous holidays can be tracked in a number of ways in OpenERP. You can get a report of leave requests by all users from :menuselection:`Human Resources --> Holidays --> Leave Requests`. Click :guilabel:`Clear` and then :guilabel:`Validated` to see a list of all approved leave requests. To see refused requests, click :guilabel:`Clear` and see the records marked with the colour red.
..

在OpenERP的一系列方式中可以找到以前的假期申请。你可以在 :menuselection:`人力资源 --> 假期 --> 准假申请` :menuselection:`Human Resources --> Holidays --> Leave Requests` 中看到所有用户的准假申请记录.
点击 :guilabel:`清除` 然后 :guilabel:`生效` 从而看到所有已批准的准假申请。看拒绝的申请，点击 :guilabel:`清除` 并且看到红色标记的记录。

.. i18n: To see previous allocation requests, navigate to :menuselection:`Human Resources --> Holidays --> Allocation Requests` and follow the same procedure as above.
..

在 :menuselection:`人力资源 --> 假期 --> 分配准假` :menuselection:`Human Resources --> Holidays --> Allocation Requests` 中看到以前的分配准假，之后的操作流程同上。

.. i18n: Through :menuselection:`Human Resources --> Holidays --> Leaves Summary`, you can track previous leaves as well as allocation requests in the same manner, but only for the currently logged in user. By default, you can see the requests grouped by leave type.
..

在 :menuselection:`人力资源 --> 假期 --> 准假摘要` :menuselection:`Human Resources --> Holidays --> Leaves Summary` 中，用同样的方法你可以找到以前的
准假摘要，但是仅限于当前登录的用户。默认地，你可以根据准假类型看到不同的申请分类。

.. i18n: :menuselection:`Human Resources --> Reporting --> Holidays --> Leaves Analysis` will give you the statistical report of leaves and allocations grouped by employee and leave type. To see all requests without grouping, click :guilabel:`Clear`.
..

在 :menuselection:`人力资源 --> 报告 --> 准假 --> 准假分析` :menuselection:`Human Resources --> Reporting --> Holidays --> Leaves Analysis` 中可以看到请假统计纪录，并且根据员工和准假类型分类。点击 `清除` 看到
所有未分类的准假申请。

.. i18n: All the above statistical reports are enhanced by various filters and groupings to assist you in your search for required information. You can filter requests by their :guilabel:`State` (`Validated`, `To Confirm`, `To Approve`), :guilabel:`Employee`, :guilabel:`Department` and :guilabel:`Leave Type`. You can also view requests placed in :guilabel:`This Month`. You can group by :guilabel:`Employee`, :guilabel:`Manager`, :guilabel:`Department`, :guilabel:`Type` and :guilabel:`State`.
..

通过各种过滤和分类上述所有统计报告有助于你搜索到你需要的信息。你可以通过他们的 :guilabel:`状态` （ `生效`, `确认`, `审批`）， :guilabel:`员工` ， :guilabel:`部门` 
和 :guilabel:`准假类型` 来过滤申请。你也可以查看 :guilabel:`当月` 的申请。你可以通过 :guilabel:`员工` ， :guilabel:`经理` ， :guilabel:`部门` ， :guilabel:`类型` 和 :guilabel:`状态` 分类。

.. i18n: .. figure::  images/holidays_leaves_analysis.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Leaves Analysis statistical report*
..

.. figure::  images/holidays_leaves_analysis.png
   :scale: 75
   :align: center

   *Leaves Analysis statistical report*

.. i18n: To get an overview of leaves by department, go to :menuselection:`Human Resource --> Reporting --> Holidays --> Leaves by Department`. You may select a :guilabel:`From` date, a :guilabel:`Leave Type` (``Validated``, ``Confirmed`` or ``Both Validated and Confirmed``) and select at least one department. Click :guilabel:`Print` to generate a PDF report based on your specifications.
..

在 :menuselection:`人力资源 --> 报告 --> 假期 --> 部门准假` :menuselection:`Human Resource --> Reporting --> Holidays --> Leaves by Department` 中可以看到完整的部门准假。你也可以选择一个 :guilabel:`开始时间` ， :guilabel:`准假类型` 
（ ``生效``， ``确认`` 或者 ``生效确认`` ）并且至少喜欢则一个部门。点击 :guilabel:`打印` 将根据你的设置生成一个PDF文件。

.. i18n: .. figure::  images/holidays_dept_leaves.png
.. i18n:    :scale: 80
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Leaves by Department PDF report*
..

.. figure::  images/holidays_dept_leaves.png
   :scale: 80
   :align: center

   *Leaves by Department PDF report*

.. i18n: .. index::
.. i18n:    single: holidays; allocation requests
..

.. index::
   single: holidays; allocation requests

.. i18n: Allow employees to enter their own allocation requests
.. i18n: ------------------------------------------------------
..

允许员工输入他们自己的分配请求
------------------------------------------------------

.. i18n: To be able to request leaves at all, an employee must be allocated some leaves which he can avail of. Usually the management makes an allocation of leaves for its employees. But, for instance, when an employee has been working on an exceptional basis on weekends, he might be entitled to extra leaves. In such a case, the employee himself can be allowed to place a request for allocation, which can then be approved or rejected by his manager. If approved, the employee can request leaves based on the type and limit of this allocation too.
..

为了能够休假，员工必须被分配一些可以利用的假期。通常管理会为员工安排一些休假。但是当一个员工由于特殊原因要在周末
上班，那么他将被允许在其他时间休假。这种情况下，员工被允许自己安排休假，但准假申请是否被批准由他的经理决定。如果
获得批准，那么员工根据该休假类型及限制进行休假。

.. i18n: Leave allocations can be requested from :menuselection:`Human Resources --> Holidays --> Allocation Requests`. In its form view you can fill the following details:
..

在 :menuselection:`人力资源 --> 假期 --> 分配准假` :menuselection:`Human Resources --> Holidays --> Allocation Requests` 中进行分配准假。需要完成下列信息:

.. i18n: * :guilabel:`Description` : A name for the request.
.. i18n: * :guilabel:`Allocation Category` : Either ``By Employee`` or ``By Employee Category``.
.. i18n: * :guilabel:`Employee` : If allocation category is ``By Employee``, you must select an employee for whom this allocation is made.
.. i18n: * :guilabel:`Category` : If allocation category is ``By Employee Category``, you must select an employee category for whom this allocation is made.
.. i18n: * :guilabel:`Leave Type` : Select a pre-defined leave type.
.. i18n: * :guilabel:`Number of Days` : The number of days requested for allocation.
.. i18n: * :guilabel:`Reasons` : Specify the reason of request.
..

* :guilabel:`说明` : 请假类型名称.                                      
* :guilabel:`分配模式` : ``按员工`` 或者 ``按员工分类`` .           
* :guilabel:`员工` : 如果分配分类是 ``员工`` ，必须选择一个 ``员工`` .     
* :guilabel:`分类` : 如果分配分类是 ``员工分类`` ，必须选择 ``员工分类`` . 
* :guilabel:`准假类型` : 选择之前设置好的准假类型.
* :guilabel:`天数` : 分配准假的天数.
* :guilabel:`原因` : 说明原因.

.. i18n: The remaining fields are read-only and will acquire details once the request has been accepted or rejected. The employee can click :guilabel:`Confirm` to send the allocation request to his manager. The state of the request will now be ``Waiting Approval``.
..

一旦申请被批准或者被拒绝那么其余部分是只读并且将获得细节。员工点击 :guilabel:`确认` 将分配准假发送给他的经理。此时申请将处于
 ``待审批`` 状态。

.. i18n: .. figure::  images/holidays_allocation_request.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Allocation Requests form*
..

.. figure::  images/holidays_allocation_request.png
   :scale: 75
   :align: center

   *Allocation Requests form*

.. i18n: The manager will then find this request in his list of allocation requests. He can then either click :guilabel:`Refuse` to reject the request or click :guilabel:`Approve` to accept the request.
..

经理将在他的分配准假明细中找到申请。他可以点击 :guilabel:`拒绝` 拒绝该申请或者点击 :guilabel:`审批` 批准该申请.

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
