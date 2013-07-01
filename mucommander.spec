%define oname muCommander
Name: mucommander 
Version: 0.9.0
Release: 2
Summary: Lightweight, cross-platform file manager
License: GPL
Group:   File tools
URL:		http://www.mucommander.com/
Source0:	http://www.mucommander.com/download/mucommander-0_9_0.tar.gz
BuildArch:      noarch
Requires:       java >= 1.6.0

%description

muCommander is a lightweight, cross-platform file manager with a dual-pane
interface. It runs on any operating system with Java support
(Mac OS X, Windows, Linux, *BSD, Solaris...).
 
Here's a non-exhaustive list of what you'll find:

* Virtual filesystem with support for local volumes,
    FTP, SFTP, SMB, NFS, HTTP, Amazon S3, Hadoop HDFS and Bonjour
* Quickly copy, move, rename files, create directories, email files...
* Browse, create and uncompress ZIP, RAR, 7z, TAR, GZip, BZip2, ISO/NRG,
    AR/Deb and LST archives
* ZIP files can be modified on-the-fly, without having to recompress the 
    whole archive
* Universal bookmarks and credentials manager
* Multiple windows support
* Full keyboard access
* Highly configurable
* Available in 23 languages : American & British English, French, German,
    Spanish, Czech, Simplified & Traditional Chinese, Polish, Hungarian,
    Russian, Slovenian, Romanian, Italian, Korean, Brazilian Portuguese,
    Dutch, Slovak, Japanese, Swedish, Danish, Ukrainian and Arabic.
* Free Software (GPL)

%prep 

%setup -q -n %{oname}-0_9_0

%install
%__install -dm 755 %{buildroot}/usr/lib
cp -r $RPM_BUILD_DIR/%{oname}-0_9_0 $RPM_BUILD_ROOT/usr/lib/%{name}

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=muCommander
GenericName=muCommander
Comment=File Manager
Exec=/usr/bin/mucommander
Icon=/usr/lib/mucommander/mucommander.png
Terminal=false
Type=Application
StartupNotify=true
MimeType=foo/bar;foo2/bar2;
Categories=Application;Utility;
EOF




%post
ln -sf /usr/lib/mucommander/mucommander.sh /usr/bin/mucommander

%postun
rm -f /usr/bin/mucommander

%files
%defattr(-,root,root)
%doc license.txt readme.txt
/usr/lib/*
/usr/share/*

