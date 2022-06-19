# CCU_Course_Selection

### 中正大學搶課程式

待選課系統開放再更新

##### setting.json範例

```json
{
	"wait":1,   //每次發送請求等待時間(單位為秒)
	"stuID": "你的學號",   
	"password": "選課系統密碼",  
	"courseInfo": {
		"隨便你取": {
			"courseID": "課程代碼",
			"courseNum": "班別",
			"deptID": "系所編號",
			"grade": "年級",
			"page": "在加選頁面第幾頁",
			"credit": "學分數",
			"general": 是否為通識課 true/false,
			"cate": "基礎通識填1/博雅通識填2",
			"subcate": "向度"
		},
		"科學飲茶實務": {      //這是個範例
			"courseID": "7500021",  
			"courseNum": "01",
			"deptID": "I001",
			"grade": "1",
			"page": "1",
			"credit": "3",
			"general": true,
			"cate": "2",
			"subcate": "6"
		}
	}
}
```

##### 系所代碼與學分數

* 系所代碼

  大學部：系所代碼加上4

  > 範例：地環系：2354 資工系：4104
  >

  碩班：系所代碼加上6

  > 範例：資工所：4106
  >

  通識中心：I001

  體育中心：F000

  語中：Z121

  軍訓：V000

  > 在查詢開課資料點選系所 https://kiki.ccu.edu.tw/~ccmisp06/Course/xxxx.html xxxx即為系所編號
  >
* 學分數

    一般系所：按照開課列表填寫

    通識&通英&通國：3

    體育：一&二年級：1 三年級：2

    軍訓：2
