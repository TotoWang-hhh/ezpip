import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import tkinter.filedialog as filebox
import webbrowser
from threading import Thread
import sys
import ctypes, sys

sdo=False
sdi=False


if len(sys.argv)>=1 and '--debug' in sys.argv:
    sdi=True

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def be_admin():
    if is_admin():
        msgbox.showinfo('无需再次提权','程序正以管理员身份运行，无需再次提权')
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        exit()

def showDebug(show_info=False):
    global sdo,sdo_btn,sdi,egg_count
    if show_info:
        if sdi:
            sdi=False
            sdi_btn['text']='显示调试信息'
        else:
            sdi=True
            sdi_btn['text']='隐藏调试信息'
    else:
        if sdo:
            win.geometry('300x397')
            sdo_btn['text']='显示调试选项  v'
            egg_count=0
            sdo=False
        else:
            win.geometry('300x505')
            sdo_btn['text']='隐藏调试选项  ^'
            sdo=True

def dprint(msg):
    global sdi
    if sdi:
        print(msg)

def init():
    global py_path,pip_path,python_path
    try:
        if '--init' in sys.argv:#如果用户要求重新配置
            i=abc#以前这部分关于判断文件是否存在的写法令我震惊，我决定通过制造异常来直接触发except，将错就错（划去
        dprint('正在读取配置信息')
        py_path_f=open("./py_path.cfg",'r',encoding='utf-8')
        py_path=py_path_f.read()
        dprint('根据配置信息，您的Python位于：'+py_path)
        py_path_f.close()
        pip_path=py_path+"/scripts/pip.exe"
        python_path=py_path+"/python.exe"
        dprint('读取完成')
        if py_path=='使用环境变量':
            dprint('使用环境变量')
            pip_path='pip'
            python_path='python'
    except Exception as e:
        dprint('读取设置失败：'+str(e))
        win=tk.Tk()
        win.withdraw()
        py_path=filebox.askdirectory(title='请选择Python安装路径')
        py_path_f=open("./py_path.cfg",'w',encoding='utf-8')
        py_path_f.write(py_path)
        py_path_f.close()
        pip_path=py_path+"/scripts/pip.exe"

def locate_pip(name=''):
    os.system("where pip")
    os.system("where pip3")
    print('==================================================')

def install(name):
    os.system(pip_path+" install "+name+' -i https://pypi.douban.com/simple')
    print('==================================================')

def uninstall(name):
    if name=='pip':
        print('请勿卸载pip！否则通常情况下，您将无法装回！')
    else:
        accept=msgbox.askokcancel(title = '请确认您的高危操作',message='您确定要卸载 '+name+' 吗？') # 返回值为True或者False
        if accept:
            os.system(pip_path+" uninstall "+name+' -y')
        else:
            print('用户取消了卸载 '+name+' 的操作')
    print('==================================================')

def upgrade(name=''):
    os.system(python_path+" -m pip install --upgrade pip -i https://pypi.douban.com/simple")
    print('==================================================')

def list_pkg(name=''):
    os.system(pip_path+" list")
    print('==================================================')

def about(name=''):
    os.system(pip_path+" --version")
    print('==================================================')
    
def start(func,p=''):
    #print(func)
    dprint('将向函数传入此类型的参数：'+str(type(p)))
    dprint('将向函数传入参数：'+str(p))
    #t=Thread(target=func,args=p)
    t=Thread(target=lambda:func(p))
    t.start()

def view(url):
    webwin=tk.Tk()
    webwin.title('网页查看器')
    frame=WebView2(webwin,1200,680)
    frame.load_url(url)
    frame.pack(fill=tk.BOTH,expand=True)
    ttk.Button(webwin,text='在浏览器打开',command=lambda:webbrowser.open(url)).pack(fill=tk.X,side=tk.BOTTOM)
    webwin.mainloop()

def inst_from_lst(lst):
    for i in lst:
        print('正在安装：'+str(i))
        install(str(i))

def start_inst_from_lst(lst,sel,window):#一个杂到无法注释的函数，用于获取选中的库然后开始安装
    selm=[]
    for i in list(sel):
        selm.append(lst[int(i)])
    dprint('即将安装您选中的库：'+str(selm))
    start(inst_from_lst,selm)
    window.destroy()

def inst_from_py(name=''):
    fpath=filebox.askopenfilename(title='请选择Python源码文件',filetypes=[('Python源码文件','.py')])
    f=open(fpath,'r',encoding='utf-8')
    cont=f.read()
    f.close()
    print('正在分析文件...')
    modules=[]#空列表，用于存储要安装的依赖名称（每一项的类型为字符串）
    i=0#记录行数
    for line in cont.split('\n'):#遍历所有代码
        i+=1
        #判断是不是一行导入库的代码，后面的大段条件是为了排除变量（或函数）名含“import”，就例如这段代码，“line.split('#')[0]”的意思是忽略注释满足（或不满足）条件
        if 'import' in line.split('#')[0] and ('=' not in line.split('#')[0]) and ('if' not in line.split('#')[0]) and ('while' not in line.split('#')[0]) and ('print' not in line.split('#')[0]) and ('(' not in line.split('#')[0]):
            thismodule=line
            if 'from' in line:#“from ... import ...”比较特殊，因为它把库名分开了
                thismodule=line.split(' ')[line.split(' ').index('from')+1]#获取“from”后面那个词
            elif 'as' in line:#“import ... as ...”也很特殊，因为里面不仅包含库名，还包含一个别名...
                thismodule=line.split(' ')[line.split(' ').index('import')+1]#同理，获取“import”后面那个词
            else:
                thismodule=thismodule.replace(' ','').replace('import','').replace('as','').replace('from','')#一般情况下，可以直接剔除除了库名以外的所有信息
            thismodule=thismodule.split('.')[0]#如果代码只调用了里面的某一部分，则获取最顶层的名称
            dprint('检测到于第 '+str(i)+' 行导入的库：'+thismodule)
            modules.append(thismodule)#存储依赖名称
            #但愿这个if语句里面没问题
    #去重（副作用：重排）
    modules=list(set(modules))
    #完成
    print('分析完成！请继续操作...')
    print('==================================================')
    #多选窗口这块我直接照搬了WordLST
    dwin=tk.Toplevel()
    dwin.title('选择欲安装的依赖 - EasyPyPI')
    dwin.transient(win)
    tk.Label(dwin,text='请选择欲安装的依赖，然后点击“开始安装”',anchor='w').pack(fill=tk.X,padx=20)
    tk.Label(dwin,text='默认不会以管理员身份安装，若个别库安装时提示权限不足，请单独安装',anchor='w',fg='#707070').pack(fill=tk.X,padx=20)
    tk.Label(dwin,text='可能会识别到并显示自带的库，此BUG已知且暂不打算修复，请谅解',anchor='w',fg='#707070').pack(fill=tk.X,padx=20)
    dlst=tk.Listbox(dwin,width=20,bd=0,highlightthickness=0,activestyle='none',selectmode='multiple',height=20)
    dlst.pack(fill=tk.BOTH,padx=20,pady=15)
    ttk.Button(dwin,text='开始安装',command=lambda:start_inst_from_lst(modules,dlst.curselection(),dwin)).pack(fill=tk.X,expand=True)
    for i in modules:
        dlst.insert(tk.END,i)

dprint('您传入了参数：'+str(sys.argv))

init()

dprint('执行：     '+pip_path+' install '+'（库名）'+' -i https://pypi.douban.com/simple')
dprint('==================================================')

try:
    from tkwebview2.tkwebview2 import WebView2
except ModuleNotFoundError:
    print('将为您安装必须的库：')
    install('tkwebview2')
    print('==================================================')

win=tk.Tk()
win.title('Easy PyPI')
win.geometry('300x397')
win.resizable(0,0)
win.update()


name_enter=ttk.Entry(win)
name_enter.pack(fill=tk.X)

#功能区
ttk.Button(win,text='安装',command=lambda:start(install,name_enter.get())).pack(fill=tk.X)
ttk.Button(win,text='卸载',command=lambda:start(uninstall,name_enter.get())).pack(fill=tk.X)
ttk.Button(win,text='关于此库',command=lambda:view("https://pypi.org/project/"+name_enter.get()+"/")).pack(fill=tk.X)
ttk.Button(win,text='列出所有已经安装的库',command=lambda:start(list_pkg)).pack(fill=tk.X)
be_admin_btn=ttk.Button(win,text='提权',command=be_admin)
be_admin_btn.pack(fill=tk.X)
ttk.Button(win,text='更新PIP',command=lambda:start(upgrade)).pack(fill=tk.X)
ttk.Button(win,text='关于PIP',command=lambda:start(about)).pack(fill=tk.X)
ttk.Button(win,text='查看环境变量中有关PIP路径的配置',command=lambda:start(locate_pip)).pack(fill=tk.X)
ttk.Button(win,text='根据Python源码安装依赖',command=inst_from_py).pack(fill=tk.X)
sdo_btn=ttk.Button(win,text='显示调试选项  v',command=showDebug)
sdo_btn.pack(fill=tk.X)

#提权按钮
if is_admin():
    be_admin_btn['text']='程序正以管理员身份运行'
    be_admin_btn['state']='disabled'

#介绍区被删去，因为它被CHM所替代

tk.Button(win,text='2022 By 人工智障',bg='lightgrey',bd=0,command=lambda:view("http://rgzz.great-site.net/?i=1")).pack(fill=tk.X)
tk.Button(win,text='问题反馈',bg='lightgrey',bd=0,command=lambda:view("https://support.qq.com/products/384388?")).pack(fill=tk.X)
tk.Button(win,text='帮助',bg='lightgrey',bd=0,command=lambda:view("http://rgzz.great-site.net/soft/ezpip/WebHelp/")).pack(fill=tk.X)
tk.Button(win,text='开源许可证',bg='lightgrey',bd=0,command=lambda:view("https://www.mozilla.org/en-US/MPL/1.1/")).pack(fill=tk.X)


#调试选项
ttk.Button(win,text='显示输入的内容',command=lambda:print(name_enter.get()+'\n'+'==================================================')).pack(fill=tk.X)
ttk.Button(win,text='使用内建网页查看器打开输入的网址',command=lambda:view(name_enter.get())).pack(fill=tk.X)

sdi_btn=ttk.Button(win,text='显示调试信息',command=lambda:showDebug(show_info=True))
sdi_btn.pack(fill=tk.X)

egg_btn=ttk.Button(win,text='要相信彩蛋会永远陪着你，好吗？:)',state='disabled')
egg_btn.pack(fill=tk.X)


win.mainloop()
