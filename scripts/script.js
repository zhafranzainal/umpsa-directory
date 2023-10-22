const clearBtn = document.getElementById("clearBtn"), studentId = document.getElementById("studentId");

clearBtn.style.display = "none",

    studentId.addEventListener("input", (() => {
        studentId.value.length > 0 ? clearBtn.style.display = "block" : (clearBtn.style.display = "none")
    }
    )),
    clearBtn.addEventListener("click", (() => {
        studentId.value = "", clearBtn.style.display = "none"
    }
    ))