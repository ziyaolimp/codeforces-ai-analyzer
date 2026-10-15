import os
import requests
from dotenv import load_dotenv
from groq import Groq
from django.shortcuts import render

# .env faylından mühit dəyişənlərini yükləyirik
load_dotenv()

# Groq klientini başladırıq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_roadmap(handle, wrong_tags, good_tags):
    """Groq API vasitəsilə fərdi öyrənmə planı yaradır."""
    if not wrong_tags and not good_tags:
        return None

    sorted_tags_wrong = sorted(wrong_tags.items(), key=lambda x: x[1], reverse=True)[:5]
    sorted_tags_good = sorted(good_tags.items(), key=lambda x: x[1], reverse=True)[:5]

    summary_wrong = ", ".join([f"{tag} ({count} səhv)" for tag, count in sorted_tags_wrong])
    summary_good = ", ".join([f"{tag} ({count} doğru)" for tag, count in sorted_tags_good])

    prompt = f"""
    İstifadəçi: {handle}
    Codeforces-da ən çox çətinlik çəkdiyi (səhv etdiyi) mövzular: {summary_wrong if summary_wrong else "Məlumat yoxdur"}.
    Codeforces-da uğurlu olduğu (yaxşı etdiyi) mövzular: {summary_good if summary_good else "Məlumat yoxdur"}.

    Bu proqramçı üçün 3 maddəlik qısa, dəqiq və motivasiyaedici fərdi öyrənmə planı (roadmap) hazırla. 
    Onun güclü tərəflərini nəzərə alaraq zəif tərəflərini necə inkişaf etdirməli olduğunu aydın izah et. Cavabı Azərbaycan dilində ver.
    """

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Groq AI xətası: {str(e)}"

def ask_ai_coach(handle, roadmap, user_question):
    """AI məşqçi ilə chat etmək üçün funksiya."""
    prompt = f"""
    Sən Codeforces üzrə peşəkar süni intellekt məşqçisisən.
    İstifadəçi: {handle}
    Əvvəlki təqdim olunan öyrənmə planı (roadmap): 
    {roadmap}

    İstifadəçinin sualı: {user_question}

    Bu suala qısa, dəqiq, motivasiyaedici və kod nümunələri ilə (lazım gələrsə) Azərbaycan dilində cavab ver.
    """

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Groq AI xətası: {str(e)}"

def home(request):
    context = {}
    
    if request.method == 'POST':
        # 1. Əgər əsas analiz düyməsinə (handle göndəriləndə) basılıbsa
        if 'handle' in request.POST and not 'chat_submit' in request.POST and request.POST.get('handle'):
            handle = request.POST.get('handle')
            url = f"https://codeforces.com/api/user.status?handle={handle}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if data.get('status') == 'OK':
                        submissions = data.get('result', [])
                        wrong_tags = {}
                        good_tags = {}
                        
                        for sub in submissions:
                            tags = sub.get('problem', {}).get('tags', [])
                            if sub.get('verdict') != 'OK':
                                for tag in tags:
                                    wrong_tags[tag] = wrong_tags.get(tag, 0) + 1
                            else:
                                for tag in tags:
                                    good_tags[tag] = good_tags.get(tag, 0) + 1

                        ai_roadmap = get_ai_roadmap(handle, wrong_tags, good_tags)

                        # Məlumatları həm kontekstə, həm də sessiyaya yazırıq ki, chat zamanı itməsin
                        request.session['handle'] = handle
                        request.session['wrong_tags'] = wrong_tags
                        request.session['good_tags'] = good_tags
                        request.session['ai_roadmap'] = ai_roadmap

                        context['handle'] = handle
                        context['wrong_tags'] = wrong_tags
                        context['good_tags'] = good_tags
                        context['ai_roadmap'] = ai_roadmap
                    else:
                        context['error'] = "İstifadəçi tapılmadı!"
                else:
                    context['error'] = f"Codeforces API xətası verdi (Status: {response.status_code})"
            except requests.exceptions.RequestException:
                context['error'] = "Codeforces serveri ilə əlaqə kəsildi."

        # 2. Əgər istifadəçi chat-a mesaj yazıbsa ('chat_submit' düyməsinə basılıbsa)
        elif 'chat_submit' in request.POST:
            user_question = request.POST.get('user_question')
            
            # Sessiyadan əvvəlki məlumatları bərpa edirik
            handle = request.session.get('handle')
            ai_roadmap = request.session.get('ai_roadmap')
            wrong_tags = request.session.get('wrong_tags')
            good_tags = request.session.get('good_tags')
            
            if user_question and ai_roadmap:
                chat_answer = ask_ai_coach(handle, ai_roadmap, user_question)
                context['chat_answer'] = chat_answer
                context['user_question'] = user_question
            
            # Ekran yenidən yüklənəndə statistikalar və roadmap qalsın deyə kontekstə ötürürük
            context['handle'] = handle
            context['wrong_tags'] = wrong_tags
            context['good_tags'] = good_tags
            context['ai_roadmap'] = ai_roadmap

    return render(request, 'analyzer/home.html', context)