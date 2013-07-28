
.. i18n: .. index::
.. i18n:    single: accounting; workflow
.. i18n:    single: accounting; invoicing
.. i18n:    single: invoicing
.. i18n: ..
..

.. index::
   single: accounting; workflow
   single: accounting; invoicing
   single: invoicing
..

.. i18n: Accounting Workflow and Automatic Invoice Creation
.. i18n: ==================================================
..

会计工作流和自动创建发票
==================================================

.. i18n: The chart :ref:`fig-accfl` shows the financial workflow followed by each invoice.
..

The chart :ref:`fig-accfl` shows the financial workflow followed by each invoice.

.. i18n: .. _fig-accfl:
.. i18n: 
.. i18n: .. figure::  images/account_flow.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Accounting workflow for invoicing and payment*
..

.. _fig-accfl:

.. figure::  images/account_flow.png
   :scale: 50
   :align: center

   *Accounting workflow for invoicing and payment*

.. i18n: In general, when you use all of OpenERP's functionality, invoices do not need to be entered
.. i18n: manually. Draft invoices are generated automatically from other documents such as Purchase Orders.
..

In general, when you use all of OpenERP's functionality, invoices do not need to be entered
manually. Draft invoices are generated automatically from other documents such as Purchase Orders.

.. i18n: .. index::
.. i18n:    single: invoices
..

.. index::
   single: invoices

.. i18n: Draft Invoices
.. i18n: --------------
..

发票草稿
--------------

.. i18n: The system generates invoice proposals which are initially set to the \ ``Draft``\   state. While
.. i18n: these invoices remain unconfirmed, they have no accounting impact within the system. There is nothing
.. i18n: to stop users creating their own draft invoices if they want to.
..

The system generates invoice proposals which are initially set to the \ ``Draft``\   state. While
these invoices remain unconfirmed, they have no accounting impact within the system. There is nothing
to stop users creating their own draft invoices if they want to.

.. i18n: You can create draft customer invoice manually using the menu :menuselection:`Accounting --> Customers --> Customer Invoices`.
..

You can create draft customer invoice manually using the menu :menuselection:`Accounting --> Customers --> Customer Invoices`.

.. i18n: The information that is needed for invoicing is automatically taken from the Partner form (such as
.. i18n: payment conditions and the invoice address) or from the Product (such as the account to be used) or
.. i18n: from a combination of the two (such as applicable Taxes and the Price of the product).
..

The information that is needed for invoicing is automatically taken from the Partner form (such as
payment conditions and the invoice address) or from the Product (such as the account to be used) or
from a combination of the two (such as applicable Taxes and the Price of the product).

.. i18n: .. tip:: Draft Invoices
.. i18n: 
.. i18n:         There are several advantages in working with draft invoices:
.. i18n: 
.. i18n:         * You have got an intermediate validation state before the invoice is approved.
.. i18n:           This is useful when your accountants are not the people creating the initial invoice,
.. i18n:           but are still required to approve it before the invoice is entered into the accounts.
.. i18n: 
.. i18n:         * It enables you to create invoices in advance, without approving them at the same time.
.. i18n:           You are also able to list all of the invoices awaiting approval.
..

.. tip:: Draft Invoices

        There are several advantages in working with draft invoices:

        * You have got an intermediate validation state before the invoice is approved.
          This is useful when your accountants are not the people creating the initial invoice,
          but are still required to approve it before the invoice is entered into the accounts.

        * It enables you to create invoices in advance, without approving them at the same time.
          You are also able to list all of the invoices awaiting approval.

.. i18n: Open or Pro Forma Invoices
.. i18n: --------------------------
..

商业或形式发票
--------------------------

.. i18n: You can approve (or validate) an invoice in the \ ``Open``\   or \ ``Pro-forma``\   state.
.. i18n: A pro forma invoice does not have an invoice number yet, nor accounting entries.
.. i18n: It is commonly used as a preliminary invoice or for customs purposes.
.. i18n: It is more formal than a draft invoice and a pro forma invoice can later be converted to an open invoice.
..

You can approve (or validate) an invoice in the \ ``Open``\   or \ ``Pro-forma``\   state.
A pro forma invoice does not have an invoice number yet, nor accounting entries.
It is commonly used as a preliminary invoice or for customs purposes.
It is more formal than a draft invoice and a pro forma invoice can later be converted to an open invoice.

.. i18n: An open invoice has a unique invoice number. The invoice is sent to the customer and is marked on
.. i18n: the system as awaiting payment.
..

An open invoice has a unique invoice number. The invoice is sent to the customer and is marked on
the system as awaiting payment.

.. i18n: .. index::
.. i18n:    single: reconciliation
..

.. index::
   single: reconciliation

.. i18n: Reconciliation and Payments
.. i18n: ---------------------------
..

核销和支付
---------------------------

.. i18n: In OpenERP, an invoice is considered to be paid when its accounting entries have been reconciled
.. i18n: with the payment entries. If there has not been a reconciliation, an invoice can remain in the ``Open``
.. i18n: state until you have entered the payment.
..

In OpenERP, an invoice is considered to be paid when its accounting entries have been reconciled
with the payment entries. If there has not been a reconciliation, an invoice can remain in the ``Open``
state until you have entered the payment.

.. i18n: .. tip::  Payment and Reconciliation
.. i18n: 
.. i18n:         To avoid surprises, it is important to understand the idea of reconciliation and its link with
.. i18n:         invoice payment.
.. i18n: 
.. i18n:         You will find the :guilabel:`Paid/Reconciled` checkbox on an invoice.
.. i18n:         It is checked if the Journal Entry of the invoice has been totally reconciled
.. i18n:         with one or several Journal Entries of payment.
..

.. tip::  Payment and Reconciliation

        To avoid surprises, it is important to understand the idea of reconciliation and its link with
        invoice payment.

        You will find the :guilabel:`Paid/Reconciled` checkbox on an invoice.
        It is checked if the Journal Entry of the invoice has been totally reconciled
        with one or several Journal Entries of payment.

.. i18n: .. note:: Reconciliation
.. i18n: 
.. i18n:         Reconciliation links entries in an account that cancel each other out – they are reconciled
.. i18n:         to each other (sum of credits = sum of debits).
.. i18n: 
.. i18n:         This is generally applied to payments against corresponding invoices.
..

.. note:: Reconciliation

        Reconciliation links entries in an account that cancel each other out – they are reconciled
        to each other (sum of credits = sum of debits).

        This is generally applied to payments against corresponding invoices.

.. i18n: Without the reconciliation process, OpenERP would be incapable of marking invoices that have been
.. i18n: paid. Suppose that you have got the following situation for the ``Smith and Offspring`` customer:
..

Without the reconciliation process, OpenERP would be incapable of marking invoices that have been
paid. Suppose that you have got the following situation for the ``Smith and Offspring`` customer:

.. i18n: * Invoice 145: 50,
.. i18n: 
.. i18n: * Invoice 167: 120,
.. i18n: 
.. i18n: * Invoice 184: 70.
..

* Invoice 145: 50,

* Invoice 167: 120,

* Invoice 184: 70.

.. i18n: If you receive a payment of 120, OpenERP will delay reconciliation because there is a choice of
.. i18n: invoices to pay. It could either reconcile the payment against invoices 145 and 184 or against
.. i18n: invoice 167.
..

If you receive a payment of 120, OpenERP will delay reconciliation because there is a choice of
invoices to pay. It could either reconcile the payment against invoices 145 and 184 or against
invoice 167.

.. i18n: .. tip:: Treatment in Lots
.. i18n: 
.. i18n:         Usually, different transactions are grouped together and handled at the same time rather than
.. i18n:         invoice by invoice. This is called batch work or lot handling.
.. i18n: 
.. i18n:         You can select several documents in the list of invoices: check the checkboxes of
.. i18n:         the interesting lines using the web client and click the appropriate shortcut button at the right;
.. i18n:         or shift-click the lines using the mouse in the GTK client and use the action or print button at
.. i18n:         the top –
.. i18n:         these give you the option of a number of possible actions on the selected objects.
..

.. tip:: Treatment in Lots

        Usually, different transactions are grouped together and handled at the same time rather than
        invoice by invoice. This is called batch work or lot handling.

        You can select several documents in the list of invoices: check the checkboxes of
        the interesting lines using the web client and click the appropriate shortcut button at the right;
        or shift-click the lines using the mouse in the GTK client and use the action or print button at
        the top –
        these give you the option of a number of possible actions on the selected objects.

.. i18n: At regular intervals, and independent of the invoices, an automatic import procedure or a manual
.. i18n: accounts procedure can be used to bring in bank statements. These comprise all of the payments of
.. i18n: suppliers and customers and general transactions, such as between accounts.
..

At regular intervals, and independent of the invoices, an automatic import procedure or a manual
accounts procedure can be used to bring in bank statements. These comprise all of the payments of
suppliers and customers and general transactions, such as between accounts.

.. i18n: When an account is validated, the corresponding accounting entries are automatically generated by
.. i18n: OpenERP.
..

When an account is validated, the corresponding accounting entries are automatically generated by
OpenERP.

.. i18n: Invoices are marked as ``Paid`` when accounting entries on the invoice have been reconciled with
.. i18n: accounting entries about their payment.
..

Invoices are marked as ``Paid`` when accounting entries on the invoice have been reconciled with
accounting entries about their payment.

.. i18n: This reconciliation transaction can be carried out at various places in the process, depending on
.. i18n: your preference:
..

This reconciliation transaction can be carried out at various places in the process, depending on
your preference:

.. i18n: * at data entry for the accounting statement,
.. i18n: 
.. i18n: * manually from the account records,
.. i18n: 
.. i18n: * automatically using OpenERP's intelligent reconciliation.
..

* at data entry for the accounting statement,

* manually from the account records,

* automatically using OpenERP's intelligent reconciliation.

.. i18n: You can create the accounting records directly, without using the invoice and account statements. To
.. i18n: do this, use the rapid data entry form in a journal. Some accountants prefer this approach because
.. i18n: they are used to thinking in terms of accounting records rather than in terms of invoices and
.. i18n: payments.
..

You can create the accounting records directly, without using the invoice and account statements. To
do this, use the rapid data entry form in a journal. Some accountants prefer this approach because
they are used to thinking in terms of accounting records rather than in terms of invoices and
payments.

.. i18n: You should really use the forms designed for invoices and bank statements rather than manual data
.. i18n: entry records, however. These are simpler and are managed within an error-controlling system.
..

You should really use the forms designed for invoices and bank statements rather than manual data
entry records, however. These are simpler and are managed within an error-controlling system.

.. i18n: Records-based Accounting System
.. i18n: -------------------------------
..

基于记录的会计系统
-------------------------------

.. i18n: All the accounting transactions in OpenERP are based on records, whether they are created by an
.. i18n: invoice or created directly.
..

All the accounting transactions in OpenERP are based on records, whether they are created by an
invoice or created directly.

.. i18n: So, customer reminders are generated quickly from the list of unreconciled entries in the trade
.. i18n: receivables account for that partner. In a single reminder, you will find the whole set of unpaid
.. i18n: invoices as well as unreconciled payments, such as advance payments.
..

So, customer reminders are generated quickly from the list of unreconciled entries in the trade
receivables account for that partner. In a single reminder, you will find the whole set of unpaid
invoices as well as unreconciled payments, such as advance payments.

.. i18n: Similarly, financial statements such as the general ledger, account balance, aged balance (or
.. i18n: chronological balance) and the various journals are all based on accounting entries. It does not
.. i18n: matter if you generated the entry from an invoice form or directly in the invoice journal. It is the
.. i18n: same for the tax declaration and other statutory financial statements.
..

Similarly, financial statements such as the general ledger, account balance, aged balance (or
chronological balance) and the various journals are all based on accounting entries. It does not
matter if you generated the entry from an invoice form or directly in the invoice journal. It is the
same for the tax declaration and other statutory financial statements.

.. i18n: When using integrated accounting, you should still go through the standard billing process because
.. i18n: some modules are directly dependent on invoice documents. For example, a sales order can be
.. i18n: configured to wait for payment of the invoice before triggering a delivery. In such a case,
.. i18n: OpenERP automatically generates a draft invoice to send to the client.
..

When using integrated accounting, you should still go through the standard billing process because
some modules are directly dependent on invoice documents. For example, a sales order can be
configured to wait for payment of the invoice before triggering a delivery. In such a case,
OpenERP automatically generates a draft invoice to send to the client.

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
