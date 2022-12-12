var quiz = {
  // (A) PROPERTIES
  // (A1) QUESTIONS & ANSWERS
  // Q = QUESTION, O = OPTIONS, A = CORRECT ANSWER
  data: [
  {
    q : "How do you say \"hello\" in Spanish?",
    o : [
      "Hola",
      "Adios",
      "Jabon",
      "Bonjour"
    ],
    a : 0 // arrays start with 0
  },
  {
    q : "How do you say \"dog\" in Spanish?",
    o : [
      "Gato",
      "Raton",
      "Perro",
      "Sag"
    ],
    a : 2
  },
  {
    q : "If you want to ask where the bathroom is what is the correct phrase to use?",
    o : [
      "Adonde estamos?",
      "Adonde esta el bano?",
      "Y las llaves?",
      "Podemos ir a la tienda?"
    ],
    a : 1
  },
  {
    q : "How do you say \"wash\" in Spanish?",
    o : [
      "Pintar",
      "Lavar",
      "Ajudar",
      "Vashar"
    ],
    a : 1
  },
  {
    q : "How do you say \"Miss\" in Spanish?",
    o : [
      "Chiquita",
      "Mademoiselle",
      "Belleza",
      "Senorita"
    ],
    a : 3
  },
  {
    q : "What is the correct phrase for Good Morning?",
    o : [
      "Buenas Noches",
      "Buenas Tardes",
      "Buenos Dias",
      "Bonne Nuit"
    ],
    a : 2
  },
  {
    q : "If someone asks you in Spanish, Adonde esta la farmacia,? you answer",
    o : [
      "Esta en la esquina",
      "Ven con migo",
      "Quieres ir a la escuela",
      "Queremos ir a el parque"
    ],
    a : 0
  },
  {
    q : "If someone asks you in Spanish Adonde vas? you answer",
    o : [
      "No quiero",
      "Para esto",
      "Fuimos al parque",
      "Para la casa de mi amigo"
    ],
    a : 3
  },
  {
    q : "Click the best translation of Piedra:",
    o : [
      "Pardon",
      "Sac",
      "Stone",
      "Pier"
    ],
    a : 2
  },
  {
    q : "Click the best translation of el cristal:",
    o : [
      "Glass",
      "Cyrstal",
      "Ball",
      "Christ"
    ],
    a : 0
  }
  ],

  // (A2) HTML ELEMENTS
  hWrap: null, // HTML quiz container
  hQn: null, // HTML question wrapper
  hAns: null, // HTML answers wrapper

  // (A3) GAME FLAGS
  now: 0, // current question
  score: 0, // current score

  // (B) INIT QUIZ HTML
  init: () => {
    // (B1) WRAPPER
    quiz.hWrap = document.getElementById("quizWrap");

    // (B2) QUESTIONS SECTION
    quiz.hQn = document.createElement("div");
    quiz.hQn.id = "quizQn";
    quiz.hWrap.appendChild(quiz.hQn);

    // (B3) ANSWERS SECTION
    quiz.hAns = document.createElement("div");
    quiz.hAns.id = "quizAns";
    quiz.hWrap.appendChild(quiz.hAns);

    // (B4) GO!
    quiz.draw();
  },

  // (C) DRAW QUESTION
  draw: () => {
    // (C1) QUESTION
    quiz.hQn.innerHTML = quiz.data[quiz.now].q;

    // (C2) OPTIONS
    quiz.hAns.innerHTML = "";
    for (let i in quiz.data[quiz.now].o) {
      let radio = document.createElement("input");
      radio.type = "radio";
      radio.name = "quiz";
      radio.id = "quizo" + i;
      quiz.hAns.appendChild(radio);
      let label = document.createElement("label");
      label.innerHTML = quiz.data[quiz.now].o[i];
      label.setAttribute("for", "quizo" + i);
      label.dataset.idx = i;
      label.addEventListener("click", () => { quiz.select(label); });
      quiz.hAns.appendChild(label);
    }
  },

  // (D) OPTION SELECTED
  select: (option) => {
    // (D1) DETACH ALL ONCLICK
    let all = quiz.hAns.getElementsByTagName("label");
    for (let label of all) {
      label.removeEventListener("click", quiz.select);
    }

    // (D2) CHECK IF CORRECT
    let correct = option.dataset.idx == quiz.data[quiz.now].a;
    if (correct) {
      quiz.score++;
      option.classList.add("correct");
    } else {
      option.classList.add("wrong");
    }

    // (D3) NEXT QUESTION OR END GAME
    quiz.now++;
    setTimeout(() => {
      if (quiz.now < quiz.data.length) { quiz.draw(); }
      else {
        quiz.hAns.innerHTML = "Book your trial <a href='/trial'>here</a> or Purchase <a href='/purchase' target=\"_blank\">now</a>";
        score_message=`You have answered ${quiz.score} of ${quiz.data.length} correctly.`
        if (quiz.score <=3){
          quiz.hQn.innerHTML = score_message + " You seem to be at a lower elementary level";
        } else if (quiz.score > 3 && quiz.score < 6) {
          quiz.hQn.innerHTML = score_message + " You seem to be at an upper elementary level";
        } else if (quiz.score > 5 && quiz.score < 9) {
          quiz.hQn.innerHTML = score_message + " You seem to be at a lower intermediate level";
        } else if (quiz.score > 8 && quiz.score <= 10) {
          quiz.hQn.innerHTML = score_message + " You seem to be at an upper intermediate level";
        }
      }
    }, 1000);
  },

  // (E) RESTART QUIZ
  reset : () => {
    quiz.now = 0;
    quiz.score = 0;
    quiz.draw();
  }
};
window.addEventListener("load", quiz.init);