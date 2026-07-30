import streamlit as st


def load_theme():

    st.markdown(
        """
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main App */
.stApp{
    background: linear-gradient(135deg,#0F172A,#111827,#1E293B);
    color:white;
}

/* Remove Streamlit Header */
header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Toolbar */
[data-testid="stToolbar"]{
    right:2rem;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #374151;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Containers */

div[data-testid="stVerticalBlockBorderWrapper"]{
    background:#1E293B;
    border-radius:18px;
    border:1px solid #334155;
    padding:20px;
}

/* Metric Cards */

div[data-testid="metric-container"]{
    background:#1E293B;
    border:1px solid #334155;
    border-radius:16px;
    padding:20px;
    transition:0.3s;
}

div[data-testid="metric-container"]:hover{
    transform:translateY(-4px);
    border:1px solid #3B82F6;
}

/* Buttons */

.stButton>button{

    width:100%;
    border-radius:12px;
    background:#2563EB;
    color:white;
    border:none;
    height:48px;
    font-weight:600;
    transition:0.3s;
}

.stButton>button:hover{

    background:#1D4ED8;
    transform:scale(1.02);

}

/* Text Input */

.stTextInput input{

    border-radius:12px;
    background:#1E293B;
    color:white;
    border:1px solid #334155;

}

/* Text Area */

.stTextArea textarea{

    border-radius:12px;
    background:#1E293B;
    color:white;
    border:1px solid #334155;

}

/* Select Box */

.stSelectbox div{

    border-radius:12px;

}

/* Chat Message */

[data-testid="stChatMessage"]{

    border-radius:16px;
    border:1px solid #334155;
    padding:15px;
    margin-bottom:10px;

}

/* Chat Input */

[data-testid="stChatInput"]{

    border-radius:18px;

}

/* Success */

.stSuccess{

    border-radius:12px;

}

/* Info */

.stInfo{

    border-radius:12px;

}

/* Warning */

.stWarning{

    border-radius:12px;

}

/* Divider */

hr{

    border:1px solid #334155;

}

/* Hero */

.hero{

    text-align:center;
    padding:15px;

}

.hero h1{

    font-size:48px;
    color:white;
    margin-bottom:5px;

}

.hero p{

    color:#CBD5E1;
    font-size:18px;

}

/* Dashboard Cards */

.card{

    background:#1E293B;
    padding:25px;
    border-radius:18px;
    border:1px solid #334155;

}

.card:hover{

    border:1px solid #3B82F6;
    transition:.3s;

}

/* Small Badge */

.badge{

    background:#2563EB;
    color:white;
    padding:6px 14px;
    border-radius:30px;
    font-size:13px;

}

/* Scroll Bar */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#3B82F6;
    border-radius:10px;

}

::-webkit-scrollbar-track{

    background:#111827;

}

</style>
""",
        unsafe_allow_html=True,
    )


def hero(title, subtitle):

    st.markdown(
        f"""
<div class="hero">

<h1>{title}</h1>

<p>{subtitle}</p>

</div>
""",
        unsafe_allow_html=True,
    )