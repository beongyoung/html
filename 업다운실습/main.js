let randomNum = 0;
let inputData = "";
let chance = 5;

let check_btn = document.getElementById("check-btn");
let reset_btn = document.getElementById("reset-btn");

let result_text = document.getElementById("result-area");
let input_text = document.getElementById("input-area");
let change_text = document.getElementById("chance-area")

function random(){
    // Math.random() : 0 ~ 1 사이의 값을 랜덤으로 생성
    randomNum = Math.floor(Math.random() * 100 + 1);
    console.log(randomNum);
}

random();

check_btn.addEventListener("click", function(){
    inputData = input_text.value;
    console.log("input : ", inputData);

    chance--;
    change_text.innerHTML = chance <= 0 ? "남은 기회가 없습니다." : "남은 기회는 " + chance + "회입니다.";

    // 버튼 비활성화
    if(chance <= 0 || inputData == randomNum){
        check_btn.disabled = true;
    }

    if(inputData > randomNum){
        result_text.innerHTML = "다운...ㅜㅜ";
    } else if(inputData < randomNum){
        result_text.innerHTML = "업!!";
    } else{
        result_text.innerHTML = "정답입니다.";
    }
})

reset_btn.addEventListener("click", function(){
    if(check_btn.disabled) check_btn.disabled = false;
    
    chance = 5;
    random();
    result_text.innerHTML = "업일까 다운일까"
    change_text.innerHTML = "남은기회는 " + chance + "회 입니다."
})