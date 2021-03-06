# -*- coding: utf-8 -*-
from string import punctuation, whitespace, digits


def convertTounicode(source_text, filtered=False, debug=False):
    translated = source_text
    # Independent Vowels
    translated = translated.replace(u"«", u"அ")
    translated = translated.replace(u"¬", u"ஆ")
    translated = translated.replace(u"­", u"இ")
    translated = translated.replace(u"®", u"ஈ")
    translated = translated.replace(u"¯", u"உ")
    translated = translated.replace(u"°", u"ஊ")
    translated = translated.replace(u"±", u"எ")
    translated = translated.replace(u"²", u"ஏ")
    translated = translated.replace(u"³", u"ஐ")
    translated = translated.replace(u"´", u"ஒ")
    translated = translated.replace(u"µ", u"ஓ")
    translated = translated.replace(u"¶", u"ஔ")
    translated = translated.replace(u"∙", u"ஃ")

    # க Family
    translated = translated.replace(u"ì", u"க்")
    translated = translated.replace(u"¦¸ª", u"கௌ")
    translated = translated.replace(u"§¸¡", u"கோ")
    translated = translated.replace(u"¦¸¡", u"கொ")
    translated = translated.replace(u"¨¸", u"கை")
    translated = translated.replace(u"§¸", u"கே")
    translated = translated.replace(u"¦¸", u"கெ")
    translated = translated.replace(u"Ü", u"கூ")
    translated = translated.replace(u"Ì", u"கு")
    translated = translated.replace(u"¸£", u"கீ")
    translated = translated.replace(u"¸¢", u"கி")
    translated = translated.replace(u"¸¡", u"கா")
    translated = translated.replace(u"¸", u"க")

    # ங Family
    translated = translated.replace(u"í", u"ங்")
    translated = translated.replace(u"¦¹ª", u"ஙௌ")
    translated = translated.replace(u"§¹¡", u"ஙோ")
    translated = translated.replace(u"¦¹¡", u"ஙொ")
    translated = translated.replace(u"¨¹", u"ஙை")
    translated = translated.replace(u"§¹", u"ஙே")
    translated = translated.replace(u"¦¹", u"ஙெ")
    translated = translated.replace(u"›", u"ஙூ")
    translated = translated.replace(u"™", u"ஙு")
    translated = translated.replace(u"¹£", u"ஙீ")
    translated = translated.replace(u"¹¢", u"ஙி")
    translated = translated.replace(u"¹¡", u"ஙா")
    translated = translated.replace(u"¹", u"ங")

    # ச Family
    translated = translated.replace(u"î", u"ச்")
    translated = translated.replace(u"¦ºª", u"சௌ")
    translated = translated.replace(u"§º¡", u"சோ")
    translated = translated.replace(u"¦º¡", u"சொ")
    translated = translated.replace(u"¨º", u"சை")
    translated = translated.replace(u"§º", u"சே")
    translated = translated.replace(u"¦º", u"செ")
    translated = translated.replace(u"Ý", u"சூ")
    translated = translated.replace(u"Í", u"சு")
    translated = translated.replace(u"º£", u"சீ")
    translated = translated.replace(u"º¢", u"சி")
    translated = translated.replace(u"º¡", u"சா")
    translated = translated.replace(u"º", u"ச")

    # ஜ Family
    translated = translated.replace(u"ˆ", u"ஜ்")
    translated = translated.replace(u"¦ƒª", u"ஜௌ")
    translated = translated.replace(u"§ƒ¡", u"ஜோ")
    translated = translated.replace(u"¦ƒ¡", u"ஜொ")
    translated = translated.replace(u"¨ƒ", u"ஜை")
    translated = translated.replace(u"§ƒ", u"ஜே")
    translated = translated.replace(u"¦ƒ", u"ஜெ")
    translated = translated.replace(u"ƒ¥", u"ஜூ")
    translated = translated.replace(u"ƒ¤", u"ஜு")
    translated = translated.replace(u"ƒ£", u"ஜீ")
    translated = translated.replace(u"ƒ¢", u"ஜி")
    translated = translated.replace(u"ƒ¡", u"ஜா")
    translated = translated.replace(u"ƒ", u"ஜ")

    # ஞ Family
    translated = translated.replace(u"ï", u"ஞ்")
    translated = translated.replace(u"¦»ª", u"ஞௌ")
    translated = translated.replace(u"§»¡", u"ஞோ")
    translated = translated.replace(u"¦»¡", u"ஞொ")
    translated = translated.replace(u"¨»", u"ஞை")
    translated = translated.replace(u"§»", u"ஞே")
    translated = translated.replace(u"¦»", u"ஞெ")
    translated = translated.replace(u"œ", u"ஞூ")
    translated = translated.replace(u"", u"ஞு")
    translated = translated.replace(u"»£", u"ஞீ")
    translated = translated.replace(u"»¢", u"ஞி")
    translated = translated.replace(u"»¡", u"ஞா")
    translated = translated.replace(u"»", u"ஞ")

    # ட Family
    translated = translated.replace(u"ð", u"ட்")
    translated = translated.replace(u"¦¼ª", u"டௌ")
    translated = translated.replace(u"§¼¡", u"டோ")
    translated = translated.replace(u"¦¼¡", u"டொ")
    translated = translated.replace(u"¨¼", u"டை")
    translated = translated.replace(u"§¼", u"டே")
    translated = translated.replace(u"¦¼", u"டெ")
    translated = translated.replace(u"Þ", u"டூ")
    translated = translated.replace(u"Î", u"டு")
    translated = translated.replace(u"Ë", u"டீ")
    translated = translated.replace(u"Ê", u"டி")
    translated = translated.replace(u"¼¡", u"டா")
    translated = translated.replace(u"¼", u"ட")

    # ண Family
    translated = translated.replace(u"ñ", u"ண்")
    translated = translated.replace(u"¦½ª", u"ணௌ")
    translated = translated.replace(u"§½¡", u"ணோ")
    translated = translated.replace(u"¦½¡", u"ணொ")
    translated = translated.replace(u"¨½", u"ணை")
    translated = translated.replace(u"§½", u"ணே")
    translated = translated.replace(u"¦½", u"ணெ")
    translated = translated.replace(u"ß", u"ணூ")
    translated = translated.replace(u"Ï", u"ணு")
    translated = translated.replace(u"½£", u"ணீ")
    translated = translated.replace(u"½¢", u"ணி")
    translated = translated.replace(u"½¡", u"ணா")
    translated = translated.replace(u"½", u"ண")

    # த Family
    translated = translated.replace(u"ò", u"த்")
    translated = translated.replace(u"¦¾ª", u"தௌ")
    translated = translated.replace(u"§¾¡", u"தோ")
    translated = translated.replace(u"¦¾¡", u"தொ")
    translated = translated.replace(u"¨¾", u"தை")
    translated = translated.replace(u"§¾", u"தே")
    translated = translated.replace(u"¦¾", u"தெ")
    translated = translated.replace(u"à", u"தூ")
    translated = translated.replace(u"Ð", u"து")
    translated = translated.replace(u"¾£", u"தீ")
    translated = translated.replace(u"¾¢", u"தி")
    translated = translated.replace(u"¾¡", u"தா")
    translated = translated.replace(u"¾", u"த")

    # ந Family
    translated = translated.replace(u"ó", u"ந்")
    translated = translated.replace(u"¦¿ª", u"நௌ")
    translated = translated.replace(u"§¿¡", u"நோ")
    translated = translated.replace(u"¦¿¡", u"நொ")
    translated = translated.replace(u"¨¿", u"நை")
    translated = translated.replace(u"§¿", u"நே")
    translated = translated.replace(u"¦¿", u"நெ")
    translated = translated.replace(u"á", u"நூ")
    translated = translated.replace(u"Ñ", u"நு")
    translated = translated.replace(u"¿£", u"நீ")
    translated = translated.replace(u"¿¢", u"நி")
    translated = translated.replace(u"¿¡", u"நா")
    translated = translated.replace(u"¿", u"ந")

    # ன Family
    translated = translated.replace(u"ý", u"ன்")
    translated = translated.replace(u"¦Éª", u"னௌ")
    translated = translated.replace(u"§É¡", u"னோ")
    translated = translated.replace(u"¦É¡", u"னொ")
    translated = translated.replace(u"¨É", u"னை")
    translated = translated.replace(u"§É", u"னே")
    translated = translated.replace(u"¦É", u"னெ")
    translated = translated.replace(u"ë", u"னூ")
    translated = translated.replace(u"Û", u"னு")
    translated = translated.replace(u"É£", u"னீ")
    translated = translated.replace(u"É¢", u"னி")
    translated = translated.replace(u"É¡", u"னா")
    translated = translated.replace(u"É", u"ன")

    # ப Family
    translated = translated.replace(u"ô", u"ப்")
    translated = translated.replace(u"¦Àª", u"பௌ")
    translated = translated.replace(u"§À¡", u"போ")
    translated = translated.replace(u"¦À¡", u"பொ")
    translated = translated.replace(u"¨À", u"பை")
    translated = translated.replace(u"§À", u"பே")
    translated = translated.replace(u"¦À", u"பெ")
    translated = translated.replace(u"â", u"பூ")
    translated = translated.replace(u"Ò", u"பு")
    translated = translated.replace(u"À£", u"பீ")
    translated = translated.replace(u"À¢", u"பி")
    translated = translated.replace(u"À¡", u"பா")
    translated = translated.replace(u"À", u"ப")

    # ம Family
    translated = translated.replace(u"õ", u"ம்")
    translated = translated.replace(u"¦Áª", u"மௌ")
    translated = translated.replace(u"§Á¡", u"மோ")
    translated = translated.replace(u"¦Á¡", u"மொ")
    translated = translated.replace(u"¨Á", u"மை")
    translated = translated.replace(u"§Á", u"மே")
    translated = translated.replace(u"¦Á", u"மெ")
    translated = translated.replace(u"ã", u"மூ")
    translated = translated.replace(u"Ó", u"மு")
    translated = translated.replace(u"Á£", u"மீ")
    translated = translated.replace(u"Á¢", u"மி")
    translated = translated.replace(u"Á¡", u"மா")
    translated = translated.replace(u"Á", u"ம")

    # ய Family
    translated = translated.replace(u"ö", u"ய்")
    translated = translated.replace(u"¦Âª", u"யௌ")
    translated = translated.replace(u"§Â¡", u"யோ")
    translated = translated.replace(u"¦Â¡", u"யொ")
    translated = translated.replace(u"¨Â", u"யை")
    translated = translated.replace(u"§Â", u"யே")
    translated = translated.replace(u"¦Â", u"யெ")
    translated = translated.replace(u"ä", u"யூ")
    translated = translated.replace(u"Ô", u"யு")
    translated = translated.replace(u"Â£", u"யீ")
    translated = translated.replace(u"Â¢", u"யி")
    translated = translated.replace(u"Â¡", u"யா")
    translated = translated.replace(u"Â", u"ய")

    # ர Family
    translated = translated.replace(u"÷", u"ர்")
    translated = translated.replace(u"¦Ãª", u"ரௌ")
    translated = translated.replace(u"§Ã¡", u"ரோ")
    translated = translated.replace(u"¦Ã¡", u"ரொ")
    translated = translated.replace(u"¨Ã", u"ரை")
    translated = translated.replace(u"§Ã", u"ரே")
    translated = translated.replace(u"¦Ã", u"ரெ")
    translated = translated.replace(u"å", u"ரூ")
    translated = translated.replace(u"Õ", u"ரு")
    translated = translated.replace(u"Ã£", u"ரீ")
    translated = translated.replace(u"Ã¢", u"ரி")
    translated = translated.replace(u"Ã¡", u"ரா")
    translated = translated.replace(u"Ã", u"ர")

    # ற Family
    translated = translated.replace(u"ü", u"ற்")
    translated = translated.replace(u"¦Èª", u"றௌ")
    translated = translated.replace(u"§È¡", u"றோ")
    translated = translated.replace(u"¦È¡", u"றொ")
    translated = translated.replace(u"¨È", u"றை")
    translated = translated.replace(u"§È", u"றே")
    translated = translated.replace(u"¦Ã", u"ரெ")
    translated = translated.replace(u"ê", u"றூ")
    translated = translated.replace(u"Ú", u"று")
    translated = translated.replace(u"È£", u"றீ")
    translated = translated.replace(u"È¢", u"றி")
    translated = translated.replace(u"È¡", u"றா")
    translated = translated.replace(u"È", u"ற")

    # ல Family
    translated = translated.replace(u"ø", u"ல்")
    translated = translated.replace(u"¦Äª", u"லௌ")
    translated = translated.replace(u"§Ä¡", u"லோ")
    translated = translated.replace(u"¦Ä¡", u"லொ")
    translated = translated.replace(u"¨Ä", u"லை")
    translated = translated.replace(u"§Ä", u"லே")
    translated = translated.replace(u"¦Ä", u"லெ")
    translated = translated.replace(u"æ", u"லூ")
    translated = translated.replace(u"Ö", u"லு")
    translated = translated.replace(u"Ä£", u"லீ")
    translated = translated.replace(u"Ä¢", u"லி")
    translated = translated.replace(u"Ä¡", u"லா")
    translated = translated.replace(u"Ä", u"ல")

    # ள Family
    translated = translated.replace(u"û", u"ள்")
    translated = translated.replace(u"¦Çª", u"ளௌ")
    translated = translated.replace(u"§Ç¡", u"ளோ")
    translated = translated.replace(u"¦Ç¡", u"ளொ")
    translated = translated.replace(u"¨Ç", u"ளை")
    translated = translated.replace(u"§Ç", u"ளே")
    translated = translated.replace(u"¦Ç", u"ளெ")
    translated = translated.replace(u"é", u"ளூ")
    translated = translated.replace(u"Ù", u"ளு")
    translated = translated.replace(u"Ç£", u"ளீ")
    translated = translated.replace(u"Ç¢", u"ளி")
    translated = translated.replace(u"Ç¡", u"ளா")
    translated = translated.replace(u"Ç", u"ள")

    # ழ Family
    translated = translated.replace(u"ú", u"ழ்")
    translated = translated.replace(u"¦Æª", u"ழௌ")
    translated = translated.replace(u"§Æ¡", u"ழோ")
    translated = translated.replace(u"¦Æ¡", u"ழொ")
    translated = translated.replace(u"¨Æ", u"ழை")
    translated = translated.replace(u"§Æ", u"ழே")
    translated = translated.replace(u"¦Æ", u"ழெ")
    translated = translated.replace(u"è", u"ழூ")
    translated = translated.replace(u"Ø", u"ழு")
    translated = translated.replace(u"Æ£", u"ழீ")
    translated = translated.replace(u"Æ¢", u"ழி")
    translated = translated.replace(u"Æ¡", u"ழா")
    translated = translated.replace(u"Æ", u"ழ")

    # வ Family
    translated = translated.replace(u"ù", u"வ்")
    translated = translated.replace(u"¦Åª", u"வௌ")
    translated = translated.replace(u"§Å¡", u"வோ")
    translated = translated.replace(u"¦Å¡", u"வொ")
    translated = translated.replace(u"¨Å", u"வை")
    translated = translated.replace(u"§Å", u"வே")
    translated = translated.replace(u"¦Å", u"வெ")
    translated = translated.replace(u"ç", u"வூ")
    translated = translated.replace(u"×", u"வு")
    translated = translated.replace(u"Å£", u"வீ")
    translated = translated.replace(u"Å¢", u"வி")
    translated = translated.replace(u"Å¡", u"வா")
    translated = translated.replace(u"Å", u"வ")

    # ஷ Family
    translated = translated.replace(u"‰", u"ஷ்")
    translated = translated.replace(u"¦„ª", u"ஷௌ")
    translated = translated.replace(u"§„¡", u"ஷோ")
    translated = translated.replace(u"¦„¡", u"ஷொ")
    translated = translated.replace(u"¨„", u"ஷை")
    translated = translated.replace(u"§„", u"ஷே")
    translated = translated.replace(u"¦„", u"ஷெ")
    translated = translated.replace(u"„£", u"ஷீ")
    translated = translated.replace(u"„¢", u"ஷி")
    translated = translated.replace(u"„¡", u"ஷா")
    translated = translated.replace(u"„", u"ஷ")

    # ஸ Family
    translated = translated.replace(u"Š", u"ஸ்")
    translated = translated.replace(u"¦…ª", u"ஸௌ")
    translated = translated.replace(u"§…¡", u"ஸோ")
    translated = translated.replace(u"¦…¡", u"ஸொ")
    translated = translated.replace(u"¨…", u"ஸை")
    translated = translated.replace(u"§…", u"ஸே")
    translated = translated.replace(u"¦…", u"ஸெ")
    translated = translated.replace(u"…£", u"ஸீ")
    translated = translated.replace(u"…¢", u"ஸி")
    translated = translated.replace(u"…¡", u"ஸா")
    translated = translated.replace(u"…", u"ஸ")

    # ஹ Family
    translated = translated.replace(u"‹", u"ஹ்")
    translated = translated.replace(u"¦†ª", u"ஹௌ")
    translated = translated.replace(u"§†¡", u"ஹோ")
    translated = translated.replace(u"¦†¡", u"ஹொ")
    translated = translated.replace(u"¨†", u"ஹை")
    translated = translated.replace(u"§†", u"ஹே")
    translated = translated.replace(u"¦†", u"ஹெ")
    translated = translated.replace(u"†£", u"ஹீ")
    translated = translated.replace(u"†¢", u"ஹி")
    translated = translated.replace(u"†¡", u"ஹா")
    translated = translated.replace(u"†", u"ஹ")

    unconverted = [i for i in translated if i in source_text and not i in
                    punctuation+whitespace+digits]
    translated_trimed = ''.join([i for i in translated if not i in unconverted])

    if debug:
        return unconverted
    elif filtered:
        return translated_trimed
    else:
        return translated