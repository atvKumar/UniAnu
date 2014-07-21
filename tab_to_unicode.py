# -*- coding: utf-8 -*-
from string import punctuation, whitespace, digits


def convertTounicode(source_text, filtered=False, debug=False):
    translated = source_text
    # Independent Vowels
    translated = translated.replace(u"Ü", u"அ")
    translated = translated.replace(u"Ý", u"ஆ")
    translated = translated.replace(u"Þ", u"இ")
    translated = translated.replace(u"ß", u"ஈ")
    translated = translated.replace(u"à", u"உ")
    translated = translated.replace(u"á", u"ஊ")
    translated = translated.replace(u"â", u"எ")
    translated = translated.replace(u"ã", u"ஏ")
    translated = translated.replace(u"ä", u"ஐ")
    translated = translated.replace(u"å", u"ஒ")
    translated = translated.replace(u"æ", u"ஓ")
    translated = translated.replace(u"å÷", u"ஔ")
    translated = translated.replace(u"ç", u"ஃ")

    # க Family
    translated = translated.replace(u"è¢", u"க்")
    translated = translated.replace(u"ªè÷", u"கௌ")
    translated = translated.replace(u"«è£", u"கோ")
    translated = translated.replace(u"ªè£", u"கொ")
    translated = translated.replace(u"¬è", u"கை")
    translated = translated.replace(u"«è", u"கே")
    translated = translated.replace(u"ªè", u"கெ")
    translated = translated.replace(u"Ã", u"கூ")
    translated = translated.replace(u"°", u"கு")
    translated = translated.replace(u"è¦", u"கீ")
    translated = translated.replace(u"è¤", u"கி")
    translated = translated.replace(u"è£", u"கா")
    translated = translated.replace(u"è", u"க")

    # ங Family
    translated = translated.replace(u"é¢", u"ங்")
    translated = translated.replace(u"ªé÷", u"ஙௌ")
    translated = translated.replace(u"«é£", u"ஙோ")
    translated = translated.replace(u"ªé£", u"ஙொ")
    translated = translated.replace(u"¬é", u"ஙை")
    translated = translated.replace(u"«é", u"ஙே")
    translated = translated.replace(u"ªé", u"ஙெ")
    translated = translated.replace(u"Ä", u"ஙூ")
    translated = translated.replace(u"±", u"ஙு")
    translated = translated.replace(u"é¦", u"ஙீ")
    translated = translated.replace(u"é¤", u"ஙி")
    translated = translated.replace(u"é£", u"ஙா")
    translated = translated.replace(u"é", u"ங")

    # ச Family
    translated = translated.replace(u"ê¢", u"ச்")
    translated = translated.replace(u"ªê÷", u"சௌ")
    translated = translated.replace(u"«ê£", u"சோ")
    translated = translated.replace(u"ªê£", u"சொ")
    translated = translated.replace(u"¬ê", u"சை")
    translated = translated.replace(u"«ê", u"சே")
    translated = translated.replace(u"ªê", u"செ")
    translated = translated.replace(u"Å", u"சூ")
    translated = translated.replace(u"²", u"சு")
    translated = translated.replace(u"ê¦", u"சீ")
    translated = translated.replace(u"ê¤", u"சி")
    translated = translated.replace(u"ê£", u"சா")
    translated = translated.replace(u"ê", u"ச")

    # ஜ Family
    translated = translated.replace(u"ü¢", u"ஜ்")
    translated = translated.replace(u"ªü÷", u"ஜௌ")
    translated = translated.replace(u"«ü£", u"ஜோ")
    translated = translated.replace(u"ªü£", u"ஜொ")
    translated = translated.replace(u"¬ü", u"ஜை")
    translated = translated.replace(u"«ü", u"ஜே")
    translated = translated.replace(u"ªü", u"ஜெ")
    translated = translated.replace(u"ü¨", u"ஜூ")
    translated = translated.replace(u"ü§", u"ஜு")
    translated = translated.replace(u"ü¦", u"ஜீ")
    translated = translated.replace(u"ü¤", u"ஜி")
    translated = translated.replace(u"ü£", u"ஜா")
    translated = translated.replace(u"ü", u"ஜ")

    # ஞ Family
    translated = translated.replace(u"ë¢", u"ஞ்")
    translated = translated.replace(u"ªë÷", u"ஞௌ")
    translated = translated.replace(u"«ë£", u"ஞோ")
    translated = translated.replace(u"ªë£", u"ஞொ")
    translated = translated.replace(u"¬ë", u"ஞை")
    translated = translated.replace(u"«ë", u"ஞே")
    translated = translated.replace(u"ªë", u"ஞெ")
    translated = translated.replace(u"Æ", u"ஞூ")
    translated = translated.replace(u"³", u"ஞு")
    translated = translated.replace(u"ë¦", u"ஞீ")
    translated = translated.replace(u"ë¤", u"ஞி")
    translated = translated.replace(u"ë£", u"ஞா")
    translated = translated.replace(u"ë", u"ஞ")

    # ட Family
    translated = translated.replace(u"ì¢", u"ட்")
    translated = translated.replace(u"ªì÷", u"டௌ")
    translated = translated.replace(u"«ì£", u"டோ")
    translated = translated.replace(u"ªì£", u"டொ")
    translated = translated.replace(u"¬ì", u"டை")
    translated = translated.replace(u"«ì", u"டே")
    translated = translated.replace(u"ªì", u"டெ")
    translated = translated.replace(u"Ç", u"டூ")
    translated = translated.replace(u"´", u"டு")
    translated = translated.replace(u"¯", u"டீ")
    translated = translated.replace(u"ì¤", u"டி")
    translated = translated.replace(u"ì£", u"டா")
    translated = translated.replace(u"ì", u"ட")

    # ண Family
    translated = translated.replace(u"í¢", u"ண்")
    translated = translated.replace(u"ªí÷", u"ணௌ")
    translated = translated.replace(u"«í£", u"ணோ")
    translated = translated.replace(u"ªí£", u"ணொ")
    translated = translated.replace(u"¬í", u"ணை")
    translated = translated.replace(u"«í", u"ணே")
    translated = translated.replace(u"ªí", u"ணெ")
    translated = translated.replace(u"È", u"ணூ")
    translated = translated.replace(u"µ", u"ணு")
    translated = translated.replace(u"í¦", u"ணீ")
    translated = translated.replace(u"í¤", u"ணி")
    translated = translated.replace(u"í£", u"ணா")
    translated = translated.replace(u"í", u"ண")

    # த Family
    translated = translated.replace(u"î¢", u"த்")
    translated = translated.replace(u"ªî÷", u"தௌ")
    translated = translated.replace(u"«î£", u"தோ")
    translated = translated.replace(u"ªî£", u"தொ")
    translated = translated.replace(u"¬î", u"தை")
    translated = translated.replace(u"«î", u"தே")
    translated = translated.replace(u"ªî", u"தெ")
    translated = translated.replace(u"É", u"தூ")
    translated = translated.replace(u"¶", u"து")
    translated = translated.replace(u"î¦", u"தீ")
    translated = translated.replace(u"î¤", u"தி")
    translated = translated.replace(u"î£", u"தா")
    translated = translated.replace(u"î", u"த")

    # ந Family
    translated = translated.replace(u"ï¢", u"ந்")
    translated = translated.replace(u"ªï÷", u"நௌ")
    translated = translated.replace(u"«ï£", u"நோ")
    translated = translated.replace(u"ªï£", u"நொ")
    translated = translated.replace(u"¬ï", u"நை")
    translated = translated.replace(u"«ï", u"நே")
    translated = translated.replace(u"ªï", u"நெ")
    translated = translated.replace(u"Ë", u"நூ")
    translated = translated.replace(u"¸", u"நு")
    translated = translated.replace(u"ï¦", u"நீ")
    translated = translated.replace(u"ï¤", u"நி")
    translated = translated.replace(u"ï£", u"நா")
    translated = translated.replace(u"ï", u"ந")

    # ன Family
    translated = translated.replace(u"ù¢", u"ன்")
    translated = translated.replace(u"ªù÷", u"னௌ")
    translated = translated.replace(u"«ù£", u"னோ")
    translated = translated.replace(u"ªù£", u"னொ")
    translated = translated.replace(u"¬ù", u"னை")
    translated = translated.replace(u"«ù", u"னே")
    translated = translated.replace(u"ªù", u"னெ")
    translated = translated.replace(u"Û", u"னூ")
    translated = translated.replace(u"Â", u"னு")
    translated = translated.replace(u"ù¦", u"னீ")
    translated = translated.replace(u"ù¤", u"னி")
    translated = translated.replace(u"ù£", u"னா")
    translated = translated.replace(u"ù", u"ன")

    # ப Family
    translated = translated.replace(u"ð¢", u"ப்")
    translated = translated.replace(u"ªð÷", u"பௌ")
    translated = translated.replace(u"«ð£", u"போ")
    translated = translated.replace(u"ªð£", u"பொ")
    translated = translated.replace(u"¬ð", u"பை")
    translated = translated.replace(u"«ð", u"பே")
    translated = translated.replace(u"ªð", u"பெ")
    translated = translated.replace(u"Ì", u"பூ")
    translated = translated.replace(u"¹", u"பு")
    translated = translated.replace(u"ð¦", u"பீ")
    translated = translated.replace(u"ð¤", u"பி")
    translated = translated.replace(u"ð£", u"பா")
    translated = translated.replace(u"ð", u"ப")

    # ம Family
    translated = translated.replace(u"ñ¢", u"ம்")
    translated = translated.replace(u"ªñ÷", u"மௌ")
    translated = translated.replace(u"«ñ£", u"மோ")
    translated = translated.replace(u"ªñ£", u"மொ")
    translated = translated.replace(u"¬ñ", u"மை")
    translated = translated.replace(u"«ñ", u"மே")
    translated = translated.replace(u"ªñ", u"மெ")
    translated = translated.replace(u"Í", u"மூ")
    translated = translated.replace(u"º", u"மு")
    translated = translated.replace(u"ñ¦", u"மீ")
    translated = translated.replace(u"ñ¤", u"மி")
    translated = translated.replace(u"ñ£", u"மா")
    translated = translated.replace(u"ñ", u"ம")

    # ய Family
    translated = translated.replace(u"ò¢", u"ய்")
    translated = translated.replace(u"ªò÷", u"யௌ")
    translated = translated.replace(u"«ò£", u"யோ")
    translated = translated.replace(u"ªò£", u"யொ")
    translated = translated.replace(u"¬ò", u"யை")
    translated = translated.replace(u"«ò", u"யே")
    translated = translated.replace(u"ªò", u"யெ")
    translated = translated.replace(u"Î", u"யூ")
    translated = translated.replace(u"»", u"யு")
    translated = translated.replace(u"ò¦", u"யீ")
    translated = translated.replace(u"ò¤", u"யி")
    translated = translated.replace(u"ò£", u"யா")
    translated = translated.replace(u"ò", u"ய")

    # ர Family
    translated = translated.replace(u"ó¢", u"ர்")
    translated = translated.replace(u"ªó÷", u"ரௌ")
    translated = translated.replace(u"«ó£", u"ரோ")
    translated = translated.replace(u"ªó£", u"ரொ")
    translated = translated.replace(u"¬ó", u"ரை")
    translated = translated.replace(u"«ó", u"ரே")
    translated = translated.replace(u"ªó", u"ரெ")
    translated = translated.replace(u"Ï", u"ரூ")
    translated = translated.replace(u"¼", u"ரு")
    translated = translated.replace(u"ó¦", u"ரீ")
    translated = translated.replace(u"ó¤", u"ரி")
    translated = translated.replace(u"ó£", u"ரா")
    translated = translated.replace(u"ó", u"ர")

    # ற Family
    translated = translated.replace(u"ø¢", u"ற்")
    translated = translated.replace(u"ªø÷", u"றௌ")
    translated = translated.replace(u"«ø£", u"றோ")
    translated = translated.replace(u"ªø£", u"றொ")
    translated = translated.replace(u"¬ø", u"றை")
    translated = translated.replace(u"«ø", u"றே")
    translated = translated.replace(u"ªó", u"ரெ")
    translated = translated.replace(u"Ú", u"றூ")
    translated = translated.replace(u"Á", u"று")
    translated = translated.replace(u"ø¦", u"றீ")
    translated = translated.replace(u"ø¤", u"றி")
    translated = translated.replace(u"ø£", u"றா")
    translated = translated.replace(u"ø", u"ற")

    # ல Family
    translated = translated.replace(u"ô¢", u"ல்")
    translated = translated.replace(u"ªô÷", u"லௌ")
    translated = translated.replace(u"«ô£", u"லோ")
    translated = translated.replace(u"ªô£", u"லொ")
    translated = translated.replace(u"¬ô", u"லை")
    translated = translated.replace(u"«ô", u"லே")
    translated = translated.replace(u"ªô", u"லெ")
    translated = translated.replace(u"Ö", u"லூ")
    translated = translated.replace(u"½", u"லு")
    translated = translated.replace(u"ô¦", u"லீ")
    translated = translated.replace(u"ô¤", u"லி")
    translated = translated.replace(u"ô£", u"லா")
    translated = translated.replace(u"ô", u"ல")

    # ள Family
    translated = translated.replace(u"÷¢", u"ள்")
    translated = translated.replace(u"ª÷÷", u"ளௌ")
    translated = translated.replace(u"«÷£", u"ளோ")
    translated = translated.replace(u"ª÷£", u"ளொ")
    translated = translated.replace(u"¬÷", u"ளை")
    translated = translated.replace(u"«÷", u"ளே")
    translated = translated.replace(u"ª÷", u"ளெ")
    translated = translated.replace(u"Ù", u"ளூ")
    translated = translated.replace(u"À", u"ளு")
    translated = translated.replace(u"÷¦", u"ளீ")
    translated = translated.replace(u"÷¤", u"ளி")
    translated = translated.replace(u"÷£", u"ளா")
    translated = translated.replace(u"÷", u"ள")

    # ழ Family
    translated = translated.replace(u"ö¢", u"ழ்")
    translated = translated.replace(u"ªö÷", u"ழௌ")
    translated = translated.replace(u"«ö£", u"ழோ")
    translated = translated.replace(u"ªö£", u"ழொ")
    translated = translated.replace(u"¬ö", u"ழை")
    translated = translated.replace(u"«ö", u"ழே")
    translated = translated.replace(u"ªö", u"ழெ")
    translated = translated.replace(u"Ø", u"ழூ")
    translated = translated.replace(u"¿", u"ழு")
    translated = translated.replace(u"ö¦", u"ழீ")
    translated = translated.replace(u"ö¤", u"ழி")
    translated = translated.replace(u"ö£", u"ழா")
    translated = translated.replace(u"ö", u"ழ")

    # வ Family
    translated = translated.replace(u"õ¢", u"வ்")
    translated = translated.replace(u"ªõ÷", u"வௌ")
    translated = translated.replace(u"«õ£", u"வோ")
    translated = translated.replace(u"ªõ£", u"வொ")
    translated = translated.replace(u"¬õ", u"வை")
    translated = translated.replace(u"«õ", u"வே")
    translated = translated.replace(u"ªõ", u"வெ")
    translated = translated.replace(u"×", u"வூ")
    translated = translated.replace(u"¾", u"வு")
    translated = translated.replace(u"õ¦", u"வீ")
    translated = translated.replace(u"õ¤", u"வி")
    translated = translated.replace(u"õ£", u"வா")
    translated = translated.replace(u"õ", u"வ")

    # ஷ Family
    translated = translated.replace(u"û¢", u"ஷ்")
    translated = translated.replace(u"ªû÷", u"ஷௌ")
    translated = translated.replace(u"«û£", u"ஷோ")
    translated = translated.replace(u"ªû£", u"ஷொ")
    translated = translated.replace(u"¬û", u"ஷை")
    translated = translated.replace(u"«û", u"ஷே")
    translated = translated.replace(u"ªû", u"ஷெ")
    translated = translated.replace(u"û¦", u"ஷீ")
    translated = translated.replace(u"û¤", u"ஷி")
    translated = translated.replace(u"û£", u"ஷா")
    translated = translated.replace(u"û", u"ஷ")

    # ஸ Family
    translated = translated.replace(u"ú¢", u"ஸ்")
    translated = translated.replace(u"ªú÷", u"ஸௌ")
    translated = translated.replace(u"«ú£", u"ஸோ")
    translated = translated.replace(u"ªú£", u"ஸொ")
    translated = translated.replace(u"¬ú", u"ஸை")
    translated = translated.replace(u"«ú", u"ஸே")
    translated = translated.replace(u"ªú", u"ஸெ")
    translated = translated.replace(u"ú¦", u"ஸீ")
    translated = translated.replace(u"ú¤", u"ஸி")
    translated = translated.replace(u"ú£", u"ஸா")
    translated = translated.replace(u"ú", u"ஸ")

    # ஹ Family
    translated = translated.replace(u"ý¢", u"ஹ்")
    translated = translated.replace(u"ªý÷", u"ஹௌ")
    translated = translated.replace(u"«ý£", u"ஹோ")
    translated = translated.replace(u"ªý£", u"ஹொ")
    translated = translated.replace(u"¬ý", u"ஹை")
    translated = translated.replace(u"«ý", u"ஹே")
    translated = translated.replace(u"ªý", u"ஹெ")
    translated = translated.replace(u"ý¦", u"ஹீ")
    translated = translated.replace(u"ý¤", u"ஹி")
    translated = translated.replace(u"ý£", u"ஹா")
    translated = translated.replace(u"ý", u"ஹ")

    unconverted = [i for i in translated if i in source_text and not i in
                    punctuation+whitespace+digits]
    translated_trimed = ''.join([i for i in translated if not i in unconverted])

    if debug:
        return unconverted
    elif filtered:
        return translated_trimed
    else:
        return translated