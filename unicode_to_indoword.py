# -*- coding: utf-8 -*-
from string import punctuation, whitespace, digits


def convertToindoweb(source_text, filtered=False, debug=False):
    translated = source_text

    translated = translated.replace(u"பு", u"μ")
    translated = translated.replace(u"ர்", u"õÐ")
    # translated = translated.replace(u"ர்", u"èÐ")  # Added
    translated = translated.replace(u"ரீ", u"õ©")
    # translated = translated.replace(u"ரீ", u"è©")  # Added
    translated = translated.replace(u"ரி", u"õ¨")
    # translated = translated.replace(u"ரி", u"¨è")  # Added
    
    translated = translated.replace(u"அ", u"í")
    translated = translated.replace(u"ஆ", u"Í")
    translated = translated.replace(u"இ", u"¬")
    translated = translated.replace(u"ஈ", u"¼")
    translated = translated.replace(u"உ", u"ã")
    translated = translated.replace(u"ஊ", u"Ã")
    translated = translated.replace(u"எ", u"ö")
    translated = translated.replace(u"ஏ", u"Ö")
    translated = translated.replace(u"ஐ", u"É")
    translated = translated.replace(u"ஒ", u"ø")
    translated = translated.replace(u"ஓ", u"Ø")
    translated = translated.replace(u"ஔ", u"øó")
    translated = translated.replace(u"ஃ", u"þ")
    translated = translated.replace(u"ௐ", u"ØÐ")
    translated = translated.replace(u"ஸ்ரீ", u"¤")
    
    translated = translated.replace(u"க்", u"æÐ")
    translated = translated.replace(u"கௌ", u"âæó")
    translated = translated.replace(u"கோ", u"îæè")
    translated = translated.replace(u"கொ", u"âæè")
    translated = translated.replace(u"கை", u"éæ")
    translated = translated.replace(u"கே", u"îæ")
    translated = translated.replace(u"கெ", u"âæ")
    translated = translated.replace(u"கூ", u"Ô")
    translated = translated.replace(u"கு", u"Æ")
    translated = translated.replace(u"கீ", u"æ©")
    translated = translated.replace(u"கி", u"æ¨")
    translated = translated.replace(u"கா", u"æè")
    translated = translated.replace(u"க", u"æ")
    
    translated = translated.replace(u"ங்", u"§Ð")
    translated = translated.replace(u"ஙௌ", u"â§ó")
    translated = translated.replace(u"ஙோ", u"î§è")
    translated = translated.replace(u"ஙொ", u"â§è")
    translated = translated.replace(u"ஙை", u"é§")
    translated = translated.replace(u"ஙே", u"î§")
    translated = translated.replace(u"ஙெ", u"â§")
    translated = translated.replace(u"ஙூ", u"º")
    translated = translated.replace(u"ஙு", u"³")
    translated = translated.replace(u"ஙீ", u"§©")
    translated = translated.replace(u"ஙி", u"§¨")
    translated = translated.replace(u"ஙா", u"§è")
    translated = translated.replace(u"ங", u"§")
    
    translated = translated.replace(u"ச்", u"òÐ")
    translated = translated.replace(u"சௌ", u"âòó")
    translated = translated.replace(u"சோ", u"îòè")
    translated = translated.replace(u"சொ", u"âòè")
    translated = translated.replace(u"சை", u"éò")
    translated = translated.replace(u"சே", u"îò")
    translated = translated.replace(u"செ", u"âò")
    translated = translated.replace(u"சூ", u"Î")
    translated = translated.replace(u"சு", u"à")
    translated = translated.replace(u"சீ", u"ò©")
    translated = translated.replace(u"சி", u"ò¨")
    translated = translated.replace(u"சா", u"òè")
    translated = translated.replace(u"ச", u"ò")
    
    translated = translated.replace(u"ஜ்", u"£Ð")
    translated = translated.replace(u"ஜௌ", u"â£ó")
    translated = translated.replace(u"ஜோ", u"î£è")
    translated = translated.replace(u"ஜொ", u"â£è")
    translated = translated.replace(u"ஜை", u"é£")
    translated = translated.replace(u"ஜே", u"î£")
    translated = translated.replace(u"ஜெ", u"â£")
    translated = translated.replace(u"ஜூ", u"£ð")
    translated = translated.replace(u"ஜு", u"£¦")
    translated = translated.replace(u"ஜீ", u"£©")
    translated = translated.replace(u"ஜி", u"£¨")
    translated = translated.replace(u"ஜா", u"£è")
    translated = translated.replace(u"ஜ", u"£")
    
    translated = translated.replace(u"ஞ்", u"¢Ð")
    translated = translated.replace(u"ஞௌ", u"â¢ó")
    translated = translated.replace(u"ஞோ", u"î¢è")
    translated = translated.replace(u"ஞொ", u"â¢è")
    translated = translated.replace(u"ஞை", u"é¢")
    translated = translated.replace(u"ஞே", u"î¢")
    translated = translated.replace(u"ஞெ", u"â¢")
    translated = translated.replace(u"ஞூ", u"»")
    translated = translated.replace(u"ஞு", u"ü")
    translated = translated.replace(u"ஞீ", u"¢©")
    translated = translated.replace(u"ஞி", u"¢¨")
    translated = translated.replace(u"ஞா", u"¢è")
    translated = translated.replace(u"ஞ", u"¢")
    
    translated = translated.replace(u"ட்", u"ìÐ")
    translated = translated.replace(u"டௌ", u"âìó")
    translated = translated.replace(u"டோ", u"îìè")
    translated = translated.replace(u"டொ", u"âìè")
    translated = translated.replace(u"டை", u"éì")
    translated = translated.replace(u"டே", u"îì")
    translated = translated.replace(u"டெ", u"âì")
    translated = translated.replace(u"டூ", u"Þ")
    translated = translated.replace(u"டு", u"Ì")
    translated = translated.replace(u"டீ", u"Ï")
    translated = translated.replace(u"டி", u"ï")
    translated = translated.replace(u"டா", u"ìè")
    translated = translated.replace(u"ட", u"ì")
    
    translated = translated.replace(u"ண்", u"úª")
    translated = translated.replace(u"ணௌ", u"âúó")
    translated = translated.replace(u"ணோ", u"îúè")
    translated = translated.replace(u"ணொ", u"âúè")
    translated = translated.replace(u"ணை", u"éú")
    translated = translated.replace(u"ணே", u"îú")
    translated = translated.replace(u"ணெ", u"âú")
    translated = translated.replace(u"ணூ", u"½")
    translated = translated.replace(u"ணு", u"Ñ")
    translated = translated.replace(u"ணீ", u"ú©")
    translated = translated.replace(u"ணி", u"ú¨")
    translated = translated.replace(u"ணா", u"úè")
    translated = translated.replace(u"ண", u"ú")
    
    translated = translated.replace(u"த்", u"êÐ")
    translated = translated.replace(u"தௌ", u"âêó")
    translated = translated.replace(u"தோ", u"îêè")
    translated = translated.replace(u"தொ", u"âêè")
    translated = translated.replace(u"தை", u"éê")
    translated = translated.replace(u"தே", u"îê")
    translated = translated.replace(u"தெ", u"âê")
    translated = translated.replace(u"தூ", u"œ")
    translated = translated.replace(u"து", u"Ê")
    translated = translated.replace(u"தீ", u"ê©")
    translated = translated.replace(u"தி", u"ê¨")
    translated = translated.replace(u"தா", u"êè")
    translated = translated.replace(u"த", u"ê")
    
    translated = translated.replace(u"ந்", u"åÐ")
    translated = translated.replace(u"நௌ", u"âåó")
    translated = translated.replace(u"நோ", u"îåè")
    translated = translated.replace(u"நொ", u"âåè")
    translated = translated.replace(u"நை", u"éå")
    translated = translated.replace(u"நே", u"îå")
    translated = translated.replace(u"நெ", u"âå")
    translated = translated.replace(u"நூ", u"¿")
    translated = translated.replace(u"நு", u"Å")
    translated = translated.replace(u"நீ", u"å©")
    translated = translated.replace(u"நி", u"å¨")
    translated = translated.replace(u"நா", u"åè")
    translated = translated.replace(u"ந", u"å")
    
    translated = translated.replace(u"ன்", u"äª")
    translated = translated.replace(u"னௌ", u"âäó")
    translated = translated.replace(u"னோ", u"îäè")
    translated = translated.replace(u"னொ", u"âäè")
    translated = translated.replace(u"னை", u"éä")
    translated = translated.replace(u"னே", u"îä")
    translated = translated.replace(u"னெ", u"âä")
    translated = translated.replace(u"னூ", u"Û")
    translated = translated.replace(u"னு", u"Ä")
    translated = translated.replace(u"னீ", u"ä©")
    translated = translated.replace(u"னி", u"ä¨")
    translated = translated.replace(u"னா", u"äè")
    translated = translated.replace(u"ன", u"ä")
    
    translated = translated.replace(u"ப்", u"çÐ")
    translated = translated.replace(u"பௌ", u"âçó")
    translated = translated.replace(u"போ", u"îçè")
    translated = translated.replace(u"பொ", u"âçè")
    translated = translated.replace(u"பை", u"éç")
    translated = translated.replace(u"பே", u"îç")
    translated = translated.replace(u"பெ", u"âç")
    translated = translated.replace(u"பூ", u"—")
    translated = translated.replace(u"பு", u"µ")
    translated = translated.replace(u"பீ", u"ç©")
    translated = translated.replace(u"பி", u"ç¨")
    translated = translated.replace(u"பா", u"çè")
    translated = translated.replace(u"ப", u"ç")
    
    translated = translated.replace(u"ம்", u"ëÐ")
    translated = translated.replace(u"மௌ", u"âëó")
    translated = translated.replace(u"மோ", u"îëè")
    translated = translated.replace(u"மொ", u"âëè")
    translated = translated.replace(u"மை", u"éë")
    translated = translated.replace(u"மே", u"îë")
    translated = translated.replace(u"மெ", u"âë")
    translated = translated.replace(u"மூ", u"ß")
    translated = translated.replace(u"மு", u"Ë")
    translated = translated.replace(u"மீ", u"ë©")
    translated = translated.replace(u"மி", u"ë¨")
    translated = translated.replace(u"மா", u"ëè")
    translated = translated.replace(u"ம", u"ë")
    
    translated = translated.replace(u"ய்", u"áÐ")
    translated = translated.replace(u"யௌ", u"âáó")
    translated = translated.replace(u"யோ", u"îáè")
    translated = translated.replace(u"யொ", u"âáè")
    translated = translated.replace(u"யை", u"éá")
    translated = translated.replace(u"யே", u"îá")
    translated = translated.replace(u"யெ", u"âá")
    translated = translated.replace(u"யூ", u"¹")
    translated = translated.replace(u"யு", u"±")
    translated = translated.replace(u"யீ", u"á©")
    translated = translated.replace(u"யி", u"á¨")
    translated = translated.replace(u"யா", u"áè")
    translated = translated.replace(u"ய", u"á")
    

    translated = translated.replace(u"ரௌ", u"âõó")
    translated = translated.replace(u"ரோ", u"îõè")
    translated = translated.replace(u"ரொ", u"âõè")
    translated = translated.replace(u"ரை", u"éõ")
    translated = translated.replace(u"ரே", u"îõ")
    translated = translated.replace(u"ரெ", u"âõ")
    translated = translated.replace(u"ரூ", u"¥")
    translated = translated.replace(u"ரு", u"Õ")

    translated = translated.replace(u"ரா", u"õè")
    translated = translated.replace(u"ர", u"õ")
    
    translated = translated.replace(u"ற்", u"÷Ð")
    translated = translated.replace(u"றௌ", u"â÷ó")
    translated = translated.replace(u"றோ", u"î÷è")
    translated = translated.replace(u"றொ", u"â÷è")
    translated = translated.replace(u"றை", u"é÷")
    translated = translated.replace(u"றே", u"î÷")
    translated = translated.replace(u"ரெ", u"âõ")
    translated = translated.replace(u"றூ", u"®")
    translated = translated.replace(u"று", u"×")
    translated = translated.replace(u"றீ", u"÷©")
    translated = translated.replace(u"றி", u"÷¨")
    translated = translated.replace(u"றா", u"÷è")
    translated = translated.replace(u"ற", u"÷")
    
    translated = translated.replace(u"ல்", u"ùÐ")
    translated = translated.replace(u"லௌ", u"âùó")
    translated = translated.replace(u"லோ", u"îùè")
    translated = translated.replace(u"லொ", u"âùè")
    translated = translated.replace(u"லை", u"éù")
    translated = translated.replace(u"லே", u"îù")
    translated = translated.replace(u"லெ", u"âù")
    translated = translated.replace(u"லூ", u"û")
    translated = translated.replace(u"லு", u"Ù")
    translated = translated.replace(u"லீ", u"ù©")
    translated = translated.replace(u"லி", u"ù¨")
    translated = translated.replace(u"லா", u"ùè")
    translated = translated.replace(u"ல", u"ù")
    
    translated = translated.replace(u"ள்", u"óª")
    translated = translated.replace(u"ளௌ", u"âóó")
    translated = translated.replace(u"ளோ", u"îóè")
    translated = translated.replace(u"ளொ", u"âóè")
    translated = translated.replace(u"ளை", u"éó")
    translated = translated.replace(u"ளே", u"îó")
    translated = translated.replace(u"ளெ", u"âó")
    translated = translated.replace(u"ளூ", u"ñ")
    translated = translated.replace(u"ளு", u"Ó")
    translated = translated.replace(u"ளீ", u"ó©")
    translated = translated.replace(u"ளி", u"ó¨")
    translated = translated.replace(u"ளா", u"óè")
    translated = translated.replace(u"ள", u"ó")
    
    translated = translated.replace(u"ழ்", u"ÈÐ")
    translated = translated.replace(u"ழௌ", u"âÈó")
    translated = translated.replace(u"ழோ", u"îÈè")
    translated = translated.replace(u"ழொ", u"âÈè")
    translated = translated.replace(u"ழை", u"éÈ")
    translated = translated.replace(u"ழே", u"îÈ")
    translated = translated.replace(u"ழெ", u"âÈ")
    translated = translated.replace(u"ழூ", u"¾")
    translated = translated.replace(u"ழு", u"Ç")
    translated = translated.replace(u"ழீ", u"È©")
    translated = translated.replace(u"ழி", u"È¨")
    translated = translated.replace(u"ழா", u"Èè")
    translated = translated.replace(u"ழ", u"È")
    
    translated = translated.replace(u"வ்", u"ôÐ")
    translated = translated.replace(u"வௌ", u"âôó")
    translated = translated.replace(u"வோ", u"îôè")
    translated = translated.replace(u"வொ", u"âôè")
    translated = translated.replace(u"வை", u"éô")
    translated = translated.replace(u"வே", u"îô")
    translated = translated.replace(u"வெ", u"âô")
    translated = translated.replace(u"வூ", u"´")
    translated = translated.replace(u"வு", u"²")
    translated = translated.replace(u"வீ", u"ô©")
    translated = translated.replace(u"வி", u"ô¨")
    translated = translated.replace(u"வா", u"ôè")
    translated = translated.replace(u"வ", u"ô")
    
    translated = translated.replace(u"ஷ்", u"ÜÐ")
    translated = translated.replace(u"ஷௌ", u"âÜó")
    translated = translated.replace(u"ஷோ", u"îÜè")
    translated = translated.replace(u"ஷொ", u"âÜè")
    translated = translated.replace(u"ஷை", u"éÜ")
    translated = translated.replace(u"ஷே", u"îÜ")
    translated = translated.replace(u"ஷெ", u"âÜ")
    translated = translated.replace(u"ஷூ", u"Üð")
    translated = translated.replace(u"ஷு", u"Ü¦")
    translated = translated.replace(u"ஷீ", u"Ü©")
    translated = translated.replace(u"ஷி", u"Ü¨")
    translated = translated.replace(u"ஷா", u"Üè")
    translated = translated.replace(u"ஷ", u"Ü")
    
    translated = translated.replace(u"ஹ்", u"ÁÐ")
    translated = translated.replace(u"ஹௌ", u"âÁó")
    translated = translated.replace(u"ஹோ", u"îÁè")
    translated = translated.replace(u"ஹொ", u"âÁè")
    translated = translated.replace(u"ஹை", u"éÁ")
    translated = translated.replace(u"ஹே", u"îÁ")
    translated = translated.replace(u"ஹெ", u"âÁ")
    translated = translated.replace(u"ஹீ", u"Á©")
    translated = translated.replace(u"ஹி", u"Á¨")
    translated = translated.replace(u"ஹா", u"Áè")
    translated = translated.replace(u"ஹ", u"Á")

    translated = translated.replace(u"்" , u"ª")  # Added
    # translated = translated.replace(u"ி" , u"¨")  # Added
    
    unconverted = [i for i in translated if i in source_text and not i in
                    punctuation+whitespace+digits]
    translated_trimed = ''.join([i for i in translated if not i in unconverted])

    if debug:
        return ''.join(unconverted)
    elif filtered:
        return translated_trimed
    else:
        return translated