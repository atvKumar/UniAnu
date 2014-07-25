# -*- coding: utf-8 -*-
from string import punctuation, whitespace, digits


def convertTounicode(source_text, filtered=False, debug=False):
    translated = source_text
    
    translated = translated.replace(u"Ã‚Â¶", u"அ")
    translated = translated.replace(u"g", u"ஆ")
    translated = translated.replace(u"Ãƒâ€“", u"இ")
    translated = translated.replace(u"~", u"ஈ")
    translated = translated.replace(u"c", u"உ")
    translated = translated.replace(u"Ã‚Â»", u"ஊ")
    translated = translated.replace(u"Ã‚Â¨", u"எ")
    translated = translated.replace(u"Ã‚Â°", u"ஏ")
    translated = translated.replace(u"n", u"ஐ")
    translated = translated.replace(u"ÃƒÅ½", u"ஒ")
    translated = translated.replace(u"{", u"ஓ")
    translated = translated.replace(u"ÃƒÅ½e", u"ஔ")
    translated = translated.replace(u"ÃƒÂ ", u"ஃ")
    translated = translated.replace(u"--", u"ௐ")
    translated = translated.replace(u"p", u"ஸ்ரீ")
    
    translated = translated.replace(u"Ãƒâ€š", u"க்")
    translated = translated.replace(u"ÃƒËœÃƒÂ¯e", u"கௌ")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ¯V", u"கோ")
    translated = translated.replace(u"ÃƒËœÃƒÂ¯V", u"கொ")
    translated = translated.replace(u"ÃƒÂ§ÃƒÂ¯", u"கை")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ¯", u"கே")
    translated = translated.replace(u"ÃƒËœÃƒÂ¯", u"கெ")
    translated = translated.replace(u"ÃƒÂ­", u"கூ")
    translated = translated.replace(u"z", u"கு")
    translated = translated.replace(u"ÃƒÂ¿", u"கீ")
    translated = translated.replace(u"ÃƒÂ¾", u"கி")
    translated = translated.replace(u"ÃƒÂ¯V", u"கா")
    translated = translated.replace(u"ÃƒÂ¯", u"க")
    
    translated = translated.replace(u"Ã‚Âº", u"ங்")
    translated = translated.replace(u"ÃƒËœÃƒÂ´e", u"ஙௌ")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ´V", u"ஙோ")
    translated = translated.replace(u"ÃƒËœÃƒÂ´V", u"ஙொ")
    translated = translated.replace(u"ÃƒÂ§ÃƒÂ´", u"ஙை")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ´", u"ஙே")
    translated = translated.replace(u"ÃƒËœÃƒÂ´", u"ஙெ")
    translated = translated.replace(u"dd", u"ஙூ")
    translated = translated.replace(u"dd", u"ஙு")
    translated = translated.replace(u"dd", u"ஙீ")
    translated = translated.replace(u"dd", u"ஙி")
    translated = translated.replace(u"ÃƒÂ´V", u"ஙா")
    translated = translated.replace(u"ÃƒÂ´", u"ங")
    
    translated = translated.replace(u"ÃƒÅ¸", u"ச்")
    translated = translated.replace(u"ÃƒËœÃƒâ€že", u"சௌ")
    translated = translated.replace(u"Ã‚Â¼Ãƒâ€žV", u"சோ")
    translated = translated.replace(u"ÃƒËœÃƒâ€žV", u"சொ")
    translated = translated.replace(u"ÃƒÂ§Ãƒâ€ž", u"சை")
    translated = translated.replace(u"Ã‚Â¼Ãƒâ€ž", u"சே")
    translated = translated.replace(u"ÃƒËœÃƒâ€ž", u"செ")
    translated = translated.replace(u"ÃƒÂ³", u"சூ")
    translated = translated.replace(u"Ã‚Â·", u"சு")
    translated = translated.replace(u"ÃƒÂ¦", u"சீ")
    translated = translated.replace(u"E", u"சி")
    translated = translated.replace(u"Ãƒâ€žV", u"சா")
    translated = translated.replace(u"Ãƒâ€ž", u"ச")
    
    translated = translated.replace(u"ÃƒÂ«", u"ஜ்")
    translated = translated.replace(u"ÃƒËœÃƒâ€ºe", u"ஜௌ")
    translated = translated.replace(u"Ã‚Â¼Ãƒâ€ºV", u"ஜோ")
    translated = translated.replace(u"ÃƒËœÃƒâ€ºV", u"ஜொ")
    translated = translated.replace(u"ÃƒÂ§Ãƒâ€º", u"ஜை")
    translated = translated.replace(u"Ã‚Â¼Ãƒâ€º", u"ஜே")
    translated = translated.replace(u"ÃƒËœÃƒâ€º", u"ஜெ")
    translated = translated.replace(u"Ãƒâ€°", u"ஜூ")
    translated = translated.replace(u"h", u"ஜு")
    translated = translated.replace(u"ÃƒÂ½", u"ஜீ")
    translated = translated.replace(u"ÃƒÂ·", u"ஜி")
    translated = translated.replace(u"Ãƒâ€ºV", u"ஜா")
    translated = translated.replace(u"Ãƒâ€º", u"ஜ")
    
    translated = translated.replace(u"ÃƒÅ¾", u"ஞ்")
    translated = translated.replace(u"ÃƒËœQe", u"ஞௌ")
    translated = translated.replace(u"Ã‚Â¼QV", u"ஞோ")
    translated = translated.replace(u"ÃƒËœQV", u"ஞொ")
    translated = translated.replace(u"ÃƒÂ§Q", u"ஞை")
    translated = translated.replace(u"Ã‚Â¼Q", u"ஞே")
    translated = translated.replace(u"ÃƒËœQ", u"ஞெ")
    translated = translated.replace(u"dd", u"ஞூ")
    translated = translated.replace(u"dd", u"ஞு")
    translated = translated.replace(u"dd", u"ஞீ")
    translated = translated.replace(u"dd", u"ஞி")
    translated = translated.replace(u"QV", u"ஞா")
    translated = translated.replace(u"Q", u"ஞ")
    
    translated = translated.replace(u"ÃƒÂ¢", u"ட்")
    translated = translated.replace(u"ÃƒËœÃ‚Â¦e", u"டௌ")
    translated = translated.replace(u"Ã‚Â¼Ã‚Â¦V", u"டோ")
    translated = translated.replace(u"ÃƒËœÃ‚Â¦V", u"டொ")
    translated = translated.replace(u"ÃƒÂ§Ã‚Â¦", u"டை")
    translated = translated.replace(u"Ã‚Â¼Ã‚Â¦", u"டே")
    translated = translated.replace(u"ÃƒËœÃ‚Â¦", u"டெ")
    translated = translated.replace(u"ÃƒÂ¹", u"டூ")
    translated = translated.replace(u"|", u"டு")
    translated = translated.replace(u"Ãƒ", u"டீ")
    translated = translated.replace(u"Ã‚Â½", u"டி")
    translated = translated.replace(u"Ã‚Â¦V", u"டா")
    translated = translated.replace(u"Ã‚Â¦", u"ட")
    
    translated = translated.replace(u"ÃƒÂµ", u"ண்")
    translated = translated.replace(u"ÃƒËœÃƒÂ°e", u"ணௌ")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ°V", u"ணோ")
    translated = translated.replace(u"ÃƒËœÃƒÂ°V", u"ணொ")
    translated = translated.replace(u"ÃƒÂ§ÃƒÂ°", u"ணை")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ°", u"ணே")
    translated = translated.replace(u"ÃƒËœÃƒÂ°", u"ணெ")
    translated = translated.replace(u"dd", u"ணூ")
    translated = translated.replace(u"b", u"ணு")
    translated = translated.replace(u"Ã‚Â§", u"ணீ")
    translated = translated.replace(u"ÃƒÂ¨", u"ணி")
    translated = translated.replace(u"ÃƒÂ°V", u"ணா")
    translated = translated.replace(u"ÃƒÂ°", u"ண")
    
    translated = translated.replace(u"Ãƒ", u"த்")
    translated = translated.replace(u"ÃƒËœ>e", u"தௌ")
    translated = translated.replace(u"Ã‚Â¼>V", u"தோ")
    translated = translated.replace(u"ÃƒËœ>V", u"தொ")
    translated = translated.replace(u"ÃƒÂ§>", u"தை")
    translated = translated.replace(u"Ã‚Â¼>", u"தே")
    translated = translated.replace(u"ÃƒËœ>", u"தெ")
    translated = translated.replace(u"#", u"தூ")
    translated = translated.replace(u"m", u"து")
    translated = translated.replace(u"y", u"தீ")
    translated = translated.replace(u"]", u"தி")
    translated = translated.replace(u">V", u"தா")
    translated = translated.replace(u">", u"த")
    
    translated = translated.replace(u"Ãƒ", u"ந்")
    translated = translated.replace(u"ÃƒËœÃƒÂ¥e", u"நௌ")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ¥V", u"நோ")
    translated = translated.replace(u"ÃƒËœÃƒÂ¥V", u"நொ")
    translated = translated.replace(u"ÃƒÂ§ÃƒÂ¥", u"நை")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ¥", u"நே")
    translated = translated.replace(u"ÃƒËœÃƒÂ¥", u"நெ")
    translated = translated.replace(u"Ã‚Â±", u"நூ")
    translated = translated.replace(u"O", u"நு")
    translated = translated.replace(u"Ãƒâ‚¬", u"நீ")
    translated = translated.replace(u"W", u"நி")
    translated = translated.replace(u"ÃƒÂ¥V", u"நா")
    translated = translated.replace(u"ÃƒÂ¥", u"ந")
    
    translated = translated.replace(u"[", u"ன்")
    translated = translated.replace(u"ÃƒËœÃ‚Âªe", u"னௌ")
    translated = translated.replace(u"Ã‚Â¼Ã‚ÂªV", u"னோ")
    translated = translated.replace(u"ÃƒËœÃ‚ÂªV", u"னொ")
    translated = translated.replace(u"ÃƒÂ§Ã‚Âª", u"னை")
    translated = translated.replace(u"Ã‚Â¼Ã‚Âª", u"னே")
    translated = translated.replace(u"ÃƒËœÃ‚Âª", u"னெ")
    translated = translated.replace(u"ÃƒÂ»", u"னூ")
    translated = translated.replace(u"Ãƒ", u"னு")
    translated = translated.replace(u"ÃƒÅ’", u"னீ")
    translated = translated.replace(u"M", u"னி")
    translated = translated.replace(u"Ã‚ÂªV", u"னா")
    translated = translated.replace(u"Ã‚Âª", u"ன")
    
    translated = translated.replace(u"Ã‚Â©", u"ப்")
    translated = translated.replace(u"ÃƒËœÃƒÆ’e", u"பௌ")
    translated = translated.replace(u"Ã‚Â¼ÃƒÆ’V", u"போ")
    translated = translated.replace(u"ÃƒËœÃƒÆ’V", u"பொ")
    translated = translated.replace(u"ÃƒÂ§ÃƒÆ’", u"பை")
    translated = translated.replace(u"Ã‚Â¼ÃƒÆ’", u"பே")
    translated = translated.replace(u"ÃƒËœÃƒÆ’", u"பெ")
    translated = translated.replace(u"Ã‚Â¯", u"பூ")
    translated = translated.replace(u"A", u"பு")
    translated = translated.replace(u"Ã‚Â¬", u"பீ")
    translated = translated.replace(u"Ã‚Â¸", u"பி")
    translated = translated.replace(u"ÃƒÆ’V", u"பா")
    translated = translated.replace(u"ÃƒÆ’", u"ப")
    
    translated = translated.replace(u"D", u"ம்")
    translated = translated.replace(u"ÃƒËœ\e", u"மௌ")
    translated = translated.replace(u"Ã‚Â¼\V", u"மோ")
    translated = translated.replace(u"ÃƒËœ\V", u"மொ")
    translated = translated.replace(u"ÃƒÂ§\\", u"மை")
    translated = translated.replace(u"Ã‚Â¼\\", u"மே")
    translated = translated.replace(u"ÃƒËœ\\", u"மெ")
    translated = translated.replace(u"J", u"மூ")
    translated = translated.replace(u"x", u"மு")
    translated = translated.replace(u"*", u"மீ")
    translated = translated.replace(u"t", u"மி")
    translated = translated.replace(u"\V", u"மா")
    translated = translated.replace(u"\\", u"ம")
    
    translated = translated.replace(u"F", u"ய்")
    translated = translated.replace(u"ÃƒËœBe", u"யௌ")
    translated = translated.replace(u"Ã‚Â¼BV", u"யோ")
    translated = translated.replace(u"ÃƒËœBV", u"யொ")
    translated = translated.replace(u"ÃƒÂ§B", u"யை")
    translated = translated.replace(u"Ã‚Â¼B", u"யே")
    translated = translated.replace(u"ÃƒËœB", u"யெ")
    translated = translated.replace(u"R", u"யூ")
    translated = translated.replace(u"Ã‚Â¥", u"யு")
    translated = translated.replace(u"X", u"யீ")
    translated = translated.replace(u"l", u"யி")
    translated = translated.replace(u"BV", u"யா")
    translated = translated.replace(u"B", u"ய")
    
    translated = translated.replace(u"ÃƒÂ¬", u"ர்")
    translated = translated.replace(u"ÃƒËœÃ‚Â«e", u"ரௌ")
    translated = translated.replace(u"Ã‚Â¼Ã‚Â«V", u"ரோ")
    translated = translated.replace(u"ÃƒËœÃ‚Â«V", u"ரொ")
    translated = translated.replace(u"ÃƒÂ§Ã‚Â«", u"ரை")
    translated = translated.replace(u"Ã‚Â¼Ã‚Â«", u"ரே")
    translated = translated.replace(u"ÃƒËœÃ‚Â«", u"ரெ")
    translated = translated.replace(u"Ãƒâ€", u"ரூ")
    translated = translated.replace(u"ÃƒÂ²", u"ரு")
    translated = translated.replace(u"Z", u"ரீ")
    translated = translated.replace(u"ÃƒÂ¶", u"ரி")
    translated = translated.replace(u"Ã‚Â«V", u"ரா")
    translated = translated.replace(u"Ã‚Â«", u"ர")
    
    translated = translated.replace(u"u", u"ற்")
    translated = translated.replace(u"ÃƒËœÃƒâ€¦e", u"றௌ")
    translated = translated.replace(u"Ã‚Â¼Ãƒâ€¦V", u"றோ")
    translated = translated.replace(u"ÃƒËœÃƒâ€¦V", u"றொ")
    translated = translated.replace(u"ÃƒÂ§Ãƒâ€¦", u"றை")
    translated = translated.replace(u"Ã‚Â¼Ãƒâ€¦", u"றே")
    translated = translated.replace(u"ÃƒËœÃ‚Â«", u"ரெ")
    translated = translated.replace(u"G", u"றூ")
    translated = translated.replace(u"Ã‚Â®", u"று")
    translated = translated.replace(u"S", u"றீ")
    translated = translated.replace(u"Ã‚Â¤", u"றி")
    translated = translated.replace(u"Ãƒâ€¦V", u"றா")
    translated = translated.replace(u"Ãƒâ€¦", u"ற")
    
    translated = translated.replace(u"_", u"ல்")
    translated = translated.replace(u"ÃƒËœÃƒÂ©e", u"லௌ")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ©V", u"லோ")
    translated = translated.replace(u"ÃƒËœÃƒÂ©V", u"லொ")
    translated = translated.replace(u"ÃƒÂ§ÃƒÂ©", u"லை")
    translated = translated.replace(u"Ã‚Â¼ÃƒÂ©", u"லே")
    translated = translated.replace(u"ÃƒËœÃƒÂ©", u"லெ")
    translated = translated.replace(u"Ãƒâ„¢", u"லூ")
    translated = translated.replace(u"K", u"லு")
    translated = translated.replace(u"ÃƒÅ“", u"லீ")
    translated = translated.replace(u"o", u"லி")
    translated = translated.replace(u"ÃƒÂ©V", u"லா")
    translated = translated.replace(u"ÃƒÂ©", u"ல")
    
    translated = translated.replace(u"^", u"ள்")
    translated = translated.replace(u"ÃƒËœee", u"ளௌ")
    translated = translated.replace(u"Ã‚Â¼eV", u"ளோ")
    translated = translated.replace(u"ÃƒËœeV", u"ளொ")
    translated = translated.replace(u"ÃƒÂ§e", u"ளை")
    translated = translated.replace(u"Ã‚Â¼e", u"ளே")
    translated = translated.replace(u"ÃƒËœe", u"ளெ")
    translated = translated.replace(u"j", u"ளூ")
    translated = translated.replace(u"Ãƒâ€œ", u"ளு")
    translated = translated.replace(u"C", u"ளீ")
    translated = translated.replace(u"Ã‚Â¹", u"ளி")
    translated = translated.replace(u"eV", u"ளா")
    translated = translated.replace(u"e", u"ள")
    
    translated = translated.replace(u"Ã‚Âµ", u"ழ்")
    translated = translated.replace(u"ÃƒËœwe", u"ழௌ")
    translated = translated.replace(u"Ã‚Â¼wV", u"ழோ")
    translated = translated.replace(u"ÃƒËœwV", u"ழொ")
    translated = translated.replace(u"ÃƒÂ§w", u"ழை")
    translated = translated.replace(u"Ã‚Â¼w", u"ழே")
    translated = translated.replace(u"ÃƒËœw", u"ழெ")
    translated = translated.replace(u"ÃƒÂ±", u"ழூ")
    translated = translated.replace(u"Ã‚Â¿", u"ழு")
    translated = translated.replace(u"Ãƒâ€˜", u"ழீ")
    translated = translated.replace(u"a", u"ழி")
    translated = translated.replace(u"wV", u"ழா")
    translated = translated.replace(u"w", u"ழ")
    
    translated = translated.replace(u"Ãƒâ€¹", u"வ்")
    translated = translated.replace(u"ÃƒËœke", u"வௌ")
    translated = translated.replace(u"Ã‚Â¼kV", u"வோ")
    translated = translated.replace(u"ÃƒËœkV", u"வொ")
    translated = translated.replace(u"ÃƒÂ§k", u"வை")
    translated = translated.replace(u"Ã‚Â¼k", u"வே")
    translated = translated.replace(u"ÃƒËœk", u"வெ")
    translated = translated.replace(u"Ãƒâ€ ", u"வூ")
    translated = translated.replace(u"Ã‚Â¡", u"வு")
    translated = translated.replace(u"T", u"வீ")
    translated = translated.replace(u"s", u"வி")
    translated = translated.replace(u"kV", u"வா")
    translated = translated.replace(u"k", u"வ")
    
    translated = translated.replace(u"i", u"ஷ்")
    translated = translated.replace(u"ÃƒËœre", u"ஷௌ")
    translated = translated.replace(u"Ã‚Â¼rV", u"ஷோ")
    translated = translated.replace(u"ÃƒËœrV", u"ஷொ")
    translated = translated.replace(u"ÃƒÂ§r", u"ஷை")
    translated = translated.replace(u"Ã‚Â¼r", u"ஷே")
    translated = translated.replace(u"ÃƒËœr", u"ஷெ")
    translated = translated.replace(u"Ã‚Â£", u"ஷூ")
    translated = translated.replace(u"Ãƒâ€”", u"ஷு")
    translated = translated.replace(u"U", u"ஷீ")
    translated = translated.replace(u"Ã‚Â´", u"ஷி")
    translated = translated.replace(u"rV", u"ஷா")
    translated = translated.replace(u"r", u"ஷ")
    
    translated = translated.replace(u"ÃƒÂ¼", u"ஸ்")
    translated = translated.replace(u"ÃƒËœve", u"ஸௌ")
    translated = translated.replace(u"Ã‚Â¼vV", u"ஸோ")
    translated = translated.replace(u"ÃƒËœvV", u"ஸொ")
    translated = translated.replace(u"ÃƒÂ§v", u"ஸை")
    translated = translated.replace(u"Ã‚Â¼v", u"ஸே")
    translated = translated.replace(u"ÃƒËœv", u"ஸெ")
    translated = translated.replace(u"`", u"ஸூ")
    translated = translated.replace(u"q", u"ஸு")
    translated = translated.replace(u"Ã‚Â¢", u"ஸீ")
    translated = translated.replace(u"L", u"ஸி")
    translated = translated.replace(u"vV", u"ஸா")
    translated = translated.replace(u"v", u"ஸ")
    
    translated = translated.replace(u"ÃƒÂ£", u"ஹ்")
    translated = translated.replace(u"ÃƒËœÃƒâ€¡e", u"ஹௌ")
    translated = translated.replace(u"Ã‚Â¼Ãƒâ€¡V", u"ஹோ")
    translated = translated.replace(u"ÃƒËœÃƒâ€¡V", u"ஹொ")
    translated = translated.replace(u"ÃƒÂ§Ãƒâ€¡", u"ஹை")
    translated = translated.replace(u"Ã‚Â¼Ãƒâ€¡", u"ஹே")
    translated = translated.replace(u"ÃƒËœÃƒâ€¡", u"ஹெ")
    translated = translated.replace(u"ÃƒÂª", u"ஹீ")
    translated = translated.replace(u"N", u"ஹி")
    translated = translated.replace(u"Ãƒâ€¡V", u"ஹா")
    translated = translated.replace(u"Ãƒâ€¡", u"ஹ")

    translated = translated.replace(u"Ãƒâ€¢", u"க்ஷ்")
    translated = translated.replace(u"ÃƒËœÃ‚Â³e", u"க்ஷௌ")
    translated = translated.replace(u"Ã‚Â¼Ã‚Â³V", u"க்ஷோ")
    translated = translated.replace(u"ÃƒËœÃ‚Â³V", u"க்ஷொ")
    translated = translated.replace(u"ÃƒÂ§Ã‚Â³", u"க்ஷை")
    translated = translated.replace(u"Ã‚Â¼Ã‚Â³", u"க்ஷே")
    translated = translated.replace(u"ÃƒËœÃ‚Â³", u"க்ஷெ")
    translated = translated.replace(u"f", u"க்ஷூ")
    translated = translated.replace(u"Y", u"க்ஷு")
    translated = translated.replace(u"ÃƒË†", u"க்ஷீ")
    translated = translated.replace(u"H", u"க்ஷி")
    translated = translated.replace(u"Ã‚Â³V", u"க்ஷா")
    translated = translated.replace(u"Ã‚Â³", u"க்ஷ")
    
    unconverted = [i for i in translated if i in source_text and not i in
                    punctuation+whitespace+digits]
    translated_trimed = ''.join([i for i in translated if not i in unconverted])

    if debug:
        return unconverted
    elif filtered:
        return translated_trimed
    else:
        return translated