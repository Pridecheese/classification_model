menu_sets = []
//메뉴 생성기 시작 S===========================
class Menu{
    constructor(mtitle){
        this.mtitle=mtitle;
    }
    mtitle;url;tips;
}
menu0 = new Menu("심심풀이 Racing Game")
menu0.url = "https://pridecheese.github.io/classification_model/race.html"
menu0.tips = "아주 기본적이고 간단한 심심풀이 땅콩 레이싱 고고~"
menu1 = new Menu("CNN AND Crawling");
menu1.url="https://pridecheese.github.io/classification_model/";
menu1.tips="네이버,구글 이미지 크롤링 및 컨볼루션 적용한 모델";
menu2 = new Menu("test menu")
menu2.url = "127.0.0.1"
menu2.tips = "테스트용 메뉴"
menu_sets.push(menu0)
menu_sets.push(menu1)
menu_sets.push(menu2)