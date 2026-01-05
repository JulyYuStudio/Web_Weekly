
from string import Template

templateRedTitleH2 = Template('''<h2 data-tool="mdnice编辑器" style="margin-top: 30px; padding: 0px; font-weight: bold; font-size: 25px; border-bottom: 2px solid rgb(0,0,0); margin-bottom: 5px; color: rgb(0,0,0);"><span class="content" style="font-size: 25px; display: inline-block; border-bottom: 2px solid rgb(89,89,89);">$h2</span></h2>''')

templateRedUl = Template('''<ul data-tool="mdnice编辑器" style="margin-top: 4px; margin-bottom: 4px; padding-left: 25px; color: black; list-style-type: disc;">$ul</ul>''')

templateRedLi = Template('''<li><section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">$li</section><p data-tool="mdnice编辑器" style="font-size: 15px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: rgb(89,89,89);"><strong style="font-weight: bold; color: rgb(71, 193, 168);">$url</strong></p></li>''')

templateRedTitleH3 = Template('''<h3 data-tool="mdnice编辑器" style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-weight: bold; font-size: 20px; color: rgb(0,0,0);"><span class="prefix" style="display: none;"></span><span class="content"># $h3</span></h3>''')

templateRedUrl= Template('''<p data-tool="mdnice编辑器" style="font-size: 15px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: rgb(0,0,0);"><strong style="font-weight: bold; color: rgb(71, 193, 168);">$url</strong></p>''')

templateContent = Template('''<p data-tool="mdnice编辑器" style="font-size: 15px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 1.5em; color: #333333;">$content</p>''')


templateMiddleTitle = Template('''<p data-tool="mdnice编辑器" style="font-size: 15px; padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; text-align: center;"><span leaf="">$content</span></p>''')

templateDividerLine = '''<hr style="border-style: solid; border-width: 1px 0 0; border-color: rgba(0,0,0,0.1); -webkit-transform-origin: 0 0; -webkit-transform: scale(1, 0.5); transform-origin: 0 0; transform: scale(1, 0.5);" contenteditable="false" class="">'''

templateWXCard = '''<section class="mp_profile_iframe_wrp custom_select_card_wrp" nodeleaf=""><mp-common-profile class="mpprofile js_uneditable custom_select_card mp_profile_iframe custom_select_card_selected ProseMirror-selectednode" data-pluginname="mpprofile" data-nickname="JulyYuStudio" data-alias="julyyu910" data-headimg="http://mmbiz.qpic.cn/mmbiz_png/bPIhNYICt0dmj4maw6wicB5vBgaVH1PibqByJuiaeZ0VR5o7he3m5grshD7EIoUOD74l0bSX1PHU1v937sPibOaOJQ/0?wx_fmt=png" data-signature="JulyYu的个人日常/技术/稀奇古怪/有的没的" data-id="MzUxODI4NTY5OA==" data-service_type="1" draggable="true"></mp-common-profile><br class="ProseMirror-trailingBreak"></section>'''





templateTitleH3 = Template('''<h3 data-tool="mdnice编辑器" style="display: inline-block;border: 2px solid transparent;border-radius: 4px;background: linear-gradient(#f5f7fa, #f5f7fa) padding-box,linear-gradient(135deg, #36d1dc, #5b86e5) border-box;margin-top: 30px; margin-bottom: 15px; padding: 5px 10px; font-weight: bold; font-size: 20px; color: rgb(0,0,0);"><span class="prefix" style="display: none;"></span><span class="content">$h3</span></h3>''')

##templateTitleH2 = Template('''<h2 data-tool="mdnice编辑器" style="margin-top: 30px; padding: 0px; font-weight: bold; font-size: 25px; margin-bottom: 5px; color: rgb(0,0,0); padding-bottom: 1px; background: linear-gradient(to right, #f5f7fa, #f5f7fa) 0 100% / 100% 2px no-repeat;"><span class="content" style="font-size: 25px; display: inline-block; padding-bottom: 2px; border-bottom: 2px solid transparent; background: linear-gradient(to right, #36d1dc, #5b86e5) 0 100% / 100% 2px no-repeat;">$h2</span></h2>''')
##templateTitleH2 = Template('''<h2 data-tool="mdnice编辑器" style="margin-top: 30px; padding: 0px; font-weight: bold; font-size: 25px; margin-bottom: 5px; color: rgb(0,0,0); background: linear-gradient(to right, rgba(232, 244, 248, 0.8), rgba(240, 247, 255, 0.8)) 0 100% / 100% 2px no-repeat;"><span class="content" style="font-size: 25px; display: inline-block; padding-bottom: 2px; background: linear-gradient(to right, #36d1dc, #5b86e5) 0 100% / 100% 2px no-repeat;">$h2</span></h2>''')
templateTitleH2 = Template('''<h2 data-tool="mdnice编辑器" style="margin-top: 30px; padding: 0px; font-weight: bold; font-size: 25px; margin-bottom: 5px; color: rgb(0,0,0); background: linear-gradient(to right, #e8f4f8, #5b86e5) 0 100% / 100% 2px no-repeat;"><span class="content" style="font-size: 25px; display: inline-block; padding-bottom: 4px; background: linear-gradient(to right, #36d1dc, #5b86e5) 0 100% / 100% 4px no-repeat;">$h2</span></h2>''')



templateTitleBgH3 = Template('''<h3 data-tool="mdnice编辑器" style="margin-top: 30px; margin-bottom: 15px; padding: 0; font-weight: bold; font-size: 21px; color: #000; display: inline-block;"><span class="prefix" style="display: none;"></span><span class="content" style="padding: 1px 8px; line-height: 1.2; background: linear-gradient(to top, #e9ecef 80%, transparent 80%);background-size: 100% 100%;background-repeat: no-repeat;">$h3</span></h3>''')

templateArtileLi = Template('''<li><section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;"><span leaf="">$li</span><span leaf="" data-pm-slice="1 1 [&quot;para&quot;,{&quot;tagName&quot;:&quot;p&quot;,&quot;attributes&quot;:{&quot;data-tool&quot;:&quot;mdnice编辑器&quot;,&quot;style&quot;:&quot;font-size: 15px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: rgb(89,89,89);&quot;},&quot;namespaceURI&quot;:&quot;http://www.w3.org/1999/xhtml&quot;}]"><span textstyle="" style="font-size: 10px; color: rgb(153, 195, 255); text-decoration: underline">$url</span></span></section></li>''')

templateNetUrl = Template('''<p data-tool="mdnice编辑器" style="font-size: 15px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: rgb(89,89,89);"><span leaf=""><span textstyle="" style="font-size: 10px; color: #0269c8; text-decoration: underline">$url</span></span></p>''')