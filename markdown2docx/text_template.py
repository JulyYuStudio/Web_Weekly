
from string import Template

templateRedTitleH2 = Template('''<h2 data-tool="mdnice编辑器" style="margin-top: 30px; padding: 0px; font-weight: bold; font-size: 22px; border-bottom: 2px solid rgb(89,89,89); margin-bottom: 5px; color: rgb(89,89,89);"><span class="content" style="font-size: 22px; display: inline-block; border-bottom: 2px solid rgb(89,89,89);">$h2</span></h2>''')

templateRedUl = Template('''<ul data-tool="mdnice编辑器" style="margin-top: 4px; margin-bottom: 4px; padding-left: 25px; color: black; list-style-type: disc;">$ul</ul>''')

templateRedLi = Template('''<li><section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">$li</section><p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: rgb(89,89,89);"><strong style="font-weight: bold; color: rgb(71, 193, 168);">$url</strong></p></li>''')

templateRedTitleH3 = Template('''<h3 data-tool="mdnice编辑器" style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-weight: bold; font-size: 20px; color: rgb(89,89,89);"><span class="prefix" style="display: none;"></span><span class="content">$h3</span></h3>''')

templateRedUrl= Template('''<p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: rgb(89,89,89);"><strong style="font-weight: bold; color: rgb(71, 193, 168);">$url</strong></p>''')

templateContent = Template('''<p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;">$content</p>''')


templateMiddleTitle = Template('''<p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; text-align: center;"><span leaf="">$content</span></p>''')

templateDividerLine = '''<hr style="border-style: solid; border-width: 1px 0 0; border-color: rgba(0,0,0,0.1); -webkit-transform-origin: 0 0; -webkit-transform: scale(1, 0.5); transform-origin: 0 0; transform: scale(1, 0.5);" contenteditable="false" class="">'''

templateWXCard = '''<section class="mp_profile_iframe_wrp custom_select_card_wrp" nodeleaf=""><mp-common-profile class="mpprofile js_uneditable custom_select_card mp_profile_iframe custom_select_card_selected ProseMirror-selectednode" data-pluginname="mpprofile" data-nickname="JulyYuStudio" data-alias="julyyu910" data-headimg="http://mmbiz.qpic.cn/mmbiz_png/bPIhNYICt0dmj4maw6wicB5vBgaVH1PibqByJuiaeZ0VR5o7he3m5grshD7EIoUOD74l0bSX1PHU1v937sPibOaOJQ/0?wx_fmt=png" data-signature="JulyYu的个人日常/技术/稀奇古怪/有的没的" data-id="MzUxODI4NTY5OA==" data-service_type="1" draggable="true"></mp-common-profile><br class="ProseMirror-trailingBreak"></section>'''