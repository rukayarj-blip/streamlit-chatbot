import streamlit as st
import random

st.set_page_config(
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stStatusWidget"] {
    display: none;
}

.viewerBadge_container__1QSob {
    display: none;
}

.stDeployButton {
    display: none;
}
</style>
""", unsafe_allow_html=True)
    page_title="DARC",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================
# إخفاء عناصر Streamlit
# ==========================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

[data-testid="stToolbar"]{
display:none;
}

[data-testid="stDecoration"]{
display:none;
}

[data-testid="stStatusWidget"]{
display:none;
}

.viewerBadge_container__1QSob{
display:none;
}

*{
user-select:none;
-webkit-user-select:none;
-ms-user-select:none;
}

textarea,input{
user-select:text !important;
-webkit-user-select:text !important;
}

html,body,[class*="css"]{
font-family:Tahoma;
direction:rtl;
scroll-behavior:smooth;
}

.stApp{
background:
linear-gradient(135deg,#fdf1ff,#eef7ff,#f9f3ff);
background-size:300% 300%;
animation:bgmove 12s ease infinite;
overflow-x:hidden;
}

@keyframes bgmove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.block-container{
max-width:1200px;
padding-top:20px;
padding-bottom:40px;
}

/* ==========================
العنوان
========================== */

.hero{
position:relative;
background:rgba(255,255,255,0.82);
border-radius:35px;
padding:35px;
box-shadow:0 10px 35px rgba(120,80,160,.18);
overflow:hidden;
text-align:center;
}

.main-title{
font-size:75px;
font-weight:bold;
background:linear-gradient(90deg,#7b2cbf,#9d4edd,#ff4d8d);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:10px;
}

.sub-title{
font-size:32px;
color:#ff4d8d;
font-weight:bold;
line-height:1.8;
}

.sub2{
font-size:28px;
color:#2f2f7f;
font-weight:bold;
}

/* ==========================
الروبوت
========================== */

.robot-box{
margin-top:25px;
display:flex;
justify-content:center;
align-items:center;
gap:40px;
flex-wrap:wrap;
}

.robot{
font-size:180px;
animation:robotFloat 2.5s infinite ease-in-out;
filter:drop-shadow(0 10px 20px rgba(0,0,0,.15));
}

@keyframes robotFloat{
0%{transform:translateY(0px);}
50%{transform:translateY(-15px);}
100%{transform:translateY(0px);}
}

.speech{
background:white;
padding:25px;
border-radius:30px;
width:320px;
box-shadow:0 8px 25px rgba(0,0,0,.12);
font-size:28px;
line-height:2;
position:relative;
animation:talk 1.5s infinite alternate;
}

@keyframes talk{
0%{transform:scale(1);}
100%{transform:scale(1.03);}
}

.wave{
display:flex;
gap:6px;
justify-content:center;
margin-top:15px;
}

.wave span{
width:8px;
height:30px;
background:#9d4edd;
border-radius:10px;
animation:wave 1s infinite;
}

.wave span:nth-child(2){
animation-delay:.2s;
}

.wave span:nth-child(3){
animation-delay:.4s;
}

.wave span:nth-child(4){
animation-delay:.6s;
}

@keyframes wave{
0%{height:15px;}
50%{height:45px;}
100%{height:15px;}
}

/* ==========================
البطاقات
========================== */

.card-container{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-top:35px;
}

.card{
background:white;
padding:25px;
border-radius:25px;
text-align:center;
box-shadow:0 8px 20px rgba(0,0,0,.08);
transition:.3s;
border:2px solid #f0e5ff;
}

.card:hover{
transform:translateY(-8px);
}

.card-number{
width:55px;
height:55px;
border-radius:50%;
background:linear-gradient(135deg,#7b2cbf,#ff4d8d);
color:white;
font-size:28px;
font-weight:bold;
display:flex;
justify-content:center;
align-items:center;
margin:auto;
margin-bottom:15px;
}

.card-icon{
font-size:55px;
margin-bottom:10px;
}

.card-title{
font-size:28px;
font-weight:bold;
color:#7b2cbf;
margin-bottom:10px;
}

.card-text{
font-size:20px;
line-height:1.8;
color:#555;
}

/* ==========================
النموذج
========================== */

.form-box{
margin-top:35px;
background:white;
padding:30px;
border-radius:30px;
box-shadow:0 10px 30px rgba(0,0,0,.08);
}

.stTextArea textarea{
border-radius:20px !important;
font-size:22px !important;
padding:15px !important;
}

.stButton button{
width:100%;
border:none;
padding:18px;
border-radius:20px;
font-size:28px;
font-weight:bold;
color:white;
background:linear-gradient(135deg,#7b2cbf,#ff4d8d);
transition:.3s;
}

.stButton button:hover{
transform:scale(1.02);
}

/* ==========================
النتيجة
========================== */

.result{
margin-top:25px;
background:#ffffff;
padding:25px;
border-radius:25px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
line-height:2.2;
font-size:24px;
border-right:10px solid #9d4edd;
animation:fade .7s;
}

@keyframes fade{
from{
opacity:0;
transform:translateY(20px);
}
to{
opacity:1;
transform:translateY(0px);
}
}

/* ==========================
الموبايل
========================== */

@media screen and (max-width:768px){

.main-title{
font-size:48px;
}

.sub-title{
font-size:22px;
}

.sub2{
font-size:22px;
}

.robot{
font-size:120px;
}

.speech{
width:100%;
font-size:22px;
}

.card-title{
font-size:24px;
}

.card-text{
font-size:18px;
}

.stButton button{
font-size:22px;
}

.result{
font-size:20px;
}
}

</style>

<script>

document.addEventListener("contextmenu",function(e){
e.preventDefault();
});

document.addEventListener("keydown",function(e){

if(
e.ctrlKey &&
(
e.key=="a" ||
e.key=="A" ||
e.key=="c" ||
e.key=="C" ||
e.key=="u" ||
e.key=="U" ||
e.key=="s" ||
e.key=="S"
)
){
e.preventDefault();
}

});

</script>

""", unsafe_allow_html=True)

# ==========================
# العنوان
# ==========================

st.markdown("""
<div class="hero">

<div class="main-title">
DARC
</div>

<div class="sub-title">
خطاب الكراهية الرقمي لدى طالبات المرحلة الثانوية
</div>

<div class="sub2">
في مادة علم الاجتماع
</div>

<div class="robot-box">

<div class="speech">
مرحبًا 👋<br>
أنا روبوت DARC الذكي<br>
سأساعدكِ على فهم خطاب الكراهية الرقمي والتعامل معه بذكاء واحترام

<div class="wave">
<span></span>
<span></span>
<span></span>
<span></span>
</div>

</div>

<div class="robot">
🤖
</div>

</div>

</div>
""", unsafe_allow_html=True)

# ==========================
# البطاقات
# ==========================

st.markdown("""

<div class="card-container">

<div class="card">
<div class="card-number">1</div>
<div class="card-icon">🔍</div>
<div class="card-title">الكشف</div>
<div class="card-text">
التعرف على العبارات التي تمثل خطاب كراهية رقمي
</div>
</div>

<div class="card">
<div class="card-number">2</div>
<div class="card-icon">📊</div>
<div class="card-title">التحليل</div>
<div class="card-text">
تحليل نوع الخطاب وأسبابه والفئة المستهدفة
</div>
</div>

<div class="card">
<div class="card-number">3</div>
<div class="card-icon">🛡️</div>
<div class="card-title">الاستجابة</div>
<div class="card-text">
اختيار الرد المناسب والآمن باحترام
</div>
</div>

<div class="card">
<div class="card-number">4</div>
<div class="card-icon">✏️</div>
<div class="card-title">الإنشاء</div>
<div class="card-text">
إنشاء خطاب رقمي إيجابي وبديل محترم
</div>
</div>

</div>

""", unsafe_allow_html=True)

# ==========================
# الإدخال
# ==========================

st.markdown('<div class="form-box">', unsafe_allow_html=True)

stage = st.selectbox(
"اختاري مرحلة التعلم",
[
"1 - الكشف",
"2 - التحليل",
"3 - الاستجابة",
"4 - الإنشاء"
]
)

text = st.text_area(
"اكتبي تعليقًا أو منشورًا رقميًا لتحليله",
height=170,
placeholder="اكتبي هنا..."
)

hate_words = [
"أكره",
"اقتل",
"اطرد",
"قذرين",
"لا يستحقون",
"خونة",
"كلهم",
"اسحقوهم",
"لا مكان لهم"
]

positive = [
"نختلف في الآراء لكن يجب احترام الجميع.",
"الحوار المحترم أفضل من الإساءة.",
"الاختلاف لا يبرر الكراهية.",
"احترام الآخرين أساس التواصل الرقمي."
]

if st.button("✨ تحليل العبارة"):

    found = []

    for word in hate_words:
        if word in text:
            found.append(word)

    if len(found) == 0:
        level = "🟢 منخفض"
        msg = "لا توجد مؤشرات قوية على خطاب كراهية."
    elif len(found) <= 2:
        level = "🟡 متوسط"
        msg = "توجد مؤشرات محتملة على خطاب كراهية رقمي."
    else:
        level = "🔴 مرتفع"
        msg = "العبارة تحتوي على خطاب كراهية واضح."

    st.markdown(f"""
    <div class="result">

    <b>مستوى الخطورة:</b> {level}<br>

    <b>التحليل:</b><br>
    {msg}<br><br>

    <b>الكلمات المكتشفة:</b><br>
    {", ".join(found) if found else "لا توجد"}

    <br><br>

    <b>النصيحة:</b><br>
    {random.choice(positive)}

    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

