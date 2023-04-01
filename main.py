import requests

#Systems

Ubuntu = 'https://releases.ubuntu.com/22.04.2/ubuntu-22.04.2-desktop-amd64.iso' #22.04
Fedora = 'https://download.fedoraproject.org/pub/fedora/linux/releases/37/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-37-1.7.iso' #Fedora37
Windows7 = 'https://windowstan.com/download/windows-7-home-basic-x86/?wpdmdl=10901&refresh=6427a2d5e012f1680319189' #Windows7
Kali_main = 'https://cdimage.kali.org/kali-2023.1/kali-linux-2023.1-installer-amd64.iso' 
Kali_virtual_vmware = 'https://cdimage.kali.org/kali-2023.1/kali-linux-2023.1-vmware-amd64.7z'
Kali_virtual_virtualbox = 'https://cdimage.kali.org/kali-2023.1/kali-linux-2023.1-virtualbox-amd64.7z'
Kali_virtual_Qemu = 'https://cdimage.kali.org/kali-2023.1/kali-linux-2023.1-qemu-amd64.7z'
Arch = 'https://irltoolkit.mm.fcix.net/archlinux/iso/2023.04.01/archlinux-2023.04.01-x86_64.iso' #This is Arch from USA fcix.net(The download can be slow)


#Function

def Downloader():
    Question = input('Please enter your System you want do download(Ubuntu/Fedora/Kali/Arch/Windows7): ')
    if Question == 'Ubuntu' or Question == 'Ub':
        print('Downloading Ubuntu...')
        first = requests.get(Ubuntu, allow_redirects=True)
        open('Ubuntu.iso', 'wb').write(first.content)
    elif Question == 'Fedora' or Question == 'Fe':
        print('Downloading Fedora...')
        second = requests.get(Fedora, allow_redirects=True)
        open('Fedora.iso', 'wb').write(second.content)
    elif Question == 'Windows7' or Question == 'W7':
        print('Downloading Windows7...')
        third = requests.get(Windows7, allow_redirects=True)
        open('Windows7.iso', 'wb').write(third.content)
    elif Question == 'Kali':
        forKali = input('Select ur Kali(Normal/Vmware/Virtualbox/QEMU): ')
        if forKali == 'Normal':
            print('Downloading Normal Kali...')
            four = requests.get(Kali_main, allow_redirects=True)
            open('Kali_Linux_Normal.iso', 'wb').write(four.content)
        elif forKali == 'Vmware':
            print('Downloading Vmware Kali...')
            five = requests.get(Kali_virtual_vmware, allow_redirects=True)
            open('Kali_vmware.7z', 'wb').write(five.content)
        elif forKali == 'Virtualbox':
            print('Downloading Virtualbox Kali...')
            six = requests.get(Kali_virtual_virtualbox, allow_redirects=True)
            open('Kali_virtualbox.7z', 'wb').write(six.content)
        elif forKali == 'QEMU':
            print('Downloading QEMU Kali...')
            seven = requests.get(Kali_virtual_Qemu, allow_redirects=True)
            open('Kali_QEMU.7z', 'wb').write(seven.content)
    elif Question == 'Arch':
        print('Downloading Arch...')
        eight = requests.get(Arch, allow_redirects=True)
        open('Arch.iso', 'wb').write(eight.content)
    else:
        exit(0)


Downloader()