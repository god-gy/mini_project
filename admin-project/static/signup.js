// 값 받아오기
const id = document.getElementById("id")
const pw = document.getElementById("pw")
const password = document.getElementById("password")
const name = document.getElementById("name")
const number = document.getElementById("number")
const button = document.getElementById("button")

function buttonClick() {
    const idValue = id.value.trim()
    const pwValue = pw.value.trim()
    const passwordValue = password.value.trim()
    const nameValue = name.value.trim()
    const numberValue = number.value.trim()

    if (!idValue) {
        alert("아이디를 입력해주세요")
        return
    }

    if (!pwValue) {
        alert("비밀번호를 입력해주세요")
        return
    }

    if (pwValue.length < 8) {
        alert("비밀번호는 8자 이상 필요합니다.")
        return
    }

    if (pwValue !== passwordValue) {
        alert("비밀번호가 동일하지 않습니다.")
        return
    }

    if (!nameValue) {
        alert("사용자 이름을 입력해주세요")
        return
    }

    if (!numberValue) {
        alert("전화번호를 입력해주세요")
        return
    }

    alert(`🎉 회원가입이 완료되었습니다!🎉 \n아이디: ${idValue}\n이름: ${nameValue}`)
    location.href = "../html/mypage.html"
}

button.addEventListener("click", function (e) {
    e.preventDefault()
    buttonClick()
})
