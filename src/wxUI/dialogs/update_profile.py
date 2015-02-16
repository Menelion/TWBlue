# -*- coding: utf-8 -*-
import wx

class updateProfile(wx.Dialog):
 def __init__(self, parent):
  super(updateProfile, self).__init__(parent=None, id=-1)
  self.SetTitle(_(u"Update your profile"))
  panel = wx.Panel(self)
  labelName = wx.StaticText(panel, -1, _(u"Name (20 characters maximum)"))
  self.name = wx.TextCtrl(panel, -1)
  self.name.SetFocus()
  dc = wx.WindowDC(self.name)
  dc.SetFont(self.name.GetFont())
  self.name.SetSize(dc.GetTextExtent("0"*20))
  labelLocation = wx.StaticText(panel, -1, _(u"Location"))
  self.location = wx.TextCtrl(panel, -1)
  dc = wx.WindowDC(self.location)
  dc.SetFont(self.location.GetFont())
  self.location.SetSize(dc.GetTextExtent("0"*35))
  labelUrl = wx.StaticText(panel, -1, _(u"Website"))
  self.url = wx.TextCtrl(panel, -1)
  dc = wx.WindowDC(self.url)
  dc.SetFont(self.url.GetFont())
  self.url.SetSize(dc.GetTextExtent("0"*22))
  labelDescription = wx.StaticText(panel, -1, _(u"Bio (160 characters maximum)"))
  self.description = wx.TextCtrl(panel, -1, size=(400, 400))
  dc = wx.WindowDC(self.description)
  dc.SetFont(self.description.GetFont())
  self.description.SetSize(dc.GetTextExtent("0"*160))
  self.image = None
  self.upload_image = wx.Button(panel, -1, _(u"Upload a picture"))
  self.upload_image.Bind(wx.EVT_BUTTON, self.onUpload_picture)
  ok = wx.Button(panel, wx.ID_OK, _(u"Update profile"))
  ok.Bind(wx.EVT_BUTTON, self.onUpdateProfile)
  ok.SetDefault()
  close = wx.Button(panel, wx.ID_CANCEL, _("Close"))
  sizer = wx.BoxSizer(wx.VERTICAL)
  nameBox = wx.BoxSizer(wx.HORIZONTAL)
  nameBox.Add(labelName, 0, wx.ALL, 5)
  nameBox.Add(self.name, 0, wx.ALL, 5)
  sizer.Add(nameBox, 0, wx.ALL, 5)
  locationBox = wx.BoxSizer(wx.HORIZONTAL)
  locationBox.Add(labelLocation, 0, wx.ALL, 5)
  locationBox.Add(self.location, 0, wx.ALL, 5)
  sizer.Add(locationBox, 0, wx.ALL, 5)
  urlBox = wx.BoxSizer(wx.HORIZONTAL)
  urlBox.Add(labelUrl, 0, wx.ALL, 5)
  urlBox.Add(self.url, 0, wx.ALL, 5)
  sizer.Add(urlBox, 0, wx.ALL, 5)
  descriptionBox = wx.BoxSizer(wx.HORIZONTAL)
  descriptionBox.Add(labelDescription, 0, wx.ALL, 5)
  descriptionBox.Add(self.description, 0, wx.ALL, 5)
  sizer.Add(descriptionBox, 0, wx.ALL, 5)
  sizer.Add(self.upload_image, 5, wx.CENTER, 5)
  btnBox = wx.BoxSizer(wx.HORIZONTAL)
  btnBox.Add(ok, 0, wx.ALL, 5)
  btnBox.Add(close, 0, wx.ALL, 5)
  sizer.Add(btnBox, 0, wx.ALL, 5)
  panel.SetSizer(sizer)
  self.SetClientSize(sizer.CalcMin())

 def onUpload_picture(self, ev):
  if self.upload_image.GetLabel() == _(u"Discard image"):
   self.upload_image.SetLabel(_(u"Upload a picture"))
   self.controller.clear_file()
  else:
   openFileDialog = wx.FileDialog(self, _(u"Select the picture to be uploaded"), "", "", _("Image files (*.png, *.jpg, *.gif)|*.png; *.jpg; *.gif"), wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
   if openFileDialog.ShowModal() == wx.ID_CANCEL:
    return
   self.controller.get_file(openFileDialog.GetPath())
   self.upload_image.SetLabel(_(u"Discard image"))
  ev.Skip()

 def get_response(self):
  return self.ShowModal()