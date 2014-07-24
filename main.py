# from translator import unicode_to_indica, indica_to_unicode
from unicode_to_indica import convertToindica as unicode_to_indica
from indica_to_unicode import convertTounicode as indica_to_unicode
from unicode_to_roman import convertToroman as unicode_to_roman
from roman_to_unicode import convertTounicode as roman_to_unicode
from unicode_to_indoweb import convertToindoweb as unicode_to_indoweb
from indoweb_to_unicode import convertTounicode as indoweb_to_unicode
from unicode_to_tscii import convertTotscii as unicode_to_tscii
from tscii_to_unicode import convertTounicode as tscii_to_unicode
from unicode_to_tab import convertTotab as unicode_to_tab
from tab_to_unicode import convertTounicode as tab_to_unicode
from unicode_to_tam import convertTotam as unicode_to_tam
from tam_to_unicode import convertTounicode as tam_to_unicode
from unicode_to_anjal import convertToanjal as unicode_to_anjal
from anjal_to_unicode import convertTounicode as anjal_to_unicode
from unicode_to_murasoli import convertTomurasoli as unicode_to_murasoli
from murasoli_to_unicode import convertTounicode as murasoli_to_unicode
from unicode_to_bamini import convertTobamini as unicode_to_bamini
from bamini_to_unicode import convertTounicode as bamini_to_unicode
from unicode_to_shreelipi import convertToshreelipi as unicode_to_shreelipi
from shreelipi_to_unicode import convertTounicode as shreelipi_to_unicode
import wx
import goslate


class Tats(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=u"TATS (Tamil Transliteration System) 2.0",
                          pos=wx.DefaultPosition, size=wx.Size(500, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.fp_source = wx.FontPickerCtrl(self, wx.ID_ANY, wx.Font(
            wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Arial"),
                                           wx.DefaultPosition, wx.DefaultSize,
                                           wx.FNTP_USE_TEXTCTRL)
        self.fp_source.SetMaxPointSize(100)
        main_sizer.Add(self.fp_source, 0, wx.ALL | wx.EXPAND, 5)

        self.tc_source = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                     wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_MULTILINE)
        main_sizer.Add(self.tc_source, 1, wx.ALL | wx.EXPAND, 5)

        fgSizer1 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer1.AddGrowableCol(0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        cb_translationChoices = [u"unicode to indica (mac)",
                                 u"indica (mac) to unicode",
                                 u"unicode to roman", u"roman to unicode",
                                 u"unicode to indoweb", u"indoweb to unicode",
                                 u"unicode to tscii", u"tscii to unicode",
                                 u"unicode to tab", u"tab to unicode",
                                 u"unicode to tam", u"tam to unicode",
                                 u"unicode to anjal", u"anjal to unicode",
                                 u"unicode to murasoli", u"murasoli to unicode",
                                 u"unicode to bamini", u"bamini to unicode",
                                 u"unicode to ShreeLipi",
                                 u"ShreeLipi to unicode"]
        self.cb_translation = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition,
                                        wx.DefaultSize, cb_translationChoices,
                                        0)
        self.cb_translation.SetSelection(0)
        fgSizer1.Add(self.cb_translation, 0, wx.ALL | wx.EXPAND, 5)

        self.cb_google = wx.CheckBox(self, wx.ID_ANY, u"Google Pre Translate",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.cb_google, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.btn_translate = wx.Button(self, wx.ID_ANY, u"Translate",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.btn_translate, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        main_sizer.Add(fgSizer1, 0, wx.EXPAND | wx.ALIGN_RIGHT, 5)

        self.tc_destination = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                          wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_MULTILINE)
        main_sizer.Add(self.tc_destination, 1, wx.ALL | wx.EXPAND, 5)

        self.fp_destination = wx.FontPickerCtrl(self, wx.ID_ANY, wx.Font(
            wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Arial"),
                                                wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.FNTP_USE_TEXTCTRL)
        self.fp_destination.SetMaxPointSize(100)
        main_sizer.Add(self.fp_destination, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.fp_source.Bind(wx.EVT_FONTPICKER_CHANGED, self.source_font_changed)
        self.cb_translation.Bind(wx.EVT_CHOICE, self.translation_selected)
        self.cb_google.Bind(wx.EVT_CHECKBOX, self.google_translate)
        self.btn_translate.Bind(wx.EVT_BUTTON, self.translate)
        self.fp_destination.Bind(wx.EVT_FONTPICKER_CHANGED,
                                 self.destination_font_changed)

        # Variables
        self.gs = goslate.Goslate()

    def __del__(self):
        pass


        # Virtual event handlers, overide them in your derived class
    def source_font_changed(self, event):
        selectedFont = self.fp_source.GetSelectedFont()
        self.tc_source.SetFont(selectedFont)
        event.Skip()

    def destination_font_changed(self, event):
        selectedFont = self.fp_destination.GetSelectedFont()
        self.tc_destination.SetFont(selectedFont)
        event.Skip()

    def translation_selected(self, event):
        # print self.cb_translation.GetCurrentSelection()
        if (self.cb_google.GetValue() is True and
                    self.cb_translation.GetCurrentSelection() != 0):
            wx.MessageBox("Google does not work with indica to unicode!!!",
                          "WARNING!")
            self.cb_google.SetValue(False)
        event.Skip()

    def google_translate(self, event):
        if (self.cb_google.GetValue() is True and
                    self.cb_translation.GetCurrentSelection() != 0):
            wx.MessageBox("Google does not work with indica to unicode!!!",
                          "WARNING!")
            self.cb_google.SetValue(False)
        event.Skip()

    def translate(self, event):
        self.tc_destination.Clear()
        for i, line in enumerate(self.tc_source.GetValue().split('\n')):
            if (self.cb_translation.GetCurrentSelection() == 0 and
                    self.tc_source.GetValue()):
                if not self.cb_google.GetValue():
                    self.tc_destination.AppendText(unicode_to_indica(line)+'\n')
                else:
                    pre_translate = self.gs.translate(line, 'ta')
                    self.tc_source.AppendText('\n'+pre_translate)
                    self.tc_destination.AppendText(
                        unicode_to_indica(pre_translate)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 1 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    indica_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 2 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_roman(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 3 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    roman_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 4 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_indoweb(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 5 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    indoweb_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 6 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_tscii(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 7 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    tscii_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 8 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_tab(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 9 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    tab_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 10 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_tam(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 11 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    tam_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 12 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_anjal(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 13 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    anjal_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 14 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_murasoli(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 15 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    murasoli_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 16 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_bamini(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 17 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    bamini_to_unicode(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 18 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    unicode_to_shreelipi(' ' + line)+'\n')
            elif (self.cb_translation.GetCurrentSelection() == 19 and
                    self.tc_source.GetValue()):
                self.tc_destination.AppendText(
                    shreelipi_to_unicode(' ' + line)+'\n')
        event.Skip()

def main():
    app = wx.App(False)
    appFrm = Tats(None)
    appFrm.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()