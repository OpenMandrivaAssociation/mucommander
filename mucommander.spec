%define distsuffix edm
Name: mucommander 
Version: 0.8.5
Release: %mkrel 1
Summary: muCommander is a lightweight, cross-platform file manager
License: GPL
Group:   Utility

URL:		http://www.mucommander.com/
Source0:	mucommander-0.8.5.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

BuildArch:      noarch
Requires:       java-1.6.0-sun

%description

muCommander es un ligero y multiplataforma administrador de archivos con una interfaz de doble panel. Funciona en cualquier sistema operativo con soporte para Java (Mac OS X, Windows, Linux, * BSD, Solaris ...).
 
He aquí una lista no exhaustiva de lo que encontrarás en el programa:

*   un sistema de archivos virtual con soporte para los volúmenes locales, FTP, SFTP, SMB, NFS, HTTP, Amazon S3, Hadoop HDFS y Bonjour
*   permite rápidamente copiar, mover, renombrar archivos, crear directorios, archivos de correo electrónico...
*   Permite Buscar, comprimir y descomprimir archivos ZIP, RAR, 7z, TAR, GZIP, BZIP2, ISO / NRG, AR / Deb y LST archivos
*   los archivos ZIP pueden ser modificados sobre la marcha, sin tener que descomprimir todo el archivo
*   Marcadores Universal y administrador de credenciales de
*   Soporte para múltiples ventanas
*   completo acceso desde el teclado 
*   Altamente configurable
*   Disponible en 23 idiomas: Inglés américano y británico, francés, alemán, español, checo, chino simplificado y tradicional, polaco, húngaro, ruso, esloveno, rumano, italiano, coreano, portugués de Brasil, neerlandés, eslovaco, japonés, sueco, danés , ucraniano y árabe.
* es Software Libre (GPL)

(English)

muCommander is a lightweight, cross-platform file manager with a dual-pane interface. It runs on any operating system with Java support (Mac OS X, Windows, Linux, *BSD, Solaris...).
 
Here's a non-exhaustive list of what you'll find:

* 	Virtual filesystem with support for local volumes, FTP, SFTP, SMB, NFS, HTTP, Amazon S3, Hadoop HDFS and Bonjour
* 	Quickly copy, move, rename files, create directories, email files...
* 	Browse, create and uncompress ZIP, RAR, 7z, TAR, GZip, BZip2, ISO/NRG, AR/Deb and LST archives
* 	ZIP files can be modified on-the-fly, without having to recompress the whole archive
* 	Universal bookmarks and credentials manager
* 	Multiple windows support
* 	Full keyboard access
* 	Highly configurable
* 	Available in 23 languages : American & British English, French, German, Spanish, Czech, Simplified & Traditional Chinese, Polish, Hungarian, Russian, Slovenian, Romanian, Italian, Korean, Brazilian Portuguese, Dutch, Slovak, Japanese, Swedish, Danish, Ukrainian and Arabic.
* 	Free Software (GPL)

%prep 

%setup -q -n %{name}

%install
%__install -dm 755 %{buildroot}/usr/lib
cp -r $RPM_BUILD_DIR/mucommander $RPM_BUILD_ROOT/usr/lib/

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


%clean

rm -rf $RPM_BUILD_ROOT

%post
ln -sf /usr/lib/mucommander/mucommander.sh /usr/bin/mucommander

%postun
rm -rf /usr/bin/mucommander

%files
%defattr(-,root,root)
/usr/*
/usr/lib/*
/usr/share/*

