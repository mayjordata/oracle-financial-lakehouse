dmay@Mac ~ % bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
oci setup config
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16926  100 16926    0     0   215k      0 --:--:-- --:--:-- --:--:--  217k

    ******************************************************************************
    You have started the OCI CLI Installer in interactive mode. If you do not wish
    to run this in interactive mode, please include the --accept-all-defaults option.
    If you have the script locally and would like to know more about
    input options for this script, then you can run:
    ./install.sh -h
    If you would like to know more about input options for this script, refer to:
    https://github.com/oracle/oci-cli/blob/master/scripts/install/README.rst
    ******************************************************************************
Downloading Oracle Cloud Infrastructure CLI install script from https://raw.githubusercontent.com/oracle/oci-cli/v3.2.1/scripts/install/install.py to /var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.CdrJIu6CKr.
###################################################################################################################### 100.0%
python not found on system PATH
System version of Python must be a Python 3 version >= 3.6.0.
OCI CLI will only run on Python 3.6 or higher. Would you like to upgrade to Python 3? Please enter Y or N. Y
Installing Python 3...
ERROR: Could not install Python 3 based on operating system. Please install Python 3.6+ manually and re-run this script.
zsh: command not found: oci
dmay@Mac ~ % brew install python
zsh: command not found: brew
dmay@Mac ~ % !brew install python
brew install python install python
zsh: command not found: brew
dmay@Mac ~ % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
==> This script will install:
/opt/homebrew/bin/brew
/opt/homebrew/share/doc/homebrew
/opt/homebrew/share/man/man1/brew.1
/opt/homebrew/share/zsh/site-functions/_brew
/opt/homebrew/etc/bash_completion.d/brew
/opt/homebrew
/etc/paths.d/homebrew
==> The following new directories will be created:
/opt/homebrew/bin
/opt/homebrew/etc
/opt/homebrew/include
/opt/homebrew/lib
/opt/homebrew/sbin
/opt/homebrew/share
/opt/homebrew/var
/opt/homebrew/opt
/opt/homebrew/share/zsh
/opt/homebrew/share/zsh/site-functions
/opt/homebrew/var/homebrew
/opt/homebrew/var/homebrew/linked
/opt/homebrew/Cellar
/opt/homebrew/Caskroom
/opt/homebrew/Frameworks
==> The Xcode Command Line Tools will be installed.

Press RETURN/ENTER to continue or any other key to abort:
==> /usr/bin/sudo /usr/bin/install -d -o root -g wheel -m 0755 /opt/homebrew
==> /usr/bin/sudo /bin/mkdir -p /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /bin/chmod ug=rwx /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /bin/chmod go-w /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions
==> /usr/bin/sudo /usr/sbin/chown dmay /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /usr/bin/chgrp admin /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /usr/sbin/chown -R dmay:admin /opt/homebrew
==> /usr/bin/sudo /bin/mkdir -p /Users/dmay/Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Users/dmay/Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown -R dmay /Users/dmay/Library/Caches/Homebrew
==> Searching online for the Command Line Tools
==> /usr/bin/sudo /usr/bin/touch /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
==> Installing Command Line Tools for Xcode-16.4
==> /usr/bin/sudo /usr/sbin/softwareupdate -i Command\ Line\ Tools\ for\ Xcode-16.4
Software Update Tool

Finding available software

Downloaded Command Line Tools for Xcode
Installing Command Line Tools for Xcode
Done with Command Line Tools for Xcode
Done.
==> /usr/bin/sudo /usr/bin/xcode-select --switch /Library/Developer/CommandLineTools
==> /usr/bin/sudo /bin/rm -f /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
==> Downloading and installing Homebrew...
remote: Enumerating objects: 308844, done.
remote: Counting objects: 100% (342/342), done.
remote: Compressing objects: 100% (172/172), done.
remote: Total 308844 (delta 232), reused 219 (delta 170), pack-reused 308502 (from 4)
remote: Enumerating objects: 55, done.
remote: Counting objects: 100% (34/34), done.
remote: Total 55 (delta 34), reused 34 (delta 34), pack-reused 21 (from 1)
==> /usr/bin/sudo /bin/mkdir -p /etc/paths.d
==> /usr/bin/sudo tee /etc/paths.d/homebrew
/opt/homebrew/bin
==> /usr/bin/sudo /usr/sbin/chown root:wheel /etc/paths.d/homebrew
==> /usr/bin/sudo /bin/chmod a+r /etc/paths.d/homebrew
==> Updating Homebrew...
==> Downloading https://ghcr.io/v2/homebrew/portable-ruby/portable-ruby/blobs/sha256:20fa657858e44a4b39171d6e4111f8a9716eb62a78ebbd1491d94f90bb7b830a
###################################################################################################################### 100.0%
==> Pouring portable-ruby-3.4.5.arm64_big_sur.bottle.tar.gz
==> Installation successful!

==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
  https://docs.brew.sh/Analytics
No analytics data has been sent yet (nor will any be during this install run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
  https://github.com/Homebrew/brew#donations

==> Next steps:
- Run these commands in your terminal to add Homebrew to your PATH:
    echo >> /Users/dmay/.zprofile
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/dmay/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
- Run brew help to get started
- Further documentation:
    https://docs.brew.sh

dmay@Mac ~ % echo >> /Users/dmay/.zprofile
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/dmay/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
dmay@Mac ~ % brew --version
Homebrew 4.6.4
dmay@Mac ~ % brew install python
==> Fetching downloads for: python@3.13
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.13/manifests/3.13.7
###################################################################################################################### 100.0%
==> Fetching dependencies for python@3.13: mpdecimal, ca-certificates, openssl@3, readline, sqlite and xz
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/manifests/4.0.1
###################################################################################################################### 100.0%
==> Fetching mpdecimal
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/blobs/sha256:e21da583e42e86d5a2f0aedfaf7820e51b8af3065da599cff179d
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2025-08-12-1
###################################################################################################################### 100.0%
==> Fetching ca-certificates
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/blobs/sha256:80f4508a2a5711fcabeeaafdeebb88c9eec6b0e834e75f4
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/manifests/3.5.2
###################################################################################################################### 100.0%
==> Fetching openssl@3
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/blobs/sha256:4066d7983ad535f0e460fc340f343f9de933073882470d5ea968b
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.3.1
###################################################################################################################### 100.0%
==> Fetching readline
==> Downloading https://ghcr.io/v2/homebrew/core/readline/blobs/sha256:3afa0c228ce704810d09d40ce7d1265777df8b9034a7bfc18f0f4c
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.50.4
###################################################################################################################### 100.0%
==> Fetching sqlite
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/blobs/sha256:3e335d368e5121928ce36ac773e3288f4fb6c41101444f1b4af4d1db
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/xz/manifests/5.8.1
###################################################################################################################### 100.0%
==> Fetching xz
==> Downloading https://ghcr.io/v2/homebrew/core/xz/blobs/sha256:dcd7823f2624cbcd08f55c232097a79300c7d76ab5969004db1a4785c6c0
###################################################################################################################### 100.0%
==> Fetching python@3.13
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.13/blobs/sha256:821887b8f438c6a43828c9e893ee73e011012bb46fcac862974
###################################################################################################################### 100.0%
==> Installing dependencies for python@3.13: mpdecimal, ca-certificates, openssl@3, readline, sqlite and xz
==> Installing python@3.13 dependency: mpdecimal
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/manifests/4.0.1
Already downloaded: /Users/dmay/Library/Caches/Homebrew/downloads/dbbf60721dc54b6215f6c0988496331d4110a2a358da867a1129cd84b8166b31--mpdecimal-4.0.1.bottle_manifest.json
==> Pouring mpdecimal--4.0.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mpdecimal/4.0.1: 22 files, 645.6KB
==> Installing python@3.13 dependency: ca-certificates
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2025-08-12-1
Already downloaded: /Users/dmay/Library/Caches/Homebrew/downloads/0c788150cb28c41121baa5dcb0032bdec0ab95890252cb26a69f6fbe4ba640c2--ca-certificates-2025-08-12-1.bottle_manifest.json
==> Pouring ca-certificates--2025-08-12.all.bottle.1.tar.gz
==> Regenerating CA certificate bundle from keychain, this may take a while...
🍺  /opt/homebrew/Cellar/ca-certificates/2025-08-12: 4 files, 232.7KB
==> Installing python@3.13 dependency: openssl@3
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/manifests/3.5.2
Already downloaded: /Users/dmay/Library/Caches/Homebrew/downloads/e6659abe178bdf49b65451e77f6165a3e07274432f445342092e5ad2a927b23c--openssl@3-3.5.2.bottle_manifest.json
==> Pouring openssl@3--3.5.2.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/openssl@3/3.5.2: 7,563 files, 35.4MB
==> Installing python@3.13 dependency: readline
==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.3.1
Already downloaded: /Users/dmay/Library/Caches/Homebrew/downloads/52cb2bb3f0d9e66789968b865501c41ed80dc303eb488939476b309f1d350dc5--readline-8.3.1.bottle_manifest.json
==> Pouring readline--8.3.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/readline/8.3.1: 56 files, 2.6MB
==> Installing python@3.13 dependency: sqlite
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.50.4
Already downloaded: /Users/dmay/Library/Caches/Homebrew/downloads/f0760e6010149d3ea5bf9e64ddada251d25038daf612eb1c55fb18a9c6d6d53a--sqlite-3.50.4.bottle_manifest.json
==> Pouring sqlite--3.50.4.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/sqlite/3.50.4: 13 files, 4.9MB
==> Installing python@3.13 dependency: xz
==> Downloading https://ghcr.io/v2/homebrew/core/xz/manifests/5.8.1
Already downloaded: /Users/dmay/Library/Caches/Homebrew/downloads/86a115cc1d43ff8a480fd907f812e70a403e1675d8a7223f61bbb08cbd2adc27--xz-5.8.1.bottle_manifest.json
==> Pouring xz--5.8.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/xz/5.8.1: 96 files, 2.5MB
==> Installing python@3.13
==> Pouring python@3.13--3.13.7.arm64_sequoia.bottle.tar.gz
==> Caveats
Python is installed as
  /opt/homebrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, are installed into
  /opt/homebrew/opt/python@3.13/libexec/bin

`idle3.13` requires tkinter, which is available separately:
  brew install python-tk@3.13

See: https://docs.brew.sh/Homebrew-and-Python
==> Summary
🍺  /opt/homebrew/Cellar/python@3.13/3.13.7: 3,620 files, 66.6MB
==> Running `brew cleanup python@3.13`...
Disable this behaviour by setting `HOMEBREW_NO_INSTALL_CLEANUP=1`.
Hide these hints with `HOMEBREW_NO_ENV_HINTS=1` (see `man brew`).
==> No outdated dependents to upgrade!
==> Caveats
==> python@3.13
Python is installed as
  /opt/homebrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, are installed into
  /opt/homebrew/opt/python@3.13/libexec/bin

`idle3.13` requires tkinter, which is available separately:
  brew install python-tk@3.13

See: https://docs.brew.sh/Homebrew-and-Python
dmay@Mac ~ % python3 --version
Python 3.9.6
dmay@Mac ~ % bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16926  100 16926    0     0  75477      0 --:--:-- --:--:-- --:--:-- 75226

    ******************************************************************************
    You have started the OCI CLI Installer in interactive mode. If you do not wish
    to run this in interactive mode, please include the --accept-all-defaults option.
    If you have the script locally and would like to know more about
    input options for this script, then you can run:
    ./install.sh -h
    If you would like to know more about input options for this script, refer to:
    https://github.com/oracle/oci-cli/blob/master/scripts/install/README.rst
    ******************************************************************************
Downloading Oracle Cloud Infrastructure CLI install script from https://raw.githubusercontent.com/oracle/oci-cli/v3.2.1/scripts/install/install.py to /var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.Rnpcp6FSFe.
###################################################################################################################### 100.0%
cat: /etc/os-release: No such file or directory
Running install script.
python3 /var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.Rnpcp6FSFe 
/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.Rnpcp6FSFe:524: SyntaxWarning: invalid escape sequence '\E'
  command = "powershell -Command \"[Environment]::SetEnvironmentVariable(\\\"PATH\\\", \\\"{};\\\" + (Get-ItemProperty -Path 'Registry::HKEY_CURRENT_USER\Environment' -Name PATH).Path, \\\"User\\\")".format(exec_dir)  # noqa: W605
-- Verifying Python version.
-- Python version 3.13.7 okay.

===> In what directory would you like to place the install? (leave blank to use '/Users/dmay/lib/oracle-cli'): 
-- Creating directory '/Users/dmay/lib/oracle-cli'.
-- We will install at '/Users/dmay/lib/oracle-cli'.

===> In what directory would you like to place the 'oci' executable? (leave blank to use '/Users/dmay/bin'): 
-- Creating directory '/Users/dmay/bin'.
-- The executable will be in '/Users/dmay/bin'.

===> In what directory would you like to place the OCI scripts? (leave blank to use '/Users/dmay/bin/oci-cli-scripts'): 
-- Creating directory '/Users/dmay/bin/oci-cli-scripts'.
-- The scripts will be in '/Users/dmay/bin/oci-cli-scripts'.

===> Currently supported optional packages are: ['db (will install cx_Oracle)']
What optional CLI packages would you like to be installed (comma separated names; press enter if you don't need any optional packages)?: 
-- The optional packages installed will be ''.
-- Trying to use python3 venv.
-- Executing: ['/opt/homebrew/opt/python@3.13/bin/python3.13', '-m', 'venv', '/Users/dmay/lib/oracle-cli']
-- Executing: ['/Users/dmay/lib/oracle-cli/bin/pip', 'install', '--upgrade', 'pip']
Requirement already satisfied: pip in ./lib/oracle-cli/lib/python3.13/site-packages (25.2)
-- Executing: ['/Users/dmay/lib/oracle-cli/bin/pip', 'install', '--cache-dir', '/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/tmpnwwsn7r4', 'wheel', '--upgrade']
Collecting wheel
  Downloading wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Downloading wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel
Successfully installed wheel-0.45.1
-- Executing: ['/Users/dmay/lib/oracle-cli/bin/pip', 'install', '--cache-dir', '/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/tmpnwwsn7r4', 'oci_cli', '--upgrade']
Collecting oci_cli
  Downloading oci_cli-3.64.1-py3-none-any.whl.metadata (7.1 kB)
Collecting oci==2.158.2 (from oci_cli)
  Downloading oci-2.158.2-py3-none-any.whl.metadata (5.8 kB)
Collecting arrow>=1.0.0 (from oci_cli)
  Downloading arrow-1.3.0-py3-none-any.whl.metadata (7.5 kB)
Collecting certifi>=2025.1.31 (from oci_cli)
  Downloading certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
Collecting click==8.0.4 (from oci_cli)
  Downloading click-8.0.4-py3-none-any.whl.metadata (3.2 kB)
Collecting cryptography<46.0.0,>=3.2.1 (from oci_cli)
  Downloading cryptography-45.0.6-cp311-abi3-macosx_10_9_universal2.whl.metadata (5.7 kB)
Collecting jmespath==0.10.0 (from oci_cli)
  Downloading jmespath-0.10.0-py2.py3-none-any.whl.metadata (8.0 kB)
Collecting python-dateutil<3.0.0,>=2.5.3 (from oci_cli)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2016.10 (from oci_cli)
  Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting six>=1.15.0 (from oci_cli)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting terminaltables==3.1.10 (from oci_cli)
  Downloading terminaltables-3.1.10-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting pyOpenSSL<25.0.0,>=17.5.0 (from oci_cli)
  Downloading pyOpenSSL-24.3.0-py3-none-any.whl.metadata (15 kB)
Collecting PyYAML<=6.0.2,>=5.4 (from oci_cli)
  Downloading PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.1 kB)
Collecting prompt-toolkit<=3.0.43,>=3.0.38 (from oci_cli)
  Downloading prompt_toolkit-3.0.43-py3-none-any.whl.metadata (6.5 kB)
Collecting circuitbreaker<3.0.0,>=1.3.1 (from oci==2.158.2->oci_cli)
  Downloading circuitbreaker-2.1.3-py3-none-any.whl.metadata (8.0 kB)
Collecting cffi>=1.14 (from cryptography<46.0.0,>=3.2.1->oci_cli)
  Downloading cffi-1.17.1-cp313-cp313-macosx_11_0_arm64.whl.metadata (1.5 kB)
Collecting wcwidth (from prompt-toolkit<=3.0.43,>=3.0.38->oci_cli)
  Downloading wcwidth-0.2.13-py2.py3-none-any.whl.metadata (14 kB)
Collecting cryptography<46.0.0,>=3.2.1 (from oci_cli)
  Downloading cryptography-44.0.3-cp39-abi3-macosx_10_9_universal2.whl.metadata (5.7 kB)
Collecting types-python-dateutil>=2.8.10 (from arrow>=1.0.0->oci_cli)
  Downloading types_python_dateutil-2.9.0.20250809-py3-none-any.whl.metadata (1.8 kB)
Collecting pycparser (from cffi>=1.14->cryptography<46.0.0,>=3.2.1->oci_cli)
  Downloading pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Downloading oci_cli-3.64.1-py3-none-any.whl (24.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.7/24.7 MB 20.2 MB/s  0:00:01
Downloading click-8.0.4-py3-none-any.whl (97 kB)
Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)
Downloading oci-2.158.2-py3-none-any.whl (32.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.2/32.2 MB 14.8 MB/s  0:00:02
Downloading terminaltables-3.1.10-py2.py3-none-any.whl (15 kB)
Downloading circuitbreaker-2.1.3-py3-none-any.whl (7.7 kB)
Downloading prompt_toolkit-3.0.43-py3-none-any.whl (386 kB)
Downloading pyOpenSSL-24.3.0-py3-none-any.whl (56 kB)
Downloading cryptography-44.0.3-cp39-abi3-macosx_10_9_universal2.whl (6.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.7/6.7 MB 30.7 MB/s  0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl (171 kB)
Downloading arrow-1.3.0-py3-none-any.whl (66 kB)
Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
Downloading cffi-1.17.1-cp313-cp313-macosx_11_0_arm64.whl (178 kB)
Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading types_python_dateutil-2.9.0.20250809-py3-none-any.whl (17 kB)
Downloading pycparser-2.22-py3-none-any.whl (117 kB)
Downloading wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Installing collected packages: wcwidth, pytz, circuitbreaker, types-python-dateutil, terminaltables, six, PyYAML, pycparser, prompt-toolkit, jmespath, click, certifi, python-dateutil, cffi, cryptography, arrow, pyOpenSSL, oci, oci_cli
Successfully installed PyYAML-6.0.2 arrow-1.3.0 certifi-2025.8.3 cffi-1.17.1 circuitbreaker-2.1.3 click-8.0.4 cryptography-44.0.3 jmespath-0.10.0 oci-2.158.2 oci_cli-3.64.1 prompt-toolkit-3.0.43 pyOpenSSL-24.3.0 pycparser-2.22 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 terminaltables-3.1.10 types-python-dateutil-2.9.0.20250809 wcwidth-0.2.13
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from distutils.sysconfig import get_python_lib; print(get_python_lib())
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'distutils'
Traceback (most recent call last):
  File "/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.Rnpcp6FSFe", line 722, in <module>
    main()
    ~~~~^^
  File "/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.Rnpcp6FSFe", line 705, in main
    venv_site_packages_directory = subprocess.check_output([venv_python_executable, '-c', 'from distutils.sysconfig import get_python_lib; print(get_python_lib())']).strip()
                                   ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/subprocess.py", line 472, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
           ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
               **kwargs).stdout
               ^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/subprocess.py", line 577, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['/Users/dmay/lib/oracle-cli/bin/python', '-c', 'from distutils.sysconfig import get_python_lib; print(get_python_lib())']' returned non-zero exit status 1.
dmay@Mac ~ % /Users/dmay/lib/oracle-cli/bin/pip install setuptools
Collecting setuptools
  Downloading setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
Downloading setuptools-80.9.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 1.6 MB/s  0:00:00
Installing collected packages: setuptools
Successfully installed setuptools-80.9.0
dmay@Mac ~ % bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16926  100 16926    0     0   235k      0 --:--:-- --:--:-- --:--:--  236k

    ******************************************************************************
    You have started the OCI CLI Installer in interactive mode. If you do not wish
    to run this in interactive mode, please include the --accept-all-defaults option.
    If you have the script locally and would like to know more about
    input options for this script, then you can run:
    ./install.sh -h
    If you would like to know more about input options for this script, refer to:
    https://github.com/oracle/oci-cli/blob/master/scripts/install/README.rst
    ******************************************************************************
Downloading Oracle Cloud Infrastructure CLI install script from https://raw.githubusercontent.com/oracle/oci-cli/v3.2.1/scripts/install/install.py to /var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.4W6JMKdSQK.
###################################################################################################################### 100.0%
cat: /etc/os-release: No such file or directory
Running install script.
python3 /var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.4W6JMKdSQK 
/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.4W6JMKdSQK:524: SyntaxWarning: invalid escape sequence '\E'
  command = "powershell -Command \"[Environment]::SetEnvironmentVariable(\\\"PATH\\\", \\\"{};\\\" + (Get-ItemProperty -Path 'Registry::HKEY_CURRENT_USER\Environment' -Name PATH).Path, \\\"User\\\")".format(exec_dir)  # noqa: W605
-- Verifying Python version.
-- Python version 3.13.7 okay.

===> In what directory would you like to place the install? (leave blank to use '/Users/dmay/lib/oracle-cli'): 
-- Install directory '/Users/dmay/lib/oracle-cli' is not empty and may contain a previous installation.

===> Remove this directory? (y/N): y
-- Deleted '/Users/dmay/lib/oracle-cli'.
-- Creating directory '/Users/dmay/lib/oracle-cli'.
-- We will install at '/Users/dmay/lib/oracle-cli'.

===> In what directory would you like to place the 'oci' executable? (leave blank to use '/Users/dmay/bin'): 
-- The executable will be in '/Users/dmay/bin'.

===> In what directory would you like to place the OCI scripts? (leave blank to use '/Users/dmay/bin/oci-cli-scripts'): 
-- The scripts will be in '/Users/dmay/bin/oci-cli-scripts'.

===> Currently supported optional packages are: ['db (will install cx_Oracle)']
What optional CLI packages would you like to be installed (comma separated names; press enter if you don't need any optional packages)?: 
-- The optional packages installed will be ''.
-- Trying to use python3 venv.
-- Executing: ['/opt/homebrew/opt/python@3.13/bin/python3.13', '-m', 'venv', '/Users/dmay/lib/oracle-cli']
-- Executing: ['/Users/dmay/lib/oracle-cli/bin/pip', 'install', '--upgrade', 'pip']
Requirement already satisfied: pip in ./lib/oracle-cli/lib/python3.13/site-packages (25.2)
-- Executing: ['/Users/dmay/lib/oracle-cli/bin/pip', 'install', '--cache-dir', '/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/tmpwjg68muy', 'wheel', '--upgrade']
Collecting wheel
  Downloading wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Downloading wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel
Successfully installed wheel-0.45.1
-- Executing: ['/Users/dmay/lib/oracle-cli/bin/pip', 'install', '--cache-dir', '/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/tmpwjg68muy', 'oci_cli', '--upgrade']
Collecting oci_cli
  Downloading oci_cli-3.64.1-py3-none-any.whl.metadata (7.1 kB)
Collecting oci==2.158.2 (from oci_cli)
  Downloading oci-2.158.2-py3-none-any.whl.metadata (5.8 kB)
Collecting arrow>=1.0.0 (from oci_cli)
  Downloading arrow-1.3.0-py3-none-any.whl.metadata (7.5 kB)
Collecting certifi>=2025.1.31 (from oci_cli)
  Downloading certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
Collecting click==8.0.4 (from oci_cli)
  Downloading click-8.0.4-py3-none-any.whl.metadata (3.2 kB)
Collecting cryptography<46.0.0,>=3.2.1 (from oci_cli)
  Downloading cryptography-45.0.6-cp311-abi3-macosx_10_9_universal2.whl.metadata (5.7 kB)
Collecting jmespath==0.10.0 (from oci_cli)
  Downloading jmespath-0.10.0-py2.py3-none-any.whl.metadata (8.0 kB)
Collecting python-dateutil<3.0.0,>=2.5.3 (from oci_cli)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2016.10 (from oci_cli)
  Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting six>=1.15.0 (from oci_cli)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting terminaltables==3.1.10 (from oci_cli)
  Downloading terminaltables-3.1.10-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting pyOpenSSL<25.0.0,>=17.5.0 (from oci_cli)
  Downloading pyOpenSSL-24.3.0-py3-none-any.whl.metadata (15 kB)
Collecting PyYAML<=6.0.2,>=5.4 (from oci_cli)
  Downloading PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.1 kB)
Collecting prompt-toolkit<=3.0.43,>=3.0.38 (from oci_cli)
  Downloading prompt_toolkit-3.0.43-py3-none-any.whl.metadata (6.5 kB)
Collecting circuitbreaker<3.0.0,>=1.3.1 (from oci==2.158.2->oci_cli)
  Downloading circuitbreaker-2.1.3-py3-none-any.whl.metadata (8.0 kB)
Collecting cffi>=1.14 (from cryptography<46.0.0,>=3.2.1->oci_cli)
  Downloading cffi-1.17.1-cp313-cp313-macosx_11_0_arm64.whl.metadata (1.5 kB)
Collecting wcwidth (from prompt-toolkit<=3.0.43,>=3.0.38->oci_cli)
  Downloading wcwidth-0.2.13-py2.py3-none-any.whl.metadata (14 kB)
Collecting cryptography<46.0.0,>=3.2.1 (from oci_cli)
  Downloading cryptography-44.0.3-cp39-abi3-macosx_10_9_universal2.whl.metadata (5.7 kB)
Collecting types-python-dateutil>=2.8.10 (from arrow>=1.0.0->oci_cli)
  Downloading types_python_dateutil-2.9.0.20250809-py3-none-any.whl.metadata (1.8 kB)
Collecting pycparser (from cffi>=1.14->cryptography<46.0.0,>=3.2.1->oci_cli)
  Downloading pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Downloading oci_cli-3.64.1-py3-none-any.whl (24.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.7/24.7 MB 9.2 MB/s  0:00:02
Downloading click-8.0.4-py3-none-any.whl (97 kB)
Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)
Downloading oci-2.158.2-py3-none-any.whl (32.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.2/32.2 MB 9.8 MB/s  0:00:03
Downloading terminaltables-3.1.10-py2.py3-none-any.whl (15 kB)
Downloading circuitbreaker-2.1.3-py3-none-any.whl (7.7 kB)
Downloading prompt_toolkit-3.0.43-py3-none-any.whl (386 kB)
Downloading pyOpenSSL-24.3.0-py3-none-any.whl (56 kB)
Downloading cryptography-44.0.3-cp39-abi3-macosx_10_9_universal2.whl (6.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.7/6.7 MB 7.2 MB/s  0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl (171 kB)
Downloading arrow-1.3.0-py3-none-any.whl (66 kB)
Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
Downloading cffi-1.17.1-cp313-cp313-macosx_11_0_arm64.whl (178 kB)
Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading types_python_dateutil-2.9.0.20250809-py3-none-any.whl (17 kB)
Downloading pycparser-2.22-py3-none-any.whl (117 kB)
Downloading wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Installing collected packages: wcwidth, pytz, circuitbreaker, types-python-dateutil, terminaltables, six, PyYAML, pycparser, prompt-toolkit, jmespath, click, certifi, python-dateutil, cffi, cryptography, arrow, pyOpenSSL, oci, oci_cli
Successfully installed PyYAML-6.0.2 arrow-1.3.0 certifi-2025.8.3 cffi-1.17.1 circuitbreaker-2.1.3 click-8.0.4 cryptography-44.0.3 jmespath-0.10.0 oci-2.158.2 oci_cli-3.64.1 prompt-toolkit-3.0.43 pyOpenSSL-24.3.0 pycparser-2.22 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 terminaltables-3.1.10 types-python-dateutil-2.9.0.20250809 wcwidth-0.2.13
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from distutils.sysconfig import get_python_lib; print(get_python_lib())
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'distutils'
Traceback (most recent call last):
  File "/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.4W6JMKdSQK", line 722, in <module>
    main()
    ~~~~^^
  File "/var/folders/vs/rkkmpj8j3gbgmkwxlsp1tyrc0000gn/T/oci_cli_install_tmp_XXXX.4W6JMKdSQK", line 705, in main
    venv_site_packages_directory = subprocess.check_output([venv_python_executable, '-c', 'from distutils.sysconfig import get_python_lib; print(get_python_lib())']).strip()
                                   ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/subprocess.py", line 472, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
           ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
               **kwargs).stdout
               ^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/subprocess.py", line 577, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['/Users/dmay/lib/oracle-cli/bin/python', '-c', 'from distutils.sysconfig import get_python_lib; print(get_python_lib())']' returned non-zero exit status 1.
dmay@Mac ~ % brew install pipx
pipx ensurepath
==> Downloading https://formulae.brew.sh/api/formula.jws.json
==> Downloading https://formulae.brew.sh/api/cask.jws.json
==> Fetching downloads for: pipx
==> Downloading https://ghcr.io/v2/homebrew/core/pipx/manifests/1.7.1_1
###################################################################################################################### 100.0%
==> Fetching pipx
==> Downloading https://ghcr.io/v2/homebrew/core/pipx/blobs/sha256:ca676ccaaf770e835c5a9ae2d3a648ef4539893c02aa8a70875bfd3e33
###################################################################################################################### 100.0%
==> Pouring pipx--1.7.1_1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pipx/1.7.1_1: 155 files, 1019.3KB
==> Running `brew cleanup pipx`...
Disable this behaviour by setting `HOMEBREW_NO_INSTALL_CLEANUP=1`.
Hide these hints with `HOMEBREW_NO_ENV_HINTS=1` (see `man brew`).
==> No outdated dependents to upgrade!
==> Caveats
zsh completions have been installed to:
  /opt/homebrew/share/zsh/site-functions
Success! Added /Users/dmay/.local/bin to the PATH environment variable.

Consider adding shell completions for pipx. Run 'pipx completions' for instructions.

You will need to open a new terminal or re-login for the PATH changes to take effect. Alternatively, you can source your
shell's config file with e.g. 'source ~/.bashrc'.

Otherwise pipx is ready to go! ✨ 🌟 ✨
dmay@Mac ~ % source ~/.zshrc
dmay@Mac ~ % pipx install oci-cli
  installed package oci-cli 3.64.1, installed using Python 3.13.7
  These apps are now globally available
    - create_backup_from_onprem
    - oci
done! ✨ 🌟 ✨
dmay@Mac ~ % oci --version
3.64.1
dmay@Mac ~ % oci setup config
    This command provides a walkthrough of creating a valid CLI config file.

    The following links explain where to find the information required by this
    script:

    User API Signing Key, OCID and Tenancy OCID:

        https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#Other

    Region:

        https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm

    General config documentation:

        https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm


Enter a location for your config [/Users/dmay/.oci/config]: 
Enter a user OCID: ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta
Enter a tenancy OCID: ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta
Enter a region by index or name(e.g.
1: af-johannesburg-1, 2: ap-batam-1, 3: ap-chiyoda-1, 4: ap-chuncheon-1, 5: ap-chuncheon-2,
6: ap-dcc-canberra-1, 7: ap-dcc-gazipur-1, 8: ap-delhi-1, 9: ap-hyderabad-1, 10: ap-ibaraki-1,
11: ap-melbourne-1, 12: ap-mumbai-1, 13: ap-osaka-1, 14: ap-seoul-1, 15: ap-seoul-2,
16: ap-singapore-1, 17: ap-singapore-2, 18: ap-suwon-1, 19: ap-sydney-1, 20: ap-tokyo-1,
21: ca-montreal-1, 22: ca-toronto-1, 23: eu-amsterdam-1, 24: eu-budapest-1, 25: eu-crissier-1,
26: eu-dcc-dublin-1, 27: eu-dcc-dublin-2, 28: eu-dcc-milan-1, 29: eu-dcc-milan-2, 30: eu-dcc-rating-1,
31: eu-dcc-rating-2, 32: eu-dcc-zurich-1, 33: eu-frankfurt-1, 34: eu-frankfurt-2, 35: eu-jovanovac-1,
36: eu-madrid-1, 37: eu-madrid-2, 38: eu-marseille-1, 39: eu-milan-1, 40: eu-paris-1,
41: eu-stockholm-1, 42: eu-zurich-1, 43: il-jerusalem-1, 44: me-abudhabi-1, 45: me-abudhabi-2,
46: me-abudhabi-3, 47: me-abudhabi-4, 48: me-alain-1, 49: me-dcc-doha-1, 50: me-dcc-muscat-1,
51: me-dubai-1, 52: me-jeddah-1, 53: me-riyadh-1, 54: mx-monterrey-1, 55: mx-queretaro-1,
56: sa-bogota-1, 57: sa-santiago-1, 58: sa-saopaulo-1, 59: sa-valparaiso-1, 60: sa-vinhedo-1,
61: uk-cardiff-1, 62: uk-gov-cardiff-1, 63: uk-gov-london-1, 64: uk-london-1, 65: us-ashburn-1,
66: us-ashburn-2, 67: us-chicago-1, 68: us-gov-ashburn-1, 69: us-gov-chicago-1, 70: us-gov-phoenix-1,
71: us-langley-1, 72: us-luke-1, 73: us-newark-1, 74: us-phoenix-1, 75: us-saltlake-2,
76: us-sanjose-1, 77: us-somerset-1, 78: us-thames-1): us-phoenix-1
Do you want to generate a new API Signing RSA key pair? (If you decline you will be asked to supply the path to an existing key.) [Y/n]: Y
Enter a directory for your keys to be created [/Users/dmay/.oci]: 
Enter a name for your key [oci_api_key]: dmay_key
Public key written to: /Users/dmay/.oci/dmay_key_public.pem
Enter a passphrase for your private key ("N/A" for no passphrase): 
Repeat for confirmation: 
Private key written to: /Users/dmay/.oci/dmay_key.pem
Fingerprint: 2a:da:f5:4a:92:5b:4d:18:5b:ac:7e:e5:6c:8c:0c:66
Do you want to write your passphrase to the config file? (If not, you will need to enter it when prompted each time you run an oci command) [y/N]: y
Config written to /Users/dmay/.oci/config


    If you haven't already uploaded your API Signing public key through the
    console, follow the instructions on the page linked below in the section
    'How to upload the public key':

        https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#How2


dmay@Mac ~ % nano ~/.oci/config
dmay@Mac ~ % cat ~/.oci/oci_api_key_public.pem         
cat: /Users/dmay/.oci/oci_api_key_public.pem: No such file or directory
dmay@Mac ~ % ~/.oci/oci_api_key_public.pem
zsh: no such file or directory: /Users/dmay/.oci/oci_api_key_public.pem
dmay@Mac ~ % ~/.oci/dmay_key.pem          
zsh: permission denied: /Users/dmay/.oci/dmay_key.pem
dmay@Mac ~ % cat ~/.oci/dmay_key.pem
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFNTBfBgkqhkiG9w0BBQ0wUjAxBgkqhkiG9w0BBQwwJAQQzof7+1IZQB5rU51R
d/iWvwICCAAwDAYIKoZIhvcNAgkFADAdBglghkgBZQMEASoEENwnzU+/GACW74u/
vDT27h0EggTQ3LZuXxJcYSJujMcUrRzFoVLGiU2V4w2EXaB2JTuyDaypCR1qGa70
zO1s8tIMBwTqrkVXqhEtett21/HkN+YrbWXW+658CRMbBZH0pX/9vs3Y63zzu/Vv
F+fT9E7ZvEJQG6z4hX29UAJDhzrJn3cdWIRSM9HjbDME8h4bhH40y1pTuBWNKMNZ
MCpCc/A0hBaCyOXgS57zA0SxqfT0QzXFa9OPQBflLYSoaNe1zOMGnFb4REBNHT1t
dmFXi1SnDtShG9hmCz/2ZufFkXfDamE2lY3Lmihb9AbbFQpUuQSRD6xX3RKap8dz
xrLSf1pA9EfBTS5dsIbrCF4/O2Ay01o/TOICdvmHVJzo/mXFLQOOPOtwhTUoch/U
w2dE0qVUSj19EAXXJeYgLmLv9b1TIU3ojcsbI/xkH0SEBjIeBajaU3pD91/lSXJJ
qa2ddGNyrJ3AGX+xBktTTiGJ+hEZQGAnwz2CMiVxHCOEnuKPcDRxe9qdEzR8T/wr
rVyzGqyHuAj3CEz3pyTljxaxzIQZEjxy8yn3MbJPKcg+cJ+1BS7Zrgx+G8B6h8tT
oieaLiXBP31RLx5Ep8yPmq3QfD7BtzsD/BLiCl4IuKJTFOZ4h6zFTycS+qu4cG2z
kG31dbwGJwqVlkhmaVkuDCcr6Vod/eCABLKJBgT7N97WYvYJ9lEORLtgNJwn9Qb2
B89kzAl/EqpfSq8jza6KEQwf3UQds+jyQiRoTTiUBCTPxw4gjD4VfZLODnlO9NTt
yRblPrWNv1oUej+YVrL+6LmbbselhTAGlEf5NEZPVnYjlFX028Oh1O4b7zN/wKyv
gf1ISN8iXal2wBaKm/6lZQx7EAYumHkXMhgG2Z7Hg0igRWWg2ifSLxLTi1R/x6nB
YnhESnq5b+v9lREu6YDZmDLVJY3H1FfX7iMl4FzFWvTHqYAimptU8cuFYPlO4wPY
YpPYCjAApKtYvp74rBGt+UUzNbtpB8K4spHcDBrZCRqLjot950RAiNlv0pnwbPmx
xERoOUsxZ/xXjMxggV0gikiWip5NgmxneneAtgemO9ADDnWEXrPo6+DgB2arWOgH
Rc9oFMmtKzbTeJesquV+hzJkmrijdcyO9I0rTICMLsPoIC+ean1kDILzBCrEyBei
HhSmkjgPUWHzGFmQovzCEJahKzHQWV0SuMBAkZHAeTN1TF1t0Ljv6VW5Xv2EELqA
qG+56WYb++sDaOFD7ma5pbcT1P9Dbev0SP0KL0om+JuSH0POEleyw0DToHD9CGGa
xaGk+rQIDnhClx4iw7wmmqGHVAx+JWp/Tp9uq09xX9ByaEpX8evH7hWx2pLOAXox
zFz94YbS3wAfnieYvCkdgOO9RzL+rSUJXAAm8AemJyq0YxjQ/G7buq09U8F0Bzt6
EShIkVizsbw7EIOMIEb2VADYBXmUHEUSHEX+e4vlJ/zMZtZ9FsIQ7iLKbsS4V+By
fQC+JsH5T9YyUORfF28FMIie+oHIPN/AY8tnL/Q+0TZQCqt2arZt318TrGUNnbk8
TtMjhxOo9xuETrfwTtdN4k7ntNEyr//n3Eg+JwB/RilMnHUNmN7omUCJFzeZUQFU
dImBHugnvgAbxz4J4qVtOORrZvz3U7AGpz2l6cMm4793EglbESpa0Bg=
-----END ENCRYPTED PRIVATE KEY-----
OCI_API_KEY%                                                                                                                 dmay@Mac ~ % cat ~/.oci/dmay_key_public.pem
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4+FHTDNi8CWRU1oEN1OS
qKExy1Nx1hITMu9lcH59Txah1XNyankR+Usk0blo/7SbBeHtdUS5d/dAw9fziSD4
C98HTWhCpqqoCD8n8qmDsS1jL4Gn0yB29D/SApnBgKXpG+BDjDnUM9uhuGtQpYY/
yjU661ly5WyVAnw7YJqAXxSe3/trsNPajUqguRjUsTPzTN5FRLF5/o7pJltjKF/t
HV+lJdoK5porHKVL4W3eogZomkzPiqxd5kG/kF5Ed4U2vfRCoJGmYtGwVU+dU0i/
E42LZ4xywQCrdLGak7pSO2ar8W+nNEPy5Lxdq6igamAyetBkdIyuvi5SQvhaw7T8
PQIDAQAB
-----END PUBLIC KEY-----
dmay@Mac ~ % nano ~/.oci/config               
dmay@Mac ~ % oci iam compartment list --all
{
  "data": [
    {
      "compartment-id": "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta",
      "defined-tags": {
        "Oracle-Tags": {
          "CreatedBy": "default/d.may1906@gmail.com",
          "CreatedOn": "August 21, 2025"
        }
      },
      "description": "Contains personal project aimed to capitalize on free trial credits and gain experience across several domains with finance being the theme. ",
      "freeform-tags": {
        "Domain": "Finance"
      },
      "id": "ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq",
      "inactive-status": null,
      "is-accessible": null,
      "lifecycle-state": "ACTIVE",
      "name": "finance-project",
      "time-created": "2025-08-21T21:49:35.511000+00:00"
    }
  ]
}
dmay@Mac ~ % ssh-keygen -t rsa -b 4096 -f ~/.ssh/oci_vm_key
Generating public/private rsa key pair.
Enter passphrase for "/Users/dmay/.ssh/oci_vm_key" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/dmay/.ssh/oci_vm_key
Your public key has been saved in /Users/dmay/.ssh/oci_vm_key.pub
The key fingerprint is:
SHA256:gb07DACOWadmxAS17+9FNmTYzJXrZHvi3r/Mrt64u4M dmay@Mac.lan
The key's randomart image is:
+---[RSA 4096]----+
|.=* .     ..     |
| *.=   B ..      |
|o * . o O  .     |
| o . . o o+      |
|    . . S+ .     |
|   .   = o+ .    |
|    .   =. +     |
|     . . .E..=   |
|     .o  ...OOB. |
+----[SHA256]-----+
dmay@Mac ~ % oci --version
3.64.1
dmay@Mac ~ % oci iam compartment list --all
{
  "data": [
    {
      "compartment-id": "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta",
      "defined-tags": {
        "Oracle-Tags": {
          "CreatedBy": "default/d.may1906@gmail.com",
          "CreatedOn": "August 21, 2025"
        }
      },
      "description": "Contains personal project aimed to capitalize on free trial credits and gain experience across several domains with finance being the theme. ",
      "freeform-tags": {
        "Domain": "Finance"
      },
      "id": "ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq",
      "inactive-status": null,
      "is-accessible": null,
      "lifecycle-state": "ACTIVE",
      "name": "finance-project",
      "time-created": "2025-08-21T21:49:35.511000+00:00"
    }
  ]
}
dmay@Mac ~ % oci iam compartment list --name "finance-project" --compartment-id YOUR_TENANCY_OCID
ServiceError:
{
    "client_version": "Oracle-PythonSDK/2.158.2, Oracle-PythonCLI/3.64.1",
    "code": "NotAuthorizedOrNotFound",
    "logging_tips": "Please run the OCI CLI command using --debug flag to find more debug information.",
    "message": "Authorization failed or requested resource not found",
    "opc-request-id": "45CEC5EA569542BB9BB918652A42C717/67CF23B909BD1C3F85983F90C35E8526/A41DDB9D7221E55F568B0FC4E9A99B12",
    "operation_name": "list_compartments",
    "request_endpoint": "GET https://identity.us-phoenix-1.oci.oraclecloud.com/20160918/compartments",
    "status": 404,
    "target_service": "identity",
    "timestamp": "2025-08-22T19:41:26.001994+00:00",
    "troubleshooting_tips": "See [https://docs.oracle.com/iaas/Content/API/References/apierrors.htm] for more information about resolving this error. If you are unable to resolve this issue, run this CLI command with --debug option and contact Oracle support and provide them the full error message."
}
dmay@Mac ~ % oci iam compartment list --name "finance-project" --compartment-id "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta"
{
  "data": [
    {
      "compartment-id": "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta",
      "defined-tags": {
        "Oracle-Tags": {
          "CreatedBy": "default/d.may1906@gmail.com",
          "CreatedOn": "August 21, 2025"
        }
      },
      "description": "Contains personal project aimed to capitalize on free trial credits and gain experience across several domains with finance being the theme. ",
      "freeform-tags": {
        "Domain": "Finance"
      },
      "id": "ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq",
      "inactive-status": null,
      "is-accessible": null,
      "lifecycle-state": "ACTIVE",
      "name": "finance-project",
      "time-created": "2025-08-21T21:49:35.511000+00:00"
    }
  ]
}
dmay@Mac ~ % oci compute image list \
  --compartment-id "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta" \
  --operating-system "Oracle Linux" \
  --operating-system-version "9" \
  --query 'data[*].{Name:"display-name", OCID:id, Date:"time-created"}' \
  --output table
+----------------------------------+----------------------------------------+----------------------------------------------------------------------------------+
| Date                             | Name                                   | OCID                                                                             |
+----------------------------------+----------------------------------------+----------------------------------------------------------------------------------+
| 2025-07-25T07:17:15.356000+00:00 | Oracle-Linux-9.6-aarch64-2025.07.21-0  | ocid1.image.oc1.phx.aaaaaaaa72cedjfaq5smtmwxpjwrhmcfpvcpqo2ppomzxlpfb72svn7vnapq |
| 2025-06-24T07:16:02.203000+00:00 | Oracle-Linux-9.6-aarch64-2025.06.17-0  | ocid1.image.oc1.phx.aaaaaaaaaawp4x63fjccfs2cwdq63ofvftcktl56xp2afophsp4xvemr52ba |
| 2025-07-25T07:16:55.106000+00:00 | Oracle-Linux-9.6-Gen2-GPU-2025.07.21-0 | ocid1.image.oc1.phx.aaaaaaaa2h5rdqzjfvzoc2kvryzsebcty4gnzifunjrvypkfyts5x5fzxx3a |
| 2025-06-24T07:16:08.978000+00:00 | Oracle-Linux-9.6-Gen2-GPU-2025.06.17-0 | ocid1.image.oc1.phx.aaaaaaaaxtx5e3vilq727xx2f32ad72l46gt2tvanlqfoi7mkrbae4zafeea |
| 2025-07-25T07:16:44.611000+00:00 | Oracle-Linux-9.6-2025.07.21-0          | ocid1.image.oc1.phx.aaaaaaaaih2igwfekpammueml4gfv6y27az7peb6zy5nwyhptgwanssoqaja |
| 2025-06-24T07:16:20.843000+00:00 | Oracle-Linux-9.6-2025.06.17-0          | ocid1.image.oc1.phx.aaaaaaaanoh2ncjgaee7kxlkkeify2hux7nqcrfn4fjacruqupzlm6572zwa |
| 2025-05-21T12:59:52.305000+00:00 | Oracle-Linux-9.5-aarch64-2025.05.19-0  | ocid1.image.oc1.phx.aaaaaaaaeqdefxlbovrp5uafn6gp5kxmesjdmkk7e7lhqcfgfy67zckwynlq |
| 2025-05-21T12:59:23.952000+00:00 | Oracle-Linux-9.5-Gen2-GPU-2025.05.19-0 | ocid1.image.oc1.phx.aaaaaaaasf3pcrpo2imqhubylckjnh7zsveth7zbrfmvnmwmnk3cyrtjookq |
| 2025-05-21T12:59:16.693000+00:00 | Oracle-Linux-9.5-2025.05.19-0          | ocid1.image.oc1.phx.aaaaaaaa3eqzjvwrxuoswhcw5gfrmi2wj7mbxknrtdbynfmh3p5dojeqps3a |
+----------------------------------+----------------------------------------+----------------------------------------------------------------------------------+
dmay@Mac ~ % oci network vcn list --compartment-id "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta"
{
  "data": [
    {
      "byoipv6-cidr-blocks": null,
      "cidr-block": "10.0.0.0/16",
      "cidr-blocks": [
        "10.0.0.0/16"
      ],
      "compartment-id": "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta",
      "default-dhcp-options-id": "ocid1.dhcpoptions.oc1.phx.aaaaaaaaod5a4jal6ivjvtlmtmgbhu53y5f3rg6l2fusimelo6uw5qkr27hq",
      "default-route-table-id": "ocid1.routetable.oc1.phx.aaaaaaaafvw7fpl3qkac76j6izgddbyj3amgr2hrwgq2jbwr7f6ppybnkuqa",
      "default-security-list-id": "ocid1.securitylist.oc1.phx.aaaaaaaa74x33copg6aporfrw4hvctxtlfkdrw7rielb3466yasckkh44y5q",
      "defined-tags": {
        "Oracle-Tags": {
          "CreatedBy": "default/d.may1906@gmail.com",
          "CreatedOn": "2025-08-14T01:30:23.394Z"
        }
      },
      "display-name": "vcn-20250813-1828",
      "dns-label": "vcn08131830",
      "freeform-tags": {},
      "id": "ocid1.vcn.oc1.phx.amaaaaaahhgov4ias7kbo36zfjn6rkdk5nw65smijbbjoy6ofc3iydz7qyga",
      "ipv6-cidr-blocks": null,
      "ipv6-private-cidr-blocks": null,
      "is-zpr-only": null,
      "lifecycle-state": "AVAILABLE",
      "security-attributes": {},
      "time-created": "2025-08-14T01:30:23.489000+00:00",
      "vcn-domain-name": "vcn08131830.oraclevcn.com"
    },
    {
      "byoipv6-cidr-blocks": null,
      "cidr-block": "10.0.0.0/16",
      "cidr-blocks": [
        "10.0.0.0/16"
      ],
      "compartment-id": "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta",
      "default-dhcp-options-id": "ocid1.dhcpoptions.oc1.phx.aaaaaaaajiuarffhimtmg6ptj6x4p6cffbafqyzyleerl2c4pmbz7qucps3a",
      "default-route-table-id": "ocid1.routetable.oc1.phx.aaaaaaaaguxzfpat7ccwurxsmer6qon7jh5gtwrc2mr46etgnru7xq2vmexa",
      "default-security-list-id": "ocid1.securitylist.oc1.phx.aaaaaaaadhuzzen7j7ukzr5sefa5odftych2i5lqffuccqtgek4w3p66cdda",
      "defined-tags": {
        "Oracle-Tags": {
          "CreatedBy": "default/d.may1906@gmail.com",
          "CreatedOn": "2025-08-14T00:43:06.443Z"
        }
      },
      "display-name": "vcn-20250813-1741",
      "dns-label": "vcn08131743",
      "freeform-tags": {},
      "id": "ocid1.vcn.oc1.phx.amaaaaaahhgov4iaqasqtjuymm5pvg3qm2anqj4mqzibejri4tflqh7entqa",
      "ipv6-cidr-blocks": null,
      "ipv6-private-cidr-blocks": null,
      "is-zpr-only": null,
      "lifecycle-state": "AVAILABLE",
      "security-attributes": {},
      "time-created": "2025-08-14T00:43:06.517000+00:00",
      "vcn-domain-name": "vcn08131743.oraclevcn.com"
    },
    {
      "byoipv6-cidr-blocks": null,
      "cidr-block": "10.0.0.0/16",
      "cidr-blocks": [
        "10.0.0.0/16"
      ],
      "compartment-id": "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta",
      "default-dhcp-options-id": "ocid1.dhcpoptions.oc1.phx.aaaaaaaasuhdrdz6fk4b2xlnhg24yntvtx7rqvwakpl3ejo6xlpwlrwoz5ua",
      "default-route-table-id": "ocid1.routetable.oc1.phx.aaaaaaaajyxlsqooeqdc4u7elzztl5bsgqmvwgbcv7ia5qq3fr2oqg36yk3q",
      "default-security-list-id": "ocid1.securitylist.oc1.phx.aaaaaaaatpes3uopaix3qvgoltvnl7m347f7pjb3f7nrdcgvtnqxrfvrvyhq",
      "defined-tags": {
        "Oracle-Tags": {
          "CreatedBy": "default/d.may1906@gmail.com",
          "CreatedOn": "2025-08-14T00:38:48.457Z"
        }
      },
      "display-name": "vcn-20250813-1729",
      "dns-label": "vcn08131738",
      "freeform-tags": {},
      "id": "ocid1.vcn.oc1.phx.amaaaaaahhgov4iacxiqmbw5zlwjesin3fmeyhtjrtrlhpwr75ihm453hkoa",
      "ipv6-cidr-blocks": null,
      "ipv6-private-cidr-blocks": null,
      "is-zpr-only": null,
      "lifecycle-state": "AVAILABLE",
      "security-attributes": {},
      "time-created": "2025-08-14T00:38:48.517000+00:00",
      "vcn-domain-name": "vcn08131738.oraclevcn.com"
    },
    {
      "byoipv6-cidr-blocks": null,
      "cidr-block": "10.0.0.0/16",
      "cidr-blocks": [
        "10.0.0.0/16"
      ],
      "compartment-id": "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta",
      "default-dhcp-options-id": "ocid1.dhcpoptions.oc1.phx.aaaaaaaaokehdpci53nypkudsmkhopi5nz5qzmexcdxpfdlksim6mzlafmta",
      "default-route-table-id": "ocid1.routetable.oc1.phx.aaaaaaaaso7h6ikagxx475uq6qwdyqj2ym7mre4y5owbyydtagq3tnv4i6sq",
      "default-security-list-id": "ocid1.securitylist.oc1.phx.aaaaaaaa55fr3tvex7dhezg2sta6lce577u4ka3zverwhz7mdtlanhbk35ua",
      "defined-tags": {
        "Oracle-Tags": {
          "CreatedBy": "default/d.may1906@gmail.com",
          "CreatedOn": "2025-07-28T22:26:55.883Z"
        }
      },
      "display-name": "vcn-20250728-1512",
      "dns-label": "vcn07281526",
      "freeform-tags": {},
      "id": "ocid1.vcn.oc1.phx.amaaaaaahhgov4iajsctwwmxlzzliwhbnyb2nlmrl7i4zelxuudipqx63afq",
      "ipv6-cidr-blocks": null,
      "ipv6-private-cidr-blocks": null,
      "is-zpr-only": null,
      "lifecycle-state": "AVAILABLE",
      "security-attributes": {},
      "time-created": "2025-07-28T22:26:55.989000+00:00",
      "vcn-domain-name": "vcn07281526.oraclevcn.com"
    }
  ]
}
dmay@Mac ~ % # Get your finance-project compartment OCID
oci iam compartment list \
  --query 'data[?name==`finance-project`].id' \
  --raw-output
zsh: command not found: #
[
  "ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq"
]
dmay@Mac ~ % ssh -i ~/.ssh/oci_vm_key opc@129.146.243.189
pwd

Last login: Sun Aug 24 21:11:28 2025 from 172.115.51.4
pwd

[opc@finance-etl-server ~]$ pwd
/home/opc
[opc@finance-etl-server ~]$ 
[opc@finance-etl-server ~]$ Connection to 129.146.243.189 closed by remote host.
Connection to 129.146.243.189 closed.
dmay@Mac ~ % 
  [Restored Sep 2, 2025 at 10:58:23 AM]
Last login: Tue Sep  2 10:58:09 on console
Restored session: Tue Sep  2 08:26:07 PDT 2025
dmay@Mac ~ % ssh -i ~/.ssh/oci_vm_key opc@129.146.243.189
Last login: Mon Aug 25 16:17:05 2025 from 172.115.51.4
[opc@finance-etl-server ~]$ oci compute instance list --compartment-id "ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta" --query 'data[].{Name:"display-name",OCID:id,State:"lifecycle-state"}' --output table
+---------------+-------------------------------------------------------------------------------------+---------+
| Name          | OCID                                                                                | State   |
+---------------+-------------------------------------------------------------------------------------+---------+
| GEN-AI-LABS   | ocid1.instance.oc1.phx.anyhqljthhgov4ic42dnibrqb46e4csplnsmazx3ri7pjflxvi4w7qu4omdq | STOPPED |
| n8n-workflows | ocid1.instance.oc1.phx.anyhqljshhgov4ich2ftsiddkdw4gkqbsqhgp3k3cubwhzqp2mwkd5lqpcza | RUNNING |
+---------------+-------------------------------------------------------------------------------------+---------+
[opc@finance-etl-server ~]$ oci compute instance list --compartment-id "ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq" --query 'data[].{Name:"display-name",OCID:id,State:"lifecycle-state"}' --output table
+--------------------+-------------------------------------------------------------------------------------+---------+
| Name               | OCID                                                                                | State   |
+--------------------+-------------------------------------------------------------------------------------+---------+
| finance-etl-server | ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q | RUNNING |
+--------------------+-------------------------------------------------------------------------------------+---------+
[opc@finance-etl-server ~]$ oci compute instance get --instance-id "ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q" --query 'data."lifecycle-state"'
"RUNNING"
[opc@finance-etl-server ~]$ oci compute instance action --action STOP --instance-id "ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q"
{
  "data": {
    "agent-config": {
      "are-all-plugins-disabled": false,
      "is-management-disabled": false,
      "is-monitoring-disabled": false,
      "plugins-config": [
        {
          "desired-state": "DISABLED",
          "name": "WebLogic Management Service"
        },
        {
          "desired-state": "DISABLED",
          "name": "Vulnerability Scanning"
        },
        {
          "desired-state": "DISABLED",
          "name": "Oracle Java Management Service"
        },
        {
          "desired-state": "DISABLED",
          "name": "OS Management Hub Agent"
        },
        {
          "desired-state": "DISABLED",
          "name": "Management Agent"
        },
        {
          "desired-state": "DISABLED",
          "name": "Fleet Application Management Service"
        },
        {
          "desired-state": "ENABLED",
          "name": "Custom Logs Monitoring"
        },
        {
          "desired-state": "DISABLED",
          "name": "Compute RDMA GPU Monitoring"
        },
        {
          "desired-state": "ENABLED",
          "name": "Compute Instance Run Command"
        },
        {
          "desired-state": "ENABLED",
          "name": "Compute Instance Monitoring"
        },
        {
          "desired-state": "DISABLED",
          "name": "Compute HPC RDMA Auto-Configuration"
        },
        {
          "desired-state": "DISABLED",
          "name": "Compute HPC RDMA Authentication"
        },
        {
          "desired-state": "ENABLED",
          "name": "Cloud Guard Workload Protection"
        },
        {
          "desired-state": "DISABLED",
          "name": "Block Volume Management"
        },
        {
          "desired-state": "DISABLED",
          "name": "Bastion"
        }
      ]
    },
    "availability-config": {
      "is-live-migration-preferred": null,
      "recovery-action": "RESTORE_INSTANCE"
    },
    "availability-domain": "cFCZ:PHX-AD-1",
    "capacity-reservation-id": null,
    "cluster-placement-group-id": null,
    "compartment-id": "ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq",
    "dedicated-vm-host-id": null,
    "defined-tags": {
      "Oracle-Tags": {
        "CreatedBy": "default/d.may1906@gmail.com",
        "CreatedOn": "2025-08-22T20:38:30.421Z"
      }
    },
    "display-name": "finance-etl-server",
    "extended-metadata": {},
    "fault-domain": "FAULT-DOMAIN-3",
    "freeform-tags": {},
    "id": "ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q",
    "image-id": "ocid1.image.oc1.phx.aaaaaaaaih2igwfekpammueml4gfv6y27az7peb6zy5nwyhptgwanssoqaja",
    "instance-configuration-id": null,
    "instance-options": {
      "are-legacy-imds-endpoints-disabled": false
    },
    "ipxe-script": null,
    "is-cross-numa-node": false,
    "launch-mode": "PARAVIRTUALIZED",
    "launch-options": {
      "boot-volume-type": "PARAVIRTUALIZED",
      "firmware": "UEFI_64",
      "is-consistent-volume-naming-enabled": true,
      "is-pv-encryption-in-transit-enabled": true,
      "network-type": "PARAVIRTUALIZED",
      "remote-data-volume-type": "PARAVIRTUALIZED"
    },
    "licensing-configs": null,
    "lifecycle-state": "STOPPING",
    "metadata": {
      "ssh_authorized_keys": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCS2GqvALGF1VYGZMwhqyR+Zmnrpq2mVqnRcncEMKVhIQe/rPCe9eJN3f1h0yE3ozblU93FDeACaB2j4hG4j/X0ZOZum9mxo3bgkMdVHHQObgHlIGwVO1KYM0FdFUwMyXL7A6jpr3SJ03RvUxTc5ZOdAxOOBjeScNV/BC8qVyAl4DlopwiK/o0oOh/Vq8AGcIT+VjoYKPlI0OBIvw6S2LrX4+bZ6qc4KFoPH7vo6cYCK/tdpTs7MwFMbvLfAQ7YxPjEag9SZqP57mJgxsitVrXd1ac8B/waeC6uNzFqIABkMWTgQYA28ENztU9mCmk3sUdwDvx5Y5cRpEyCVscsfPFV9eUaEXr/7CI/BI/uCFShS8xP1nYNmQNvpj2hDDI7df7cXiNLa1iIJOw5mRGDO32KCqXIciG1S2lQsqWqBAhZ1Fys8/sVcKB0X/y28Ze4TLNtThbCpoG7UQCFme17mrH7mc9TFdHW/EpAlXBZrKzkCjw/skitVEt33eFL3dnbGtsaKirekVKhk/ktrP56IGhkPFIeZFzTOiFD5Nz6KO4JZAGB+UmD2b4M7E06xOmBuH8KBZ7o/trnyUiXw4JAj76RWYNUkMoG1vUcBdb24sTEm/Dk60/YZrCrwru00s19xIkkHfKl5o0bbmGV0ExA1mpXWRhSggw3rzYwyu0SGRYcKw== dmay@Mac.lan"
    },
    "placement-constraint-details": null,
    "platform-config": {
      "is-measured-boot-enabled": false,
      "is-memory-encryption-enabled": false,
      "is-secure-boot-enabled": false,
      "is-symmetric-multi-threading-enabled": true,
      "is-trusted-platform-module-enabled": false,
      "type": "AMD_VM"
    },
    "preemptible-instance-config": null,
    "region": "phx",
    "security-attributes": {},
    "security-attributes-state": "STABLE",
    "shape": "VM.Standard.E4.Flex",
    "shape-config": {
      "baseline-ocpu-utilization": "BASELINE_1_2",
      "gpu-description": null,
      "gpus": 0,
      "local-disk-description": null,
      "local-disks": 0,
      "local-disks-total-size-in-gbs": null,
      "max-vnic-attachments": 2,
      "memory-in-gbs": 32.0,
      "networking-bandwidth-in-gbps": 4.0,
      "ocpus": 2.0,
      "processor-description": "2.55 GHz AMD EPYC™ 7J13 (Milan)",
      "vcpus": 4
    },
    "source-details": {
      "boot-volume-size-in-gbs": null,
      "boot-volume-vpus-per-gb": null,
      "image-id": "ocid1.image.oc1.phx.aaaaaaaaih2igwfekpammueml4gfv6y27az7peb6zy5nwyhptgwanssoqaja",
      "instance-source-image-filter-details": null,
      "kms-key-id": null,
      "source-type": "image"
    },
    "system-tags": {},
    "time-created": "2025-08-22T20:38:30.990000+00:00",
    "time-maintenance-reboot-due": null
  },
  "etag": "39f0451dc1c410f1c361270b49c432bc45f735ba871e6fc4a526594fb16e4e1d"
}
[opc@finance-etl-server ~]$ Read from remote host 129.146.243.189: Operation timed out
Connection to 129.146.243.189 closed.
client_loop: send disconnect: Broken pipe
dmay@Mac ~ % ssh -i ~/.ssh/oci_vm_key opc@129.146.243.189
ssh: connect to host 129.146.243.189 port 22: Operation timed out