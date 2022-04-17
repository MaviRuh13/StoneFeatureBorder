// Arat:
	def AppendMetinInformation(self):
		affectType, affectValue = item.GetAffect(0)
		#affectType = item.GetValue(0)
		#affectValue = item.GetValue(1)

		affectString = self.__GetAffectString(affectType, affectValue)

		if affectString:
			self.AppendSpace(5)
			self.AppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))

// Değiştir:
	def AppendMetinInformation(self):
		for i in xrange(item.ITEM_APPLY_MAX_NUM):
			(affectType, affectValue) = item.GetAffect(i)
			affectString = self.__GetAffectString(affectType, affectValue)
			if affectString:
				self.AppendSpace(5)
				self.AppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))

// Arat:
			elif itemIndex!=constInfo.ERROR_METIN_STONE:
				affectType, affectValue = item.GetAffect(0)
				affectString = self.__GetAffectString(affectType, affectValue)
				if affectString:
					affectTextLine.SetText(affectString)
			else:
				affectTextLine.SetText(localeInfo.TOOLTIP_APPLY_NOAFFECT)

// Değiştir:
			elif itemIndex!=constInfo.ERROR_METIN_STONE:
				for i in xrange(item.ITEM_APPLY_MAX_NUM):
					(affectType, affectValue) = item.GetAffect(i)
					affectString = self.__GetAffectString(affectType, affectValue)
					if affectString:
						self.AppendSpace(20)
						self.MaviRuhAppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))
			else:
				affectTextLine.SetText(localeInfo.TOOLTIP_APPLY_NOAFFECT)

// Arat:
	def AppendTextLine(self, text, color = FONT_COLOR, centerAlign = True):

// Üstüne Ekle:
	def MaviRuhAppendTextLine(self, text, color = FONT_COLOR, centerAlign = True):
		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(self.defFontName)
		textLine.SetPackedFontColor(color)
		textLine.SetText(text)
		textLine.SetOutline()
		textLine.SetFeather(False)
		textLine.Show()

		if centerAlign:
			textLine.SetPosition(52, self.toolTipHeight)

		else:
			textLine.SetPosition(10, self.toolTipHeight)

		self.childrenList.append(textLine)

		self.childrenList.append(textLine)
		self.ResizeToolTip()

		return textLine