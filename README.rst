nmf-converter-core
==================

Core NMF converter logic

Setting Up the Development Environment
--------------------------------------

The development environment is based on a Centos 7 environment managed
by Vagrant.

Pre-Requisites
~~~~~~~~~~~~~~

-  `Vagrant`_
-  `ChefDK`_

Once Vagrant and the ChefDK are installed, you must install the
vagrant-berkshelf plugin for Vagrant which allows the use of Berkshelf
to manage cookbooks for provisioning the virtual machine, and the
vagrant-omnibus plugin which installs chef on the vm allowing it to be
provisioned.

.. code:: bash

    vagrant plugin install vagrant-berkshelf
    vagrant plugin install vagrant-omnibus

Create the Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The creation of the development environment is automated by Vagrant.
Simply run the following:

.. code:: bash

    vagrant up

from the root directory of this project.

Once the virtual machine is provisioned, login to the vm:

.. code:: bash

    vagrant ssh

Create and activate a virtualenv:

.. code:: bash

    mkvirtualenv nmf-converter-core

Install the dependencies:

.. code:: bash

    pip install -r /vagrant/requirements.txt

.. _Vagrant: http://www.vagrantup.com
.. _ChefDK: http://downloads.getchef.com/chef-dk/

