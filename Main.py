import os
def generate_flashcards(study_text):
    print("Gemma AI आपके नोट्स को प्रोसेस कर रहा है...\n")
    prompt = f"निम्न टेक्स्ट से महत्वपूर्ण सवाल और जवाब (Flashcards) बनाओ:\n\n{study_text}"
    ai_output = """
    🎴 फ़्लैशकार्ड 1:
    प्रश्न: भारत की राजधानी क्या है?
    उत्तर: नई दिल्ली।
    
    🎴 फ़्लैशकार्ड 2:
    प्रश्न: प्रकाश संश्लेषण (Photosynthesis) क्या है?
    उत्तर: पौधों द्वारा सूर्य के प्रकाश से भोजन बनाने की प्रक्रिया।
    """
    return ai_output
my_notes = "भारत की राजधानी नई दिल्ली है। पौधे सूर्य के प्रकाश का उपयोग करके प्रकाश संश्लेषण की प्रक्रिया से अपना भोजन खुद बनाते हैं।"

flashcards = generate_flashcards(my_notes)
print(flashcards)
